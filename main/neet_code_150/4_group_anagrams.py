'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''

from collections import Counter,defaultdict

class Solution:

    @staticmethod
    def group_anagrams_sol1(strs: list[str]) -> list[list[str]]: # time complexity: O(n² * k)
        def is_anagram(s: str, t: str) -> bool:
            count_t,count_s = Counter(s),Counter(t) #O(k)
            if count_t == count_s:
                return True
            return False

        result_array = []
        visited = set()

        for i in range(len(strs)): # O(n)
            first_val = strs[i]
            place_holder_array = []
            if first_val not in visited:
                place_holder_array.append(first_val)

                for j in range(i+1,len(strs)): # O(n-1) ~ O(n)
                    if strs[j] not in visited or strs[j] == first_val:
                        visited.add(first_val)
                        second_val = strs[j]
                        if is_anagram(first_val,second_val):
                            visited.add(second_val)
                            place_holder_array.append(second_val)

                if len(place_holder_array)>0:
                    result_array.append(place_holder_array)

        return result_array

    @staticmethod
    def group_anagrams_sol2(strs: list[str]) -> list[list[str]]: # O(n*klogk)
        result_dict = defaultdict(list)
        for text in strs:
            place_holder_str = ''.join(sorted(text)) # time sort time complexity is: O(klogk)
            result_dict[place_holder_str].append(text)
        return list(result_dict.values())

    @staticmethod
    def group_anagrams_sol3(strs: list[str]) -> list[list[str]]: # O(n*k)
        result_dict = defaultdict(list)
        for text in strs:
            place_holder_str = [0]*26
            for c in text:
                place_holder_str[ord(c)-ord('a')]=1
            result_dict[tuple(place_holder_str)].append(text)
        return list(result_dict.values())


if __name__ == "__main__":
    sol= Solution()
    chk = ["", "cat", "","act","","dog"]
    print(sol.group_anagrams_sol1(chk))
    print(sol.group_anagrams_sol2(chk))
    print(sol.group_anagrams_sol3(chk))