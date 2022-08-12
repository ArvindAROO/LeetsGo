# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        i = 0
        while head:
            if head not in lst:
                lst.append(head)
                i += 1
            else:
                return head
            head = head.next
        return None