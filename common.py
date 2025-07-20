from datetime import datetime
import pygetwindow as gw

def log(msg):
    """带时间前缀的打印函数"""
    now = datetime.now().strftime("[%H:%M:%S]")
    print(f"{now} {msg}")

def find_target_window():
    """查找并返回窗口标题为 '星痕共鸣' 的窗口对象"""
    windows = gw.getWindowsWithTitle("星痕共鸣")
    if windows:
        log("成功获取目标窗口")
        return windows[0]
    else:
        log("未找到游戏窗口")
        return None