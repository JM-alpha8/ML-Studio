# routes/gd.py
from flask import Blueprint, render_template
import pandas as pd

gd_bp = Blueprint('gd', __name__, url_prefix='/gd')

@gd_bp.route('/')
def gd():
    # CSV 파일에서 데이터 불러오기
    df = pd.read_csv('data/study_score.csv')

    # 필요한 컬럼만 추출 후 딕셔너리 리스트로 변환
    data = df[['study_time', 'score']].to_dict(orient='records')

    return render_template('gd.html', chart_data=data, table_data=data[:10])  # 표엔 10개만 보여줌
