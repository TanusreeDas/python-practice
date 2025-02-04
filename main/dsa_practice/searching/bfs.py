'''
Breadth-first search is a graph traversal algorithm that explores all nodes at the current depth level before moving on to nodes at the next depth level.

Concept:
	•	Layer-by-Layer Exploration: Explores nodes level by level starting from the source.
	•	Queue-Based Approach: Uses a queue to keep track of nodes to explore.
	•	Suitable for Shortest Path: Finds the shortest path in an unweighted graph.
	•	Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges., Space Complexity: O(V) (for the queue and visited list).

How it works:
	•	Start at the source node and mark it as visited.
	•	Add it to the queue.
	•	While the queue is not empty: Dequeue a node and process it. Enqueue all its unvisited neighbors and mark them as visited.
	•	Continue until all nodes are visited or the target node is found.
'''