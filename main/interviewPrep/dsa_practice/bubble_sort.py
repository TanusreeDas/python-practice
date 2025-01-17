'''
The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

How it works:
	•	Go through the array, one value at a time.
	•	For each value, compare the value with the next value.
	•	If the value is higher than the next one, swap the values so that the highest value comes last.
	•	Go through the array as many times as there are values in the array.
'''
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)   # Call the original function
        end_time = time.perf_counter()   # End the timer
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.10f} seconds")
        return result
    return wrapper

@timing_decorator
def bubble_sort(arr):
    arr_len=len(arr)-1
    for i in range(arr_len):
        for j in range(arr_len-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

@timing_decorator
def improved_bubble_sort(arr):
    arr_len=len(arr)-1
    for i in range(arr_len):
        swapped = False
        for j in range(arr_len-i):
            if arr[j]>arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped=True
            if not swapped:
                break

    return arr

if __name__=="__main__":
    arry_to_sort=[4,3,7,1,9,10,2,5]
    print(bubble_sort(arry_to_sort))
    print(improved_bubble_sort(arry_to_sort))

