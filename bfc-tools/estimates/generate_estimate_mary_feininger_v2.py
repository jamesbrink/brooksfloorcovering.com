from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

OUTPUT = "/mnt/user-data/outputs/BFC Estimate Mary Feininger 20285 E Maya Rd Queen Creek Updated.pdf"

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
gold_data = [[Paragraph("Estimate", gold_l), Paragraph("Date: November 23, 2026", gold_r)]]
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
    [Paragraph("Mary Feininger", val_top_bold),
     Paragraph("616-690-2910", val_top),
     Paragraph("mjfeininger@yahoo.com", val_top)],
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
    [Paragraph("20285 E. Maya Rd, Queen Creek, AZ 85142", val_top)],
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
    [Paragraph("Casita — Shower, Bedroom Floor, Bathroom Floor, Concrete Prep", val_top)],
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
deduct_s = ParagraphStyle("DEDs", parent=styles["Normal"], fontSize=10,
    fontName="Helvetica-Oblique", textColor=colors.HexColor("#8B0000"), alignment=TA_RIGHT, leading=14)

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

# ══════════════════════════════════════════════════════════════
# SECTION 1: SHOWER
# ══════════════════════════════════════════════════════════════
shower_total = 4500.00
bench_deduct = 240.00

denshield_total = 462.00

shower_items = [
    ([Paragraph("Prep shower-pan, liner, drain, walls, waterproofing, build bench, install tile and trim", desc_s),
      Paragraph("Includes block, deck mud, liner, waterproofing, thinset, grout", detail_s),
      Paragraph("Tile to be installed on back wall and bench — side walls and curb to receive micro cement topping", detail_s),
      Paragraph("All walls, curb, and bench to be waterproofed", detail_s),
      Paragraph("Includes install of owner supplied porcelain subway tile on bench and vanity ledge", detail_s)],
     f"${shower_total:,.2f}"),
    ([Paragraph("Furnish and install Denshield backerboard", desc_s)],
     f"${denshield_total:,.2f}"),
    ([Paragraph("Option — Build bench only, no tile install on bench: deduct $240.00 from shower total", desc_s)],
     f"-${bench_deduct:,.2f}"),
]

story.append(KeepTogether([
    section_header("Shower"),
    col_header_row2(),
    line_items_table2(shower_items),
    total_row2("Shower Total", f"${shower_total + denshield_total:,.2f}"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# SECTION 2: TILE SELECTION
# ══════════════════════════════════════════════════════════════
tile_24_sf    = 298
tile_24_price = 5.16
tile_24_total = round(tile_24_sf * tile_24_price, 2)   # $1,537.68

tile_2x2_qty   = 14
tile_2x2_price = 11.20
tile_2x2_total = round(tile_2x2_qty * tile_2x2_price, 2)  # $156.80

tile_sel_total = tile_24_total + tile_2x2_total  # $1,694.48

tile_sel_items = [
    ([Paragraph("Furnish Arizona Tile Verazzo Avorio 24x24 Active R11 finish — shower walls, bath floor &amp; bedroom floor", desc_s)],
     f"{tile_24_sf} sqft", f"${tile_24_price:.2f}/sqft", f"${tile_24_total:,.2f}"),
    ([Paragraph("Furnish Arizona Tile Verazzo Avorio 2x2 sheet Active R11 finish — shower floor/pan", desc_s)],
     f"{tile_2x2_qty} sheets", f"${tile_2x2_price:.2f}/ea", f"${tile_2x2_total:,.2f}"),
]

story.append(KeepTogether([
    section_header("Tile Selection"),
    tile_col_header_row(),
    tile_line_items_table(tile_sel_items),
    tile_total_row("Tile Selection Total", f"${tile_sel_total:,.2f}"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# SECTION 3: TILE INSTALL
# ══════════════════════════════════════════════════════════════
install_sf    = 196
install_price = 5.25
install_total = round(install_sf * install_price, 2)  # $1,029.00

install_items = [
    ([Paragraph("Install Arizona Tile Verazzo Avorio 24x24 — bathroom &amp; bedroom floor", desc_s),
      Paragraph("Includes thinset and grout", detail_s)],
     f"{install_sf} sqft", f"${install_price:.2f}/sqft", f"${install_total:,.2f}"),
]

story.append(KeepTogether([
    section_header("Tile Install"),
    tile_col_header_row(),
    tile_line_items_table(install_items),
    tile_total_row("Tile Install Total", f"${install_total:,.2f}"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# SECTION 4: CONCRETE PREP
# ══════════════════════════════════════════════════════════════
concrete_prep_total = 200.00

concrete_items = [
    ([Paragraph("Grind concrete to remove paint", desc_s)],
     f"${concrete_prep_total:,.2f}"),
]

story.append(KeepTogether([
    section_header("Concrete Prep"),
    col_header_row2(),
    line_items_table2(concrete_items),
    total_row2("Concrete Prep Total", f"${concrete_prep_total:,.2f}"),
]))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════════
# TAX + GRAND TOTAL
# ══════════════════════════════════════════════════════════════
tax_amount  = 184.98
grand_total = shower_total + denshield_total + tile_sel_total + install_total + concrete_prep_total + tax_amount
# $4,500.00 + $462.00 + $1,694.48 + $1,029.00 + $200.00 + $184.98 = $8,070.46

# Tax row
tax_table = Table([[
    Paragraph("Tax", ParagraphStyle("TXL", parent=styles["Normal"], fontSize=10,
        fontName="Helvetica-Bold", textColor=DARK_BLUE, alignment=TA_RIGHT)),
    Paragraph(f"${tax_amount:,.2f}", amt_s),
]], colWidths=COL_W2)
tax_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), LIGHT_GRAY),
    ("TOPPADDING",    (0,0),(-1,-1), 7),
    ("BOTTOMPADDING", (0,0),(-1,-1), 7),
    ("LEFTPADDING",   (0,0),(-1,-1), 12),
    ("RIGHTPADDING",  (-1,0),(-1,-1), 12),
    ("BOX",           (0,0),(-1,-1), 0.5, MID_GRAY),
]))
story.append(tax_table)
story.append(Spacer(1, 4))

grand_style_l = ParagraphStyle("GTL", parent=styles["Normal"], fontSize=12,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_RIGHT)
grand_style_r = ParagraphStyle("GTR", parent=styles["Normal"], fontSize=12,
    fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_RIGHT)
grand_table = Table([[
    Paragraph("GRAND TOTAL", grand_style_l),
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
    "Does not include anti-fracture membrane, leveling, or excessive thinset  |  "
    "Does not include unforeseen framing or plumbing conditions",
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
