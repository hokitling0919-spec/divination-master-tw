import os
import json
from datetime import datetime

RECORD_PATH = "logs/lot_record.txt"

# 儲存抽籤紀錄
def save_divination_record(time_str, lot_info):
    content = f"【{time_str}】{lot_info['number']}號 {lot_info['title']}｜吉凶：{lot_info['level']}｜{lot_info['poem']}\n"
    with open(RECORD_PATH, "a", encoding="utf-8") as f:
        f.write(content)

# 讀取全部歷史紀錄
def read_all_record():
    if not os.path.exists(RECORD_PATH):
        return ""
    with open(RECORD_PATH, "r", encoding="utf-8") as f:
        return f.read()
