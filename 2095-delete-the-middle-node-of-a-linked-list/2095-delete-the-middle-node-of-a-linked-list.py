# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head is None:
            return head
        if head.next is None:
            return None
        slow=head
        fast=head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head
        