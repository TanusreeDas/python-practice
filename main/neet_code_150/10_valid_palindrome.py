'''Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.'''


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        modified_s = ''.join(filter(str.isalnum,s.lower()))
        return modified_s[::-1]==modified_s

    def is_alnum_custom(self,c): #if we are not allowed to use inbuilt isalnum
        return (
            (ord('A')<=ord(c)<=ord('Z')) or #cconsidering we will only use uppercase letter
            (ord('0') <= ord(c) <= ord('9'))
        )


    def is_palindrome_two_pointer(self,s:str)->bool:
        left_position, right_position = 0, len(s)-1
        while left_position<right_position:
            while left_position<right_position and not self.is_alnum_custom(s[left_position].upper()):
                left_position += 1
            while left_position<right_position and  not self.is_alnum_custom(s[right_position].upper()):
                right_position -= 1
            if s[left_position].upper() != s[right_position].upper():
                return False
            left_position,right_position = left_position+1, right_position-1
        return True

if __name__ == "__main__":
    sol = Solution()
    inputs = ['A man, a plan, a canal: Panama', ".,", ""]
    for input_str in inputs:
        print(f"Given input: {input_str}")
        print(f"Given output using generic method: {sol.is_palindrome(input_str)}")
        print(f"Given output using custom method: {sol.is_palindrome_two_pointer(input_str)}")
        print("*"*40)