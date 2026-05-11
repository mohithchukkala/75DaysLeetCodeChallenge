# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def leng(head,count):
        temp=head
        while temp.next is not None:
            temp=temp.next
            count+=1
        return count
        
class Solution(object):
    def middleNode(self, head):
        count=1
        l=leng(head,count)
        curr=head
        mid=l//2
        if l%2==0:
            while mid!=0:
                curr=curr.next
                mid-=1
            return curr
        else:
            while mid!=0:
                curr=curr.next
                mid-=1
            return curr
    