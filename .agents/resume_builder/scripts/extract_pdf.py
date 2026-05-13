import sys
import pymupdf

def extract_pdf_text(pdf_path):
    try:
        doc = pymupdf.open(pdf_path)
        for page in doc:
            print(page.get_text())
        doc.close()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <path_to_pdf>")
        sys.exit(1)
    
    extract_pdf_text(sys.argv[1])
