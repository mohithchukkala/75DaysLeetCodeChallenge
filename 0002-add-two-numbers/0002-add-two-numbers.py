# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        tail=dummy
        carry=0
        while l1 or l2 or carry:
            if l1:
                val1=l1.val
            else:
                val1=0
            if l2:
                val2=l2.val
            else:
                val2=0
            tot=val1+val2+carry

            tail.next=ListNode(tot%10)
            tail=tail.next
            carry=tot//10

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        dummy=dummy.next
        return dummy
        