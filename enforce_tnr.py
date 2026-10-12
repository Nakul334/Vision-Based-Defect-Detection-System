import os
import docx

for path in [
    r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_Project_Report_Final_v2.docx',
    r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_Project_Report_Final.docx'
]:
    if os.path.exists(path):
        try:
            doc = docx.Document(path)
            for p in doc.paragraphs:
                for r in p.runs:
                    r.font.name = 'Times New Roman'
            for t in doc.tables:
                for row in t.rows:
                    for cell in row.cells:
                        for p in cell.paragraphs:
                            for r in p.runs:
                                r.font.name = 'Times New Roman'
            doc.save(path)
            print(f"Enforced Times New Roman across 100% of runs in {os.path.basename(path)}!")
        except Exception as e:
            print(f"Skipping {os.path.basename(path)}: {e}")
