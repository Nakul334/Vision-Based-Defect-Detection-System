import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for s_idx, sec in enumerate(doc.sections):
    print(f"\n================ SECTION {s_idx} ================")
    # python-docx doesn't directly map paragraphs to sections simply, but let's check sec.start_type
    print(f"Start type: {sec.start_type}")

# Let's inspect where page breaks or section breaks are
for i, p in enumerate(doc.paragraphs):
    has_page_break = False
    for r in p.runs:
        if '<w:br' in r._r.xml:
            has_page_break = True
    if has_page_break or 'Chapter' in p.text or 'Abstract' in p.text or 'Contents' in p.text or 'Approval' in p.text:
        print(f"P{i:03d} (br={has_page_break}): {p.text[:60]}")
