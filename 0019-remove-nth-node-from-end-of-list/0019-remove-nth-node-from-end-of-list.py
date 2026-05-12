# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        count=1
        while temp.next is not None:
            temp=temp.next
            count+=1
        if head is None:
            return None
        if count==1 and n==1:
            return None
        res=count-n
        temp=head
        prev=None
        if n==count:
            return head.next
        if res!=count:
            while res!=0:
                prev=temp
                temp=temp.next
                res-=1
            prev.next=temp.next
            return head
        

        