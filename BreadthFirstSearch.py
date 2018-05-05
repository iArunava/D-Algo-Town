from Graph import Graph

class BFS(Graph):

    def __init__(self, max_nodes):
        super().__init__(max_nodes)

    def bfs(self, s):
        visited = [False] * self.max_nodes
        queue   = []

        queue.append(s)
        visited[s] = True

        while queue:
            cnode = queue.pop(0)
            print (cnode, end=' ')

            for node in self._graph[cnode]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

# Driver Code
g = BFS(7)
g.add_edge(2, 3)
g.add_edge(1, 3)
g.add_edge(5, 6)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 7)
g.add_edge(4, 5)
g.bfs(1)
