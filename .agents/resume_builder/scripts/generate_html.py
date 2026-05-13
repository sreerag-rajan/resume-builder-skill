import sys
import os
import markdown

def generate_html(md_path, css_path, html_path):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Remove YAML frontmatter if present
        import re
        md_content = re.sub(r'^---.*?---', '', md_content, flags=re.DOTALL).strip()

        # Support manual page breaks
        md_content = md_content.replace('<!-- PAGE BREAK -->', '<div class="page-break"></div>')

        # Convert to HTML
        html_body = markdown.markdown(md_content)

        # Read CSS
        css_content = ""
        if os.path.exists(css_path):
            with open(css_path, 'r', encoding='utf-8') as f:
                css_content = f.read()

        # Wrap in HTML template
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Resume</title>
    <style>
{css_content}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        print(f"Successfully generated {html_path}")
    except Exception as e:
        print(f"Failed to generate HTML: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        generate_html(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        # Default paths relative to project root
        md = "output/resume.md"
        css = ".agents/resume_builder/templates/style.css"
        html = "output/resume.html"
        generate_html(md, css, html)
