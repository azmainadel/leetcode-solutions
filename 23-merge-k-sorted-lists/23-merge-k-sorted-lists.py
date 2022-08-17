# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        if len(lists) == 0:
            return None
        
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            result = ListNode()
            currentNode = result

            while list1 and list2:
                if list1.val < list2.val:
                    currentNode.next = list1
                    list1 = list1.next  
                else:
                    currentNode.next = list2
                    list2 = list2.next
                    
                currentNode = currentNode.next

            if list1:
                currentNode.next = list1
            elif list2:
                currentNode.next = list2

            return result.next
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                mergedLists.append(mergeTwoLists(l1, l2))
            
            lists = mergedLists
            
        return lists[0]