import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str):

    document = fitz.open(pdf_path)

    extracted_text = ""

    for page in document:

        text = page.get_text()

        extracted_text += text + "\n"

    document.close()

    return extracted_text

