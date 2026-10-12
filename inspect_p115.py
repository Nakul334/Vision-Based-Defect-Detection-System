import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for i in range(110, 125):
    p = doc.paragraphs[i]
    print(f"P{i} [{p.style.name}]: {p.text}")
