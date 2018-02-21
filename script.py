import csv
import re
import pandas as pd 
d = {}
with open('content.txt', 'r', encoding = 'utf8') as f:
    lines = f.readlines()
    for line in lines:
        if line == '\n' or len(line) < 3 :
            continue
        # extract_num = line[:7]
        # num =  re.findall('\d+', extract_num )
        num = line[0:5]
        content = line[5:].rstrip()
        d[num] = content
# print(d)
data_csv = []
with open('data.csv', 'r', encoding = 'utf8') as f:
    re = csv.reader(f)
  
    for idx, r in enumerate(re):
        # skip first three rows
        if(idx <= 2 or len(r) < 3):
            continue
        
        target_idx = r[0]

        # 14: content index 
        if target_idx in d:
            r[14] = d[target_idx]
            print(r)
        data_csv.append(r)    

writer = csv.writer(open('tmp.csv', 'w', encoding = 'utf8', newline=''))
writer.writerows(data_csv)
