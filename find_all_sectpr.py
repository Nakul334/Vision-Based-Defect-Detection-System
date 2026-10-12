import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

children = list(doc._body._element)
for idx, c in enumerate(children):
    tag = c.tag.split('}')[-1]
    if tag == 'sectPr':
        print(f"Child {idx:03d} is body-level sectPr")
    elif tag == 'p':
        sect = c.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr/{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr')
        if sect is not None:
            text = "".join(c.itertext())[:40].encode('ascii', 'replace').decode('ascii')
            print(f"Child {idx:03d} [p] has sectPr: {repr(text)}")
