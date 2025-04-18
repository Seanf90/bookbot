def num_of_words(book_contents):
    count = 0
    words = book_contents.split()
    for word in words:
        count += 1
    return count


def num_of_characters(book_contents):
    book_contents = book_contents.lower()
    character_count = {}
    characters = list(book_contents)

    for c in characters:
        character_count[c] = 0

    for c in characters:
        if c in character_count:
            character_count[c] += 1
    return character_count


def sort_on(char_dict):
    return char_dict["count"]

def sort_dictionary(character_count):
    character_list = []
    for char, count in character_count.items():
        character_list.append({"char": char, "count": count})
    character_list.sort(reverse=True, key=sort_on)
    return character_list


def generate_report(character_list):
    for char in character_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")