# 📁 routes/logistic.py
from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

logistic_bp = Blueprint('logistic', __name__)

DATA_PATH = 'data/height_weight_overweight.csv'
MODEL_PATH = 'model/logistic_model.pkl'

@logistic_bp.route('/logistic')
def logistic_page():
    df = pd.read_csv(DATA_PATH)
    sample = df.sample(10).to_dict(orient='records')
    chart_data = df.to_dict(orient='records')
    return render_template('logistic.html', table_data=sample, chart_data=chart_data)

@logistic_bp.route('/train_logistic', methods=['POST'])
def train_logistic():
    params = request.get_json()
    df = pd.read_csv(DATA_PATH)
    X = df[['height', 'weight']]
    y = df['overweight']

    try:
        model = LogisticRegression(
            C=float(params['C']),
            penalty=params['penalty'],
            solver=params['solver'],
            max_iter=int(params['max_iter']),
            l1_ratio=float(params['l1_ratio']) if 'l1_ratio' in params else None
        )
        model.fit(X, y)
        pickle.dump(model, open(MODEL_PATH, 'wb'))

        acc = model.score(X, y)
        return jsonify({
            "coef": model.coef_[0].tolist(),
            'intercept': model.intercept_.tolist(),
            'accuracy': round(acc, 4)
        })

    except Exception as e:
        return jsonify({'error': str(e)})
