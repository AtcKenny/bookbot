def count_words(text: str) -> int:
    list_of_words = text.split()
    return len(list_of_words)

def character_count(text: str) -> dict[str, int]:
    result = {}
    for letter in text.lower():
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def sorted_char_count(characters: dict[str, int]) -> list:
    list_of_dicts = []
    for key, value in characters.items():
        list_of_dicts.append({'char': key, 'num': value})
    return sorted(list_of_dicts, key=lambda x: x['num'], reverse=True)

