from __future__ import annotations


# T: O(n), S: O(1)
class ListNode:
    def __init__(self, val: int | list = 0, next_node: ListNode | None = None):
        if isinstance(val, list) and not val:
            raise ValueError("can't be empty")

        if isinstance(val, list):
            self.val = val[0]
            self.next = None

            current = self
            for item in val[1:]:
                current.next = ListNode(item)
                current = current.next

        else:
            self.val = val
            self.next = next_node


class Solution:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        current = head
        prev = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            print(prev.val)

        return head


head = ListNode([1, 2, 3, 4, 5])
sol = Solution()
print(sol.reverse_list(head))
