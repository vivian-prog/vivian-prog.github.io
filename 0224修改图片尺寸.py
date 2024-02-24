from PIL import Image


def crop_image(input_image_path, output_image_path, target_width, target_height):
    image = Image.open(input_image_path)
    width, height = image.size

    # 计算裁剪的边界
    left = (width - target_width) / 2
    top = (height - target_height)/2
    right = (width + target_width) / 2
    bottom = (height + target_height) / 2

    # 裁剪图像
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_image_path)


# 输入图像路径和输出图像路径
input_image_path = 'images/menu640/WechatIMG4423.jpg'
output_image_path = 'images/menu640/WechatIMG44231.jpg'

# 目标宽度和高度
target_width = 1280*2
target_height = 1280*2

# 调用函数进行裁剪
crop_image(input_image_path, output_image_path, target_width, target_height)
