from modules.color_output import get_level_color
from modules.record_manager import save_divination_record
import json
import random
import os
from datetime import datetime

# 抽籤核心類別
class LotDivination:
    def __init__(self):
        # 載入籤詩檔案
        with open("data/lot_book.json","r",encoding="utf-8") as f:
            self.lots = json.load(f)

    def draw(self):
        # 隨機抽一支籤
        return random.choice(self.lots)

# 執行抽籤入口，main.py 會呼叫這個函數
def run_draw_lot():
    # 建立抽籤物件
    div_tool = LotDivination()
    # 執行抽籤，拿到籤結果
    lot_result = div_tool.draw()

    # 取得吉凶對應顏色
    text_color = get_level_color(lot_result["level"])
    color_reset = "\033[0m"

    # 在畫面上印出籤文
    print("\n======================================")
    print(text_color + f"【{lot_result['number']}號 {lot_result['title']}】" + color_reset)
    print(text_color + f"吉凶：{lot_result['level']}" + color_reset)
    print(f"籤詩：{lot_result['poem']}")
    print(f"解釋：{lot_result['explain']}")
    print("======================================")

    # 儲存本次抽籤紀錄
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_divination_record(now_time, lot_result)

# 單獨執行這個檔案時，可以直接測試抽籤
if __name__ == "__main__":
    run_draw_lot()
