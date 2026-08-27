# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        curr=head
        temp=curr
        while curr is not None and curr.next is not None:
            nextnode=curr.next
            if nextnode.val==curr.val:
                curr.next=nextnode.next
                nextnode=nextnode.next
            else:
                curr=curr.next
        return temp
            
        