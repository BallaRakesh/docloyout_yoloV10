import os
import shutil
folder1 = '/media/ntlpt19/5250315B5031474F/finance_data_modeling/Classification/benchmark_images/table_results/set_data/eval_data_master/images'
folder2 = '/media/ntlpt19/5250315B5031474F/finance_data_modeling/Classification/benchmark_images/table_results/set_data/Test_data/Images'
temp_folder = '/media/ntlpt19/5250315B5031474F/finance_data_modeling/Classification/benchmark_images/table_results/set_data/temp_fol'
os.makedirs(temp_folder, exist_ok=True)
sa = os.listdir(folder1)
for samp in os.listdir(folder2):
    if samp in sa:
        shutil.move(os.path.join(folder1, samp), temp_folder)
        print(f'Moved: {samp}')