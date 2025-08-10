"""
In-place Reversal of LinkedList Pattern

In many problems, we are asked to reverse the links between a set of nodes of a 
LinkedList. Often, the constraint is that we need to do this in-place, i.e., 
using the existing node objects and without using extra memory.

Time Complexity: O(n)
Space Complexity: O(1)

Common Problems:
- Reverse a LinkedList
- Reverse a Sub-list
- Reverse every K-element Sub-list
- Reverse alternating K-element Sub-list
- Rotate a LinkedList
"""

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse_linkedlist(head):
    """
    Reverse a singly linked list.
    
    Args:
        head: head of the linked list
    
    Returns:
        head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # temporarily store the next node
        current.next = prev       # reverse the current node
        prev = current           # move prev and current one step forward
        current = next_temp
    
    return prev


def reverse_sub_list(head, p, q):
    """
    Reverse a sub-list of a LinkedList from position p to q.
    
    Args:
        head: head of the linked list
        p: starting position (1-indexed)
        q: ending position (1-indexed)
    
    Returns:
        head of the linked list with reversed sub-list
    """
    if p == q:
        return head
    
    # Skip the first p-1 nodes, current will point to pth node
    current = head
    prev = None
    
    for _ in range(p - 1):
        prev = current
        current = current.next
    
    # We are interested in three parts of the LinkedList:
    # 1. part before index 'p'
    # 2. part between 'p' and 'q'
    # 3. part after index 'q'
    last_node_of_first_part = prev  # points to the node at index 'p-1'
    last_node_of_sub_list = current # after reversing, current will become last node of sub-list
    
    # Reverse nodes between 'p' and 'q'
    for _ in range(q - p + 1):
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    # Connect with the first part
    if last_node_of_first_part:
        last_node_of_first_part.next = prev  # 'prev' is now the first node of the sub-list
    else:  # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
        head = prev
    
    # Connect with the last part
    last_node_of_sub_list.next = current
    
    return head


def reverse_every_k_elements(head, k):
    """
    Reverse every k-element sub-list of a LinkedList.
    
    Args:
        head: head of the linked list
        k: size of each sub-list to reverse
    
    Returns:
        head of the linked list with reversed sub-lists
    """
    if k <= 1 or not head:
        return head
    
    current = head
    prev = None
    
    while True:
        last_node_of_prev_part = prev
        # After reversing the LinkedList 'current' will become the last node of the current sub-list
        last_node_of_sub_list = current
        
        # Reverse 'k' nodes
        for _ in range(k):
            if not current:  # if we've reached the end of the list
                break
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # Connect with the previous part
        if last_node_of_prev_part:
            last_node_of_prev_part.next = prev  # 'prev' is now the first node of the current sub-list
        else:  # this means we are changing the first node (head) of the LinkedList
            head = prev
        
        # Connect with the next part
        last_node_of_sub_list.next = current
        
        if not current:  # break, if we've reached the end of the LinkedList
            break
        
        prev = last_node_of_sub_list
    
    return head


def reverse_alternate_k_elements(head, k):
    """
    Reverse alternating k-element sub-lists of a LinkedList.
    
    Args:
        head: head of the linked list
        k: size of each sub-list to reverse
    
    Returns:
        head of the linked list with reversed alternating sub-lists
    """
    if k <= 1 or not head:
        return head
    
    current = head
    prev = None
    
    while current:
        last_node_of_prev_part = prev
        # After reversing the LinkedList 'current' will become the last node of the current sub-list
        last_node_of_sub_list = current
        
        # Reverse 'k' nodes
        for _ in range(k):
            if not current:
                break
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # Connect with the previous part
        if last_node_of_prev_part:
            last_node_of_prev_part.next = prev
        else:
            head = prev
        
        # Connect with the next part
        last_node_of_sub_list.next = current
        
        # Skip 'k' nodes
        for _ in range(k):
            if not current:
                break
            prev = current
            current = current.next
    
    return head


def rotate_linkedlist(head, k):
    """
    Rotate a LinkedList to the right by k positions.
    
    Args:
        head: head of the linked list
        k: number of positions to rotate
    
    Returns:
        head of the rotated linked list
    """
    if not head or not head.next or k <= 0:
        return head
    
    # Find the length and the last node of the list
    last_node = head
    list_length = 1
    
    while last_node.next:
        last_node = last_node.next
        list_length += 1
    
    # Connect the last node with the head to make it a circular list
    last_node.next = head
    
    # No need to do rotations more than the length of the list
    k %= list_length
    skip_length = list_length - k
    last_node_of_rotated_list = head
    
    for _ in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next
    
    # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
    
    return head


def reverse_nodes_in_k_group(head, k):
    """
    Reverse nodes of a linked list k at a time and return its modified list.
    If the number of nodes is not a multiple of k then leave the remaining nodes as is.
    
    Args:
        head: head of the linked list
        k: group size
    
    Returns:
        head of the modified linked list
    """
    if not head or k == 1:
        return head
    
    # Check if we have k nodes left in the linked list
    count = 0
    current = head
    
    while current and count < k:
        current = current.next
        count += 1
    
    if count == k:  # if we have k nodes, then we proceed with reversing
        current = reverse_nodes_in_k_group(current, k)  # reverse list with k+1 node as head
        
        # Reverse current k-group
        while count > 0:
            next_temp = head.next
            head.next = current
            current = head
            head = next_temp
            count -= 1
        
        head = current
    
    return head


def swap_nodes_in_pairs(head):
    """
    Swap every two adjacent nodes in a linked list.
    
    Args:
        head: head of the linked list
    
    Returns:
        head of the modified linked list
    """
    if not head or not head.next:
        return head
    
    # Save the second node which will be the new head
    new_head = head.next
    
    # Reverse the first pair
    head.next = swap_nodes_in_pairs(new_head.next)
    new_head.next = head
    
    return new_head


def reverse_nodes_between(head, left, right):
    """
    Reverse the nodes between positions left and right (1-indexed).
    
    Args:
        head: head of the linked list
        left: left position (1-indexed)
        right: right position (1-indexed)
    
    Returns:
        head of the modified linked list
    """
    if not head or left == right:
        return head
    
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Find the node before the left position
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    
    # Reverse the sub-list from left to right
    current = prev.next
    for _ in range(right - left):
        next_temp = current.next
        current.next = next_temp.next
        next_temp.next = prev.next
        prev.next = next_temp
    
    return dummy.next


# Helper functions for creating and printing test linked lists
def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    
    return head


def print_linked_list(head, max_nodes=20):
    """Print linked list values."""
    result = []
    current = head
    count = 0
    
    while current and count < max_nodes:
        result.append(current.val)
        current = current.next
        count += 1
    
    if current:
        result.append("...")
    
    return result


# Example usage and test cases
if __name__ == "__main__":
    # Test reverse_linkedlist
    print("=== Reverse LinkedList ===")
    head = create_linked_list([2, 4, 6, 8, 10])
    print(f"Original: {print_linked_list(head)}")
    reversed_head = reverse_linkedlist(head)
    print(f"Reversed: {print_linked_list(reversed_head)}")
    
    # Test reverse_sub_list
    print("\n=== Reverse Sub-list ===")
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {print_linked_list(head)}")
    modified_head = reverse_sub_list(head, 2, 4)
    print(f"Reversed sub-list (2-4): {print_linked_list(modified_head)}")
    
    # Test reverse_every_k_elements
    print("\n=== Reverse Every K Elements ===")
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Original: {print_linked_list(head)}")
    modified_head = reverse_every_k_elements(head, 3)
    print(f"Reversed every 3 elements: {print_linked_list(modified_head)}")
    
    # Test reverse_alternate_k_elements
    print("\n=== Reverse Alternate K Elements ===")
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Original: {print_linked_list(head)}")
    modified_head = reverse_alternate_k_elements(head, 2)
    print(f"Reversed alternate 2 elements: {print_linked_list(modified_head)}")
    
    # Test rotate_linkedlist
    print("\n=== Rotate LinkedList ===")
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    print(f"Original: {print_linked_list(head)}")
    rotated_head = rotate_linkedlist(head, 3)
    print(f"Rotated by 3: {print_linked_list(rotated_head)}")
    
    # Test swap_nodes_in_pairs
    print("\n=== Swap Nodes in Pairs ===")
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    print(f"Original: {print_linked_list(head)}")
    swapped_head = swap_nodes_in_pairs(head)
    print(f"Swapped pairs: {print_linked_list(swapped_head)}")
    
    # Test reverse_nodes_between
    print("\n=== Reverse Nodes Between ===")
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {print_linked_list(head)}")
    modified_head = reverse_nodes_between(head, 2, 4)
    print(f"Reversed between 2-4: {print_linked_list(modified_head)}")
