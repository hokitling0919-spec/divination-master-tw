import json
import random
import os
from modules.color_output import print_color
from modules.record_manager import save_record

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOT_FILE = os.path.join(BASE_PATH, "data", "lot_book.json")

class LotDivination:
    def __init__(self):
        with open(LOT_FILE, "r", encoding="utf-8") as f:
            self.lot_list = json.load(f)

    def draw(self):
        return random.choice(self.lot_list)


def run_draw_lot():
    div_tool = LotDivination()
    print_color("===== 抽靈籤系統 =====", "cyan")
    input("按 Enter 開始搖籤...")
    result = div_tool.draw()
    # 自動儲存本次抽籤紀錄
    save_record(result)
    print_color(f"\n【籤號】{result['number']}｜{result['level']}", "yellow")
    print_color(f"【詩句】{result['poem']}", "white")
    print_color(f"【解曰】{result['explain']}", "green")
