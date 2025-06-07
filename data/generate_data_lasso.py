import pandas as pd
import numpy as np
import os

np.random.seed(42)

n_samples = 500

# 특성 생성 (광고비: 단위는 천만원)
X1 = np.random.uniform(0, 10, n_samples)  # TV
X2 = np.random.uniform(0, 5, n_samples)   # 라디오
X3 = np.random.uniform(0, 3, n_samples)   # 소셜미디어
X4 = np.random.uniform(0, 2, n_samples)   # 인플루언서
X5 = np.random.uniform(0, 1, n_samples)   # 검색엔진

# 가중치 설정 (일부는 영향 거의 없음)
beta = [3.0, 1.5, 0.0, 0.0, 0.5]  # X3, X4는 영향 거의 없음 → Lasso가 제거할 수 있음
noise = np.random.normal(0, 1, n_samples)

# 목표 변수: 매출 (단위: 억 원)
y = 3.0*X1 + 1.5*X2 + 0.0*X3 + 0.0*X4 + 0.5*X5 + noise

# DataFrame 저장
df = pd.DataFrame({
    'X1': X1,
    'X2': X2,
    'X3': X3,
    'X4': X4,
    'X5': X5,
    'y': y
})

os.makedirs('data', exist_ok=True)
df.to_csv('data/lasso_sample.csv', index=False)
print("✅ data/lasso_sample.csv 생성 완료!")
