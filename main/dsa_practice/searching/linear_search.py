'''
Linear search is the simplest searching algorithm where each element in the list is checked sequentially until the target element is found or the list ends.

Concept:
	•	Sequential Access: Starts from the first element and moves sequentially through the list.
	•	No Sorting Required: Works on both sorted and unsorted data.
	•	Time Complexity: Best Case: O(1) (target is the first element), Worst Case: O(n) (target is the last element or not present), Space Complexity: O(1).

How it works:
	•	Start with the first element in the list.
	•	Compare the current element with the target: If they match, return the index else, move to the next element.
	•	Repeat until the target is found or the list ends.
'''

def linear_search(arr, e):
    for index in range(len(arr)):
        if arr[index] == e:
            return index
    return -1


if __name__ == "__main__":
    array = [4,5,1,7,3,90,8,10]
    target = 5

    search_result = linear_search(array,target)

    if search_result >=0:
        print (f"Element {target} is found at index {search_result}.")
    else:
        print(f"Element {target} is not found in the given array.")