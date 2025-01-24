'''
As the name suggests, Quicksort is one of the fastest sorting algorithms.

The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other
values so that lower values are on the left of the pivot element, and higher values are on the right of it.

How it works:
	•	Choose a value in the array to be the pivot element.
	•	Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
	•	Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
	•	Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
'''
from timing_decorator import function_run_time


def middle_element_quick_sort(arr):

    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    #middle value as the pivot
    mid_index = len_arr//2
    pivot_element = arr[mid_index]

    left = [x for x in arr if x < pivot_element]
    mid = [x for x in arr if x == pivot_element]
    right = [x for x in arr if x>pivot_element]

    return middle_element_quick_sort(left) + mid + middle_element_quick_sort(right)

@function_run_time
def quick_sort(arr):
    return middle_element_quick_sort(arr)

def improved_quick_sort(arr):
    pass

if __name__=="__main__":
    array_to_sort=[4,3,9,2,1,6,7]
    print(quick_sort(array_to_sort))