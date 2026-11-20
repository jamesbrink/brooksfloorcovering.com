from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

OUTPUT = "/mnt/user-data/outputs/BFC Estimate Camelback Moving 17500 N Perimeter Dr Scottsdale.pdf"

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
gold_data = [[Paragraph("Estimate", gold_l), Paragraph("Date: November 20, 2026", gold_r)]]
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
    [Paragraph("Camelback Moving Inc.", val_top_bold),
     Paragraph("602-334-9585", val_top),
     Paragraph("Chris@camelbackmoving.com", val_top)],
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

# Contact name row
contact_table = Table([
    [Paragraph("Contact", lbl_top)],
    [Paragraph("Chris Sherman", val_top)],
], colWidths=[W])
contact_table.setStyle(TableStyle([
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
story.append(contact_table)

# Job address row
addr_table = Table([
    [Paragraph("Job Address", lbl_top)],
    [Paragraph("17500 N Perimeter Dr, Scottsdale, AZ 85255", val_top)],
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
    [Paragraph("Concrete Polishing and Joint Filler — 2nd Floor Vestibule &amp; Roof Access, 1st Floor Vestibule, Hall &amp; Transformer Room, 1st Floor Entrance &amp; Storage Room", val_top)],
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

# ── STYLES ────────────────────────────────────────────────────
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
qty_s    = ParagraphStyle("QS",  parent=styles["Normal"], fontSize=10,
    fontName="Helvetica", textColor=TEXT_DARK, alignment=TA_RIGHT, leading=14)

# 4-col: Description | Qty | Price | Amount
TILE_COL_W = [3.6*inch, 0.9*inch, 1.0*inch, 1.7*inch]
# 2-col: Description | Amount
COL_W2 = [5.4*inch, 1.8*inch]

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
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
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
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
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
# SECTION 1: CONCRETE POLISHING
# ══════════════════════════════════════════════════════════════
polish_sf    = 2094
polish_price = 4.25
polish_total = round(polish_sf * polish_price, 2)  # $8,899.50
spot_fill_total = 300.00

polish_items = [
    ([Paragraph("Furnish equipment, tooling, sealer, densifier, and labor", desc_s)], "", "", ""),
    ([Paragraph("Grinding process: 30/40, 60/80 metal — 50, 100, 400 ceramic — burnish", desc_s)], "", "", ""),
    ([Paragraph("Furnish and install Prosoco densifier — 1 coat", desc_s)], "", "", ""),
    ([Paragraph("Furnish and install Convergent Pentrafinish Polish Guard sealer — 1 coat", desc_s)], "", "", ""),
    ([Paragraph("Spot fill holes, cracks, spalls, and divots", desc_s)],
     "", "", f"${spot_fill_total:,.2f}"),
    ([Paragraph("Concrete polishing — 2nd floor vestibule &amp; roof access, 1st floor vestibule, hall &amp; transformer room, 1st floor entrance &amp; storage room", desc_s)],
     f"{polish_sf:,} SF", f"${polish_price:.2f}/SF", f"${polish_total:,.2f}"),
]

story.append(KeepTogether([
    section_header("Concrete Polishing"),
    tile_col_header_row(),
    tile_line_items_table(polish_items),
    tile_total_row("Polishing Total", f"${polish_total + spot_fill_total:,.2f}"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# SECTION 2: JOINT FILLER
# ══════════════════════════════════════════════════════════════
jf_lf    = 337
jf_price = 3.75
jf_total = round(jf_lf * jf_price, 2)  # $1,263.75

jf_items = [
    ([Paragraph("Prep joints, furnish and install Euclid Quick Joint UVR joint filler", desc_s)],
     f"{jf_lf} LF", f"${jf_price:.2f}/LF", f"${jf_total:,.2f}"),
]

story.append(KeepTogether([
    section_header("Joint Filler"),
    tile_col_header_row(),
    tile_line_items_table(jf_items),
    tile_total_row("Joint Filler Total", f"${jf_total:,.2f}"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# SECTION 3: OPTION — GROUT COAT
# ══════════════════════════════════════════════════════════════
grout_sf    = 2094
grout_price = 0.75
grout_total = round(grout_sf * grout_price, 2)  # $1,570.50

grout_items = [
    ([Paragraph("Option — Furnish and install TX3 grout coat material", desc_s),
      Paragraph(f"{grout_sf:,} SF @ ${grout_price:.2f}/SF", detail_s),
      Paragraph("<i>* Not included in the total</i>", ParagraphStyle("GN2", parent=styles["Normal"],
          fontSize=8.5, fontName="Helvetica-BoldOblique", textColor=colors.HexColor("#8B0000"), leading=12))],
     "", "", f"${grout_total:,.2f}"),
]

# Option header in gold
opt_hdr = Table([[Paragraph("Option — Grout Coat", ParagraphStyle("OH", parent=styles["Normal"],
    fontSize=11, fontName="Helvetica-Bold", textColor=colors.white))]], colWidths=[W])
opt_hdr.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), ACCENT_GOLD),
    ("TOPPADDING",    (0,0),(-1,-1), 7),
    ("BOTTOMPADDING", (0,0),(-1,-1), 7),
    ("LEFTPADDING",   (0,0),(-1,-1), 12),
]))

story.append(KeepTogether([
    opt_hdr,
    tile_col_header_row(),
    tile_line_items_table(grout_items),
    tile_total_row("Grout Coat Option Total", f"${grout_total:,.2f}"),
]))
story.append(Spacer(1, 12))

# ══════════════════════════════════════════════════════════════
# GRAND TOTAL (polishing + joint filler, excluding option)
# ══════════════════════════════════════════════════════════════
grand_total = polish_total + spot_fill_total + jf_total

grand_style_l = ParagraphStyle("GTL", parent=styles["Normal"], fontSize=12,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_RIGHT)
grand_style_r = ParagraphStyle("GTR", parent=styles["Normal"], fontSize=12,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_RIGHT)
grand_table = Table([[
    Paragraph("Total", grand_style_l),
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
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# TERMS / NOTES
# ══════════════════════════════════════════════════════════════
terms_style = ParagraphStyle("TS", parent=styles["Normal"], fontSize=8,
    fontName="Helvetica-Oblique", textColor=colors.HexColor("#555555"),
    alignment=TA_CENTER, leading=12)
terms_table = Table([[Paragraph(
    "Terms: Deposit Required  |  Balance due upon completion  |  Pricing valid for 30 days  |  "
    "Polish specific to steps called out — does not include cutting deeper or polishing higher  |  "
    "Price includes normal prep — any additional prep will be judged at time of install and billed accordingly  |  "
    "Must have access to water and 110V power  |  "
    "Not responsible for inconsistent aggregate exposure",
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
