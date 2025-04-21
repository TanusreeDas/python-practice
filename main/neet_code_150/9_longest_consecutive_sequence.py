'''Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9'''

class Solution:
    @staticmethod
    def longest_consecutive_only_positive_num(nums: list[int]) -> int:

        if not nums: return 0

        max_num = max(nums)
        num_list =[0]*(max_num+1)
        longest,count =0,0

        for num in nums:
          num_list[num] = 1

        for i in range(max_num+1):
            if num_list[i] == 1:
                count +=1
            else:
                if count>longest:
                    longest = count
                count = 0

        return max(longest,count)


    @staticmethod
    def longest_consecutive(nums: list[int]) -> int:

        if not nums: return 0
        count, longest = 0,0
        num_set =set(nums)
        for num in num_set:
            if num-1 not in num_set:
                count = 1
                while count+num in num_set:
                    count +=1
                longest = max(longest,count)

        return max(longest,count)

if __name__ == "__main__":
    sol = Solution()
    numbers = [1,2,3,0,5,6,7,9,10,8,12,11,-1,-2,-3,-6,-4,-5]
    #numbers = [1, 2, 3, 0, 5, 6, 7, 9, 10, 8, 12, 11]
    print(f"Given input {numbers}")
    print(f"Given output {sol.longest_consecutive(numbers)}")
