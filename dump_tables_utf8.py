with open(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Rice_Defect_Detection_OBB\paper\paper.tex', 'r', encoding='utf-8') as f:
    text = f.read()

import re

tables = re.findall(r'(\\begin\{table\*?\}.*?\\end\{table\*?\})', text, re.DOTALL)
with open(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\paper_tables_utf8.txt', 'w', encoding='utf-8') as out:
    for i, t in enumerate(tables):
        out.write(f"\n=================== TABLE {i+1} ===================\n")
        out.write(t + "\n")

print(f"Wrote {len(tables)} tables to paper_tables_utf8.txt")
