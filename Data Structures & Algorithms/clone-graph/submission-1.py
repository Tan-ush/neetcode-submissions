# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone = {node: Node(node.val)}
        head = clone[node]
        stack = [node]

        while stack:
            cur = stack.pop()
            for child in cur.neighbors:
                if child not in clone:
                    clone[child] = Node(child.val)
                    stack.append(child)
                clone[cur].neighbors.append(clone[child])
        return head
            
                
        
            
        




        