'''
✅ Why not Recursion?
We have already implemented the algorithm using recursion, however, "Jump Search" is usually more efficient when implemented iteratively rather than recursively. Here’s why:
	•	Recursion adds extra function calls, which consume more stack memory.
	•	Each recursive call stores variables & return addresses in the call stack, leading to increased memory usage.
	•	Python has a default recursion limit (usually ~1000 recursive calls) before raising a RecursionError.
	•	Recursive calls require extra CPU cycles to manage the function call stack.
	•	Iterative methods directly modify variables and avoid the cost of function call management.
	🔹 Jump Search (Recursive vs Iterative) Space complexity:
	•	Recursive: Calls itself multiple times for block jumps: O(√n) (due to recursion stack).
	•	Iterative: Simply loops through blocks: O(1) (only uses a few variables).
	🚀 When NOT to Use Recursion:
	•	When the problem can be solved iteratively without recursion overhead.
	•	When the recursion depth could be too high (e.g., 1,000,000 elements in an array).
	•	When performance matters (Recursion can be slower in Python).

Concept:
	•	Jump in Fixed Steps: Moves in steps of size sqrt{n} through the array.
	•	Localized Search: After a potential range is identified, linear search is performed within that block.
	•	Time Complexity: O(√n), Space Complexity: O(1).

How it works:
	•	Start at the first element and jump ahead by √n steps.
	•	Stop jumping when the current element exceeds or equals the target.
	•	Perform a linear search within the block from the previous jump to the current position.
	•	If the target is found, return its index; otherwise, return -1.
'''

import math

def jump_search(arr,target):

    arr_len=len(arr)
    step = int(math.sqrt(arr_len))
    start_index = 0
    end_index = step

    for i in range(step+1):
        if start_index<arr_len and arr[start_index]<=target<=arr[end_index]:
            for j in range(start_index,end_index+1):
                if arr[j]==target:
                    return j
        start_index, end_index = end_index+1, end_index + step if end_index+step<arr_len else arr_len-1
    return -1

if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 8, 10, 12, 14, 16, 18,21,45,54,57,89,90,111,112,145,167,198,2213,2345,3451,6789,9087]
    target = 9087

    search_result = jump_search(array,target)

    if search_result > -1:
        print (f"Element {target} is found at index {search_result}.")
    else:
        print(f"Element {target} is not found in the given array.")