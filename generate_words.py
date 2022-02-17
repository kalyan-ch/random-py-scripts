import re

def load_words():
    words = []
    
    # load 5 letter words to memory
    with open('five_letter_words.txt') as f:
        words = f.readlines()

    return words

def get_words_start_end(start, end):
    result = []

    words = load_words()
        
    # get words
    if start != '' or end != '':
        
        regex = '^'+start+'.*'+end+'$'

        for word in words:
            word = word.strip()
            word = word.upper()
            
            isFound = re.search(regex, word)

            if isFound:
                result.append(word)

    return result

def get_words_containing(letters):
    words = load_words()
    filtered_words = words

    for let in letters:
        filtered_words = get_words_containing_letter(filtered_words, let)
    
    return filtered_words

def get_words_containing_letter(filtered_words, letter):
    new_words = []
    for w in filtered_words:
        w = w.strip()
        w = w.upper()

        if letter in w:
            new_words.append(w)
    
    return new_words

if __name__ == '__main__':

    for x in get_words_start_end('CH', 'R'):
        print(x)

    for x in get_words_containing(['A', 'U']):
        print(x)
