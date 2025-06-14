from flask import Blueprint, render_template
import pandas as pd

sgdregressor_bp = Blueprint('sgdregressor', __name__)

DATA_PATH = 'data/study_score.csv'

@sgdregressor_bp.route('/sgdregressor')
def sgdregressor_page():
    df = pd.read_csv(DATA_PATH)

    # 샘플 10개는 테이블용, 전체는 그래프용
    sample = df.sample(10).to_dict(orient='records')
    chart_data = df.to_dict(orient='records')

    return render_template('sgdregressor.html', table_data=sample, chart_data=chart_data)
