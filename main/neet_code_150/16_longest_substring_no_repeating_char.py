'''Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.'''


from time import time
#from collections import defaultdict

class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int: #not working change it.
        if len(s) == 0:
            return 0
        temp_str = {}#defaultdict(int)
        max_len = 1
        current_len = 0
        for c in s:
            if c in temp_str:
                current_len = 1
                temp_str ={c:1}
            else:
               current_len +=1
               temp_str[c]=1
            max_len = max(max_len,current_len)
        return max_len



if __name__ == '__main__':
    count = 1
    sol = Solution()
    inputs = ["abcabcbb","bbbbb","pwwkew","zxyzxyz","xxxx","dvdf"]
    for input in inputs:
        print(f"Processing input no: {count}")
        start_time = time()
        print(f"Output using brute force method: {sol.length_of_longest_substring(input)} and time taken ={time()-start_time} seconds")
        #start_time = time()
        #print(f"Output using two pointer method: {sol.length_of_longest_substring(input)} and time taken ={time()-start_time} seconds")
        print("*"*40)
        count +=1