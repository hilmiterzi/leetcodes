class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):

        carry = 0
        dummy_head = ListNode(0)  # Initialize the dummy head
        current = dummy_head  # Pointer to construct the new list
        while l1 is not None and l2 is not None:

            l1Number = l1.val if l1 is not None else 0
            l2Number = l2.val if l2 is not None else 0

            total = carry + l1Number + l2Number

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Creating the second linked list for the number 465
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
solution.addTwoNumbers(l1, l2)
