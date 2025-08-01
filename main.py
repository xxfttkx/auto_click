import sys
import time
import schedule
import argparse
import common

# 提前导入不同版本的 click_f_once，稍后根据参数选择
from click_postMessage import click_f_once as postMessage_click
from click_postMessage_esc import click_f_once as postMessage_click_esc
from click_pyautogui import click_f_once as pyautogui_click
from click_pyautogui_move import click_f_once as pyautogui_click_move
from click_pyautogui_move import yama, balukuang, balukuang_1, shihuiyan, fulunakuand, fulunakuand_1, lunakuang
sequences = {
    "yama": yama,
    "balukuang": balukuang,
    "balukuang_1": balukuang_1,
    "shihuiyan": shihuiyan,
    "fulunakuand": fulunakuand,
    "fulunakuand_1": fulunakuand_1,
    "lunakuang": lunakuang
}
# 保存目标窗口
target_window = None

def start_schedule(click_func, interval_seconds=10):
    common.log(f"interval_seconds = {interval_seconds}")
    global target_window
    target_window = common.find_target_window()
    if not target_window:
        common.log("终止定时任务：未找到目标窗口")
        return

    common.log("最先运行一次")
    click_func(target_window)
    schedule.every(interval_seconds).seconds.do(lambda: click_func(target_window))
    common.log(f"开始定时任务，每 {interval_seconds} 秒执行一次")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description="自动点击脚本")

    methods = {
        "postMessage": postMessage_click,
        "pm": postMessage_click,
        
        "postMessage_esc": postMessage_click_esc,
        "pm_esc": postMessage_click_esc,
        "esc": postMessage_click_esc,

        "pyautogui": pyautogui_click,
        "pag": pyautogui_click,

        "pyautogui_move": pyautogui_click_move,
        "pag_move": pyautogui_click_move,
        "pag_mv": pyautogui_click_move,
        "move": pyautogui_click_move,  # 可保留原名也可缩为 mv
        "mv": pyautogui_click_move
    }

    parser.add_argument(
        "--method","-m",
        choices = methods.keys(),
        default="pyautogui",
        help="选择使用的方法：postMessage 或 pyautogui（默认）"
    )
    parser.add_argument(
        "--interval","-i",
        type=int,
        default=37,
        help="设置点击间隔（秒）"
    )
    parser.add_argument(
        "--sequence","-s",
        choices=["yama", "balukuang", "balukuang_1", "shihuiyan", "fulunakuand", "fulunakuand_1", "lunakuang"],
        default="balukuang",
        help="指定键位序列，仅在 method=move 时有效"
    )
    args = parser.parse_args()
    # 设置序列：只在 move 相关方法中有效
    if args.method in ["mv","move", "pag_mv","pag_move","pyautogui_move"]:
        from click_pyautogui_move import set_key_sequence  # 你需要在模块中提供 setter
        key_seq = sequences.get(args.sequence, shihuiyan)
        set_key_sequence(key_seq)
        common.log(f"使用按键序列：{args.sequence}")



    common.log(f"{args.method} 方法被选中，间隔 {args.interval} 秒")

    click_func = methods.get(args.method, pyautogui_click)
    start_schedule(click_func, args.interval)
