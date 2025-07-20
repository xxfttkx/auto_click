from datetime import datetime
import pygetwindow as gw

def log(msg):
    """带时间前缀的打印函数"""
    now = datetime.now().strftime("[%H:%M:%S]")
    print(f"{now} {msg}")

def find_target_window():
    """查找并返回窗口标题完全是 '星痕共鸣' 的窗口对象"""
    all_windows = gw.getAllWindows()
    for w in all_windows:
        if w.title == "星痕共鸣":
            log("成功获取目标窗口")
            return w
    log("未找到游戏窗口")
    return None
