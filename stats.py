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
