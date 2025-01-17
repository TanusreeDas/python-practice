'''
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.

How it works:
	•	Go through the array to find the lowest value.
	•	Move the lowest value to the front of the unsorted part of the array.
	•	Go through the array again as many times as there are values in the array.
'''

def selection_sort(arr):
    arr_range=len(arr)-1
    for i in range(arr_range):
        lowest_value_index = i
        for j in range(i,arr_range+1,1):
            if arr[j]<arr[lowest_value_index]:
                lowest_value_index = j
        arr[i],arr[lowest_value_index]=arr[lowest_value_index],arr[i]
    return arr

if __name__=="__main__":
    array_to_sort=[10,11,8]
    print(selection_sort(array_to_sort))