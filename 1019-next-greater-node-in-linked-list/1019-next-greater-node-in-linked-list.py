# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        temp=head
        prev=None
        while temp is not None:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        head=prev

        stack=[]
        ans=[]
        temp=head
        while temp is not None:
            while stack and stack[-1] <= temp.val:
                stack.pop()

            if stack:
                ans.append(stack[-1])
            else:
                ans.append(0)

            stack.append(temp.val)
            temp = temp.next
        ans=ans[::-1]
        return ans