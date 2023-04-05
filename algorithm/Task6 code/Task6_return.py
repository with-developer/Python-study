import re
from math import ceil
from queue import PriorityQueue


def task6(algorithm, key_char, message_filename, dictionary_filename, max_score, key, filler):
    with open(message_filename, 'r') as f:
        text = f.read()

    text = text.replace("\n", " ")
    text = re.sub("[^a-zA-Z ]", "", text)

    text = text.lower()
    letter_count = [text.count(char.lower()) for char in key]

    with open(dictionary_filename, 'r') as f:
        dictionary_text = f.read()
    dictionary_text = dictionary_text.replace("\n", "")
    dictionary_text = re.sub("[^a-zA-Z]", "", dictionary_text)
    dictionary_text = dictionary_text.lower()
    dictionary_letter_count = [
        dictionary_text.count(char.lower()) for char in key]

    frequency = [(char, count) for char, count in zip(key, letter_count)]
    frequency.sort(key=lambda x: x[1], reverse=True)
    dictionary_frequency = [(char, count)
                            for char, count in zip(key, dictionary_letter_count)]
    dictionary_frequency.sort(key=lambda x: x[1], reverse=True)

    key_map = {}
    for i in range(len(frequency)):
        message_char, _ = frequency[i]
        key_char, _ = dictionary_frequency[i]
        key_map[message_char] = key_char

    for char in key:
        if char not in key_map:
            key_map[char] = filler

    decrypted_text = ""
    for char in text:
        if char.lower() in key_map:
            decrypted_text += key_map[char.lower()]
        else:
            decrypted_text += char

    score = 0
    for char in decrypted_text:
        if char.upper() == key_char:
            score += 1
    if score > max_score:
        score = max_score

    if algorithm == 'g':
        candidates = PriorityQueue()
        for i in range(len(key)):
            for j in range(i+1, len(key)):
                new_key_map = key_map.copy()
                new_key_map[key[i]], new_key_map[key[j]
                                                 ] = new_key_map[key[j]], new_key_map[key[i]]
                candidate_text = ""
                for char in text:
                    if char.lower() in new_key_map:
                        candidate_text += new_key_map[char.lower()]
                    else:
                        candidate_text += char
                candidate_score = 0
                for char in candidate_text:
                    if char.upper() == key_char:
                        candidate_score += 1
                if candidate_score > max_score:
                    candidate_score = max_score
                candidates.put((-candidate_score, new_key_map, candidate_text))
        _, key_map, decrypted_text = candidates.get()

    elif algorithm == 'a':
        pass

    return decrypted_text, score


if __name__ == '__main__':
    # Example function call below, you can add your own to test the task6 function
    decrypted_message, score = task6(
        'a', 'g', 'secret_msg.txt', 'common_words.txt', 90, 'AENOST', 'n')
    print(decrypted_message)
    print(score)
