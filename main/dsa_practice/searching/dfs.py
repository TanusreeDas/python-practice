from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_iterative(self, start, target):
        stack = [(start, [start])]
        visited = set()

        while stack:
            current_node, path = stack.pop()

            if current_node == target:
                print("Path to", target, ":", " -> ".join(map(str, path)))
                return

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

        print("Target", target, "not found in the graph.")


    def dfs_recursion(self, start, target, visited=None, path=None):
        if visited: visited = set()

        #stack= deque()



if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    g.dfs_iterative(1, 6)

