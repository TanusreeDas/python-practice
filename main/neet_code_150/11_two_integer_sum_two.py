'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target
and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution. Your solution must use O(1) additional space.
Constraints:
2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000'''

from collections import defaultdict

class Solution:
    @staticmethod
    def two_sum_brute_force(numbers: list[int], target: int) -> list[int]: # O(n*n)
        for i,num in enumerate(numbers):
            j = i+1
            while i < j < len(numbers):
                if num + numbers[j] == target:
                    return [i+1,j+1]
                j +=1

    @staticmethod
    def two_sum_hash_map(numbers: list[int], target: int) -> list[int]: # O(n)
        number_dict =defaultdict(int)
        for i,num in enumerate(numbers):
            remainder = target - num
            if remainder in number_dict:
                return [number_dict[remainder]+1,i+1]
            number_dict[num] = i

    @staticmethod
    def two_sum_two_pointers(numbers: list[int], target: int) -> list[int]: # O(n)
        left_position, right_position = 0, len(numbers)-1
        while left_position<right_position:
            current_sum= numbers[left_position] + numbers[right_position]
            if current_sum==target:
                return [left_position+1,right_position+1]
            elif current_sum<target:
                left_position +=1
            else:
                right_position -=1

if __name__ == '__main__':
    sol = Solution()
    inputs = [[1,2,3,4,5],[1,3,7,9,10]]
    k = 4
    for nums in inputs:
        print(f"Given input: {nums} and {k}")
        print(f"Given output using brute force method: {sol.two_sum_brute_force(nums,k)}")
        print(f"Given output using hashmap method: {sol.two_sum_hash_map(nums,k)}")
        print(f"Given output using two pointers method: {sol.two_sum_two_pointers(nums,k)}")
        print("*"*40)

