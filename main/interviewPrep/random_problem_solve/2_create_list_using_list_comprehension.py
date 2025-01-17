'''
A list comprehension allows us to create a new list by applying an operation to each item in an existing iterable (like a list or range). It’s written as:
[expression for item in iterable if condition]

1. Basic List Comprehension:
Create a list of squares for numbers 1 through 5.
squares = [x**2 for x in range(1, 6)]

2. Adding a Conditional:
Filter the squares to include only even numbers.
even_squares = [x**2 for x in range(1, 6) if x**2 % 2 == 0]

3. Nested Loops in List Comprehensions:
Generate pairs (x, y) for x in [1, 2, 3] and y in [4, 5, 6].
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]

4. Conditional Assignment (Ternary Operator):
Assign a value based on a condition.
result = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]

Problem Statement:
Can you use a list comprehension to create a list of numbers divisible by both 3 and 5 from 1 to 100?
'''

if __name__=="__main__":
    print([x for x in range(1,101) if x%15 == 0])