from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

OUTPUT = "/mnt/user-data/outputs/BFC Estimate Ross Lukje 1130 E Mohawk Dr Phoenix Revised.pdf"

DARK_BLUE   = colors.HexColor("#1A3A5C")
MID_BLUE    = colors.HexColor("#2E6DA4")
LIGHT_BLUE  = colors.HexColor("#EAF2FB")
ACCENT_GOLD = colors.HexColor("#C8922A")
LIGHT_GRAY  = colors.HexColor("#F5F5F5")
MID_GRAY    = colors.HexColor("#CCCCCC")
TEXT_DARK   = colors.HexColor("#1C1C1C")
GREEN       = colors.HexColor("#1A7A3C")

doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=0.65*inch, rightMargin=0.65*inch,
    topMargin=0.45*inch, bottomMargin=0.45*inch,
)

styles = getSampleStyleSheet()
story = []
W = 7.2*inch

# ── LOGO HEADER ───────────────────────────────────────────────
logo = RLImage("/home/claude/bfc_logo_final.jpg", width=2.5*inch, height=0.55*inch)
contact_style = ParagraphStyle("CS", parent=styles["Normal"],
    fontSize=8, fontName="Helvetica", textColor=colors.HexColor("#444444"),
    alignment=TA_RIGHT, leading=12)
contact_info = (
    "4410 W. Union Hills Dr. Ste 7-125, Glendale AZ 85308<br/>"
    "P: 623-688-8422  |  Services@BrooksFloorCovering.com  |  ROC #226840"
)
header_table = Table([[logo, Paragraph(contact_info, contact_style)]],
                     colWidths=[2.8*inch, 4.4*inch])
header_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), colors.white),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("LEFTPADDING",   (0,0),(0,-1),  0),
    ("RIGHTPADDING",  (1,0),(1,-1),  0),
    ("LINEBELOW",     (0,0),(-1,-1), 2, DARK_BLUE),
]))
story.append(header_table)
story.append(Spacer(1, 5))

# ── GOLD SUBHEADER ────────────────────────────────────────────
gold_l = ParagraphStyle("GL", parent=styles["Normal"], fontSize=10,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_LEFT)
gold_r = ParagraphStyle("GR", parent=styles["Normal"], fontSize=10,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_RIGHT)
gold_data = [[Paragraph("Estimate", gold_l), Paragraph("Date: November 13, 2026", gold_r)]]
gold_table = Table(gold_data, colWidths=[3.6*inch, 3.6*inch])
gold_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), ACCENT_GOLD),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("LEFTPADDING",   (0,0),(0,-1),  12),
    ("RIGHTPADDING",  (1,0),(1,-1),  12),
]))
story.append(gold_table)

# ── CUSTOMER INFO ─────────────────────────────────────────────
lbl_top      = ParagraphStyle("LTOP",  parent=styles["Normal"], fontSize=7,
    fontName="Helvetica-Bold", textColor=colors.HexColor("#888888"), leading=9)
val_top      = ParagraphStyle("VTOP",  parent=styles["Normal"], fontSize=9,
    fontName="Helvetica", textColor=TEXT_DARK, leading=13)
val_top_bold = ParagraphStyle("VTOPB", parent=styles["Normal"], fontSize=9,
    fontName="Helvetica-Bold", textColor=DARK_BLUE, leading=13)

cust_table = Table([
    [Paragraph("Customer", lbl_top), Paragraph("Phone", lbl_top), Paragraph("Email", lbl_top)],
    [Paragraph("Ross Lukje", val_top_bold),
     Paragraph("480-297-5004", val_top),
     Paragraph("rosslukje@hotmail.com", val_top)],
], colWidths=[2.4*inch, 1.8*inch, 3.0*inch])
cust_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), LIGHT_GRAY),
    ("TOPPADDING",    (0,0),(-1,0),  5),
    ("BOTTOMPADDING", (0,0),(-1,0),  1),
    ("TOPPADDING",    (0,1),(-1,1),  2),
    ("BOTTOMPADDING", (0,1),(-1,1),  6),
    ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ("LINEAFTER",     (0,0),(1,-1),  0.5, MID_GRAY),
    ("LINEBELOW",     (0,1),(-1,1),  1.5, DARK_BLUE),
    ("VALIGN",        (0,0),(-1,-1), "TOP"),
]))
story.append(cust_table)

