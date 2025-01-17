'''
What Are Generators?
	•	Generators are functions that yield values one at a time, instead of returning them all at once.
	•	This is useful for working with large datasets where creating a full list would consume too much memory.

Key Points:
	1.	Generators use the yield keyword instead of return.
	2.	Each call to next() retrieves the next value from the generator.
	3.	Generators maintain their state between calls, so they resume where they left off.

Why Use Generators?
	1.	Memory Efficient: They don’t store all values in memory at once.
	•	Example: Generating the first billion numbers.
	2.	Infinite Sequences: Generators can create infinite sequences, as they produce values on demand.

Problem Statement:
Can you write a generator function that yields all prime numbers up to a given limit? Take your time to think about it!
'''

def prime_number_generator(limit):
    prime_numbers = []
    for i in range(2,limit+1):
        is_prime = True
        sqrt_i= int(pow(i,0.5))+1 #A number is prime if it is not divisible by any integer from 2 to sqrt(i) (for efficiency).
        #By checking only up to the square root, we reduce the number of checks dramatically, especially for large numbers.
        for j in range(2,sqrt_i):
            if i%j == 0:
                is_prime = False
                break
        if (is_prime == True):
            yield i

if __name__ == "__main__":
    print(list(prime_number_generator(5)))