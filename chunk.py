import json

with open(
    "clean_book.txt",
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

words = text.split()

chunks = []

current = ""

for word in words:

    if len(current) + len(word) < 1500:

        current += word + " "

    else:

        chunks.append(current.strip())

        current = word + " "

if current:
    chunks.append(current.strip())

with open(
    "chunks.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        chunks,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Total Chunks: {len(chunks)}")
print(chunks[0][:500])