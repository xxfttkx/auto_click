import time
import pyautogui
import common

# 定义要按的键序列
yama = [[('a', 1.2),('w',0.3)],[('d', 1.2),('w',0.3)], ('s', 1)]
balukuang = [('a',1),('d',1)]
balukuang_2 = [('w',1.5),[('d',0.3),('w',0.3)],[('s',2.1),('a',0.4)]]
key_sequence = balukuang_2
current_index = 0  # 记录当前要按的键

def click_f_once(target_window):
    """激活目标窗口并按下 A 或 D（按住一段时间）"""
    global current_index
    if not target_window:
        common.log("目标窗口尚未设置")
        return
    try:
        target_window.activate()
    except Exception as e:
        common.log(f"Exception: {e}")
    curr = key_sequence[current_index]
    if isinstance(curr, list):
        # 多个键按顺序执行
        for key, duration in curr:
            pyautogui.keyDown(key)
            common.log(f"按下 {key.upper()} 键")
            time.sleep(duration)
            pyautogui.keyUp(key)
            common.log(f"松开 {key.upper()} 键")
    else:
        # 单个键
        key, duration = curr
        pyautogui.keyDown(key)
        common.log(f"按下 {key.upper()} 键")
        time.sleep(duration)
        pyautogui.keyUp(key)
        common.log(f"松开 {key.upper()} 键")
    time.sleep(0.2)  # 等待一段时间，避免过快切换
    # 切换到下一个键
    current_index = (current_index + 1) % len(key_sequence)
    pyautogui.press('f')
    common.log("按下F键")
