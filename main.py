from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError

PDF_PATH = 'pdf/1.pdf'

#function to extract content from pdf
def extract_information(pdf_path: str) -> object:
    pdf = PdfReader(pdf_path)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about: {pdf_path}:
    
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information
#split using name_of_split
def split(path: str, name_of_split: str) -> int:
    pdf = PdfReader(path)
    page_count = 0
    for page in range(pdf.getNumPages()):
        page_count += 1
        pdf_writer = PdfWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
    return page_count


if __name__ == '__main__':
    page_count = split(PDF_PATH, 'n')
    counter = 0
    for file in range(page_count):
        print(page_count)
        pages = convert_from_path(f'n{file}.pdf')
        for page in pages:
            page.save(f'out{counter}.png', 'PNG')
            counter += 1