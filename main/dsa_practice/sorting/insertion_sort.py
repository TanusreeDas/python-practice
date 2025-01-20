'''
The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

How it works:
	•	Take the first value from the unsorted part of the array.
	•	Move the value into the correct place in the sorted part of the array.
	•	Go through the unsorted part of the array again as many times as there are values.
'''
from timing_decorator import function_run_time

@function_run_time
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while key<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1]=key
    return arr

if __name__=="__main__":
    array_to_sort=[4,3,2,1]
    print(insertion_sort(array_to_sort))