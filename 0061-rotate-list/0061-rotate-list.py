# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head,k):
        if head is None or head.next is None:
            return head
        length=1
        temp=head
        while temp.next is not None:
            temp=temp.next
            length+=1
        k=k%length
        c=length-k
        temp=head
        if c==length:
            return head
        else:
            while c!=1:
                temp=temp.next
                c-=1
            curr=temp.next
            new_head=curr
            temp.next=None
            while curr.next is not None:
                curr=curr.next
            curr.next=head
            return new_head
            