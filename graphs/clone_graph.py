
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional
class CloneGraph:
    """
Problem: Clone Graph
Difficulty: Medium
LeetCode: https://leetcode.com/problems/clone-graph/
Pattern: Graph / BFS / DFS (Graph Traversal)
"""
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        nodesmap = {}
        queue = deque()
        queue.append(node)
        nodesmap[node] = Node(node.val, [])
        while queue:
            curr = queue.popleft() 
            for nbor in curr.neighbors:
                if nbor not in nodesmap:
                    newnode = Node(nbor.val,[])
                    nodesmap[nbor] = newnode
                    queue.append(nbor)    
                nodesmap[curr].neighbors.append(nodesmap[nbor])
        
        return nodesmap[node]