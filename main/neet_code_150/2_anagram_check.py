'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Constraints: s and t consist of lowercase English letters.
'''

from collections import Counter

class Solution:

    @staticmethod
    def is_anagram_simple_method(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s)== sorted(t)

    @staticmethod
    def is_anagram_using_hash_map(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {},{}
        for i in range(len(s)):
            count_s[s[i]] = 1+count_s.get(s[i],0)
            count_t[t[i]] = 1+count_t.get(t[i],0)
        return count_s == count_t

    @staticmethod
    def is_anagram_using_array_hash_table(s: str, t: str) -> bool: # only for lower case letters
        if len(s) != len(t):
            return False

        counter_table = [0]*26
        ascii_a = ord('a')
        for i in range(len(s)):
            counter_table[ord(s[i])-ascii_a] +=1
            counter_table[ord(t[i])-ascii_a] -=1

        for val in counter_table:
            if val !=0:
                return False

        return True

    @staticmethod
    def is_anagram_using_counter(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s,count_t = Counter(s), Counter(t)
        return count_s == count_t



if __name__ == "__main__":

    sol = Solution()

    print(f"Answer Using Sorted List Two Strings are Anagram: {sol.is_anagram_simple_method('india','ndiai')}")
    print(f"Answer Using Hash Map Two Strings are Anagram: {sol.is_anagram_using_hash_map('america','kolkata')}")
    print(f"Answer Using Hash Table Two Strings are Anagram: {sol.is_anagram_using_array_hash_table('kolkata','kauakol')}")
    print(f"Answer Using Inbuilt Counter Two Strings are Anagram: {sol.is_anagram_using_counter('mumbai','baimun')}")