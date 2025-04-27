'''Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.'''


from time import time

class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int: #not working change it.
        unique_set = set()
        max_length,l =0,0
        for i,c in enumerate(s):
            while c in unique_set:
                unique_set.remove(s[l])
                l +=1
            unique_set.add(c)
            max_length = max(max_length,i-l+1)

        return max_length


if __name__ == '__main__':
    count = 1
    sol = Solution()
    inputs = ["abcabcbb","bbbbb","pwwkew","zxyzxyz","xxxx","dvdf"]
    for input in inputs:
        print(f"Processing input no: {count}")
        start_time = time()
        print(f"For given '{input}' input the length of the Longest Substring is: {sol.length_of_longest_substring(input)} and time taken ={time()-start_time} seconds")
        print("*"*40)
        count +=1