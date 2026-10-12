import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

children = list(doc._body._element)
for idx in range(133, 140):
    c = children[idx]
    tag = c.tag.split('}')[-1]
    text = "".join(c.itertext())[:50].encode('ascii', 'replace').decode('ascii')
    print(f"Child {idx:03d} [{tag}]: {text}")
