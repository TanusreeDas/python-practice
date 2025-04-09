'''Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.'''

from  collections import Counter
from typing import List

class Solution:

    @staticmethod
    def has_duplicate(self, nums: List[int]) -> bool:
        if len(nums)>0:
            d = Counter(nums)
            max_occurrence = d.most_common(1)[0][1]
            if max_occurrence>1:
                return True
        return False


if __name__ == "__main__":
    sol= Solution()
    print(sol.has_duplicate([]))
