import os
import pandas as pd

path_annotation = '/Users/devasou/Desktop/OrnithoMate/p0133_bird_data/annotations/'
path_raw_data = '/Users/devasou/Desktop/OrnithoMate/p0133_bird_data/raw_data/'
tasks_dir = sorted(os.listdir(path_annotation))
unwanted_labels_list = ['unknown', 'human', 'noBird']
columns_input_data = ["split_value", "file_path", "label", "x_min", "y_min", "empty_1", "empty_2", "x_max", "y_max",
                      "empty_3"]
df_input = pd.DataFrame(columns=columns_input_data)
path_and_name_csv = '/Users/devasou/Desktop/input.csv'
