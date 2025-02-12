'''A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.'''

def is_pangram_simple(str): #basic approach
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in letters:
        if i not in str.lower():
            return False
    return True

def is_pangram_faster(str): #faster using sets
    str_ascii_format = [ord(i) for i in str.lower()]
    str_ascii_list = set([i for i in range(97, 123)])
    return str_ascii_list.issubset(str_ascii_format)

def is_pangram(str): #fastest approach
    letters = set('abcdefghijklmnopqrstuvwxyz')
    return letters.issubset(str.lower())


if __name__=="__main__":
    target = "The quick brown fox jumps over the lazy dog."
    print(is_pangram(target))