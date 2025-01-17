'''
Here’s a list of the most commonly used and important string methods:
	•	len(s): Returns the length of the string s.
	•	s[i:j:k]: Slicing to extract parts of a string.
	•	s.find(sub): Returns the first index where sub is found, or -1 if not found.
	•	s.split(delimiter): Splits the string into a list using delimiter.
	•	s.rsplit(delimiter): Splits the string from the right.
	•	s.partition(delimiter): Splits the string into 3 parts: before, delimiter, after.
	•	delimiter.join(iterable): Joins elements of iterable into a string with delimiter.
	•	s.isalpha(): Returns True if all characters are alphabetic.
	•	s.isdigit(): Returns True if all characters are digits.
	•	s.isalnum(): Returns True if all characters are alphanumeric.
	•	s.isspace(): Returns True if all characters are whitespace.
	•	s.islower(): Checks if all letters are lowercase.
	•	s.isupper(): Checks if all letters are uppercase.
	•	s.upper(): Converts the string to uppercase.
	•	s.lower(): Converts the string to lowercase.
	•	s.capitalize(): Capitalizes the first character.
	•	s.title(): Converts the first character of each word to uppercase.
	•	s.strip(): Removes leading and trailing whitespace.
	•	s.lstrip() / s.rstrip(): Removes leading/trailing whitespace.
	•	s.replace(old, new): Replaces all occurrences of old with new.

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

hints: use sliding window approach using two pointers
    1.	Use a sliding window approach with two pointers.
	2.	Keep track of characters in a set to identify duplicates.
	3.	Move the window when a duplicate is found.
'''


def find_length_longest_substring(s):
    seen = set()
    start = 0
    max_len = 0

    for end in range(len(s)):
        # If duplicate character is found, move the start pointer
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        # Add the current character to the set and calculate the window length
        seen.add(s[end])
        max_len = max(max_len, end - start + 1)

    return max_len


if __name__ == "__main__":
    print(find_length_longest_substring("abcdcdb"))  # Output: 8



def find_length_longest_substring1(s):
    len_s=len(s)
    max_len = 1
    if(len_s>0):
        for i in range(2,len_s+1):
            for j in range(len_s):
                window_len=len(set(s[i:j]))
                if(window_len>max_len):
                    max_len=window_len
    else:
        return len_s
    return max_len

