# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        if list2 is None:
            if list1 is None:
                return None
            else:
                return list1
        if list1 is None:
            return list2
        answer = ListNode()
        d = answer
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                d.next = ListNode(list1.val)
                list1 = list1.next
            else:
                d.next = ListNode(list2.val)
                list2 = list2.next
            d = d.next


        if list1 is None:
            d.next = list2
            return answer.next
        else:
            d.next = list1
            return answer.next




