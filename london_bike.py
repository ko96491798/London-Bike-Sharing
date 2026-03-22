import pandas as pd
import os

# =========================================================
# 專案名稱：倫敦共享單車數據 ETL 與趨勢分析預處理
# 工具：Python (Pandas)
# =========================================================

# ---------------------------------------------------------
# 1. 數據獲取與環境檢查 (Data Acquisition)
# ---------------------------------------------------------

file_path = "london_merged.csv"

if os.path.exists(file_path):
    bikes = pd.read_csv(file_path)
    print(f"成功載入數據{bikes.shape}")
else:
    print("Ｅrror")

# ---------------------------------------------------------
# 2. 探索性數據分析 (Exploratory Data Analysis)
# ---------------------------------------------------------

bikes.info()

# 檢查天氣(weather_code)與季節(season)的分布，確認數據是否有偏態
print("\n天氣代碼分布狀況：")
print(bikes.weather_code.value_counts())

print("\n季節分布狀況：")
print(bikes.season.value_counts())

# ---------------------------------------------------------
# 3. 資料清洗與特徵轉換 (Data Cleaning)
# ---------------------------------------------------------

# 為了提升在 Tableau 視覺化時的可讀性
# 我將氣溫標註單位(C)，並將 cnt 改為更直觀的 count
new_cols_dict = {
    'timestamp': 'time',
    'cnt': 'count', 
    't1': 'temp_real_C',
    't2': 'temp_feels_like_C',
    'hum': 'humidity_percent',
    'wind_speed': 'wind_speed_kph',
    'weather_code': 'weather',
    'is_holiday': 'is_holiday',
    'is_weekend': 'is_weekend',
    'season': 'season'
}
bikes.rename(new_cols_dict, axis=1, inplace=True)

# 濕度原本是百分比整數(0-100)，我將其轉換為 0 到 1 之間的小數，方便後續計算
bikes.humidity_percent = bikes.humidity_percent / 100

# 將原始數據中的數值代碼轉換為具備意義的文字
season_dict = {
    '0.0': 'spring',
    '1.0': 'summer',
    '2.0': 'autumn',
    '3.0': 'winter'
}

weather_dict = {
    '1.0': 'Clear',
    '2.0': 'Scattered clouds',
    '3.0': 'Broken clouds',
    '4.0': 'Cloudy',
    '7.0': 'Rain',
    '10.0': 'Rain with thunderstorm',
    '26.0': 'Snowfall'
}

# 數據型別為字串，避免 Mapping 出現空值
bikes.season = bikes.season.astype('str').map(season_dict)
bikes.weather = bikes.weather.astype('str').map(weather_dict)

# ---------------------------------------------------------
# 4. 結果驗證與數據導出 (Export)
# ---------------------------------------------------------

print("\n清洗後的數據：")
print(bikes.head())

# index=False 避免導出多餘的欄位
output_file = 'london_bikes_final.xlsx'
bikes.to_excel(output_file, sheet_name='Data', index=False)

print(f"\n最終檔案：{output_file}")