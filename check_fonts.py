"""
Check font names and sizes across all runs in Major_Project_Report_Final.docx.
"""

import docx

REPORT_PATH = r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_Project_Report_Final.docx'
doc = docx.Document(REPORT_PATH)

non_tnr_runs = 0
total_runs = 0

for p_idx, p in enumerate(doc.paragraphs):
    for r_idx, r in enumerate(p.runs):
        total_runs += 1
        font_name = r.font.name
        # If font_name is None, it inherits from style Normal or Heading
        if font_name and font_name != 'Times New Roman':
            non_tnr_runs += 1
            if non_tnr_runs <= 5:
                print(f"P{p_idx} R{r_idx}: font={font_name}, text={repr(r.text[:30])}")

for t_idx, t in enumerate(doc.tables):
    for r_idx, row in enumerate(t.rows):
        for c_idx, cell in enumerate(row.cells):
            for p in cell.paragraphs:
                for r in p.runs:
                    total_runs += 1
                    font_name = r.font.name
                    if font_name and font_name != 'Times New Roman':
                        non_tnr_runs += 1
                        if non_tnr_runs <= 5:
                            print(f"Table {t_idx} R{r_idx}C{c_idx}: font={font_name}, text={repr(r.text[:30])}")

print(f"Total Runs checked: {total_runs}")
print(f"Non-Times New Roman runs: {non_tnr_runs}")
