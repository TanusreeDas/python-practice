'''
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

Concept:
	•	Find the smallest element in the unsorted portion of the array and swap it with the first unsorted element.
	•	Repeat for all elements, shrinking the unsorted portion step by step.

How it works:
	•	Go through the array to find the lowest value.
	•	Move the lowest value to the front of the unsorted part of the array.
	•	Go through the array again as many times as there are values in the array.
'''
from timing_decorator import function_run_time

@function_run_time
def selection_sort(arr):
    arr_len=len(arr)
    for i in range(arr_len-1):
        lowest_value_index = i
        for j in range(i,arr_len,1):
            if arr[j]<arr[lowest_value_index]:
                lowest_value_index = j
        arr[i],arr[lowest_value_index]=arr[lowest_value_index],arr[i]
    return arr

if __name__=="__main__":
    array_to_sort=[1,4,2,6,9,7,5,3,10,11,8]
    print(selection_sort(array_to_sort))