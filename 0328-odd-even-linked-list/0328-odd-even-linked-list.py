# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        curr=head
        temp=head.next
        prev=temp
        while temp is not None and temp.next is not None:
            curr.next=temp.next
            curr=temp.next
            temp.next=curr.next
            temp=curr.next
        curr.next=prev
        return head
        