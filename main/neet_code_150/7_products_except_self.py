'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n)time without using the division operation?
Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

Best Approach: 1. Try division if no constraint is mentioned else try suffix-prefix optimal method both has  O(n) time complexity
'''

class Solution:
    @staticmethod
    def product_except_self_using_division(nums: list[int]) -> list[int]: #O(n)
        product,zero_count = 1,0
        res = [0]*len(nums)
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        if zero_count>1: return res

        for i,num in enumerate(nums):
            if zero_count:
                if num:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product//num
        return res

    @staticmethod
    def product_except_self_using_prefix_suffix(nums: list[int]) -> list[int]: #O(n) without using division
        length = len(nums)
        prefix_array =[1]*length
        suffix_array =[1]*length
        for i in range(length):
            if i==0:
                prefix_array[0] = 1
            else:
                prefix_array[i] = prefix_array[i-1]*nums[i-1]
        for j in range(length-1,-1,-1):
            if j == length -1:
                suffix_array[j] = 1
            else:
                suffix_array[j] = suffix_array [j+1] * nums [j+1]
        return [t[0] * t[1] for t in zip(prefix_array,suffix_array)]

    @staticmethod
    def product_except_self_using_prefix_suffix_optimal(nums: list[int]) -> list[int]: #O(n)
        length = len(nums)
        prefix,suffix = 1, 1
        res = [1]* length
        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
        for j in range(length-1,-1,-1):
            res[j] *= suffix
            suffix *= nums[j]
        return res


if __name__ == "__main__":
    sol = Solution()
    arg1 = [1, 2, 3, -3, 6, -4]
    print(f"input is {arg1}")
    print(f"output is {sol.product_except_self_using_division(arg1)}")
    print(f"output is {sol.product_except_self_using_prefix_suffix(arg1)}")
    print(f"output is {sol.product_except_self_using_prefix_suffix_optimal(arg1)}")