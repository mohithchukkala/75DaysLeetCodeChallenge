# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow!=None:
            nextnode=slow.next
            slow.next=prev
            prev=slow
            slow=nextnode
        tail=prev
        h=head
        while tail!=None:
            if tail.val!=h.val:
                return False
            h=h.next
            tail=tail.next
        return True