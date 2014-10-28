#!/usr/bin/env python3

"""Open Labyrinths

The labyrinth has no walls, but bushes surround the path on each
side. If a players move into a bush, they lose. The labyrinth is
presented as a matrix (a list of lists): 1 is a bush and 0 is part of
the path. The labyrinth's size is 12 x 12 and the outer cells are also
bushes. Players start at cell (1,1). The exit is at cell (10,10). You
need to find a route through the labyrinth. Players can move in only
four directions--South (down [1,0]), North (up [-1,0]), East (right
[0,1]), West (left [0, -1]). The route is described as a string
consisting of different characters: "S"=South, "N"=North, "E"=East, and
"W"=West.

Input: A labyrinth map as a list of lists with 1 and 0.

Output: The route as a string that contains "W", "E", "N" and "S".

How it is used: This is a classical problem for path-finding in graphs
-- Yes, the maze can be represented as a graph. It can be used in
navigation software for a to b navigation and computer games for
artificial intelligence. You can find your way anywhere you wish. Just
divide a map into square cells and mark up the "bad" cells.

Precondition: Outer cells are pits.
len(labyrinth) == 12
all(len(row) == 12 for row in labyrinth)

"""

"""Open labyrinth via conversion to graph then depth-first search.

In this solution we convert the maze to a graph then perform a
depth-first search to find a path from the start to the exit.

Each node in the graph is one of:
  - The start cell
  - The exit cell
  - A junction
  - A dead end

Including dead ends isn't necessary to solve the given problem, but
it's kinda nice because it means we've got a complete representation
of the maze.

The edges are represented as a mapping from source nodes to mappings
from destination nodes to sets of paths between those nodes, where a
path is a string of directions (e.g. 'NNNEEEEWWS').

This solution finds the path from start to exit via depth-first
search, but as we've got the paths we could easily weight the edges by
path length and apply Dijkstra's shortest path algorith.  Future work.
:-)

"""

from collections import defaultdict


def checkio(maze_map):
    parser = MazeMapParser(maze_map)
    maze = parser.maze_graph()
    return maze.dfs()


class MazeGraph(object):

    # Each direction has an offset and an inversion.
    DIRECTIONS = {
        'S': ((0, 1), 'N'),
        'N': ((0, -1), 'S'),
        'W': ((-1, 0), 'E'),
        'E': ((1, 0), 'W'),
    }

    def __init__(self, start_cell, exit_cell):
        super().__init__()
        self.start_cell = start_cell
        self.exit_cell = exit_cell
        self.nodes = set()
        self.edges = defaultdict(lambda: defaultdict(set))

    def __str__(self):
        lines = []
        lines.append('Nodes:')
        for node in sorted(self.nodes):
            lines.append('  {0}'.format(node))
        lines.append('Edges:')
        for src in self.edges:
            lines.append('  {0} ->'.format(src))
            for dest in self.edges[src]:
                lines.append('    {0}'.format(dest))
                for path in self.edges[src][dest]:
                    lines.append('      {0}'.format(path))
        return '\n'.join(lines)

    def dfs(self):
        """Find a path from start to exit via depth-first search."""
        def add_to_stack(stack, done, src, path):
            for dest in self.edges[src]:
                if dest not in done:
                    for step_path in self.edges[src][dest]:
                        stack.append((dest, step_path, path))
            done.add(src)
        stack = []    # Stack of steps to take
        done = set()  # Nodes we've visited
        # Seed the stack with all edges from the start cell.
        add_to_stack(stack, done, self.start_cell, '')
        while stack:
            (src, step_path, path) = stack.pop()
            path = path + step_path
            if src == self.exit_cell:
                return path
            add_to_stack(stack, done, src, path)
        return ''  # No path found.


