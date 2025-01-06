import os
import pandas as pd
from plyfile import PlyData

# edit this path
input_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/test_output/Railway3D/withTrain_5cate_all_torch_17/'

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
            pred_value = vertex['pred']
            if 0 <= pred_value <= 5:
                pred_counts[pred_value] += 1

        results[filename] = pred_counts

# create a DataFrame and save it as a CSV file
df = pd.DataFrame.from_dict(results, orient='index', columns=[f'pred={i}' for i in range(6)])
df.to_csv('pred_counts.csv')

print("统计完成，结果已保存到 pred_counts.csv")
