import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

element_order = []
for child in doc._body._element:
    tag = child.tag.split('}')[-1]
    if tag == 'p':
        element_order.append(('p', child))
    elif tag == 'tbl':
        element_order.append(('tbl', child))
    elif tag == 'sectPr':
        element_order.append(('sectPr', child))

print("Total body children:", len(element_order))
p_count = 0
tbl_count = 0
for idx, (kind, elem) in enumerate(element_order):
    if kind == 'tbl':
        print(f"Child {idx}: TABLE {tbl_count} after P{p_count-1}")
        tbl_count += 1
    elif kind == 'sectPr':
        print(f"Child {idx}: SECTPR after P{p_count-1}")
    elif kind == 'p':
        p_count += 1
