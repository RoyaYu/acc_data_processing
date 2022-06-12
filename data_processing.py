import glob
# import pandas as pd
import csv
import re

data_folders = []
scaled_fac = 64

def scale (n):
    return int(float(n)/9.8*scaled_fac)

def data_extraction(lines):
    processed_lines = []
    for line in lines:
        line = line.decode("utf-8")
        if ("ACCL" in line):
            data = re.findall("\d+\.\d+", line)
            # print(data)
            data = list(map(scale, data))
            processed_lines.append(data)
    processed_lines.pop()
    print(processed_lines)
    return processed_lines;

for file_name in glob.glob('raw_data/'+'*.txt'):
    # data_frame = pd.read_csv (file_name,sep=",", encoding='Latin-1')
    # get the data name for saving it
    data_name = file_name.split(".txt")[0].split("/")[1]
    raw_lines = []
    print(file_name)
    with open(file_name,'rb') as f:
        raw_lines = f.readlines()
        # # print(raw_lines)
        # count = 0
        # for line in raw_lines:
        #     count += 1
        #     line = line.decode("utf-8")
        #     print(f'line {count}: {line}')
            # print(type(line.decode("utf-8")))
        processed_lines = data_extraction(raw_lines)


# # print(dataFolders)



## csv to txt
# csv_file = raw_input('Enter the name of your input file: ')
# txt_file = raw_input('Enter the name of your output file: ')
# with open(txt_file, "w") as my_output_file:
#     with open(csv_file, "r") as my_input_file:
#         [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
#     my_output_file.close()

## txt to csv
# read_file = pd.read_csv (r'Path where the Text file is stored\File name.txt')
# read_file.to_csv (r'Path where the CSV will be saved\File name.csv', index=None)