# Job address row
addr_table = Table([
    [Paragraph("Job Address", lbl_top)],
    [Paragraph("1130 East Mohawk Dr., Phoenix, AZ 85024", val_top)],
], colWidths=[W])
addr_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), LIGHT_GRAY),
    ("TOPPADDING",    (0,0),(-1,0),  4),
    ("BOTTOMPADDING", (0,0),(-1,0),  1),
    ("TOPPADDING",    (0,1),(-1,1),  2),
    ("BOTTOMPADDING", (0,1),(-1,1),  6),
    ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ("LINEBELOW",     (0,1),(-1,1),  1, MID_GRAY),
    ("VALIGN",        (0,0),(-1,-1), "TOP"),
]))
story.append(addr_table)

# Scope of work row
scope_table = Table([
    [Paragraph("Scope of Work", lbl_top)],
    [Paragraph("Floor Preparation — Grinding, Self-Leveling, Baseboard and Vinyl Plank Installation", val_top)],
], colWidths=[W])
scope_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), LIGHT_GRAY),
    ("TOPPADDING",    (0,0),(-1,0),  4),
    ("BOTTOMPADDING", (0,0),(-1,0),  1),
    ("TOPPADDING",    (0,1),(-1,1),  2),
    ("BOTTOMPADDING", (0,1),(-1,1),  6),
    ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ("LINEBELOW",     (0,1),(-1,1),  1, MID_GRAY),
    ("VALIGN",        (0,0),(-1,-1), "TOP"),
]))
story.append(scope_table)
story.append(Spacer(1, 10))

# ── SECTION HEADER ────────────────────────────────────────────
def section_header(text):
    t = Table([[Paragraph(text, ParagraphStyle("SH", parent=styles["Normal"],
        fontSize=11, fontName="Helvetica-Bold", textColor=colors.white))]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), MID_BLUE),
        ("TOPPADDING",    (0,0),(-1,-1), 7),
        ("BOTTOMPADDING", (0,0),(-1,-1), 7),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
    ]))
    return t

# Styles
ch   = ParagraphStyle("CH",  parent=styles["Normal"], fontSize=8,
    fontName="Helvetica-Bold", textColor=colors.HexColor("#555555"))
ch_r = ParagraphStyle("CHR", parent=styles["Normal"], fontSize=8,
    fontName="Helvetica-Bold", textColor=colors.HexColor("#555555"), alignment=TA_RIGHT)
desc_s   = ParagraphStyle("DS",  parent=styles["Normal"], fontSize=10,
    fontName="Helvetica", textColor=TEXT_DARK, leading=14)
detail_s = ParagraphStyle("DT",  parent=styles["Normal"], fontSize=8.5,
    fontName="Helvetica-Oblique", textColor=colors.HexColor("#555555"), leading=12)
amt_s    = ParagraphStyle("AS",  parent=styles["Normal"], fontSize=10,
    fontName="Helvetica-Bold", textColor=TEXT_DARK, alignment=TA_RIGHT, leading=14)
amt_grn  = ParagraphStyle("AG",  parent=styles["Normal"], fontSize=10,
    fontName="Helvetica-Bold", textColor=GREEN, alignment=TA_RIGHT, leading=14)

# 4-col layout: Description | Qty | Price | Amount
TILE_COL_W = [3.6*inch, 0.9*inch, 1.0*inch, 1.7*inch]
# 2-col layout for totals and simple sections
COL_W2 = [5.4*inch, 1.8*inch]

qty_s = ParagraphStyle("QS", parent=styles["Normal"], fontSize=10,
    fontName="Helvetica", textColor=TEXT_DARK, alignment=TA_RIGHT, leading=14)

def tile_col_header_row():
    t = Table([[Paragraph("Description", ch), Paragraph("Qty", ch_r),
                Paragraph("Price", ch_r), Paragraph("Amount", ch_r)]], colWidths=TILE_COL_W)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), LIGHT_GRAY),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
        ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
        ("LINEBELOW",     (0,0),(-1,-1), 0.5, MID_GRAY),
        ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
    ]))
    return t

def tile_line_items_table(items):
    rows = []
    for desc_paras, qty_str, price_str, amt_str in items:
        rows.append([desc_paras, Paragraph(qty_str, qty_s),
                     Paragraph(price_str, qty_s), Paragraph(amt_str, amt_s)])
    t = Table(rows, colWidths=TILE_COL_W)
    t.setStyle(TableStyle([
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
        ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
        ("LINEBELOW",     (0,0),(-1,-2), 0.5, MID_GRAY),
        ("BACKGROUND",    (0,0),(-1,-1), LIGHT_BLUE),
    ]))
    return t

