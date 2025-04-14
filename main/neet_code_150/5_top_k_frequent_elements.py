'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique. You may return the output in any order.
Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

Best Approach: 1. Bucket Sort (O(n)) and 2. Min Heap (O(logk))
'''

from collections import Counter
import heapq

class Solution:

    @staticmethod
    def top_k_frequent_using_counter(nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        return [i[0] for i in counter.most_common(k)]

    @staticmethod
    def top_k_frequent_using_dict(nums: list[int], k: int) -> list[int]: # O(nlogn)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        counter_list = [(k,v) for k,v in counter.items()]
        k_sorted_counter_list = sorted(counter_list, key= lambda kv: kv[1], reverse=True)[:k]
        k_common_input = [k[0] for k in k_sorted_counter_list]

        return k_common_input

    @staticmethod
    def top_k_frequent_using_dict(nums: list[int], k: int) -> list[int]: # O(nlogn)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        counter_list = [(k,v) for k,v in counter.items()]
        k_sorted_counter_list = sorted(counter_list, key= lambda kv: kv[1], reverse=True)[:k]
        k_common_input = [k[0] for k in k_sorted_counter_list]

        return k_common_input

    @staticmethod
    def top_k_frequent_using_heap(nums: list[int], k: int) -> list[int]: # O(nlogn)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        heap = []
        for key,val in counter.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        # as order is not imp else we needed to sort the list
        res = [val[1] for val in heap]
        return res

    @staticmethod
    def top_k_frequent_using_bucket_sort(nums: list[int], k: int) -> list[int]: # O(n)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        freq = [[] for _ in range(len(nums)+1)]
        for key, val in counter.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq)-1,0,-1): # as no element has zero frequency
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    sol = Solution()
    arg1 = [1, 2, 1, 2, 2, 1]
    arg2 = 2
    print(sol.top_k_frequent_using_dict(arg1,arg2))
    print(sol.top_k_frequent_using_heap(arg1,arg2))
    print(sol.top_k_frequent_using_bucket_sort(arg1,arg2))