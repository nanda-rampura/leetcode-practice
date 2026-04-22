import pytest
from graphs.clone_graph import CloneGraph, Node


def build_graph():
    # Graph:
    # 1 -- 2
    # |    |
    # 4 -- 3

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    return n1


def test_clone_graph_structure():
    root = build_graph()
    clone = CloneGraph().cloneGraph(root)

    assert clone is not root
    assert clone.val == root.val
    assert len(clone.neighbors) == len(root.neighbors)


def test_clone_graph_deep_copy():
    root = build_graph()
    clone = CloneGraph().cloneGraph(root)

    # Ensure no node is same reference
    visited = set()
    queue = [(root, clone)]

    while queue:
        original, copied = queue.pop()

        assert original is not copied
        assert original.val == copied.val

        visited.add(original)

        for o, c in zip(original.neighbors, copied.neighbors):
            if o not in visited:
                queue.append((o, c))


def test_empty_graph():
    assert CloneGraph().cloneGraph(None) is None