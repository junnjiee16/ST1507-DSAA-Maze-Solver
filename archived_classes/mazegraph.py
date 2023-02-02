import networkx as nx

# graph object, stores metadata for graph and methods to manipulate graph
class MazeGraph(nx.Graph):
    def __init__(self):
        super().__init__()

    def addNode(self, node):
        self.add_node(node)

    def addEdge(self, node1, node2):
        self.add_edge(node1, node2)

    def nodeExists(self, node):
        return self.has_node(node)