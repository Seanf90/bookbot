from stats import num_of_words, num_of_characters, sort_dictionary, generate_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def print_full_report(filepath, num_words, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    generate_report(sorted_characters)
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    num_words = num_of_words(contents)
    characters = num_of_characters(contents)
    sorted_characters = sort_dictionary(characters)
    print_full_report(filepath, num_words, sorted_characters)

main()