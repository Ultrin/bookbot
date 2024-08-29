

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    char_dict = char_count(text)
    letter_count = list_of_dicts(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"This document has {num_of_words} words.")
    print()

    for i in letter_count:
        if not i["char"].isalpha():
            continue
        print(f"The {i['char']} character was found {i['num']} times")

    print()
    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    num_of_characters ={}
    
    for c in text:
        lowered = c.lower()
        if lowered in num_of_characters:
            num_of_characters[lowered] +=1
        else:
            num_of_characters[lowered] = 1

    return num_of_characters


def sort_on(dict):
    return dict["num"]


def list_of_dicts(num_char_dict):
    list_dict = []
    for c in num_char_dict:
        list_dict.append({"char": c, "num": num_char_dict[c]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict



main()
