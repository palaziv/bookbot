from stats import count_words, count_chars, sorted_dicts
import sys

def get_book_text(path:str) -> str:
    with open(path) as f:
        return f.read()

def main():

    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = args[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    text = get_book_text(book)

    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_dict = count_chars(text)
    sorted = sorted_dicts(char_dict)
    for s in sorted:
        if s["char"].isalpha():
            print(f"{s['char']}: {s['num']}")

    print("============= END ===============")


    

main()