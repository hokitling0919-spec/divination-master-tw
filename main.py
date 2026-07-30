from modules.draw_lot import run_draw_lot
from modules.record_manager import read_all_record

def main_menu():
    while True:
        print("\n========= Divination Master TW 繁體占卜系統 =========")
        print("1｜抽靈籤")
        print("2｜查詢歷史抽籤紀錄")
        print("3｜易經金錢起卦
        print("0｜離開程式")
        select = input("請輸入選項數字：")
        if select == "1":
            run_draw_lot()
        elif select == "2":
            print("\n===== 歷史抽籤紀錄 =====")
            data = read_all_record()
            print(data if data else "暫無任何抽籤紀錄")
        elif select == "0":
            print("🙏 平安吉祥，程式結束")
            break
        else:
            print("❌ 輸入錯誤，請重新選擇！")

if __name__ == "__main__":
    main_menu()
