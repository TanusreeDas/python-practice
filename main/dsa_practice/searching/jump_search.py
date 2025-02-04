'''
Jump-search is an algorithm for sorted data that skips ahead by fixed steps (jump size) and then performs a linear search within the identified block.

Concept:
	•	Jump in Fixed Steps: Moves in steps of size sqrt{n} through the array.
	•	Localized Search: After a potential range is identified, linear search is performed within that block.
	•	Time Complexity: O(sqrt{n}), Space Complexity: O(1).

How it works:
	•	Start at the first element and jump ahead by \sqrt{n} steps.
	•	Stop jumping when the current element exceeds or equals the target.
	•	Perform a linear search within the block from the previous jump to the current position.
	•	If the target is found, return its index; otherwise, return -1.
'''