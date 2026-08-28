# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge(left,right):
    dummy=ListNode(0)
    tail=dummy
    while left and right:
        if left.val<right.val:
            tail.next=left
            left=left.next
        else:
            tail.next=right
            right=right.next
        tail=tail.next
    if left is not None:
        tail.next=left
    if right is not None:
        tail.next=right
    return dummy.next
                
def length(head):
    slow=head
    fast=head
    prev=None
    while fast is not None and fast.next is not None:
        prev=slow
        slow=slow.next
        fast=fast.next.next

    prev.next=None
    return slow
def mergesort(head):
    if head is None or head.next is None:
        return head
    middle=length(head)
    left=mergesort(head)
    right=mergesort(middle)

    return merge(left,right)

class Solution(object):
    def sortList(self, head):
        return mergesort(head)
        