# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        temp=head
        prev=None
        while temp is not None:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        head=prev
        temp=head
        stack=[]
        dummy=ListNode(0)
        curr=dummy

        while temp is not None:
            while stack and stack[-1]<=temp.val:
                stack.pop()
            if stack:
                stack.append(temp.val)
            else:
                stack.append(temp.val)
                curr.next=ListNode(stack[-1])
                curr=curr.next
            temp=temp.next
        head=dummy.next
        temp=head
        prev=None
        while temp is not None:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        return prev
                
        
            
            
        