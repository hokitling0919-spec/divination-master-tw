from modules.draw_lot import run_draw_lot
from modules.record_manager import read_all_record
from modules.yijing import run_yijing

def main_menu():
    while True:
        print("\n====== Divination Master TW 繁體占卜系統 ======")
        print("(1 | 抽靈籤)")
        print("(2 | 查詢歷史抽籤紀錄)")
        print("(3 | 易經金錢起卦)")
        print("(0 | 離開程式)")
        select = input("請輸入選項數字：")
        if select == "1":
            run_draw_lot()
        elif select == "2":
            print("\n========== 歷史占卜紀錄 ==========")
            data = read_all_record()
            if not data:
                print("📜 暫無任何占卜紀錄")
            else:
                for index, item in enumerate(data, start=1):
                    record_type = item.get("type", "未知")
                    time_str = item.get("time", "無時間")
                    print(f"\n【第{index}筆】時間：{time_str}")
                    print(f"占卜類型：{record_type}")

                    if record_type == "抽靈籤":
                        lot_num = item.get("number", "無")
                        lot_level = item.get("level", "無")
                        lot_title = item.get("title", "無")
                        lot_poem = item.get("poem", "無")
                        print(f"籤號：{lot_num}｜吉凶：{lot_level}")
                        print(f"籤題：{lot_title}")
                        print(f"籤文：{lot_poem}")
                    elif record_type == "易經起卦":
                        main_gua = item.get("main_gua", "無")
                        change_gua = item.get("change_gua", "無")
                        dong_count = item.get("dong_count", 0)
                        print(f"本卦：{main_gua}｜變卦：{change_gua}｜動爻數：{dong_count}")
                    print("----------------------------------------")
        elif select == "3":
            run_yijing()
        elif select == "0":
            print("🙏平安吉祥，程式結束")
            break
        else:
            print("❌ 輸入錯誤，請重新選擇！")

if __name__ == "__main__":
    main_menu()
