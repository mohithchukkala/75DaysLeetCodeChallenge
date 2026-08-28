class Solution(object):
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next


        prev.next = None

        prev = None
        while slow:
            nextnode = slow.next
            slow.next = prev
            prev = slow
            slow = nextnode

        slow = head
        fast = prev
        new=None
        while slow is not None and slow.next is not None:
            slow_next = slow.next
            fast_next = fast.next

            slow.next = fast
            fast.next = slow_next
        
            slow = slow_next
            fast = fast_next

        if fast:
            slow.next=fast

        return head