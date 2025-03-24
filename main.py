import sys
from stats import count_words
from stats import character_count
from stats import sorted_char_count

def get_book_text(path: str):
    with open(path, 'r') as f:
        return f.read()

def print_report(path: str, word_count: int, char_count: list[dict[str, int]]) -> None:
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for entry in char_count:
        if entry['char'].isalpha():
            print(f'{entry['char']}: {entry['num']}')
    print('============= END ===============\n')

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    word_count = count_words(contents)
    sorted_chars = sorted_char_count(character_count(contents))
    print_report(path, word_count, sorted_chars)
    
if __name__ == '__main__':
    main()