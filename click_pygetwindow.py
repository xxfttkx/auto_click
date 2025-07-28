import pygetwindow as gw
import pyautogui
import common

def click_f_once(target_window):
    """激活目标窗口并按下F键，再切回原窗口并恢复鼠标位置"""
    if not target_window:
        common.log("目标窗口尚未设置")
        return

    original_win = gw.getActiveWindow()
    original_mouse_pos = pyautogui.position()
    try:
        target_window.activate()
    except Exception as e:
        common.log(f"Exception: {e}")
        return
    pyautogui.press('f')
    common.log("按下F键")
    if original_win:
        try:
            original_win.activate()
            common.log(f"已切回窗口：{original_win.title}")
        except Exception as e:
            common.log(f"激活原始窗口失败: {e}")
    else:
        common.log("找不到原始窗口，无法切回")

    pyautogui.moveTo(original_mouse_pos.x, original_mouse_pos.y)
    common.log(f"已恢复鼠标位置到：{original_mouse_pos}")