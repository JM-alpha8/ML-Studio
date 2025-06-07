import numpy as np
import pandas as pd

np.random.seed(42)
n = 500  # 샘플 수

# ✔️ 주요 유의미 특성
area = np.random.normal(85, 15, n)
floor = np.random.randint(1, 10, n)
rooms = (area / 30 + np.random.normal(0, 0.5, n)).astype(int).clip(2, 5)
parking = np.random.randint(0, 3, n)
subway_distance = np.random.normal(500, 200, n)

# ✔️ 과적합 유도 특성
noise1 = np.random.normal(0, 1, n)
noise2 = np.random.normal(0, 1, n)
duplicate_area = area * 0.95 + np.random.normal(0, 1, n)
redundant_combo = rooms * 0.5 + parking * 1.2 + np.random.normal(0, 0.3, n)
random_binary = np.random.randint(0, 2, n)

# ✔️ 가격 생성 (노이즈 포함)
price = (
    area * 0.1 +
    floor * 0.3 +
    rooms * 1.5 +
    parking * 2.0 -
    subway_distance * 0.005 +
    np.random.normal(0, 2, n)
)

# ✔️ 데이터프레임 생성
df = pd.DataFrame({
    'area': area.round(1),
    'floor': floor,
    'rooms': rooms,
    'parking': parking,
    'subway_distance': subway_distance.round(1),
    'noise1': noise1,
    'noise2': noise2,
    'duplicate_area': duplicate_area.round(1),
    'redundant_combo': redundant_combo.round(2),
    'random_binary': random_binary,
    'price': price.round(2)
})

df.to_csv('data/house_price.csv', index=False)
print('✅ 과적합 가능성 포함된 house_price.csv 저장 완료!')