class MazeMapParser(object):

    """Helper: parse a maze map string into a MazeGraph object."""

    def __init__(self, maze_map):
        self.maze_map = maze_map
        self.width = len(maze_map[0])
        self.height = len(maze_map)

    def maze_graph(self, start_cell=None, exit_cell=None):
        """Construct and return the MazeGraph."""
        # Here we default to top-left and bottom-right for start/exit.
        # But they can be anything.
        if start_cell is None:
            start_cell = (1, 1)
        if exit_cell is None:
            exit_cell = (self.width - 2, self.height - 2)
        maze = MazeGraph(start_cell, exit_cell)
        self.add_nodes(maze)
        self.add_edges(maze)
        return maze

    def add_nodes(self, maze):
        # Start and exit cells need to be nodes in the graph.
        maze.nodes.add(maze.start_cell)
        maze.nodes.add(maze.exit_cell)
        # Every cell with anything other than zero or two neighbours
        # is also a node.  That means junctions and dead ends.
        for y in range(self.height):
            for x in range(self.width):
                neighbours = self.cell_neighbours(x, y)
                if len(neighbours) not in (0, 2):
                    maze.nodes.add((x, y))

    def cell_neighbours(self, x, y):
        """Compute neighbours of a cell.  A filled cell has none."""
        if self.maze_map[y][x]:
            return set()
        neighbours = set()
        for (direction, ((i, j), dummy)) in MazeGraph.DIRECTIONS.items():
            xi, yj = (x + i) % self.width, (y + j) % self.height
            if not self.maze_map[yj][xi]:
                neighbours.add((direction, (xi, yj)))
        return neighbours

    def add_edges(self, maze):
        # From each node, for each neighbour, we walk a path starting
        # in that direction until we hit another node.  Then we add
        # that path and its inverse to the maze graph.  As we add the
        # inverse paths automatically, we can skip some explorations.
        done = set()  # Set of ((x, y), direction)
        for (x, y) in maze.nodes:
            for (direction, (i, j)) in self.cell_neighbours(x, y):
                if ((x, y), direction) in done:
                    continue  # We must have already walked its inverse.
                (path, (x2, y2)) = self.follow_path(x, y, direction, maze.nodes)
                maze.edges[(x, y)][(x2, y2)].add(path)
                done.add(((x, y), path[0]))
                rev_path = self.invert_path(path)
                maze.edges[(x2, y2)][(x, y)].add(rev_path)
                done.add(((x2, y2), rev_path[0]))

    def follow_path(self, x, y, direction, nodes):
        # First, take a single step in the specified direction.
        x1, y1 = x, y
        path = [direction]
        i, j = MazeGraph.DIRECTIONS[direction][0]
        x2, y2 = x1 + i, y1 + j
        while True:
            if (x2, y2) in nodes:
                # We've reached a node so we're be done.
                return (''.join(path), (x2, y2))
            # Where could we go, excluding where we came from?
            neighbours = [(d, (x3, y3))
                          for (d, (x3, y3)) in self.cell_neighbours(x2, y2)
                          if (x3, y3) != (x1, y1)]
            # First neighbour is only neighbour; so take it.
            x1, y1 = x2, y2
            (direction, (x2, y2)) = neighbours[0]
            path.append(direction)

    def invert_path(self, path):
        return ''.join([MazeGraph.DIRECTIONS[d][1] for d in path[::-1]])


if __name__ == '__main__':
    # This code using only for self-checking and not necessary for auto-testing
    def check_route(func, labyrinth):
        MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
        # copy maze
        route = func([row[:] for row in labyrinth])
        pos = (1, 1)
        goal = (10, 10)
        for i, d in enumerate(route):
            move = MOVE.get(d, None)
            if not move:
                print("Wrong symbol in route")
                return False
            pos = pos[0] + move[0], pos[1] + move[1]
            if pos == goal:
                return True
            if labyrinth[pos[0]][pos[1]] == 1:
                print("Player in the pit")
                return False
        print("Player did not reach exit")
        return False

    # These assert are using only for self-testing as examples.
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "First maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Empty maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Up and down maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Dotted maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Need left maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."
    print("The local tests are done.")
