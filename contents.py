def get_book_text(p):
    book_contents = ""
    with open(f"{p}") as b:

        book_contents = b.read()
    return book_contents