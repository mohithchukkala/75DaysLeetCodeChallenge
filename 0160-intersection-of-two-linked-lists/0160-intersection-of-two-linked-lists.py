# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        slow1=headA
        slow2=headB
        while slow1 or slow2 is not None:
            if slow1 is not None and slow2 is not None and (slow1==slow2):
                return slow1
        
            if slow1 is None:
                slow1=headB
            else:
                slow1=slow1.next

            if slow2 is None:
                slow2=headA
            else:
                slow2=slow2.next
            
            