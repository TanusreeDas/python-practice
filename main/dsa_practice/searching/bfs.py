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

from collections import deque

def breadth_first_search(graph,start,target):

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
        'D': ['H'],
        'E': ['B', 'G'],
        'F': ['C', 'E']
    }
    start ='A'
    target = 'H'

    search_result = breadth_first_search(graph, start, target)

    if search_result == 'Not Found':
        print(f"Element {target} is not found in the given graph.")
    else:
        print(f"Element {target} is found after visiting {search_result} nodes.")