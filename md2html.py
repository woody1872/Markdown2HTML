import markdown as md
import os

md_file = os.path.abspath("test.md")
html_file = f"{os.path.dirname(md_file)}/test.html"
md.markdownFromFile(input=md_file, output=html_file)

with open(html_file, "r+", encoding="utf-8") as f:
  html = f"""<html>
<head>
<title>
</title>
</head>
<body>
{f.read()}
</body>
</html>"""
  f.seek(0)
  f.write(html)
  # f.truncate()