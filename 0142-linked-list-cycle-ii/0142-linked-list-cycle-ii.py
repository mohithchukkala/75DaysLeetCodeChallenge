# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        dict={}
        if head is None or head.next is None:
            return None
        temp=head.next;
        count=0
        dict[head]=count
        while temp not in dict:
            dict[temp]=count+1
            count=count+1
            temp=temp.next
            if temp is None:
                return None
        return temp
        