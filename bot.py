import csv
import requests
from datetime import datetime

# ===== THÔNG TIN BOT & NHÓM =====
TOKEN = "8486225607:AAFpxAhRU7vtGqYcHANN-R9HsaBLqZyozgg"
CHAT_ID = "-1002873502521"  # Chat ID của supergroup
CSV_FILE = "contracts.csv"  # File CSV chứa hợp đồng

# ===== HÀM GỬI TIN NHẮN =====
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    print("Send result:", response.json())

# ===== HÀM KIỂM TRA HỢP ĐỒNG =====
def check_contracts():
    today = datetime.now().date()
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expire_date = datetime.strptime(row["expire"], "%Y-%m-%d").date()
            days_left = (expire_date - today).days
            if days_left in [7, 3, 1, 0]:
                send_telegram(
                    f"📄 {row['name']} sẽ hết hạn sau {days_left} ngày (ngày {expire_date})"
                )

# ===== CHẠY FILE =====
if __name__ == "__main__":
    check_contracts()
