

# use Trie data structure


# https://codeburst.io/solving-word-hunt-in-python-the-trie-9acedc1f2637
# https://mp.weixin.qq.com/s/jUsHqjQaXFZGO7b-1dLG_w

# word file from https://github.com/dwyl/english-words

import sys

def load():
    with open('./games/words_alpha.txt') as word_file:
        word_list = word_file.read().split()
        
    trie = {}
    
    for word in word_list:
        add_word_to_trie(trie, word)
        
    return trie

def add_word_to_trie(trie, word, idx=0):
    if idx >= len(word):
        # when a node is a completed word,  set 'leaf' key to True
        trie['leaf'] = True
        return
    
    if word[idx] not in trie:
        trie[word[idx]] = {}
        
    add_word_to_trie(trie[word[idx]], word, idx+1)
    
    
def findWords(trie, word, currentWord):
    myWords = set()      
    for letter in word:
        if letter in trie:
            newWord = currentWord + letter
            if 'leaf' in trie[letter] and trie[letter]['leaf']:
                myWords.add(newWord)
            myWords = myWords.union(findWords(trie[letter], word, newWord))
    return myWords

def raw_input(stdout):

    print(stdout)
    for line in sys.stdin: 
        if 'q' == line.rstrip(): 
            break
        return line.rstrip()


def main():
    print('Loading dictionary...')
    wordTrie = load()
    print('Done\n')
 
    word = raw_input("What letters should we use: ")
    minLength = int(raw_input("What is the minimum word length: "))
    print("")
 
    count = 0;
    for word in sorted(findWords(wordTrie, word, "")):
        if len(word) >= minLength:
            count = count+1
            print(word)
    print(str(count) + " words found.")


if __name__ == "__main__":
    main()