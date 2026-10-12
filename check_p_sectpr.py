import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for i, p in enumerate(doc.paragraphs):
    if p._p.pPr is not None and p._p.pPr.sectPr is not None:
        print(f"P{i:03d} has sectPr! Text: {repr(p.text)}")
