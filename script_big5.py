import csv
import re, sys

if len(sys.argv) != 4:
    print('[Usage]: python script_big5.py [info_path] [csv_path] [result_path]')
    exit(1)
content_path = sys.argv[1]
csv_path = sys.argv[2]
result_path = sys.argv[3]

d = {}
with open(content_path, 'r', encoding = 'big5') as f:
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
with open(csv_path, 'r', encoding = 'big5') as f:
    re = csv.reader(f)
    for idx, r in enumerate(re):
        # skip first two rows
        if(idx <= 1 or len(r) < 3):
            continue
        target_idx = r[0]
        # 23: content index 文字描述
        if target_idx in d:
            nhm_header = "國立歷史博物館藏"
            artefact_name = r[4]
            r[23] = nhm_header + '《' + artefact_name + '》（' + target_idx + "），" +  d[target_idx]
        data_csv.append(r)    

writer = csv.writer(open(result_path, 'w', encoding = 'big5', newline=''))
writer.writerows(data_csv)
