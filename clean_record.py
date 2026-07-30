import json
from pathlib import Path

# 紀錄檔位置，和 record_manager 內路徑保持一致
RECORD_FILE = Path("record.json")

def clean_empty_record():
    if not RECORD_FILE.exists():
        print("紀錄檔不存在，無需清理")
        return

    # 讀取舊資料
    with open(RECORD_FILE, "r", encoding="utf-8") as f:
        try:
            all_data = json.load(f)
        except json.JSONDecodeError:
            print("檔案格式錯誤！無法讀取")
            return

    clean_list = []
    delete_count = 0

    for row in all_data:
        r_type = row.get("type", "")
        # 判定條件：空白測試殘留資料直接丟棄
        if r_type == "抽靈籤":
            num = row.get("number", "")
            if num == "":
                delete_count += 1
                continue
        clean_list.append(row)

    # 覆蓋寫回清理後資料
    with open(RECORD_FILE, "w", encoding="utf-8") as f:
        json.dump(clean_list, f, ensure_ascii=False, indent=2)

    print(f"✅ 清理完成！刪除 {delete_count} 筆空白殘留紀錄")
    print(f"剩餘有效紀錄：{len(clean_list)} 筆")

if __name__ == "__main__":
    clean_empty_record()
