import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for i, p in enumerate(doc.paragraphs):
    if 'graphic' in p._p.xml or 'drawing' in p._p.xml:
        print(f"P{i}: contains drawing/graphic. Text: {p.text}")
