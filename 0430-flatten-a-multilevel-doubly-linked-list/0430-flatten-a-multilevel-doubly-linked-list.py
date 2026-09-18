class Solution(object):
    def flatten(self, head):
        temp = head
        stack = []

        while temp is not None:

            if temp.child is not None:
                if temp.next is not None:
                    stack.append(temp.next)

                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None

            elif temp.next is None and stack:
                next_node = stack.pop()
                temp.next = next_node
                next_node.prev = temp

            temp = temp.next

        return head