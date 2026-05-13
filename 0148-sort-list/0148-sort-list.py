# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge(lefthand,righthand):
    dummy=ListNode(0)
    tail=dummy
    while lefthand and righthand:
        if lefthand.val<righthand.val:
            tail.next=lefthand
            lefthand=lefthand.next
        else:
            tail.next=righthand
            righthand=righthand.next
        tail=tail.next

    if lefthand:
        tail.next=lefthand
    if righthand:
        tail.next=righthand
    return dummy.next
def mergesort(head):
    if head is None or head.next is None:
        return head
    middle=length(head)
    left=mergesort(head)
    right=mergesort(middle)
    return merge(left,right)
def length(head):
    prev=None
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=None
    return slow
class Solution(object):
    def sortList(self, head):
        return mergesort(head)
        