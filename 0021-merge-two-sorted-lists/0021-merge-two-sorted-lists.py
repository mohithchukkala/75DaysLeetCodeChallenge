# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return list1
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1
        dummy=ListNode(0)
        tail=dummy
        temp1=list1
        temp2=list2
        while temp1 is not None and temp2 is not None:
            if temp1.val<=temp2.val:
                tail.next=temp1
                temp1=temp1.next
            else:
                tail.next=temp2
                temp2=temp2.next
            tail=tail.next
        if temp1 is not None:
            tail.next=temp1
        if temp2 is not None:
            tail.next=temp2
        return dummy.next

        