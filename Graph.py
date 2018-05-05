class Graph:

    def __init__(self, max_nodes):
        self._graph = dict()
        self.max_nodes = max_nodes+1

    def add_edge(self, snode, enode, directed=False):
        try:
            self._graph[snode]
        except KeyError:
            self._graph[snode] = list()

        try:
            self._graph[enode]
        except KeyError:
            self._graph[enode] = list()

        self._graph[snode].append(enode)
        if not directed:
            self._graph[enode].append(snode)
