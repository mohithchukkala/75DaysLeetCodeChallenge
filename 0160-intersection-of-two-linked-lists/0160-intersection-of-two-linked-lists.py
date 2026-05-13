# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a=headA
        b=headB
        while a!=b:
            if a!=None:
                a=a.next
            else:
                a=headB
            
            if b!=None:
                b=b.next
            else:
                b=headA
        return a