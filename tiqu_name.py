# 提取图片名写入txt文件
import os

dir_origin_path = '/mnt/baode/CNN/segformer-pytorch-master/images' #原图片文件所在位置
new_file_path = '/mnt/baode/CNN/segformer-pytorch-master/VOCdevkit/VOC2007/ImageSets/Segmentation/test.txt' #提取的txt文件存放地址

img_names = os.listdir(dir_origin_path)
with open(new_file_path, "w") as file:  # 打开文件
    for img_name in img_names:
        image_name2 =  img_name.split('.')[0]
        file.write(image_name2 + "\n")



