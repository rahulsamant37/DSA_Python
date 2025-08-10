"""
Fast and Slow Pointers Pattern (Floyd's Cycle Detection Algorithm)

The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, 
is a pointer algorithm that uses only two pointers, which move through the array 
(or sequence/LinkedList) at different speeds. This approach is quite useful when 
dealing with cyclic LinkedLists or arrays.

Time Complexity: Usually O(n)
Space Complexity: O(1)

Common Problems:
- LinkedList Cycle Detection
- Start of LinkedList Cycle
- Happy Number
- Middle of the LinkedList
- Palindrome LinkedList
"""

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0):
        self.val = val
        self.next = None


def has_cycle(head):
    """
    Detect if a linked list has a cycle.
    
    Args:
        head: head of the linked list
    
    Returns:
        True if cycle exists, False otherwise
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next  # move one step
        fast = fast.next.next  # move two steps
        
        if slow == fast:  # found the cycle
            return True
    
    return False


def find_cycle_start(head):
    """
    Find the start of the cycle in a linked list.
    
    Args:
        head: head of the linked list
    
    Returns:
        node where the cycle starts, None if no cycle
    """
    cycle_length = 0
    
    # Find if cycle exists and get cycle length
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # found cycle
            cycle_length = calculate_cycle_length(slow)
            break
    
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):
    """Calculate the length of the cycle."""
    current = slow
    cycle_length = 0
    
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    
    return cycle_length


def find_start(head, cycle_length):
    """Find the start of the cycle using cycle length."""
    pointer1 = head
    pointer2 = head
    
    # Move pointer2 ahead 'cycle_length' nodes
    for _ in range(cycle_length):
        pointer2 = pointer2.next
    
    # Increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1


def is_happy(n):
    """
    Determine if a number is happy.
    A happy number is a number defined by the following process:
    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle.
    
    Args:
        n: positive integer
    
    Returns:
        True if n is a happy number, False otherwise
    """
    slow = n
    fast = n
    
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        
        if slow == fast:  # found a cycle
            break
    
    return slow == 1  # see if the cycle is stuck on the number 1


def find_square_sum(num):
    """Calculate sum of squares of digits."""
    square_sum = 0
    while num > 0:
        digit = num % 10
        square_sum += digit * digit
        num //= 10
    return square_sum


def find_middle_of_linkedlist(head):
    """
    Find the middle node of a linked list.
    
    Args:
        head: head of the linked list
    
    Returns:
        middle node of the linked list
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def is_palindromic_linkedlist(head):
    """
    Check if a linked list is a palindrome.
    
    Args:
        head: head of the linked list
    
    Returns:
        True if linked list is palindrome, False otherwise
    """
    if not head or not head.next:
        return True
    
    # Find middle of the linked list
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    head_second_half = reverse(slow)
    
    # Store the head of reversed part to revert back later
    copy_head_second_half = head_second_half
    
    # Compare the first and second half
    while head and head_second_half:
        if head.val != head_second_half.val:
            break  # not a palindrome
        
        head = head.next
        head_second_half = head_second_half.next
    
    # Revert the reverse of the second half
    reverse(copy_head_second_half)
    
    # If both halves match
    return not head or not head_second_half


def reverse(head):
    """Reverse a linked list."""
    prev = None
    
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    
    return prev


def rearrange_linkedlist(head):
    """
    Rearrange a LinkedList so that all even indexed nodes come after odd indexed nodes.
    
    Args:
        head: head of the linked list
    
    Returns:
        head of the rearranged linked list
    """
    if not head:
        return head
    
    # Find middle of LinkedList
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    head_second_half = reverse(slow)
    head_first_half = head
    
    # Rearrange to produce the LinkedList in the required order
    while head_first_half and head_second_half:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp
        
        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp
    
    # Set the next of the last node to 'None'
    if head_first_half:
        head_first_half.next = None
    
    return head


def find_cycle_length(head):
    """
    Find the length of cycle in a linked list.
    
    Args:
        head: head of the linked list
    
    Returns:
        length of the cycle, 0 if no cycle
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # found cycle
            return calculate_cycle_length(slow)
    
    return 0


# Helper functions for creating test linked lists
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


def print_linked_list(head, max_nodes=10):
    """Print linked list values (with cycle detection)."""
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
    # Test has_cycle
    print("=== LinkedList Cycle Detection ===")
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    # Create cycle: 6 -> 3
    current = head
    while current.next:
        current = current.next
    current.next = head.next.next  # Create cycle
    
    print(f"Has cycle: {has_cycle(head)}")  # True
    
    # Test is_happy
    print("\n=== Happy Number ===")
    test_numbers = [23, 12]
    for num in test_numbers:
        result = is_happy(num)
        print(f"{num} is happy: {result}")
    
    # Test find_middle_of_linkedlist
    print("\n=== Middle of LinkedList ===")
    head = create_linked_list([1, 2, 3, 4, 5])
    middle = find_middle_of_linkedlist(head)
    print(f"LinkedList: {print_linked_list(head)}")
    print(f"Middle node value: {middle.val}")  # 3
    
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    middle = find_middle_of_linkedlist(head)
    print(f"LinkedList: {print_linked_list(head)}")
    print(f"Middle node value: {middle.val}")  # 4
    
    # Test is_palindromic_linkedlist
    print("\n=== Palindromic LinkedList ===")
    head = create_linked_list([2, 4, 6, 4, 2])
    result = is_palindromic_linkedlist(head)
    print(f"LinkedList: {print_linked_list(head)}")
    print(f"Is palindrome: {result}")  # True
    
    head = create_linked_list([2, 4, 6, 4, 2, 2])
    result = is_palindromic_linkedlist(head)
    print(f"LinkedList: {print_linked_list(head)}")
    print(f"Is palindrome: {result}")  # False
