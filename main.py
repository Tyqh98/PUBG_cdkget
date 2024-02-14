import pyautogui
import easyocr
import time
import pyperclip
import keyboard
from PIL import ImageGrab
# 设置截图和点击的位置坐标
# screenshot_area = (933, 38, 935, 340)  # (左上角x, 左上角y, 右下角x, 右下角y)
luihuan_button = (83, 1001)  # 锐换位置
queding_button = (376, 845)  # 确定位置


# import torch
# print(torch.cuda.is_available())

# 使用easyocr加载中文和英文OCR模型，并使用GPU加速
reader = easyocr.Reader(['en'], gpu=True)

i = 5

# 等待几秒钟，以便你有时间切换到需要进行截图的窗口
# time.sleep(5)
while 1:
    if keyboard.is_pressed('enter'):
        while i:
        # 截图
            screenshot = ImageGrab.grab(bbox=(1377, 409, 1508, 436))
            # time.sleep(0.1)
            # 保存截图
            screenshot.save("screenshot.png")

            # 进行文字识别
            results = reader.readtext("screenshot.png", detail=0)

            # 输出识别的文字
            text = results[0][1]
            print("识别的文字:", text)

            i -= 1
            print(i)
            # 复制文字到剪贴板
            pyperclip.copy(text)

            pyautogui.click(luihuan_button)
            time.sleep(0.03)
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('v')
            time.sleep(0.03)
            pyautogui.click(queding_button)
    #         if keyboard.is_pressed('esc'):
    #             break
    # if keyboard.is_pressed('esc'):
    #     break
