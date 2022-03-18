class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # cursor is currently empty node (value = 0, next = None)
        # cursor is used to locate where we are at the linked list
        cur = ListNode()
        # head is the very first node in the list
        head = cur

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next

            else:
                cur.next = list2
                # same as the above (just different syntax for it)
                cur, list2 = list2, list2.next

        if list1 != None:
            cur.next = list1
        else:
            cur.next = list2

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
result = solution.mergeTwoLists(l1_head1, l2_head1)
arr = []

while (result):
    arr.append(result.val)
    # print(result.val)
    result = result.next
print(arr)


