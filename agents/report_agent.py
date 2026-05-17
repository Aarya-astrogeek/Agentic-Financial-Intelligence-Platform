from fpdf import FPDF

def generate_report(text):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, text)

    output_path = "reports/financial_report.pdf"

    pdf.output(output_path)

    return output_path