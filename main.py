import uuid
from pypdf import PdfReader, PdfWriter


def create_new_file(pdf_reader: PdfReader, pdf_writer: PdfWriter) -> None:
    file_name = pdf_reader.metadata.title
    trailing_code = uuid.uuid1().hex

    with open(f"{file_name}-{trailing_code}.pdf", "wb") as f:
        pdf_writer.write(f)


def add_pages_to_writer_object(pdf_reader: PdfReader, pages_to_keep: list[int]):
    new_pdf_writer = PdfWriter()

    for page_index in pages_to_keep:
        page = pdf_reader.pages[page_index - 1]
        new_pdf_writer.add_page(page)

    return new_pdf_writer


def main(
    pdf_path: str = "./Amit Solanki Resume.pdf",
    pages_to_keep: list[int] = [
        1,
    ],
) -> None:
    pdf_reader = PdfReader(pdf_path, "rb")
    new_pdf_writer = add_pages_to_writer_object(pdf_reader, pages_to_keep)
    create_new_file(pdf_reader, new_pdf_writer)


if __name__ == "__main__":
    main()
