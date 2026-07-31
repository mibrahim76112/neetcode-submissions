"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        data = {}
        curr = head
        while curr is not None:
            data[curr]  = Node(curr.val)
            curr = curr.next

        curr = head
        while curr is not None:
            data[curr].next = data.get(curr.next)
            data[curr].random = data.get(curr.random)
            curr = curr.next

        return data[head]




        

