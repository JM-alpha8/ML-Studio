from flask import Blueprint, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression

ridge_bp = Blueprint('ridge', __name__)

DATA_PATH = 'data/house_price.csv'  # 주택 관련 데이터 (사용자 기준)

@ridge_bp.route('/ridge')
def ridge_page():
    df = pd.read_csv(DATA_PATH)
    sample = df.sample(10).to_dict(orient='records')
    chart_data = df.to_dict(orient='records')
    return render_template('ridge.html', table_data=sample, chart_data=chart_data)

@ridge_bp.route('/train_ridge', methods=['POST'])
def train_ridge():
    data = request.get_json()
    alpha = float(data.get('alpha', 1.0))
    max_iter = int(data.get('max_iter', 1000))
    solver = data.get('solver', 'auto')

    df = pd.read_csv(DATA_PATH)
    X = df.iloc[:, :-1]  # 마지막 열 제외 (가격)
    y = df.iloc[:, -1]   # 마지막 열 (가격)

    try:
        model = Ridge(alpha=alpha, max_iter=max_iter, solver=solver)
        model.fit(X, y)

        return jsonify({
            'score': round(model.score(X, y), 4),
            'intercept': round(model.intercept_, 4),
            'coef': [round(c, 4) for c in model.coef_]
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@ridge_bp.route('/train_ridge_linear', methods=['POST'])
def train_ridge_linear():
    df = pd.read_csv(DATA_PATH)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    model = LinearRegression()
    model.fit(X, y)

    return jsonify({
        'score': round(model.score(X, y), 4),
        'intercept': round(model.intercept_, 4),
        'coef': [round(c, 4) for c in model.coef_]
    })
