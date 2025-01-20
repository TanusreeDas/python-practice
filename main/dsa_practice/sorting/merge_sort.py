'''
The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building
the array back together the correct way so that it is sorted.

How it works:
	•	Divide the unsorted array into two sub-arrays, half the size of the original.
	•	Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
	•	Merge two sub-arrays together by always putting the lowest value first.
	•	Keep merging until there are no sub-arrays left.
'''

from timing_decorator import function_run_time

def merge_sort_divide(arr):
    arr_len = len(arr)
    if arr_len<=1:
        return arr
    mid = arr_len//2
    mid_left_arr = merge_sort_divide(arr[0:mid])
    mid_right_arr = merge_sort_divide(arr[mid:arr_len])
    return merge_sort_conquer(mid_left_arr,mid_right_arr)

def merge_sort_conquer(left_arr,right_arr):
    result = []
    i = j = 0

    while i<len(left_arr) and j<len(right_arr):
        left_val = left_arr[i]
        right_val = right_arr[j]
        if left_val<right_val:
            result.append(left_val)
            i += 1
        else:
            result.append(right_val)
            j += 1

    result.extend(left_arr[i:])
    result.extend(right_arr[j:])

    return result

@function_run_time
def merge_sort(arr):
    return merge_sort_divide(arr)


if __name__=="__main__":
    array_to_sort=[4,3,9,2,1,6,7]
    print(merge_sort(array_to_sort))

