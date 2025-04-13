class Solution:

    @staticmethod
    def encode(strs: list[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str


    @staticmethod
    def decode_sol1(s: str) -> list[str]:
        first_occurrence = s.find("#")
        end_pos =0
        next_occurrence = first_occurrence+1
        res = []
        while end_pos < len(s):
            len_str = int(s[end_pos:(next_occurrence-1)])
            end_pos = len_str + next_occurrence
            res.append(s[int(next_occurrence):int(end_pos)])
            next_occurrence = s.find("#",end_pos)+1
        return res

    @staticmethod
    def decode_sol2(s: str) -> list[str]: #without find method to improve performance
        res = []
        i =0
        while i<len(s):
            j=i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i =j+1
            j =i+length
            res.append(s[i:j])
            i=j
        return res

if __name__ == "__main__":
    sol = Solution()
    input_str = ["apple", "orange", "pear", "almonds", "salt", "sweet", "cake", "biscuits"]
    encoded_str_res = sol.encode(input_str)
    decoded_str_res = sol.decode_sol2(encoded_str_res)
    print(f"input string: {input_str}")
    print(f"encoded string: {encoded_str_res}")
    print(f"encoded string: {decoded_str_res}")