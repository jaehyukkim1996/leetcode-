class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # initialization
        odd = head
        even = odd.next
        even_head = odd.next #for connecting odd part to even head

        while even and even.next is not None:
            odd.next = even.next # 1->3
            odd = odd.next # move the odd forward new odd is now 3 (odd = 3)
            even.next = odd.next # move the even pointer 2->4
            even = even.next #move the even forward new even is now 4 (even = 4)

        odd.next = even_head #connecting the last odd to even_head (5->2)
        return head


l1_node3 = ListNode(5, None)
l1_node3 = ListNode(4, l1_node3)
l1_node2 = ListNode(3, l1_node3)
l1_node1 = ListNode(2, l1_node2)
l1_head1 = ListNode(1, l1_node1)


solution = Solution()
result = solution.oddEvenList(l1_head1)
arr = []

while (result):
    arr.append(result.val)
    # print(result.val)
    result = result.next
print(arr)