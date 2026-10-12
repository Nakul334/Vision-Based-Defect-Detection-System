import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for i, p in enumerate(doc.paragraphs):
    if 'blip' in p._p.xml or 'pic:pic' in p._p.xml:
        print(f"P{i}: contains blip/pic. Text: {repr(p.text)}")
