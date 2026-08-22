# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        req=count-n
        temp=head
        prev=None
        if req==0:
            return head.next
        while req!=0:
            prev=temp
            temp=temp.next
            req-=1
        prev.next=temp.next
        del(temp)
        return head
        