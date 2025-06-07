# 📁 routes/linear.py
from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

linear_bp = Blueprint('linear', __name__)

DATA_PATH = 'data/height_weight.csv'
MODEL_PATH = 'model/linear_model.pkl'

@linear_bp.route('/linear')
def linear_page():
    df = pd.read_csv(DATA_PATH)
    sample = df.sample(10).to_dict(orient='records')
    chart_data = df.to_dict(orient='records')
    return render_template('linear.html', table_data=sample, chart_data=chart_data)

@linear_bp.route('/train_linear', methods=['POST'])
def train_linear():
    df = pd.read_csv(DATA_PATH)
    X = df[['height']]
    y = df['weight']
    model = LinearRegression().fit(X, y)
    pickle.dump(model, open(MODEL_PATH, 'wb'))
    return jsonify({'weight': model.coef_[0], 'bias': model.intercept_})

@linear_bp.route('/predict_linear', methods=['POST'])
def predict_linear():
    height = float(request.form['height'])
    model = pickle.load(open(MODEL_PATH, 'rb'))
    prediction = model.predict([[height]])[0]
    return jsonify({'prediction': round(prediction, 2)})
