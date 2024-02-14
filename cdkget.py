import keyboard
import pyautogui
from PIL import ImageGrab
import time
import pyperclip
import paddle
import win32gui
from paddleocr import PaddleOCR
# 设置截图和点击的位置坐标
# screenshot_area = (1377, 409, 1508, 436)  # (左上角x, 左上角y, 右下角x, 右下角y)
hwnd = 264622
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
screenshot_area = (left, top, right, bottom)
luihuan_button = (67, 1005)  # 锐换位置
queding_button = (281, 884)  # 确定位置

custom_det_model_dir = r'D:\A\paddle\inference\det'
custom_rec_model_dir = r'D:\A\paddle\inference\\rec'
custom_cls_model_dir = r'D:\A\paddle\inference\cls'

# 加载自定义模型
ocr = PaddleOCR(
    use_angle_cls=True,
    det_model_dir=custom_det_model_dir,
    rec_model_dir=custom_rec_model_dir,
    cls_model_dir=custom_cls_model_dir,
    use_gpu=True
)
ocr.ocr("scshot.jpg", cls=True)
i = 50
# 等待几秒钟，以便你有时间切换到需要进行截图的窗口
# time.sleep()
# ocr = (use_angle_cls=True, lang='en', use_gpu=True)
# 截图
while 1:
    if keyboard.is_pressed('enter'):
        while i:
            screenshot = ImageGrab.grab(bbox=screenshot_area)
            # screenshot = pyautogui.screenshot(region=screenshot_area)

            # 保存截图
            screenshot.save("screenshot3.png")

            # 进行文字识别
            results = ocr.ocr("screenshot3.png", cls=True)
            # results = ocr.ocr("sc2.jpg", cls=True)

            content_list = []
            for line in results:
                for word_info in line:
                    content_list.append(word_info[1][0])

            # 输出提取的文字内容
            for k, content in enumerate(content_list, 1):
                if len(content) == 12 and content.isalnum():

                # if True:

                    print(f"提取的文字内容 {k}:", content)
                    # pyperclip.copy(content)
                    #
                    # pyautogui.click(luihuan_button)
                    # # time.sleep(0.02)
                    # pyautogui.keyDown('ctrl')
                    # pyautogui.press('v')
                    # pyautogui.keyUp('ctrl')
                    # pyautogui.keyUp('v')
                    # # time.sleep(0.01)
                    # pyautogui.click(queding_button)
            i -= 1
    if keyboard.is_pressed('esc'):
        break
# text = results
# print("完整的识别结果:\n", text)

# 复制文字到剪贴板
pyperclip.copy(content)

# 如果需要点击更多的位置，可以继续添加类似的代码
# 冒泡排序  从大到小
# for i in range(len(content_list)-1):
#     for j in range(len(content_list)-1-i):
#         if content_list[j] < content_list[j+1]: # 从小到大排序只需修改这里为>
#             content_list[j],content_list[j+1] = content_list[j+1],content_list[j]
# print(content_list)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]   # 从小到大排序

