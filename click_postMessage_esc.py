import pyautogui
import pygetwindow as gw
import win32con
import win32gui
import win32api
import common

def send_key(hwnd, key):
    """使用底层方式向指定窗口发送按键"""
    vk_code = ord(key.upper())  # 将字母转换为虚拟键码（如 'F' -> 0x46）
    lparam_down = 1 | (win32api.MapVirtualKey(vk_code, 0) << 16)
    lparam_up = lparam_down | (1 << 30) | (1 << 31)

    # 发送 WM_KEYDOWN 和 WM_KEYUP
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, vk_code, lparam_down)
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, vk_code, lparam_up)

def click_f_once(win):
    """使用底层方式发送按键F，不移动鼠标、不切窗口"""
    if win:
        try:
            win.activate()
        except Exception as e:
            common.log(f"Exception: {e}")

        hwnd = win._hWnd
        send_key(hwnd, 'f')
        common.log(f"底层模拟按下 F 键")
    else:
        common.log("未找到游戏窗口")