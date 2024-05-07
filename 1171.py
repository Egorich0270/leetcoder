# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        array = []
        start = head
        while start:
            array.append(start.val)
            start = start.next
        for i in range(len(array)):
            suma = 0
            for j in range(i, len(array)):
                suma += array[j]
                if suma == 0:
                    for x in range(i, j+1):
                        array[x] = 0
        start = head
        for x in array:
            if x != 0:
                start.val = x
                start = start.next
        return head



print(Solution().removeZeroSumSublists(ListNode(1, ListNode(2, ListNode(-2)))))