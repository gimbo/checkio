#!/usr/bin/env python3

"""Disposable teleports

The island has eight stations which are connected by a network of
teleports; however, the teleports take a very long time to
recharge. This means you can only use each one once. After you use a
teleport, it will shut down and no longer function. But you can visit
any station more than once. For this task, you should begin at number 1
and try to travel around to all the stations before returning to the
starting point. The map of the teleports is presented as a string in
which the comma-separated list represents teleports. Each teleport is
given the name of the station it connects to. This name consists of two
digits, such as '12' or '32.' Each test requires you to provide a route
which passes through every station. A route is presented as a string of
the station numbers in the sequence in which they must be visited
(ex. 123456781).

Input: A teleport map as a string.

Output: The sequence of station numbers as a string.

How it is used: This task is another example of the graph-search
problem. It’s like trying to find a route where you can not to step on
the same spot twice.

Precondition:
len(stations) == 8
Teleports are not repeated and undirected.

"""


def checkio(teleports_string):
    graph = Graph.from_string(teleports_string)
    solution = graph.find_path(1)
    return ''.join([str(x) for x in solution])


class Graph(object):

    def __init__(self):
        self.edges = set()

    def __repr__(self):
        return repr(self.edges)

    @property
    def nodes(self):
        nodes = set()
        for (src, target) in self.edges:
            nodes.add(src)
            nodes.add(target)
        return nodes

    @staticmethod
    def from_string(edges_string):
        graph = Graph()
        for item in edges_string.split(','):
            left, right = sorted(map(int, item))[:2]
            graph.edges.add((left, right))
        return graph

    def find_path(self, start):
        """Return path (as list of nodes)."""
        stack = [Step(self, [start])]
        while stack:
            step = stack.pop()
            for step in step.steps_from_here():
                if step.is_solution(self.nodes, start):
                    return step.path
                stack.append(step)
        raise ValueError('No path found')

    def edges_from_node(self, node):
        edges = set()
        for (src, target) in self.edges:
            if src == node:
                edges.add((node, target))
            elif target == node:
                edges.add((node, src))
        return edges

    def duplicate_minus_edge(self, edge):
        duplicate = Graph()
        duplicate.edges = set(self.edges)
        (src, target) = edge
        duplicate.edges.discard((src, target))
        duplicate.edges.discard((target, src))
        return duplicate


class Step(object):

    """A step in the search stack."""

    def __init__(self, graph, path):
        self.graph = graph
        self.path = path

    def __repr__(self):
        return repr((self.graph, self.path))

    def steps_from_here(self):
        steps = []
        for (src, target) in self.graph.edges_from_node(self.path[-1]):
            new_graph = self.graph.duplicate_minus_edge((src, target))
            new_path = self.path + [target]
            steps.append(Step(new_graph, new_path))
        return steps

    def is_solution(self, nodes, start):
        if (self.path[0], self.path[-1]) != (start, start):
            return False
        nodes_in_path = { x for x in self.path }
        return nodes_in_path.issuperset(nodes)


# This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if teleport not in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
