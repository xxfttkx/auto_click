from datetime import datetime
import pygetwindow as gw
import win32gui
import win32con
import win32com.client
import time


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

def activate_window(hwnd):
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')  # Alt键以绕过权限问题
    # win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    time.sleep(0.1)
    win32gui.SetForegroundWindow(hwnd)