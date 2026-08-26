# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None or head.next is None:
            return head
        slow=head
        count=1
        while slow is not None and slow.next is not None:
            slow=slow.next
            count+=1
        a=count//k
        if a==0:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while a:
            group_prev = prev
            group_start = curr
            rev_prev = None

            for i in range(k):
                nextnode = curr.next
                curr.next = rev_prev
                rev_prev = curr
                curr = nextnode

            group_prev.next = rev_prev
            group_start.next = curr
            prev = group_start

            a -= 1
        return dummy.next

