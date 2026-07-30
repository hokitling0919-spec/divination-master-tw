import json
import random
import os
from modules.record_manager import save_record

# 檔案路徑
JSON_PATH = os.path.join("data", "hexagrams.json")

# 八卦對照表（用上下卦查詢六十四卦）
trigram_map = {
    "乾": 1, "兌": 2, "離": 3, "震": 4,
    "巽": 5, "坎": 6, "艮": 7, "坤": 8
}
# 爻數轉陰陽：7=少陽、8=少陰、9=老陽、6=老陰
def yao_to_symbol(num):
    if num == 6:
        return {"val": 0, "text": "× 老陰", "is_dong": True}
    elif num == 7:
        return {"val": 1, "text": "— 少陽", "is_dong": False}
    elif num == 8:
        return {"val": 0, "text": "- - 少陰", "is_dong": False}
    elif num == 9:
        return {"val": 1, "text": "○ 老陽", "is_dong": True}

# 模擬一次搖三枚銅錢
def shake_once():
    # 模擬3個銅錢，1=背(3點)，0=字(2點)
    coins = [random.randint(0,1) for _ in range(3)]
    total = sum([3 if c == 1 else 2 for c in coins])
    return total

# 連搖六次，得到六爻【初爻→上爻】
def cast_gua():
    lines = []
    for _ in range(6):
        lines.append(shake_once())
    return lines

# 將六爻數值轉成上下八卦名稱
def get_trigrams(yao_list):
    # yao_list[0]初爻，[5]上爻
    lower = yao_list[0:3]
    upper = yao_list[3:6]
    def tri_name(ys):
        vals = [yao_to_symbol(y)["val"] for y in ys]
        # 爻由下往上：初、二、三
        if vals == [1,1,1]: return "乾"
        elif vals == [0,1,1]: return "兌"
        elif vals == [1,0,1]: return "離"
        elif vals == [0,0,1]: return "震"
        elif vals == [1,1,0]: return "巽"
        elif vals == [0,1,0]: return "坎"
        elif vals == [1,0,0]: return "艮"
        elif vals == [0,0,0]: return "坤"
    return tri_name(lower), tri_name(upper)

# 產生變卦（動爻陰陽互換）
def get_changed_yao(yao_list):
    new_list = []
    for y in yao_list:
        info = yao_to_symbol(y)
        if info["is_dong"]:
            # 動爻翻轉
            new_y = 7 if info["val"] == 0 else 8
            new_list.append(new_y)
        else:
            new_list.append(y)
    return new_list

# 載入六十四卦資料
def load_hexagrams():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# 查詢卦資料
def find_gua(data, upper_name, lower_name):
    # 簡化：這裡需要卦序對應，這邊先遍歷搜尋
    for g in data:
        if g["upper_trigram"] == upper_name and g["lower_trigram"] == lower_name:
            return g
    return None

# 解卦核心邏輯，依動爻數判斷取用文辭
def analyse_divination(main_gua, changed_gua, yao_list):
    dong_index = [i for i,y in enumerate(yao_list) if yao_to_symbol(y)["is_dong"]]
    dong_count = len(dong_index)
    result = {}
    result["dong_count"] = dong_count
    result["dong_pos"] = [x+1 for x in dong_index] # 轉成初1~上6

    if dong_count == 0:
        result["focus"] = "無動爻，參考本卦卦辭"
        result["text"] = main_gua["gua_ci"] + "\n" + main_gua["xiang"]
    elif dong_count == 1:
        pos = dong_index[0]
        yao_text = main_gua["yao"][pos]
        result["focus"] = f"單動爻【第{pos+1}爻】為重點，參考本卦爻辭"
        result["text"] = yao_text
    elif 2 <= dong_count <=5:
        result["focus"] = f"{dong_count}個動爻，參考變卦卦辭為主"
        result["text"] = changed_gua["gua_ci"] + "\n" + changed_gua["xiang"]
    elif dong_count ==6:
        if main_gua["name"] == "乾為天":
            result["focus"] = "六爻全動，乾卦參看用九"
            result["text"] = main_gua["yong"]
        elif main_gua["name"] == "坤為地":
            result["focus"] = "六爻全動，坤卦參看用六"
            result["text"] = main_gua["yong"]
        else:
            result["focus"] = "六爻全動，參考變卦卦辭"
            result["text"] = changed_gua["gua_ci"]
    return result

# 完整起卦流程入口
def start_yijing_divination():
    hex_data = load_hexagrams()
    yao_list = cast_gua()
    lower_main, upper_main = get_trigrams(yao_list)
    main_gua = find_gua(hex_data, upper_main, lower_main)

    changed_yaos = get_changed_yao(yao_list)
    lower_change, upper_change = get_trigrams(changed_yaos)
    change_gua = find_gua(hex_data, upper_change, lower_change)

    analysis = analyse_divination(main_gua, change_gua, yao_list)

    # 組裝輸出文字
    output = "\n==================== 易經金錢起卦 ====================\n"
    output += f"【本卦】{main_gua['symbol']} {main_gua['name']}｜上{upper_main}下{lower_main}\n"
    if main_gua["name"] != change_gua["name"]:
        output += f"【變卦】{change_gua['symbol']} {change_gua['name']}｜上{upper_change}下{lower_change}\n"
    output += "------------------------------------------------------\n"
    # 印六爻（由上到下顯示，符合傳統閱讀習慣）
    for i in reversed(range(6)):
        y = yao_list[i]
        sym_info = yao_to_symbol(y)
        pos_name = ["初爻","二爻","三爻","四爻","五爻","上爻"][i]
        output += f"{pos_name:>4}：{sym_info['text']}\n"
    output += "------------------------------------------------------\n"
    output += f"動爻數：{analysis['dong_count']}，動爻位置：{analysis['dong_pos'] if analysis['dong_pos'] else '無'}\n"
    output += f"解卦依據：{analysis['focus']}\n"
    output += f"\n【參考文辭】\n{analysis['text']}\n"
    output += "======================================================\n"
    output += "【免責聲明】本內容僅為傳統民俗文化參考，不構成人生決策之唯一依據，命運掌握在自身選擇，請理性看待。\n"

    # 儲存紀錄
    record_info = {
        "type": "易經起卦",
        "main_gua": main_gua["name"],
        "change_gua": change_gua["name"],
        "dong_count": analysis["dong_count"],
        "full_text": output
    }
    save_record(record_info)
    return output

# 測試用

# 【新的 run_yijing 定義，放在最底部、測試程式前面】
def run_yijing():
    """易經起卦入口，main.py 呼叫用"""
    print("===== 易經金錢起卦系統 =====")
    result_text = start_yijing_divination()
    print(result_text)

# 測試用
if __name__ == "__main__":
    print(start_yijing_divination())
