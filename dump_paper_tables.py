with open(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Rice_Defect_Detection_OBB\paper\paper.tex', 'r', encoding='utf-8') as f:
    text = f.read()

import re

tables = re.findall(r'(\\begin\{table\*?\}.*?\\end\{table\*?\})', text, re.DOTALL)
for i, t in enumerate(tables):
    print(f"\n=================== TABLE {i+1} ===================")
    print(t)
