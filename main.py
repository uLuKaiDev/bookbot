def main():
    book_path = "books/frankenstein.txt"
    book_name = get_book_name(book_path)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    unique_character = get_unique_characters(text)
    sorted_dic = dic_by_value_sorted(unique_character)
   
    print(f"--- This is the report of the book: {book_name} ---")
    print(f"{num_words} words found in the document titled: {book_name}")
    print()
    
    for key, value in sorted_dic.items():
        if not key.isalpha():
            continue
        else:
            print(f"The letter: {key} was found: {value} times")
    

# Takes the path and stripes away the books/.. at the beginning and the .txt at the end
def get_book_name(path):
    end_pos = path[6:-4]
    return (end_pos.capitalize())

# Takes the path as a string of /books/title.txt and returns the full text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Takes the full text and removes the spaces, the return of words is a list of all the words
def get_num_words(text):
    words = text.split()
    return len(words)

# Takes the full text, removes spaces, loops over items in the list
def get_unique_characters(text):
    words = text.lower().split()
    unique_letters = {}
    for word in words:
        for letter in word:
            if letter in unique_letters:
                unique_letters[letter] += 1
            else:
                unique_letters[letter] = 1
    sorted_unique_letters = dict(sorted(unique_letters.items()))
    return sorted_unique_letters

def dic_by_value_sorted(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return (sorted_dict)



main()