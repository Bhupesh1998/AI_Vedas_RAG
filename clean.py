with open("book.txt", "r", encoding="utf-8") as f:
    text = f.read()

# double newlines remove
text = text.replace("\n", "")

# multiple spaces normalize
text = " ".join(text.split())

with open("clean_book.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaned successfully")