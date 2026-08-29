# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        
        prev=dummy
        curr=head
        num=0
        while curr is not None and curr.next is not None:
            nextnode=curr.next
            if nextnode.val==curr.val:
                while curr.next and curr.val==curr.next.val:
                    curr=curr.next
                curr = curr.next
                prev.next = curr
            else:
                    prev=curr
                    curr=curr.next
        return dummy.next

            
        