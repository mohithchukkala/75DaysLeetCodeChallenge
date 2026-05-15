# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        temp=head.next
        prev=head
        while temp is not None:
            if temp.val==prev.val:
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        return head