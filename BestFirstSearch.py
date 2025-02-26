import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append((cost, neighbor))
        self.graph[neighbor].append((cost, node)) 

    def best_first_search(self, start, goal):
        visited = set()
        pq = [(0, start)]  
        while pq:
            cost, node = heapq.heappop(pq)  
            if node in visited:
                continue
            print(f"Visiting: {node}")  
            visited.add(node)
            if node == goal:
                print("Goal Reached!")
                return
            for neighbor_cost, neighbor in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (neighbor_cost, neighbor))

g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('C', 'E', 10)
g.add_edge('D', 'E', 2)

print("Best First Search from A to E:")
g.best_first_search('A', 'E')
