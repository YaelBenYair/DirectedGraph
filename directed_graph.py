from typing import Any


class DirectedGraph:

    def __init__(self):
        self._nodes: dict[Any, list] = {}

    def __str__(self):
        return self._nodes

    def add_node(self, node):
        self._nodes[node] = []

    def add_edge(self, from_node, to_node):
        if from_node not in self._nodes or to_node not in self._nodes:
            raise Exception()

        self._nodes[from_node].append(to_node)

    def is_adjacent(self, node1, node2):
        if node2 not in self._nodes and node1 not in self._nodes:
            raise Exception()

        if node2 in self._nodes[node1]:
            return -1
        elif node1 in self._nodes[node2]:
            return 1
        else:
            return 0


if __name__ == '__main__':
    names = ['brussels', 'kyoto', 'tokyo', 'hong kong', 'tel aviv', 'paris', 'london', 'amsterdam']
    graph = DirectedGraph()

    for city in names:
        graph.add_node(city)






