# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp1=headA
        temp2=headB
        length1=1
        length2=1
        while temp1.next is not None:
            temp1=temp1.next
            length1+=1
        while temp2.next is not None:
            temp2=temp2.next
            length2+=1
        n=abs(length2-length1)
        if length2>length1:
            while n!=0:
                headB=headB.next
                n-=1
            while headA and headB:
                if headA!=headB:
                    headA=headA.next
                    headB=headB.next
                else:
                    return headA
            return None
        else:
            while n!=0:
                headA=headA.next
                n-=1
            while headA and headB:
                if headA!=headB:
                    headA=headA.next
                    headB=headB.next
                else:
                    return headA
            return None

        