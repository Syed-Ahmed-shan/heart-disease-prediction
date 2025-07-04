from fpdf import FPDF
import os
import unicodedata

# 🔧 Utility to clean Unicode to ASCII (removes problematic characters like — “” etc.)
def clean_text(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

def save_report_to_pdf(patient_id, report_text, output_folder='output/reports'):
    os.makedirs(output_folder, exist_ok=True)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, f"Patient Report - ID: {patient_id}", ln=True, align='C')

    pdf.set_font("Arial", '', 12)

    # ✅ Clean text to prevent Unicode errors
    cleaned_report = clean_text(report_text)

    lines = cleaned_report.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)

    file_path = os.path.join(output_folder, f"patient_{patient_id}.pdf")
    pdf.output(file_path)
    print(f"✅ Saved PDF: {file_path}")
