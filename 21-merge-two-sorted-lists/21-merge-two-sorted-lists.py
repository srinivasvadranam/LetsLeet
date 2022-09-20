# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_head = res
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val :
                res.next = ListNode(list1.val)
                list1 = list1.next
                res = res.next
                
            else:
                res.next = ListNode(list2.val)
                list2 = list2.next
                res = res.next
                
        if list1 != None or list2 != None :
            res.next = list1 if list1 else list2
            
        return res_head.next