from typing import List, Optional
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_setattr_lt:
    # the Optional type hint from the typing module is used to indicate that a variable or a return type can either be of a specified type or None
    '''
        lists = [ListNode(1), None, ListNode(2)]
        The lists parameter can contain ListNode objects or None.
        The function can return a ListNode or None.

        given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            k == lists.length
            0 <= k <= 10^4
            0 <= lists[i].length <= 500
            -10^4 <= lists[i][j] <= 10^4
            lists[i] is sorted in ascending order.
            The sum of lists[i].length won't exceed 10^4.
        '''
        head, curr = None, None
        #wrap it with custom comparator
        '''
        To have a custom less-than function using setattr. 
        Note that, simply using the tuple trick and pushing (node.val, node) to the priority queue will not work because the lists have values in common
        (duplicate values, then compare ListNode but not implemnt __lt__ func).
        '''
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)
        min_heap = list(filter(lambda node: node is not None, lists))
        heapq.heapify(min_heap)
        while min_heap:
            node = heapq.heappop(min_heap)

            #add element to result
            if head is None:
                head, curr = node, node
            else:
                curr.next = node
                curr = node

            # detach next element
            if node.next:
                next = node.next
                heapq.heappush(min_heap, next)
                node.next = None
        return head

class Solution_dummy_head_and_tuple_index:
    # the Optional type hint from the typing module is used to indicate that a variable or a return type can either be of a specified type or None
    '''
        lists = [ListNode(1), None, ListNode(2)]
        The lists parameter can contain ListNode objects or None.
        The function can return a ListNode or None.

        given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            k == lists.length
            0 <= k <= 10^4
            0 <= lists[i].length <= 500
            -10^4 <= lists[i][j] <= 10^4
            lists[i] is sorted in ascending order.
            The sum of lists[i].length won't exceed 10^4.
        '''
        dummy= ListNode()
        curr = dummy
        '''
            to resolve duplicate value comparision issue (gonna compare ListNode without __lt__ ), add index to make it distinct for tuple
        '''
        min_heap = [ (node.val, i, node) for i, node in enumerate(lists) if node is not None]
        heapq.heapify(min_heap)
        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            #add element to result
            curr.next = node
            curr = node

            # detach next element
            if node.next:
                next = node.next
                heapq.heappush(min_heap, (next.val, i, next)) # heap only compares dupicates from different ListNode input, so index i must be distinct
                node.next = None
        return dummy.next


            