# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        curr=head
        temp=head.next
        while temp is not None and temp.next is not None:
            temp=temp.next.next
            curr=curr.next
            if curr==temp:
                return True
        return False
        