#!/usr/bin/env python3

"""How to find friends

Sophia's drones are not soulless and stupid drones; they can make and
have friends. In fact, they already are working for the their own social
network just for drones! Sophia has received the data about the
connections between drones and she wants to know more about relations
between them.

We have an array of straight connections between drones. Each connection
is represented as a string with two names of friends separated by
hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are
friends. Your should write a function that allow determine more complex
connection between drones. You are given two names also. Try to
determine if they are related through common bonds by any depth. For
example: if two drones have a common friends or friends who have common
friends and so on.

Let's look at examples:

scout2 and scout3 have the common friend scout1 so they are
related. super and scout2 are related through sscout, scout4 and
scout1. But dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings;
first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

How it is used: This concept will help you find not too obvious
connections with the building of bond networks. And how to work social
networks.

Precondition: len(network) <= 45
if "name1-name2" in network, then "name2-name1" not in network
3 <= len(drone_name) <= 6
first_name and second_name in network.

"""

import collections


# For depth-first search, just replace the collections.deque with a list, and
# append() to it instead of appendleft().


def check_connection(network, src, target):
    if src == target:
        return True
    return bfs_graph(build_graph(network), src, target)


def build_graph(network):
    """Represent network as a mapping from nodes to lists of neighbours"""
    graph = collections.defaultdict(list)
    for item in network:
        left, right = sorted(item.split('-'))[:2]
        graph[left].append(right)
        graph[right].append(left)
    return dict(graph)


def bfs_graph(graph, src, target):
    """Search graph breadth-first for a path from src to target."""
    queue = collections.deque([src])
    visited = set()
    while queue:
        current = queue.pop()
        visited.add(current)
        neighbours = graph[current]
        if target in neighbours:
            return True
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.appendleft(neighbour)
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") is True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") is True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") is False, "I don't know any scouts."
