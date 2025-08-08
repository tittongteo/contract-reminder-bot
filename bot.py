import csv
import requests
from datetime import datetime

# Thông tin Telegram bot
TOKEN = "8486225607:AAFpxAhRU7vtGqYcHANN-R9HsaBLqZyozgg"
CHAT_ID = "-4943299045"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"Lỗi gửi tin: {response.text}")

def check_contracts():
    today = datetime.now().date()
    with open("contracts.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expire_date = datetime.strptime(row["expire"], "%Y-%m-%d").date()
            days_left = (expire_date - today).days
            if days_left in [7, 3, 1, 0]:
                send_telegram(f"📄 {row['name']} sẽ hết hạn sau {days_left} ngày ({expire_date})")

if __name__ == "__main__":
    check_contracts()
