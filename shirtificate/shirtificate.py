from fpdf import FPDF
#pip install fpdf2
name = input("Name: ")
pdf = FPDF(orientation="P",unit="mm",format="A4")
pdf.add_page()
pdf.set_font("helvetica","B",50)
pdf.cell(0,60,"CS50 shirtificate",align="C")
pdf.image("shirtificate.png")
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
pdf.text(x=60,y=140, text=f"{name} took CS50")
pdf.output("shirtificate.pdf")
