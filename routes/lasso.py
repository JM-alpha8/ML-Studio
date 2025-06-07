from flask import Blueprint, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression

lasso_bp = Blueprint('lasso', __name__)

DATA_PATH = 'data/lasso_sample.csv'

@lasso_bp.route('/lasso')
def lasso_page():
    df = pd.read_csv(DATA_PATH)
    sample = df.sample(10).to_dict(orient='records')
    chart_data = df.to_dict(orient='records')
    return render_template('lasso.html', table_data=sample, chart_data=chart_data)

@lasso_bp.route('/train_lasso', methods=['POST'])
def train_lasso():
    data = request.get_json()
    alpha = float(data.get('alpha', 1.0))
    max_iter = int(data.get('max_iter', 1000))

    df = pd.read_csv(DATA_PATH)
    X = df[['X1','X2','X3','X4','X5',]]
    y = df['y']

    model = Lasso(alpha=alpha, max_iter=max_iter)
    model.fit(X, y)

    return jsonify({
        'score': round(model.score(X, y), 4),
        'intercept': round(model.intercept_, 4),
        'coef': [round(c, 4) for c in model.coef_]
    })

@lasso_bp.route('/train_lasso_linear', methods=['POST'])
def train_lasso_linear():
    df = pd.read_csv(DATA_PATH)
    X = df[['X1','X2','X3','X4','X5',]]
    y = df['y']

    model = LinearRegression()
    model.fit(X, y)

    return jsonify({
        'score': round(model.score(X, y), 4),
        'intercept': round(model.intercept_, 4),
        'coef': [round(c, 4) for c in model.coef_]
    })

