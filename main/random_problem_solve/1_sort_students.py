'''
Concept:
sorted():
	•	sorted() works on any iterable (e.g., lists, tuples, dictionaries). In case of list, it creates a new sorted list: It does not modify the original list.
	•	Syntax: sorted(iterable, key=None, reverse=False)
	•	iterable: The data you want to sort (like a list, tuple, etc.).
	•	key: A function that defines how to sort the items.
	•	reverse: If True, sorts in descending order.
	•	When to use: When you need a sorted version of the data but want to keep the original data unchanged.

list.sort():
	•	Sorts the list in place: It modifies the original list and returns None.
	•	Syntax: list.sort(key=None, reverse=False)
	•	Same parameters as sorted().
	•	When to use: When you want to sort the list and don’t need to keep the original order.

Both of them use Timsort  and have a time complexity of O(n log n). Where space complexity for sorted is: O(n) and list.sort is: O(1)

Problem statement:
You have a list of students, where each student is represented as a tuple containing their name and grade.
    1.  sort() is specific to lists. Sort the students in descending order of grades.
	2.	If two students have the same grade, sort them alphabetically by name.
	3.	Return a new list with the sorted students (use sorted()).

Example: students = [("Alice", 85), ("Bob", 75), ("Charlie", 95), ("Diana", 85)]
'''

def sort_students(students):
    sort_student_list = sorted(students, key = lambda student: (-student[1], student[0]))
    return sort_student_list

if __name__ == "__main__":
    student_list = [("Alice", 85), ("Bob", 75), ("Charlie", 95), ("Diana", 85)]
    print(sort_students(student_list))


