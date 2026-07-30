from modules.draw_lot import LotDivination

def menu():
    print("===== 繁體占卜師 Divination Master TW =====")
    print("1. 抽取靈籤")
    print("2. 易經起卦 (開發中)")
    print("3. 塔羅占卜 (開發中)")
    print("0. 離開")
    return input("請選擇功能：")

if __name__ == "__main__":
    lot_tool = LotDivination()
    while True:
        select = menu()
        if select == "1":
            print("\n===== 抽籤結果 =====")
            data = lot_tool.draw()
            print(f"第{data['number']}籤｜{data['title']}")
            print(data["poem"])
            print(f"\n解曰：{data['explain']}")
            print(f"參考建議：{data['suggest']}\n")
        elif select == "0":
            print("感謝使用，祝平安順遂")
            break
        else:
            print("功能尚未實作，敬請期待\n")
