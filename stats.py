def number_words(book_text):
    book_list = book_text.split()
    return len(book_list)

def num_characters(book_text):
    char_dict = {}
    for char in book_text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(dic):
    return dic["num"]

def sorted_dict(unsorted_dict):
    unsorted_list = []
    new_dict = {}
    for k, v in unsorted_dict.items():      
            new_dict = {"char": k, "num": v,}
            unsorted_list.append(new_dict)

    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list

def generate_report(sorted_list):
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")