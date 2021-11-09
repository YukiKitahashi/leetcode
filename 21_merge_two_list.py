# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
  def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # l1,l2をlistに変換する
    merge_list = []
    if l1 != None:
      while True:
        merge_list.append(l1.val)
        if l1.next == None:
            break
        l1 = l1.next
    if l2 != None:
      while True:
        merge_list.append(l2.val)
        if l2.next == None:
            break
        l2 = l2.next
    
    result_list = sorted(merge_list, reverse=True)

    result_node = None
    for i, val in enumerate(result_list):
      result_node = ListNode(val,result_node)

    return result_node