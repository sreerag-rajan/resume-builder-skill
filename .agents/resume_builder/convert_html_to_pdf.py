import sys
import os
import subprocess

def convert_html_to_pdf(html_path, pdf_path):
    try:
        if not os.path.exists(html_path):
            print(f"HTML file '{html_path}' not found!")
            sys.exit(1)
            
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        if not os.path.exists(edge_path):
            print("MS Edge not found. Please ensure it is installed.")
            sys.exit(1)
            
        abs_html = os.path.abspath(html_path)
        abs_pdf = os.path.abspath(pdf_path)
        
        # Edge headless print to pdf
        cmd = [
            edge_path,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={abs_pdf}",
            f"file:///{abs_html}"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully converted to {pdf_path}")
        else:
            print(f"Failed to convert HTML to PDF: {result.stderr}")
            sys.exit(1)
            
    except Exception as e:
        print(f"Exception during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        html = sys.argv[1]
        pdf = sys.argv[2]
    else:
        html = "output/resume.html"
        pdf = "output/resume.pdf"
        
    convert_html_to_pdf(html, pdf)
