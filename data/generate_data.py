# generate_data.py

import pandas as pd
import numpy as np
import os

np.random.seed(42)

heights = np.random.normal(loc=170, scale=7, size=100).round(1)  # 평균 170, 표준편차 7
weights = (heights * 0.4 + np.random.normal(0, 5, 100)).round(1)  # 단순 관계 + 노이즈

df = pd.DataFrame({
    'height': heights,
    'weight': weights
})

os.makedirs('data', exist_ok=True)
df.to_csv('data/height_weight.csv', index=False)

print("CSV 파일이 저장되었습니다: data/height_weight.csv")
