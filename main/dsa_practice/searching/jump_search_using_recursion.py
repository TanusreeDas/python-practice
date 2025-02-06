'''
Jump-search is an algorithm for sorted data that skips ahead by fixed steps (jump size) and then performs a linear search within the identified block.

Concept:
	•	Jump in Fixed Steps: Moves in steps of size sqrt{n} through the array.
	•	Localized Search: After a potential range is identified, linear search is performed within that block.
	•	Time Complexity: O(√n), Space Complexity: O(√n).

How it works:
	•	Start at the first element and jump ahead by √n steps.
	•	Stop jumping when the current element exceeds or equals the target.
	•	Perform a linear search within the block from the previous jump to the current position.
	•	If the target is found, return its index; otherwise, return -1.
'''
import math

def jump_search(arr,element,jump_size,start_index,end_index,n):

    if start_index>n-1:
        return -1
    elif  end_index>n-1:
        end_index = n-1

    if element == arr[start_index]:
        return start_index
    elif element == arr[end_index]:
        return end_index
    elif arr[start_index] < element < arr[end_index]:
        for i in range(start_index,end_index+1):
            if arr[i]==element:
                return i
    else:
        return jump_search(arr,element,jump_size,end_index+1,end_index+jump_size,n)
    return -1

if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 8, 10, 12, 14, 16, 18,21,45,54,57,89,90,111,112,145,167,198,2213,2345,3451,6789,9087]
    target = 46
    len_arr = len(array)

    jump=int(math.sqrt(len_arr))

    search_result = jump_search(array,target,jump,0,jump,len_arr)

    if search_result > -1:
        print (f"Element {target} is found at index {search_result}.")
    else:
        print(f"Element {target} is not found in the given array.")