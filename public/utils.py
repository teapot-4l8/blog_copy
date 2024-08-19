# 使用Python的PIL库来调整图像大小
from PIL import Image

# 打开图像文件
img = Image.open("public\mu.png")

# 调整图像大小为1280x720像素
img_resized = img.resize((1280, 720))

# 保存调整大小后的图像
img_resized.save("public\mu.png")