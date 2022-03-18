class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            # solution = Solution()
            # newHead = solution.reverseList(head.next)
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead


l1_node3 = ListNode(4, None)
l1_node2 = ListNode(3, l1_node3)
l1_node1 = ListNode(2, l1_node2)
l1_head1 = ListNode(1, l1_node1)


solution = Solution()
result = solution.reverseList(l1_head1)
arr = []

while (result):
    arr.append(result.val)
    # print(result.val)
    result = result.next
print(arr)