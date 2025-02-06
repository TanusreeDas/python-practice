'''
✅ Why not Recursion?
We have already implemented the algorithm using recursion, however, "Binary Search" is usually more efficient when implemented iteratively rather than recursively. Here’s why:
	•	Recursion adds extra function calls, which consume more stack memory.
	•	Each recursive call stores variables & return addresses in the call stack, leading to increased memory usage.
	•	Python has a default recursion limit (usually ~1000 recursive calls) before raising a RecursionError.
	•	Recursive calls require extra CPU cycles to manage the function call stack.
	•	Iterative methods directly modify variables and avoid the cost of function call management.
	🚀 When NOT to Use Recursion:
	•	When the problem can be solved iteratively without recursion overhead.
	•	When the recursion depth could be too high (e.g., 1,000,000 elements in an array).
	•	When performance matters (Recursion can be slower in Python).

Concept:
	•	Divide-and-Conquer: Repeatedly divides the dataset into halves.
	•	Requires Sorted Data: Works only on sorted datasets (ascending or descending order).
	•	Space Complexity: O(1) (iterative) or O(\log n) (recursive).

How it works:
	•	Identify the middle element of the current range.
	•	Compare the target with the middle element: If equal, return the middle index, if smaller, discard the right half, if larger, discard the left half.
	•	Repeat on the remaining half until the target is found or the range is empty.
'''


def binary_search(arr,target):
    arr_len=len(arr)
    start_index, end_index = 0,arr_len

    while start_index <= end_index:
        middle_index = (start_index+end_index)//2
        middle_element = arr[middle_index]

        if target == middle_element:
            return middle_index
        elif target > middle_element:
            start_index = middle_index+1
        else:
            end_index = middle_index-1

    return -1


if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 8, 10, 90]
    target = 90

    search_result = binary_search(array,target)

    if search_result >=0:
        print (f"Element {target} is found at index {search_result}.")
    else:
        print(f"Element {target} is not found in the given array.")