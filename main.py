import time
import schedule
import argparse
import common

# 提前导入两个版本的 click_f_once，稍后根据参数选择
from click_postMessage import click_f_once as postMessage_click
from click_pygetwindow import click_f_once as pygetwindow_click

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
    parser = argparse.ArgumentParser(description="自动点击脚本")
    parser.add_argument(
        "--method",
        choices=["postMessage", "pygetwindow"],
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

    # 根据参数选择对应的 click 函数
    if args.method == "postMessage":
        click_func = postMessage_click
    else:
        click_func = pygetwindow_click

    start_schedule(click_func, args.interval)
