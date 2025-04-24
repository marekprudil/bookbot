def count_words(text):
    return len(text.split())

def character_frequencies(text):
    text = text.lower()
    frequencies_dict = {}
    for char in text:
        if char not in frequencies_dict.keys():
            frequencies_dict.update({char: 1})
        else:
            frequencies_dict[char] += 1
    return frequencies_dict

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append({"char": key, "num": dictionary[key]})
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list