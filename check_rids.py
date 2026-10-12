import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for idx in [2, 22, 115]:
    p = doc.paragraphs[idx]
    xml = p._p.xml
    print(f"P{idx}:")
    for rId in ['rId1', 'rId2', 'rId3', 'rId4', 'rId5', 'rId6', 'rId7', 'rId8']:
        if rId in xml:
            rel = doc.part.rels[rId]
            print(f"  {rId} -> {rel.target_ref}")
