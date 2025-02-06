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


from collections import deque

def depth_first_search(graph,start,target):

    visited=set()
    queue=deque()
    path=list()

    visited.add(start)
    queue.append(start)
    path.append(start)

    if start == target:
        return start

    while queue:
        current_node=queue.popleft()
        neighbors=graph[current_node]
        for neighbor in neighbors:
            if neighbor == target:
                return "".join(map(str,path))
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path.append('->'+neighbor)

    return 'Not Found'

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start ='A'
    target = 'B'

    search_result = depth_first_search(graph, start, target)

    if search_result == 'Not Found':
        print(f"Element {target} is not found in the given graph.")
    else:
        print(f"Element {target} is found after visiting {search_result} nodes.")