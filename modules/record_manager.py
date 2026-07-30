import json
import os
from datetime import datetime

RECORD_FILE = "record.json"

def save_record(lot_info):
    records = []
    if os.path.exists(RECORD_FILE):
        with open(RECORD_FILE, "r", encoding="utf-8") as f:
            records = json.load(f)

    new_item = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "number": lot_info.get("number", ""),
        "level": lot_info.get("level", "未知"),
        "title": lot_info.get("title", ""),
        "poem": lot_info.get("poem", "")
    }
    records.append(new_item)

    with open(RECORD_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

# 新增查詢歷史紀錄函數
def read_all_record():
    if not os.path.exists(RECORD_FILE):
        return []
    with open(RECORD_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
