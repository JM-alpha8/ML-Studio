import pandas as pd
import numpy as np

# 1. 랜덤 시드 고정 (재현 가능성)
np.random.seed(42)

# 2. 키(cm)와 몸무게(kg) 생성
heights = np.random.normal(loc=165, scale=10, size=200).round(1)  # 평균 165cm, 표준편차 10
weights = np.random.normal(loc=65, scale=15, size=200).round(1)   # 평균 65kg, 표준편차 15

# 3. BMI 계산 및 비만 여부 판별
# BMI = weight(kg) / (height(m)^2)
bmi = weights / (heights / 100) ** 2
overweight = (bmi >= 25).astype(int)  # BMI 25 이상이면 비만(1), 아니면 0

# 4. 데이터프레임 생성
df = pd.DataFrame({
    'height': heights,
    'weight': weights,
    'overweight': overweight
})

# 5. CSV로 저장
df.to_csv('height_weight_overweight.csv', index=False)

print("CSV 파일 저장 완료: height_weight_overweight.csv")
print(df.head())
