class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev



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