"""
004 - Singly Linked List Implementation
======================================

This module implements a singly linked list with all basic operations:
- Node creation
- Insertion (at beginning, end, and specific position)
- Deletion (from beginning, end, and specific position)
- Traversal and display
- Search operations
- Utility functions

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at beginning, O(n) at end/position
- Deletion: O(1) at beginning, O(n) at end/position
"""

class ListNode:
    """Node class for singly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    """Singly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the linked list"""
        return self.size
    
    def prepend(self, data):
        """Insert element at the beginning of the list"""
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def append(self, data):
        """Insert element at the end of the list"""
        new_node = ListNode(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert element at specific position (0-indexed)"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            self.prepend(data)
            return
        
        new_node = ListNode(data)
        current = self.head
        
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_first(self):
        """Delete the first element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete the last element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        if self.head.next is None:  # Only one element
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        self.size -= 1
        return deleted_data
    
    def delete_at_position(self, position):
        """Delete element at specific position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            return self.delete_first()
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data
    
    def delete_by_value(self, value):
        """Delete first occurrence of value"""
        if self.is_empty():
            return False
        
        if self.head.data == value:
            self.delete_first()
            return True
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.size -= 1
            return True
        
        return False
    
    def search(self, value):
        """Search for a value and return its position"""
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def get_at_position(self, position):
        """Get element at specific position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def update_at_position(self, position, new_value):
        """Update element at specific position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        old_value = current.data
        current.data = new_value
        return old_value
    
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def reverse_recursive(self, node=None):
        """Reverse the linked list recursively"""
        if node is None:
            node = self.head
        
        if node is None or node.next is None:
            self.head = node
            return node
        
        reversed_head = self.reverse_recursive(node.next)
        node.next.next = node
        node.next = None
        
        return reversed_head
    
    def find_middle(self):
        """Find the middle element using two pointers"""
        if self.is_empty():
            return None
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def detect_cycle(self):
        """Detect if there's a cycle in the linked list"""
        if self.is_empty():
            return False
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def remove_duplicates(self):
        """Remove duplicates from sorted linked list"""
        if self.is_empty():
            return
        
        current = self.head
        
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
                self.size -= 1
            else:
                current = current.next
    
    def merge_sorted(self, other_list):
        """Merge two sorted linked lists"""
        dummy = ListNode(0)
        current = dummy
        
        ptr1, ptr2 = self.head, other_list.head
        
        while ptr1 and ptr2:
            if ptr1.data <= ptr2.data:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next
        
        # Attach remaining elements
        current.next = ptr1 or ptr2
        
        # Create new merged list
        merged_list = SinglyLinkedList()
        merged_list.head = dummy.next
        merged_list.size = self.size + other_list.size
        
        return merged_list
    
    def display(self):
        """Display the linked list"""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) + " -> None")
    
    def to_list(self):
        """Convert linked list to Python list"""
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def from_list(self, python_list):
        """Create linked list from Python list"""
        self.head = None
        self.size = 0
        
        for item in python_list:
            self.append(item)


def test_singly_linked_list():
    """Test all singly linked list operations"""
    print("=== Testing Singly Linked List ===\n")
    
    # Create empty list
    linked_list = SinglyLinkedList()
    print(f"Created empty list. Size: {linked_list.get_size()}")
    print(f"Is empty: {linked_list.is_empty()}")
    linked_list.display()
    print()
    
    # Test insertion operations
    print("=== Insertion Operations ===")
    print("Appending elements: 10, 20, 30")
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.display()
    print(f"Size: {linked_list.get_size()}")
    print()
    
    print("Prepending element: 5")
    linked_list.prepend(5)
    linked_list.display()
    print()
    
    print("Inserting 15 at position 2:")
    linked_list.insert_at_position(15, 2)
    linked_list.display()
    print(f"Size: {linked_list.get_size()}")
    print()
    
    # Test search operations
    print("=== Search Operations ===")
    search_value = 20
    position = linked_list.search(search_value)
    print(f"Position of {search_value}: {position}")
    
    print(f"Element at position 3: {linked_list.get_at_position(3)}")
    print(f"Middle element: {linked_list.find_middle()}")
    print()
    
    # Test update operation
    print("=== Update Operation ===")
    old_value = linked_list.update_at_position(1, 25)
    print(f"Updated position 1 from {old_value} to 25")
    linked_list.display()
    print()
    
    # Test deletion operations
    print("=== Deletion Operations ===")
    deleted = linked_list.delete_first()
    print(f"Deleted first element: {deleted}")
    linked_list.display()
    print()
    
    deleted = linked_list.delete_last()
    print(f"Deleted last element: {deleted}")
    linked_list.display()
    print()
    
    deleted = linked_list.delete_at_position(1)
    print(f"Deleted element at position 1: {deleted}")
    linked_list.display()
    print()
    
    success = linked_list.delete_by_value(20)
    print(f"Deleted value 20: {success}")
    linked_list.display()
    print(f"Final size: {linked_list.get_size()}")
    print()
    
    # Test reverse operation
    print("=== Reverse Operations ===")
    linked_list.from_list([1, 2, 3, 4, 5])
    print("Original list:")
    linked_list.display()
    
    linked_list.reverse()
    print("After reversing:")
    linked_list.display()
    
    linked_list.reverse_recursive()
    print("After recursive reverse (back to original):")
    linked_list.display()
    print()
    
    # Test merge operation
    print("=== Merge Operation ===")
    list1 = SinglyLinkedList()
    list1.from_list([1, 3, 5])
    print("List 1:")
    list1.display()
    
    list2 = SinglyLinkedList()
    list2.from_list([2, 4, 6])
    print("List 2:")
    list2.display()
    
    merged = list1.merge_sorted(list2)
    print("Merged list:")
    merged.display()
    print()
    
    # Test duplicate removal
    print("=== Remove Duplicates ===")
    dup_list = SinglyLinkedList()
    dup_list.from_list([1, 1, 2, 3, 3, 4, 4, 4, 5])
    print("List with duplicates:")
    dup_list.display()
    
    dup_list.remove_duplicates()
    print("After removing duplicates:")
    dup_list.display()
    print()
    
    # Test cycle detection
    print("=== Cycle Detection ===")
    cycle_list = SinglyLinkedList()
    cycle_list.from_list([1, 2, 3, 4, 5])
    print(f"Has cycle: {cycle_list.detect_cycle()}")
    
    # Create a cycle manually for testing
    if cycle_list.head:
        current = cycle_list.head
        while current.next:
            current = current.next
        current.next = cycle_list.head.next  # Create cycle
        print(f"After creating cycle: {cycle_list.detect_cycle()}")


if __name__ == "__main__":
    test_singly_linked_list()
