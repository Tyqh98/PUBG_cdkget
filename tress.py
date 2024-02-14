import paddleocr
import pyautogui
# import pytesseract
from PIL import ImageGrab
import time
import pyperclip
import paddle
from paddleocr import PaddleOCR
# 设置截图和点击的位置坐标
# screenshot_area = (1377, 409, 1508, 436)  # (左上角x, 左上角y, 右下角x, 右下角y)
screenshot_area = (0, 0, 400, 436)
copy_button_location = (400, 100)  # 复制按钮的位置
paste_location = (500, 200)  # 粘贴位置

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

# 等待几秒钟，以便你有时间切换到需要进行截图的窗口
# time.sleep()
# ocr = (use_angle_cls=True, lang='en', use_gpu=True)
# 截图
screenshot = ImageGrab.grab(bbox=screenshot_area)

# 保存截图
screenshot.save("screenshot3.png")

# 进行文字识别
results = ocr.ocr("img.png", cls=True)

content_list = []
for line in results:
    for word_info in line:
        content_list.append(word_info[1][0])

# 输出提取的文字内容
for i, content in enumerate(content_list, 1):
    print(f"提取的文字内容 {i}:", content)

# text = results
# print("完整的识别结果:\n", text)

# 复制文字到剪贴板
pyperclip.copy(content)

# 移动到复制按钮位置并点击
pyautogui.click(copy_button_location)

# 移动到粘贴位置并粘贴
pyautogui.click(paste_location)

# 如果需要点击更多的位置，可以继续添加类似的代码
