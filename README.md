倫敦共享單車：動態營運趨勢與氣候關聯分析

📌 專案概述
本專案旨在透過倫敦共享單車的歷史數據，探索氣候因子（氣溫、風速、天氣狀況）如何具體影響租借行為。
我建立了從 Python ETL 數據清洗 到 Tableau 交互式儀表板 的完整分析流程，協助營運團隊根據天氣預報優化單車調度。

🛠 使用工具
數據處理：Python (Pandas)

環境管理：Virtualenv, pip (requirements.txt)

數據視覺化：Tableau Desktop

數據源：Kaggle - London Bike Sharing Dataset

🚀 資料處理亮點 (ETL Process)
在 Python 階段，我針對原始數據進行了以下優化：

欄位語意化：將原始代碼重命名為具備單位標註的名稱（如 temp_real_C, humidity_percent）。

類別標籤轉換：將 weather_code 與 season 的數值代碼轉換為直觀的文字標籤（如 "Clear", "Rain", "Winter"），提升後續分析的可讀性。

數據標準化：將濕度數值轉換為 0 到 1 之間的小數，並確保時間欄位格式符合時間序列分析需求。

📊 Tableau 儀表板核心功能
我設計了一個高交互性的儀表板，具備以下商業決策功能：

動態移動平均線 (Moving Average)：用戶可自由切換「天/週/月」維度，觀察租借量的長期趨勢並排除短期噪音。

氣候壓力測試 (Heatmap)：透過溫度與風速的交叉分析熱力圖，識別極端天氣對租借需求的具體衝擊點。

Tooltip 深度洞察：滑鼠懸停即可查看特定時間點的天氣分布與 24 小時內的租借高峰。

💡 關鍵發現與建議
通勤規律：工作日的租借高峰集中在 08:00 與 17:00，建議在此時段前完成站點補給。

天氣敏感度：數據顯示降雨與低溫會使租借量下降約 40% 以上，此時段可安排車輛集中維修以降低成本。

<img width="1512" height="881" alt="截圖 2026-03-22 晚上9 23 28" src="https://github.com/user-attachments/assets/a80f8524-ed6e-45de-8cec-2918f158b147" />