def tile_total_row(label, amount):
    t = Table([[
        Paragraph(label, ParagraphStyle("TL2", parent=styles["Normal"], fontSize=10,
            fontName="Helvetica-Bold", textColor=DARK_BLUE, alignment=TA_RIGHT)),
        Paragraph(amount, amt_grn),
    ]], colWidths=COL_W2)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), LIGHT_BLUE),
        ("TOPPADDING",    (0,0),(-1,-1), 7),
        ("BOTTOMPADDING", (0,0),(-1,-1), 7),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
        ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
        ("LINEABOVE",     (0,0),(-1,0),  1.5, MID_BLUE),
        ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
    ]))
    return t

# 2-col helper for simple sections
def col_header_row2():
    t = Table([[Paragraph("Description", ch), Paragraph("Amount", ch_r)]], colWidths=COL_W2)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), LIGHT_GRAY),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
        ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
        ("LINEBELOW",     (0,0),(-1,-1), 0.5, MID_GRAY),
        ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
    ]))
    return t

def line_items_table2(items):
    rows = []
    for desc_paras, amt_str in items:
        rows.append([desc_paras, Paragraph(amt_str, amt_s)])
    t = Table(rows, colWidths=COL_W2)
    t.setStyle(TableStyle([
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
        ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
        ("LINEBELOW",     (0,0),(-1,-2), 0.5, MID_GRAY),
        ("BACKGROUND",    (0,0),(-1,-1), LIGHT_BLUE),
    ]))
    return t

def total_row2(label, amount):
    t = Table([[
        Paragraph(label, ParagraphStyle("TL3", parent=styles["Normal"], fontSize=10,
            fontName="Helvetica-Bold", textColor=DARK_BLUE, alignment=TA_RIGHT)),
        Paragraph(amount, amt_grn),
    ]], colWidths=COL_W2)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), LIGHT_BLUE),
        ("TOPPADDING",    (0,0),(-1,-1), 7),
        ("BOTTOMPADDING", (0,0),(-1,-1), 7),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
        ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
        ("LINEABOVE",     (0,0),(-1,0),  1.5, MID_BLUE),
        ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
    ]))
    return t

# ══════════════════════════════════════════════════════════════
# SECTION 1: FLOOR GRINDING
# ══════════════════════════════════════════════════════════════
grinding_items = [
    ([Paragraph("32\" machine grinding — grind cracks and peaks to minimize high spots", desc_s)],
     "Per hr", "$250.00/hr", ""),
    ([Paragraph("17\" machine grinding — grind cracks and peaks to minimize high spots", desc_s)],
     "Per hr", "$125.00/hr", ""),
    ([Paragraph("Hand grinding — detail and edge work where needed", desc_s)],
     "Included", "", ""),
    ([Paragraph("Minimum charge — grinding", desc_s),
      Paragraph("Final hours billed after completion", detail_s)],
     "", "", "$1,200.00"),
]

