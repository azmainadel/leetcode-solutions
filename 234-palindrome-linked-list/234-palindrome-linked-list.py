# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        cur = head
        
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
            
        return vals == vals[::-1]