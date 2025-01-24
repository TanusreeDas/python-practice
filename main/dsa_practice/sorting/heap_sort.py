'''
Heap is a special tree-based data structure. A binary tree is said to follow a heap data structure if
	•	it is a complete binary tree
	•	All nodes in the tree follow the property that they are greater than their children i.e. the largest element is
     at the root and both its children and smaller than the root and so on. Such a heap is called a max-heap.
     If instead, all nodes are smaller than their children, it is called a min-heap.

Concept:
	•	If the index of any element in the array is i, the element in the index 2i+1 will become the left child and element
	 in 2i+2 index will become the right child. Also, the parent of any element at index i is given by the lower bound of (i-1)/2.
	•	We start with a complete binary tree, and then modify it to a Max-Heap by running a function called heapify on all the non-leaf elements of the heap.
	•	To sort from small to large build a maxheap.
	•	We build max heap only once, when we extract the root, the rest of the array below it is still in heap order. Only the root may violate the Max Heap
	property after the swap. Instead of re-heapifying the entire array, we just heapify the root, which is faster and efficient.

How it works:
	•	calculate i= len(arr)//2 - 1
	•	until i=0 for every i heapify the array : heapify(arr, len(arr), i);
	•	Remove the root element and put at the end of the array (nth position) Put the last item of the tree (heap) at the vacant place.
	•	Reduce the size of the heap by 1. Continue heapifying until all the items of the list are sorted.
'''

from timing_decorator import function_run_time

def heapify(arr,n,i):
    largest_value_index = i
    left_item_index = 2*i+1
    right_item_index = 2*i+2

    if left_item_index<n and arr[largest_value_index]<arr[left_item_index] :
        largest_value_index = left_item_index
    if right_item_index<n and arr[largest_value_index]<arr[right_item_index] :
        largest_value_index = right_item_index

    if largest_value_index != i:
        arr[i],arr[largest_value_index] = arr[largest_value_index],arr[i]
        heapify(arr,n,largest_value_index)

@function_run_time
def heap_sort(arr):
    len_arr = len(arr)
    last_non_leaf_code_index = len_arr // 2 -1
    # build max heap only once
    for i in range(last_non_leaf_code_index,-1,-1):
        heapify(arr,len_arr,i)

    for i in range(len_arr-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

    return arr

if __name__=="__main__":
    arry_to_sort=[4,3,7,1,9,10,2,5]
    print(heap_sort(arry_to_sort))