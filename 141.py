
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        items = {}
        if not head:
            return False
        while head.next:
            items[head] = True
            if items.get(head.next):
                return True
            head = head.next


        return False





a = ListNode(4)
a.next = ListNode(2)

print(id(a))
print(id(a.next))