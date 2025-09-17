"""
Simple PDF Editor using PyPDF2 and reportlab
Issue #37 for king04aman/All-In-One-Python-Projects
"""
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# Insert text into a PDF (creates a new PDF with text overlay)
def insert_text(input_pdf, output_pdf, text, x=100, y=700):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(x, y, text)
    can.save()
    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)
    existing_pdf = PyPDF2.PdfReader(open(input_pdf, "rb"))
    writer = PyPDF2.PdfWriter()
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    writer.add_page(page)
    for p in existing_pdf.pages[1:]:
        writer.add_page(p)
    with open(output_pdf, "wb") as f:
        writer.write(f)

# Insert image into a PDF (creates a new PDF with image overlay)
def insert_image(input_pdf, output_pdf, image_path, x=100, y=500, w=200, h=150):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawImage(image_path, x, y, width=w, height=h)
    can.save()
    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)
    existing_pdf = PyPDF2.PdfReader(open(input_pdf, "rb"))
    writer = PyPDF2.PdfWriter()
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    writer.add_page(page)
    for p in existing_pdf.pages[1:]:
        writer.add_page(p)
    with open(output_pdf, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    # Example usage
    # insert_text("input.pdf", "output_text.pdf", "Hello PDF!", 100, 700)
    # insert_image("input.pdf", "output_image.pdf", "image.jpg", 100, 500, 200, 150)
    print("Simple PDF Editor ready. Uncomment example usage to test.")
