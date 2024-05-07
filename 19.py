#Given the head of a linked list, remove the nth node from the end of the list and return its head.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        last = head
        for _ in range(n):
            last = last.next

        first = head

        if last is None:
            return head.next

        while last.next is not None:
            first = first.next
            last = last.next

        first.next = first.next.next

        return head



