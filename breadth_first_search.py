class Graph:

    def __init__(self, max_nodes):
        self.__graph = dict()
        self.max_nodes = max_nodes+1

    def add_edge(self, snode, enode, directed=False):
        try:
            self.__graph[snode]
        except KeyError:
            self.__graph[snode] = list()

        try:
            self.__graph[enode]
        except KeyError:
            self.__graph[enode] = list()

        self.__graph[snode].append(enode)
        if not directed:
            self.__graph[enode].append(snode)

    def bfs(self, s):
        visited = [False] * self.max_nodes
        queue   = []

        queue.append(s)
        visited[s] = True

        while queue:
            cnode = queue.pop(0)
            print (cnode, end=' ')

            for node in self.__graph[cnode]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

# Driver Code
g = Graph(7)
g.add_edge(2, 3)
g.add_edge(1, 3)
g.add_edge(5, 6)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 7)
g.add_edge(4, 5)
g.bfs(1)
