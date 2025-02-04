'''
Binary search is an efficient algorithm that divides the search range in half at every step, working only on sorted data.

Concept:
	•	Divide-and-Conquer: Repeatedly divides the dataset into halves.
	•	Requires Sorted Data: Works only on sorted datasets (ascending or descending order).
	•	Time Complexity: Best Case: O(1) (middle element matches), Worst Case: O(log n), Space Complexity: O(1) (iterative) or O(\log n) (recursive).

How it works:
	•	Identify the middle element of the current range.
	•	Compare the target with the middle element: If equal, return the middle index, if smaller, discard the right half, if larger, discard the left half.
	•	Repeat on the remaining half until the target is found or the range is empty.
'''

def binary_search(arr,e, start_index, end_index):

    if start_index > end_index:
        return -1

    middle_index = (start_index+end_index)//2
    middle_element = arr[middle_index]

    if e == middle_element:
        return middle_index
    elif e<middle_element:
        return binary_search(arr,e,middle_index-1,end_index)
    else:
        return binary_search(arr,e,start_index,middle_index+1)

    return -1


if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 8, 10, 90]
    target = 90

    search_result = binary_search(array,target,0,len(array)-1)

    if search_result >=0:
        print (f"Element {target} is found at index {search_result}.")
    else:
        print(f"Element {target} is not found in the given array.")