story.append(KeepTogether([
    section_header("Floor Grinding"),
    tile_col_header_row(),
    tile_line_items_table(grinding_items),
    tile_total_row("Grinding Minimum", "$1,200.00"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# SECTION 2: SELF-LEVELER
# ══════════════════════════════════════════════════════════════
leveler_items = [
    ([Paragraph("Install self-leveler to help minimize undulations in floor — includes primer, material, and labor", desc_s),
      Paragraph("Uzin NC 150 self-leveler  |  Uzin PE 260 primer", detail_s),
      Paragraph("Estimated 8 bags — final bag count billed at actual quantity used after grinding", detail_s)],
     "Est. 8 bags", "$75.00/bag", "$600.00"),
]

story.append(KeepTogether([
    section_header("Self-Leveler"),
    tile_col_header_row(),
    tile_line_items_table(leveler_items),
    tile_total_row("Self-Leveler Total (Est.)", "$600.00"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# SECTION 3: FLOORING INSTALL
# ══════════════════════════════════════════════════════════════
bb_lf    = 220
bb_price = 3.75
bb_total = round(bb_lf * bb_price, 2)   # $825.00

vp_sf    = 1184
vp_price = 2.75
vp_total = round(vp_sf * vp_price, 2)   # $506.00

install_total = bb_total + vp_total      # $1,331.00

install_items = [
    ([Paragraph("Install owner supplied baseboard", desc_s)],
     f"{bb_lf} LF", f"${bb_price:.2f}/LF", f"${bb_total:,.2f}"),
    ([Paragraph("Install owner supplied vinyl plank and underlayment", desc_s)],
     f"{vp_sf} SF", f"${vp_price:.2f}/SF", f"${vp_total:,.2f}"),
]

story.append(KeepTogether([
    section_header("Flooring Install"),
    tile_col_header_row(),
    tile_line_items_table(install_items),
    tile_total_row("Install Total", f"${install_total:,.2f}"),
]))
story.append(Spacer(1, 12))

# ══════════════════════════════════════════════════════════════
# GRAND TOTAL
# ══════════════════════════════════════════════════════════════
grinding_min  = 1200.00
leveler_est   = 600.00
grand_total   = grinding_min + leveler_est + install_total

grand_style_l = ParagraphStyle("GTL", parent=styles["Normal"], fontSize=12,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_RIGHT)
grand_style_r = ParagraphStyle("GTR", parent=styles["Normal"], fontSize=12,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_RIGHT)
grand_table = Table([[
    Paragraph("Estimated Total", grand_style_l),
    Paragraph(f"${grand_total:,.2f}", grand_style_r),
]], colWidths=COL_W2)
grand_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), DARK_BLUE),
    ("TOPPADDING",    (0,0),(-1,-1), 10),
    ("BOTTOMPADDING", (0,0),(-1,-1), 10),
    ("LEFTPADDING",   (0,0),(-1,-1), 12),
    ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
]))
story.append(grand_table)
story.append(Spacer(1, 4))

note_est_style = ParagraphStyle("NES", parent=styles["Normal"], fontSize=7.5,
    fontName="Helvetica-Oblique", textColor=colors.HexColor("#666666"), alignment=TA_RIGHT)
story.append(Paragraph("* Total is an estimate. Self-leveler billed at actual bag count after grinding.", note_est_style))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# TERMS / NOTES
# ══════════════════════════════════════════════════════════════
terms_style = ParagraphStyle("TS", parent=styles["Normal"], fontSize=8,
    fontName="Helvetica-Oblique", textColor=colors.HexColor("#555555"),
    alignment=TA_CENTER, leading=12)
terms_table = Table([[Paragraph(
    "Terms: Deposit Required  |  Balance due upon completion  |  Pricing valid for 30 days  |  "
    "Self-leveler bag count billed at actual quantity used after grinding assessment  |  "
    "Customer to supply 110V power, 240V power, and water  |  "
    "Baseboard and vinyl plank measurements per Ross",
    terms_style)]], colWidths=[W])
terms_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), LIGHT_GRAY),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
]))
story.append(terms_table)
story.append(Spacer(1, 10))

# ── CUSTOMER SIGNATURE ────────────────────────────────────────
sig_lbl = ParagraphStyle("SL", parent=styles["Normal"], fontSize=9,
    fontName="Helvetica-Bold", textColor=DARK_BLUE)
sig_table = Table([[Paragraph("Customer Signature:", sig_lbl), ""]], colWidths=[2.5*inch, W - 2.5*inch])
sig_table.setStyle(TableStyle([
    ("BOX",           (0,0),(-1,-1), 0.75, DARK_BLUE),
    ("BACKGROUND",    (0,0),(-1,-1), colors.white),
    ("TOPPADDING",    (0,0),(-1,-1), 14),
    ("BOTTOMPADDING", (0,0),(-1,-1), 14),
    ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ("LINEAFTER",     (0,0),(0,0),   0.5, MID_GRAY),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
]))
story.append(sig_table)
story.append(Spacer(1, 14))

# ── FOOTER ────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=1, color=MID_GRAY))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Brooks Floor Covering  |  brooksfloorcovering.com  |  ROC #226840  |  Services@BrooksFloorCovering.com",
    ParagraphStyle("Ft", parent=styles["Normal"], fontSize=8,
        fontName="Helvetica", textColor=colors.HexColor("#999999"), alignment=TA_CENTER)))

doc.build(story)
print(f"Done → {OUTPUT}")

# ── APPEND T&C ────────────────────────────────────────────────
from pypdf import PdfReader, PdfWriter

TC_PATH = "/mnt/user-data/outputs/BFC_Terms_and_Conditions_Updated.pdf"
writer = PdfWriter()
for page in PdfReader(OUTPUT).pages:
    writer.add_page(page)
for page in PdfReader(TC_PATH).pages:
    writer.add_page(page)
with open(OUTPUT, "wb") as f:
    writer.write(f)
print("T&C appended.")
