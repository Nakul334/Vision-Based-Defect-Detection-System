with open(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Rice_Defect_Detection_OBB\paper\paper.tex', 'r', encoding='utf-8') as f:
    text = f.read()

import re

sections = re.findall(r'(\\section\{[^}]+\})', text)
print("Sections found:")
for s in sections:
    print(" ", s)
