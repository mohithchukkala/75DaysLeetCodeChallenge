# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        temp=head.next
        copy=temp
        prev=head
        
        while temp is not None and temp.next is not None:
            prev.next=temp.next
            prev=temp.next
            temp.next=prev.next
            temp=prev.next
        prev.next=copy

        return head
        