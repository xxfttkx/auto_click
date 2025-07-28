import sys
import time
import schedule
import argparse
import common

# 提前导入不同版本的 click_f_once，稍后根据参数选择
from click_postMessage import click_f_once as postMessage_click
from click_postMessage_esc import click_f_once as postMessage_click_esc
from click_pygetwindow import click_f_once as pygetwindow_click
from click_pygetwindow_move import click_f_once as pygetwindow_click_move

# 保存目标窗口
target_window = None

def start_schedule(click_func, interval_seconds=10):
    common.log(f"interval_seconds = {interval_seconds}")
    global target_window
    target_window = common.find_target_window()
    if not target_window:
        common.log("终止定时任务：未找到目标窗口")
        return

    click_func(target_window)
    schedule.every(interval_seconds).seconds.do(lambda: click_func(target_window))
    common.log(f"开始定时任务，每 {interval_seconds} 秒执行一次")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description="自动点击脚本")
    parser.add_argument(
        "--method",
        choices=["postMessage", "pygetwindow","postMessage_esc","pygetwindow_move","move"],
        default="pygetwindow",
        help="选择使用的方法：postMessage 或 pygetwindow（默认）"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=37,
        help="设置点击间隔（秒）"
    )

    args = parser.parse_args()

    methods = {
        "postMessage": postMessage_click,
        "postMessage_esc": postMessage_click_esc,
        "pygetwindow": pygetwindow_click,
        "pygetwindow_move": pygetwindow_click_move,
        "move": pygetwindow_click_move
    }
    common.log(f"{args.method} 方法被选中，间隔 {args.interval} 秒")
    click_func = methods.get(args.method, pygetwindow_click)


    start_schedule(click_func, args.interval)
