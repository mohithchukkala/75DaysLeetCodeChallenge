# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow=head
        fast=head
        maxi=0
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        while slow is not None:
            nextnode=slow.next
            slow.next=prev
            prev=slow
            slow=nextnode
        temp=head
        
        while prev is not None:
            maxi=max(maxi,(prev.val+temp.val))
            temp=temp.next
            prev=prev.next
        return maxi
        

        