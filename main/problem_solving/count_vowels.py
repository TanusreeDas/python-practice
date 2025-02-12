'''Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.'''

def get_count1(sentence): #solution 1
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

def get_count2(sentence): #solution 2
    vowels = 'aeiou'
    return sum(1 for char in sentence if char in vowels)

def get_count(sentence): #solution 3
    return sum(char in 'aeiou' for char in sentence)

if __name__=="__main__":
    target = "The quick brown fox jumps over the lazy dog."
    print(get_count(target))