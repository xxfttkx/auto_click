import time
import schedule
import common
from click_postMessage import click_f_once

# 保存目标窗口
target_window = None

def start_schedule(interval_seconds=37):
    common.log(f"interval_seconds = {interval_seconds}")
    global target_window
    target_window = common.find_target_window()
    if not target_window:
        common.log("终止定时任务：未找到目标窗口")
        return

    schedule.every(interval_seconds).seconds.do(click_f_once(target_window))
    common.log(f"开始定时任务，每 {interval_seconds} 秒执行一次")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    start_schedule()