'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.
Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

Best Approach: 1. Hash Map one pass and then 2. Hash Map Two pass though both has O(n) but first one is better.
'''

from collections import Counter

class Solution:

    @staticmethod
    def two_sum1(nums: list[int], target: int) -> list[int]:
        for i,first_val in enumerate(nums):
            remainder = target - first_val
            j=i+1
            while j < len(nums):
                if nums[j] == remainder:
                    return [i,j]
                j +=1


    @staticmethod
    def two_sum2(nums: list[int], target: int) -> list[int]:

        nums_dict = {key:val for val,key in enumerate(nums)}

        for i,first_val in enumerate(nums):
            remainder = target - first_val
            j = nums_dict.get(remainder,-1)
            if j > -1 and j != i:
                return [i,j]


    @staticmethod
    def two_sum3(nums: list[int], target: int) -> list[int]:

        nums_dict = {}

        for i,first_val in enumerate(nums):
            remainder = target - first_val
            if remainder in nums_dict:
                return [nums_dict[remainder],i]
            nums_dict[first_val] = i



if __name__ == "__main__":
    sol= Solution()
    print(sol.two_sum3([1,3,4,2],6))