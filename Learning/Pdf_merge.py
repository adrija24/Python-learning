from pypdf import PdfWriter
import os
from pypdf import PdfWriter

folder = "PDFs"

merger = PdfWriter()

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        merger.append(os.path.join(folder, file))

merger.write("merged.pdf")
merger.close()