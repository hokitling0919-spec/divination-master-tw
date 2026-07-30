# 吉凶對應終端顏色
def get_level_color(level):
    color_dict = {
        "上上": "\033[92m",  # 亮綠
        "上吉": "\033[92m",
        "中平": "\033[93m",  # 黃色
        "中下": "\033[91m",  # 淺紅
        "下下": "\033[31m"   # 深紅
    }
    # 找不到等級預設白色
    return color_dict.get(level, "\033[97m")
