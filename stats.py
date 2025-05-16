def count_words(text:str) -> int:
    words = text.split()
    return len(words)

def count_chars(text:str) -> dict:
    text_lower = text.lower()
    char_dict = {}
    
    for c in text_lower:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_dicts(char_dict:dict) -> list[dict]:
    dict_list = []
    for char in char_dict:
        dict_list.append({"char": char, "num": char_dict[char]})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list