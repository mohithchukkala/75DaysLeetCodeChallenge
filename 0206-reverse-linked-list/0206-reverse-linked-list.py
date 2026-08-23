# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        temp=head
        curr=head
        prev=None
        while temp is not None:
            temp=temp.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
            
        