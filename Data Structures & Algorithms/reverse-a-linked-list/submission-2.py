# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            temp = cur.next #1 # None
            cur.next = prev # None # 2
            prev = cur # 0 # 3
            cur = temp # 1 # None
            if not cur:
                return prev
        return cur
        

        
        