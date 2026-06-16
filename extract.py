from pypdf import PdfReader

reader = PdfReader("BooksData/book_A.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

print(text[:5000])

with open(
    "book.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)

print("Done")