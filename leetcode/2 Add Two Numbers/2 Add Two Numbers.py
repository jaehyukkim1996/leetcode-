class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            if l1 is not None:
                v1 = l1.val
            else:
                v1 = 0
            if l2 is not None:
                v2 = l2.val
            else:
                v2 = 0

            # calculating digits
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # updating the pointers
            cur = cur.next
            if l1 is not None:
                l1 = l1.next
            else:
                l1 = None
            if l2 is not None:
                l2 = l2.next
            else:
                l2 = None

        return dummy.next






l1_node3 = ListNode(9, None)
l1_node2 = ListNode(9, l1_node3)
l1_node1 = ListNode(9, l1_node2)
l1_head1 = ListNode(9, l1_node1)

l2_node3 = ListNode(9, None)
l2_node2 = ListNode(9, l2_node3)
l2_node1 = ListNode(9, l2_node2)
l2_head1 = ListNode(9, l2_node1)

solution = Solution()
result = solution.addTwoNumbers(l1_head1, l2_head1)
arr = []

while (result):
    arr.append(result.val)
    # print(result.val)
    result = result.next
print(arr)
