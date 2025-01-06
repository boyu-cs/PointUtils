import os
import pandas as pd
from plyfile import PlyData


def count_pred_4_points(ply_file):
    # 读取PLY文件
    ply_data = PlyData.read(ply_file)

    # 提取顶点数据
    vertex_data = ply_data['vertex']

    # 获取pred属性的索引
    pred = vertex_data['pred']

    # 统计pred属性为4的点的数量
    count = (pred == 4).sum()

    return count


def process_ply_files(directory, output_file):
    # 创建一个空的DataFrame来存储结果
    df = pd.DataFrame(columns=['File Name', 'Count of pred=4'])

    # 遍历目录中的所有PLY文件
    for file_name in os.listdir(directory):
        if file_name.endswith('.ply'):
            file_path = os.path.join(directory, file_name)
            count = count_pred_4_points(file_path)
            df = df.append({'File Name': file_name, 'Count of Train Points': count}, ignore_index=True)

    # 将结果保存到Excel文件中
    df.to_csv(output_file, index=False)


# 设置目录路径和输出文件路径
input_directory = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/test_output/Railway3D/WithTrain_5cate_1/'
output_file = 'output.csv'

# 执行处理
process_ply_files(input_directory, output_file)
