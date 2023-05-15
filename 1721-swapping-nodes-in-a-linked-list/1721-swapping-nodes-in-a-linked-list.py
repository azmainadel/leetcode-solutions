# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left_node, right_node = head, head
        for i in range(1, k):
            left_node = left_node.next
        
        current_node = left_node
        
        while current_node.next:
            right_node = right_node.next
            current_node = current_node.next

        left_node.val, right_node.val = right_node.val, left_node.val

        return head