import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for s_idx in [1, 2]:
    sec = doc.sections[s_idx]
    print(f"Section {s_idx} footer XML:")
    print(sec.footer._element.xml)
