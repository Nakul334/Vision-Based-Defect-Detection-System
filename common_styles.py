"""
Common styling, formatting, and helper utilities for Major Project Report generation.
Enforces Times New Roman, 12pt body, 1.5 line spacing, justified alignment,
chapter-wise figure/table captions, and professional table borders.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

COLOR_NAVY = RGBColor(31, 78, 120)     # #1F4E78
COLOR_DARK = RGBColor(33, 33, 33)      # Body text
COLOR_MUTED = RGBColor(80, 80, 80)    # Captions/secondary

def configure_document_styles(doc):
    """Enforce Times New Roman throughout the document styles."""
    styles = doc.styles
    
    # Normal style
    normal = styles['Normal']
    normal.font.name = 'Times New Roman'
    normal.font.size = Pt(12)
    normal.font.color.rgb = COLOR_DARK
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Heading 1
    h1 = styles['Heading 1']
    h1.font.name = 'Times New Roman'
    h1.font.size = Pt(16)
    h1.font.bold = True
    h1.font.color.rgb = COLOR_NAVY
    h1.paragraph_format.line_spacing = 1.15
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)
    h1.paragraph_format.keep_with_next = True
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    # Heading 2
    h2 = styles['Heading 2']
    h2.font.name = 'Times New Roman'
    h2.font.size = Pt(14)
    h2.font.bold = True
    h2.font.color.rgb = COLOR_NAVY
    h2.paragraph_format.line_spacing = 1.15
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(4)
    h2.paragraph_format.keep_with_next = True
    h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    # Heading 3
    h3 = styles['Heading 3']
    h3.font.name = 'Times New Roman'
    h3.font.size = Pt(12)
    h3.font.bold = True
    h3.font.color.rgb = COLOR_DARK
    h3.paragraph_format.line_spacing = 1.15
    h3.paragraph_format.space_before = Pt(6)
    h3.paragraph_format.space_after = Pt(2)
    h3.paragraph_format.keep_with_next = True
    h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

def add_p(doc, text, bold=False, italic=False, space_after=6, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    """Add a body paragraph formatted strictly to academic standards."""
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = COLOR_DARK
    run.bold = bold
    run.italic = italic
    return p

def add_h1(doc, text, is_chapter=False):
    """Add a major heading (Heading 1). If chapter title, format prominently."""
    p = doc.add_paragraph(style='Heading 1')
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(16 if is_chapter else 12)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p

def add_h2(doc, text):
    """Add a section heading (Heading 2)."""
    p = doc.add_paragraph(style='Heading 2')
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p

def add_h3(doc, text):
    """Add a subsection heading (Heading 3)."""
    p = doc.add_paragraph(style='Heading 3')
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = COLOR_DARK
    return p

def add_bullet(doc, text, bold_prefix=""):
    """Add a bullet item using Normal style with hanging indentation."""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    r_bullet = p.add_run("•  ")
    r_bullet.font.name = 'Times New Roman'
    r_bullet.font.size = Pt(12)
    r_bullet.bold = True
    r_bullet.font.color.rgb = COLOR_NAVY
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(12)
        r_pre.bold = True
        r_pre.font.color.rgb = COLOR_DARK
        
    r_txt = p.add_run(text)
    r_txt.font.name = 'Times New Roman'
    r_txt.font.size = Pt(12)
    r_txt.font.color.rgb = COLOR_DARK
    return p

def add_figure(doc, img_path, caption_text, width_inches=5.8):
    """Insert an image and its corresponding formal caption."""
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    p_img.paragraph_format.keep_with_next = True
    
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(width_inches))
    
    # Caption
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(12)
    p_cap.paragraph_format.line_spacing = 1.15
    
    # Split "Figure X.Y: Description"
    parts = caption_text.split(":", 1)
    if len(parts) == 2:
        r_pre = p_cap.add_run(parts[0] + ":")
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_NAVY
        
        r_desc = p_cap.add_run(parts[1])
        r_desc.font.name = 'Times New Roman'
        r_desc.font.size = Pt(10.5)
        r_desc.italic = True
        r_desc.font.color.rgb = COLOR_MUTED
    else:
        r_txt = p_cap.add_run(caption_text)
        r_txt.font.name = 'Times New Roman'
        r_txt.font.size = Pt(10.5)
        r_txt.italic = True
        r_txt.font.color.rgb = COLOR_MUTED

def add_equation(doc, eq_text, eq_num_str):
    """Insert a formal mathematical equation with aligned equation number."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    
    p.paragraph_format.tab_stops.add_tab_stop(Inches(5.75), docx.enum.text.WD_TAB_ALIGNMENT.RIGHT)
    
    r_eq = p.add_run(eq_text)
    r_eq.font.name = 'Times New Roman'
    r_eq.font.size = Pt(11)
    r_eq.italic = True
    r_eq.bold = True
    
    r_tab = p.add_run("\t")
    
    r_num = p.add_run(f"({eq_num_str})")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(11)
    r_num.bold = True

