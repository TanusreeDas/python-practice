'''You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.'''

def find_outlier(integers):
    count_odd = 0
    count_even = 0
    for num in integers[:3]:
        if num%2 == 0:
            count_even += 1
        else:
            count_odd += 1
    for num in integers:
        if count_even >= 2 and num%2 == 1:
            print("The outlier is an odd number and it is: ", end="")
            return num
        elif count_odd >= 2 and num%2 == 0:
            print("The outlier is an even number and it is: ", end="")
            return num

if __name__=="__main__":
    numbers = [2, 4, 6, 8, 10, 3]
    print(find_outlier(numbers))