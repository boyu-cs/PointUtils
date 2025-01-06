import os
import pandas as pd
from plyfile import PlyData

# edit this path
input_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/at/box_4cate_fold_test/allPlyTrainTest/'

results = {}

for filename in os.listdir(input_folder):
    if filename.endswith('.ply'):
        ply_path = os.path.join(input_folder, filename)

        ply_data = PlyData.read(ply_path)
        vertices = ply_data['vertex'].data

        # count the number of points for each `pred` class
        # The `pred` classes range from 0 to 5, with a total of 6 classes (adjustable)
        pred_counts = [0] * 6

        for vertex in vertices:
            pred_value = vertex['class'] # changing vertex to class
            if 0 <= pred_value <= 5:
                pred_counts[pred_value] += 1

        results[filename] = pred_counts

# create a DataFrame and save it as a CSV file
df = pd.DataFrame.from_dict(results, orient='index', columns=[f'class={i}' for i in range(6)])
df.to_csv('class_counts.csv')

print("统计完成，结果已保存到 class_counts.csv")
