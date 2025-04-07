from  collections import Counter
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)>0:
            d = Counter(nums)
            max_occurance = d.most_common(1)[0][1]
            if max_occurance>1:
                return True
        return False


if __name__ == "__main__":
    sol= Solution()
    print(sol.hasDuplicate([]))
