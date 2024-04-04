'''https://leetcode.com/problems/clone-graph/description/'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        return self.cloneNode(node, {})

    def cloneNode(self, node, data) :
        if node.val in data :
            return data[node.val]
        nbr = []
        newNode = Node(node.val, [])
        data[node.val] = newNode
        for i in node.neighbors :
            if i.val in data :
                newNode.neighbors.append(data[i.val])
            else :
                newNode.neighbors.append(self.cloneNode(i, data))
        return newNode