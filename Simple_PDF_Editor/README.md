# Simple PDF Editor

A Python script using PyPDF2 and reportlab to edit PDF files. Supports text and image insertion.

## Features
- Insert text into PDF files
- Insert images into PDF files

## Usage
1. Install dependencies:
   ```bash
   pip install PyPDF2 reportlab
   ```
2. Use the functions in `pdf_editor.py`:
   ```python
   insert_text("input.pdf", "output_text.pdf", "Hello PDF!", 100, 700)
   insert_image("input.pdf", "output_image.pdf", "image.jpg", 100, 500, 200, 150)
   ```

## Requirements
- Python 3.x
- PyPDF2
- reportlab

## License
MIT
