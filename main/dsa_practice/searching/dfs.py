'''
Depth-first search is a graph traversal algorithm that explores as deeply as possible along each branch before backtracking.

Concept:
	•	Backtracking: Explores all nodes along a path until a dead end is reached, then backtracks.
	•	Stack-Based Approach: Uses a stack (implicit via recursion or explicit) to track the path.
	•	Suitable for Connectivity and Cycles: Identifies connected components, cycles, and topological ordering.
	•	Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges. Space Complexity: O(V) (stack space for recursion or explicit stack).

How it works:
	•	Start at the source node and mark it as visited.
	•	Explore one of its unvisited neighbors.
	•	Continue exploring deeper into the graph until a dead end is reached.
	•	Backtrack to the last visited node with unvisited neighbors.
	•	Repeat until all nodes are visited or the target node is found.
'''