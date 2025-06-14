import numpy as np
import pandas as pd

# 시드 고정 (재현 가능성)
np.random.seed(42)

# 500건의 공부 시간 (0 ~ 10시간 사이)
study_time = np.random.uniform(0, 10, 500)

# 점수 계산: y = 5x + 30 + noise (노이즈는 평균 0, 표준편차 5)
noise = np.random.normal(0, 5, 500)
score = 5 * study_time + 30 + noise

# DataFrame 생성
df = pd.DataFrame({
    'study_time': study_time.round(2),
    'score': score.round(2)
})

# CSV 저장
df.to_csv('study_score.csv', index=False, encoding='utf-8-sig')

print("✅ study_score.csv 생성 완료!")