def add_custom_table(doc, title_text, headers, rows_data, col_widths, col_alignments=None, header_bg="1F4E78"):
    """Insert a fully styled publication-grade academic table."""
    p_cap = doc.add_paragraph()
    p_cap.paragraph_format.keep_with_next = True
    p_cap.paragraph_format.space_before = Pt(10)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.line_spacing = 1.15
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    parts = title_text.split(":", 1)
    if len(parts) == 2:
        r_pre = p_cap.add_run(parts[0] + ":")
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_NAVY
        
        r_desc = p_cap.add_run(parts[1])
        r_desc.font.name = 'Times New Roman'
        r_desc.font.size = Pt(11)
        r_desc.bold = True
        r_desc.font.color.rgb = COLOR_DARK
    else:
        r_txt = p_cap.add_run(title_text)
        r_txt.font.name = 'Times New Roman'
        r_txt.font.size = Pt(11)
        r_txt.bold = True

    table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Table borders
    tblPr = table._tbl.tblPr
    borders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="1F4E78"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="1F4E78"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
        f'  <w:insideV w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders_xml)
    
    if col_alignments is None:
        col_alignments = [WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.CENTER] * (len(headers) - 1)
        
    hdr_row = table.rows[0]
    hdr_trPr = hdr_row._tr.get_or_add_trPr()
    hdr_trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    hdr_trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    
    for c_idx, h_text in enumerate(headers):
        cell = hdr_row.cells[c_idx]
        cell.width = Inches(col_widths[c_idx])
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="150" w:type="dxa"/><w:right w:w="150" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)
        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{header_bg}"/>'))
        
        p = cell.paragraphs[0]
        p.alignment = col_alignments[c_idx]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_idx, r_data in enumerate(rows_data):
        row = table.rows[r_idx + 1]
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        
        is_even = (r_idx % 2 == 1)
        bg_fill = "F7F9FB" if is_even else "FFFFFF"
        
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.width = Inches(col_widths[c_idx])
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            tcPr = cell._tc.get_or_add_tcPr()
            tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="100" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/><w:left w:w="150" w:type="dxa"/><w:right w:w="150" w:type="dxa"/></w:tcMar>')
            tcPr.append(tcMar)
            if is_even:
                tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_fill}"/>'))
                
            p = cell.paragraphs[0]
            p.alignment = col_alignments[c_idx]
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            
            val_str = str(val)
            is_bold = val_str.startswith("**") and val_str.endswith("**")
            if is_bold:
                val_str = val_str[2:-2]
                
            r = p.add_run(val_str)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            r.font.bold = is_bold
            r.font.color.rgb = COLOR_DARK
            
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(6)
    return table

def set_page_number_footer(sec, fmt="decimal", start=1):
    """Set dynamic page number field in section footer."""
    sec.different_first_page_header_footer = False
    footer = sec.footer
    footer.is_linked_to_previous = False
    
    sectPr = sec._sectPr
    for child in sectPr.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pgNumType'):
        sectPr.remove(child)
    
    pgNum = parse_xml(f'<w:pgNumType {nsdecls("w")} w:fmt="{fmt}" w:start="{start}"/>')
    sectPr.append(pgNum)
    
    for p in footer.paragraphs:
        p._p.getparent().remove(p._p)
        
    p = footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fld_xml = parse_xml(
        f'<w:p {nsdecls("w")}>'
        f'  <w:pPr><w:jc w:val="center"/></w:pPr>'
        f'  <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
        f'  <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
        f'  <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r>'
        f'  <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/></w:rPr><w:t>1</w:t></w:r>'
        f'  <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>'
        f'</w:p>'
    )
    p._p.getparent().replace(p._p, fld_xml)

print("Updated common_styles.py successfully.")
