# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        p = head.next
        while p:
            a = 0
            while p.val != 0:
                a += p.val
                p = p.next

            l.append(a)
            p = p.next

        p = head
        for x in range(len(l) - 1):
            p.val = l[x]
            p = p.next
        p.val = l[-1]
        p.next = None
        return head
