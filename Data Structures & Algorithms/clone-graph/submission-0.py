'''
Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
            bfs exploration through the nodes
        '''
        if not node:
            return
        nodeMap = {node: Node(node.val)}
        q = collections.deque([node])

        while q:
            cur = q.popleft()   
            
            for neighbor in cur.neighbors:
                if neighbor not in nodeMap:
                    nodeMap[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
            
                nodeMap[cur].neighbors.append(nodeMap[neighbor])

        return nodeMap[node]
