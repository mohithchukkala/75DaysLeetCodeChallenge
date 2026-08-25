# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        slow=head
        fast=head
        count=1
        while fast is not None and fast.next is not None:
            fast=fast.next
            count+=1
        k=k%count
        if k==0:
            return head
        req=count-k
        prev=None
        while req:
            prev=slow
            slow=slow.next
            req-=1
        tail=slow
        print(tail)
        prev.next=None
        while slow.next is not None:
            slow=slow.next
        slow.next=head
        return tail
        
        
        