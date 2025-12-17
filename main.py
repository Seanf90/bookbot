import sys
from stats import number_words, num_characters, sorted_dict, sort_on, generate_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    book = get_book_text(filepath)
    num = number_words(book)
    num_chars = num_characters(book)
    sorted_chars = sorted_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    generate_report(sorted_chars)
    print("============= END ===============")

main()