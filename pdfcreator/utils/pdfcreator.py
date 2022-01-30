from fpdf import FPDF

# Creates a new PDF from a text imput
def createpdf(texts):
    i = 0
    for text in texts:
        i += 1
        pdf = FPDF()
  
        # Add a page
        pdf.add_page()
        pdf.set_auto_page_break(True, margin = 0.0)
  
        # set style and size of font 
        # that you want in the pdf
        pdf.set_font("Arial", size = 15)
  
        # create a cell
        pdf.multi_cell(0, 5, txt = text, align = 'L', fill= False)
  
        # save the pdf with name .pdf
        pdf.output("test_" + str(i) + ".pdf")