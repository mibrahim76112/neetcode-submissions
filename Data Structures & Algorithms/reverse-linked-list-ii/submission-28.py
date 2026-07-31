# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head


        curr = head
        n = 1
        prev_left = None
        while curr is not None and n < left:
            prev_left = curr
            curr = curr.next
            n+=1

        left = curr
        prev = None
        
        while curr is not None and n <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n+=1


        if prev_left is not None:
            prev_left.next = prev
        else:
            head = prev
        
        left.next = curr
        
        return head


        