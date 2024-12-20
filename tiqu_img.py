# 从txt文件中的图片名去提取对应的图片
# import shutil
#
# txt_path = 'E:/train_val/name.txt' #txt文件所在位置
# position = 'E:/train_val/masks'  #原图片所在位置
# new_file_path = 'E:/train_val/masks2/' #提取出来的图片存放的新文件夹
#
# with open(txt_path, 'r') as f:  # 打开文件
#         lines = f.readlines() # 逐行读取文件
#         # file = open(out_txt_path, 'w') # 写入
#         nums = len(lines) # 总共有多少行
#         print(nums)
#         for i in range(nums): # 遍历每一行
#             values = lines[i].replace('\n','') #去除换行符
#             img_position = position + '\\' + values + '.bmp'  # 构造目标图片绝对路径
#             print(img_position)
#             shutil.copy(img_position, new_file_path) #将目标图片复制到新的文件夹


# 从txt文件中的图片名去提取对应的图片
import shutil

txt_path = '/mnt/12tb/ZXS/CISC-R-main/dataset/splits/suim/1_4/split_0/labeled.txt' #txt文件所在位置
position = '/mnt/12tb/ZXS/CISC-R-main/suim/SegmentationClass'  #原图片所在位置
new_file_path = '/mnt/12tb/ZXS/CISC-R-main/suim/label_mask' #提取出来的图片存放的新文件夹

with open(txt_path, 'r') as f:  # 打开文件
        lines = f.readlines() # 逐行读取文件
        print(lines)
        # line = lines.split(' ')[1]
        # print(line)
        # file = open(out_txt_path, 'w') # 写入
        nums = len(lines) # 总共有多少行
        print(nums)
        for i in range(nums): # 遍历每一行
            values = lines[i].split('/')[2].replace('\n','') #去除换行符
            # img_position = position + '\\' +  values + '.bmp'
            # values = lines[i].split(' ')[1].split('/')[1].replace('\n','') #去除换行符
            # print(values)
            img_position = position + '/' + values  # 构造目标图片绝对路径
            # print(img_position)
            shutil.copy(img_position, new_file_path) #将目标图片复制到新的文件夹