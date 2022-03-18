class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2, targetPosition):
        cur = ListNode()
        head = cur
        nodePosition = 0

        while list1 is not None and list2 is not None:
            if nodePosition == targetPosition:
                cur.next = list2
                cur = list2
                list2 = list2.next
                targetPosition +=1
                nodePosition += 1
            else:
                cur.next = list1
                cur = list1
                list1 = list1.next
                nodePosition += 1

            if list2 is None:
                cur.next = list1
                nodePosition += 1

        return head.next


l1_node3 = ListNode(10, None)
l1_node2 = ListNode(8, l1_node3)
l1_node1 = ListNode(6, l1_node2)
l1_head1 = ListNode(1, l1_node1)

l2_node3 = ListNode(14, None)
l2_node2 = ListNode(7, l2_node3)
l2_node1 = ListNode(3, l2_node2)
l2_head1 = ListNode(0, l2_node1)

solution = Solution()
result = solution.mergeTwoLists(l1_head1, l2_head1, 3)
arr = []

while (result):
    arr.append(result.val)
    # print(result.val)
    result = result.next
print(arr)


