def char_to_index(c):
        return ord(c) - ord('a')

def index_to_char(i):
    return chr(i + ord('a'))

def mod_diff(c1, c2):
    return (char_to_index(c1) - char_to_index(c2)) % 26

def load_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        word_list = [word.strip().upper() for word in file.readlines() if len(word.strip()) == 7]
        #remove the accents and special characters
        word_list = [word.encode('ascii', 'ignore').decode('utf-8') for word in word_list]
    return word_list

def word_mod_diff(word1, word2):
    return [mod_diff(c1, c2) for c1, c2 in zip(word1, word2)]

def find_word_pairs(words, diff_target):
    results = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            diff = word_mod_diff(words[i], words[j])
            if diff == diff_target:
                print(f"Found potential pair: {words[i]} and {words[j]}")
                results.append((words[i], words[j]))
    return results

cipher1 = "HQQYAJT"
cipher2 = "RJAJPWG"

diff_target = word_mod_diff(cipher1.lower(), cipher2.lower())
print(f"Target difference modulo 26: {diff_target}")

corpus_filepath = 'mots_francais.txt'
words = load_words(corpus_filepath)
print(f"Loaded {len(words)} words from the corpus.")

matching_pairs = find_word_pairs(words, diff_target)

if matching_pairs:
    print(f"Matching word pairs found: {matching_pairs}")
else:
    print("No matching word pairs found.")