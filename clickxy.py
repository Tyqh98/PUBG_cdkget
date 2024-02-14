import pyautogui
import time
import ctypes
import win32gui

time.sleep(2)
print(pyautogui.position())

# 获取鼠标位置
point = ctypes.wintypes.POINT()
ctypes.windll.user32.GetCursorPos(ctypes.byref(point))

# 获取窗口句柄
hwnd = ctypes.windll.user32.WindowFromPoint(point)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(hwnd, ':', left, top, right, bottom)
#