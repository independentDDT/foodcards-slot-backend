
# 食選轉盤後端 - Foodcards Slot Backend

## 簡介
這是「食選轉盤」的後端服務，負責OCR辨識菜單、生成介紹與推薦詞，並提供API給前端呼叫。

## 功能
- 上傳菜單圖片，OCR自動辨識菜名
- GPT生成菜品介紹與推薦
- 圖片搜尋獲取該菜品相關圖片/影片

## 使用方式
1. Clone此專案：
    ```
    git clone https://github.com/independentDDT/foodcards-slot-backend.git
    cd foodcards-slot-backend
    ```
2. 安裝必要套件：
    ```
    pip3 install -r requirements.txt
    ```
3. 啟動API：
    ```
    python3 app.py
    ```
4. 瀏覽器打開 http://<你的VPS IP>:5000 查看狀態。

## 聯絡
獨立製作 - DDT Studio  
官方網站：https://www.independent.com.tw

---

# Foodcards Slot Backend

## Description
This is the backend service for "Foodcards Slot", responsible for processing menu images via OCR, generating food introductions via GPT, and providing images and videos.

## Features
- Upload menu image, recognize dish names via OCR
- Use GPT to generate introduction and recommendation
- Search images/videos for the dish

## Usage
1. Clone this repository:
    ```
    git clone https://github.com/independentDDT/foodcards-slot-backend.git
    cd foodcards-slot-backend
    ```
2. Install dependencies:
    ```
    pip3 install -r requirements.txt
    ```
3. Run the backend service:
    ```
    python3 app.py
    ```
4. Visit http://<your VPS IP>:5000 to check service status.

## Contact
DDT Studio  
Official Website: https://www.independent.com.tw
