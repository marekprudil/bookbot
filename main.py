from stats import count_words, character_frequencies, sort_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    print_book_stats(path)
    


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def print_book_stats(path_to_book):

    book_text = get_book_text(path_to_book)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    char_nums = character_frequencies(book_text)
    char_nums_sorted = sort_dictionary(char_nums)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_nums_sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

    

main()