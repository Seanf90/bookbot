from stats import num_of_words, num_of_characters

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = num_of_words(contents)
    print(f"{num_words} words found in the document")
    print(num_of_characters(contents))
main()


    