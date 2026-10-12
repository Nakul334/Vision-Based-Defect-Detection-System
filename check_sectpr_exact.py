import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

children = list(doc._body._element)
for idx in range(78, 85):
    c = children[idx]
    tag = c.tag.split('}')[-1]
    has_sect = "YES" if c.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr/{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr') is not None else "NO"
    print(f"Child {idx:03d} [{tag}]: sectPr={has_sect}")
