###########################检查数据集标签有多少类别############################
import os
from PIL import Image

def get_unique_pixel_values(folder_path):
    unique_pixels = set()

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # 根据需要添加更多格式
            file_path = os.path.join(folder_path, filename)
            with Image.open(file_path) as img:
                # 将图像转换为灰度图像（如果需要）
                img = img.convert('L')
                # 获取图像的像素数据
                pixels = img.getdata()
                # 将像素数据添加到集合中
                unique_pixels.update(pixels)

    return unique_pixels


# 使用示例
folder_path = 'F:/1221/labels_color_8b'
unique_pixels = get_unique_pixel_values(folder_path)
print("Unique pixel values:", unique_pixels)


#############################################################################
# 将mask中的背景像素值全置为0
import os
from PIL import Image
import numpy as np

def process_label_folder(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # 假设标签文件是图片格式
            file_path = os.path.join(folder_path, filename)
            # 打开图像文件
            with Image.open(file_path) as img:
                # 将图像转换为numpy数组
                label_array = np.array(img)
                # 将像素值大于20的像素点的像素值置为0
                label_array[label_array > 20] = 0
                # 将处理后的数组转换回图像
                processed_img = Image.fromarray(label_array)
                # 保存处理后的图像
                processed_img.save(file_path)

# 使用示例
folder_path = 'F:/SegmentationClass_our_reshape'
process_label_folder(folder_path)