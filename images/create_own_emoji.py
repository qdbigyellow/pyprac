import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import pathlib

def plt_show(img):
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imageRGB)
    plt.show()

cur_dir = pathlib.Path(__file__).parent.absolute()
image = cv2.imread(cur_dir.joinpath('fg.jpg').as_posix(), 0)  # 导入前景图片

# image_resize = cv2.resize(image, None, fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)  # 缩放

# ret, image_binary = cv2.threshold(image_resize, 80, 255, cv2.THRESH_BINARY)  # 图片二值化
ret, image_binary = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)  # 图片二值化

# image_roi = image_binary[74: 185, 0: 150]  # 感兴趣区域
image_roi = image_binary[0: 125, 0: 145]  # 感兴趣区域

rows, cols = image_roi.shape
# 旋转
M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 15, 1)
image_rotate = cv2.warpAffine(image_roi, M, (140, 130))
# 填充不需要的区域
h, w = image_rotate.shape
image_rotate_copy = image_rotate.copy()
pts1 = np.array([[0, 20],  [64, 0], [0, 0]], np.int32)
pts2 = np.array([[0, 18],  [0, h], [80, h]], np.int32)
pts3 = np.array([[0, 100],  [0, h], [w, h], [w, 100]], np.int32)
pts4 = np.array([[111, 0],  [w, 0], [w, 30]], np.int32)
pts5 = np.array([[124, 0],  [115, h], [w, h]], np.int32)
pts6 = np.array([[120, 40],  [95, 100], [120, 100]], np.int32)
foreground = cv2.fillPoly(image_rotate_copy, [pts1], (255, 255, 255))
foreground = cv2.fillPoly(image_rotate_copy, [pts2], (255, 255, 255))
foreground = cv2.fillPoly(image_rotate_copy, [pts3], (255, 255, 255))
foreground = cv2.fillPoly(image_rotate_copy, [pts4], (255, 255, 255))
foreground = cv2.fillPoly(image_rotate_copy, [pts5], (255, 255, 255))
foreground = cv2.fillPoly(image_rotate_copy, [pts6], (255, 255, 255))

foreground_roi = foreground[0: 93, 0: 125]
foreground_roi_resize = cv2.resize(foreground_roi, None, fx=2.5, fy=2.5, interpolation = cv2.INTER_CUBIC)

background = cv2.imread(cur_dir.joinpath('bg.jpeg').as_posix(), 0)  # 导入背景图片
# 拼接两张图片
h_f, w_f = foreground_roi_resize.shape
h_b, w_b = background.shape
left = (w_b - w_f)//2
right = left + w_f
top = 80
bottom = top + h_f
emoji = background
emoji[top: bottom, left: right] = foreground_roi_resize

PilImg = Image.fromarray(emoji)  # cv2 转 PIL
draw = ImageDraw.Draw(PilImg)  # 创建画笔
# ttfront = ImageFont.truetype('simhei.ttf', 34)  # 设置字体
# draw.text((210, 450),"你瞅啥！！",fill=0, font=ttfront)  # （位置，文本，文本颜色，字体）
emoji_text = cv2.cvtColor(np.array(PilImg),cv2.COLOR_RGB2BGR)  # PIL 转回 cv2

cv2.imwrite(cur_dir.joinpath('emoji.png').as_posix(), np.array(emoji_text))  # 保存表情包