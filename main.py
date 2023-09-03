from fpdf import FPDF
import pandas as pd

# Set PDF configuration
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Pandas
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Add main page Topic
    pdf.add_page()
    pdf.set_text_color(200, 100, 50)
    pdf.set_font(family="Courier", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Added lines into pdf main page
    for x in range(21,297,12):
        pdf.line(11, x, 201, x)

    # Set footers for main page
    pdf.ln(265)
    pdf.set_font(family="Courier", style="I", size=8)
    pdf.set_text_color(100, 200, 50)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    # Set footers for extra page
    for x in range(row["Pages"] - 1):
        pdf.add_page()
        # Added lines into pdf extra page
        for x in range(21, 297, 12):
            pdf.line(11, x, 201, x)
        pdf.ln(275)
        pdf.set_font(family="Courier", style="I", size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")