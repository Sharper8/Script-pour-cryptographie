def char_to_index(c):
    return ord(c) - ord('a')

def index_to_char(i):
    return chr(i + ord('a'))

def mod_diff(c1, c2):
    return (char_to_index(c1) - char_to_index(c2)) % 26

def word_mod_add(c, diff):
    return [index_to_char((char_to_index(c) + d) % 26) for c, d in zip(c, diff)]

def load_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        word_list = [word.strip().lower() for word in file.readlines() if len(word.strip()) == 7]
        word_list = [word.encode('ascii', 'ignore').decode('utf-8') for word in word_list]
    return word_list

def word_mod_diff(word1, word2):
    return [mod_diff(c1, c2) for c1, c2 in zip(word1, word2)]

def find_word_pairs(words, diff_target):
    results = []
    for word in words:
        wordtest = word_mod_add(word, diff_target)
        wordtest = ''.join(wordtest)
        if wordtest in words:
            results.append((wordtest, word))     
    return results  
    
#### MAIN CODE #####

cipher1 = "HQQYAJT"
cipher2 = "RJAJPWG"

# calcule la difference entre les 2 ciphers
diff_target = word_mod_diff(cipher1.lower(), cipher2.lower())
#diff_target = word_mod_diff(cipher2.lower(), cipher1.lower())
print('diff_target:', diff_target)

# calcule le cipher qui correspond a l'ajout de la difference pour chque mot pour trouver le mot 1
target = word_mod_add(cipher1, diff_target)
print(f"Target equation modulo 26: {target}")

# charge une liste de 7 mots de long du corpus
corpus_filepath = 'mots_francais.txt'
words = load_words(corpus_filepath)
print(f"Loaded {len(words)} words from the corpus.")

matching_pairs = find_word_pairs(words, diff_target) # ajouter la diff dans chaque mot de la liste

if matching_pairs:
    print(f"Matching word pairs found: {matching_pairs}")
else:
    print("No matching word pairs found.")