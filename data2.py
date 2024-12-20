import os

def extract_and_write(input_file_path, output_file_path):
    """
    从输入文件中读取每一行，提取 "/" 后面的内容，并将这些内容写入输出文件。
    """
    # if not os.path.exists(output_file_path):
    #     os.makedirs(output_file_path)
    
    if not output_file_path:
        # 生成默认的输出文件路径
        input_dir = os.path.dirname(input_file_path)
        input_filename = os.path.basename(input_file_path)
        output_filename = f"processed_{input_filename}"
        output_file_path = os.path.join(input_dir, output_filename)
    
    with open(input_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.strip().split('/')[2]
            part = parts.split('.')[0]
            # if len(parts) > 1:
            outfile.write(part + '\n')

# 示例用法
# input_file_path = '/mnt/12tb/ZXS/U2PL-main/data/splits/useg/val0.txt'
# output_file_path = '/mnt/12tb/ZXS/U2PL-main/data/splits/useg/val.txt'
input_file_path = '/mnt/12tb/ZXS/U2PL-main/data/splits/useg/1_2_0/unlabeled.txt'
output_file_path = '/mnt/12tb/ZXS/U2PL-main/data/splits/useg/1_2/unlabeled.txt'
extract_and_write(input_file_path, output_file_path)