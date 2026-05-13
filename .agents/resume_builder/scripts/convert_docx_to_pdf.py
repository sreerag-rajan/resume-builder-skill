import os
import sys
import win32com.client

def convert_docx_to_pdf(docx_path, pdf_path):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    
    try:
        doc = word.Documents.Open(os.path.abspath(docx_path))
        doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17) # 17 is wdFormatPDF
        doc.Close()
        print(f"Successfully converted to {pdf_path}")
    except Exception as e:
        print(f"Failed to convert: {e}")
    finally:
        word.Quit()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        docx = sys.argv[1]
        pdf = sys.argv[2]
    else:
        docx = "output/resume.docx"
        pdf = "output/resume.pdf"
        
    if os.path.exists(docx):
        convert_docx_to_pdf(docx, pdf)
    else:
        print(f"DOCX file '{docx}' not found!")
