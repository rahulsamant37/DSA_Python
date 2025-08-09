"""
007 - Stack Implementation
=========================

This module implements stack data structure using different approaches:
- Array-based Stack
- Linked List-based Stack
- Built-in List Stack (Python)
- Stack applications and problems

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek/Top: O(1)
- Search: O(n)

Stack follows LIFO (Last In, First Out) principle.
Applications: Function calls, expression evaluation, undo operations, etc.
"""

class ArrayStack:
    """Stack implementation using array (list)"""
    
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top_index = -1
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top_index == -1
    
    def is_full(self):
        """Check if stack is full"""
        return self.top_index == self.capacity - 1
    
    def size(self):
        """Return current size of stack"""
        return self.top_index + 1
    
    def push(self, item):
        """Push item onto stack"""
        if self.is_full():
            raise OverflowError("Stack overflow")
        
        self.top_index += 1
        self.data[self.top_index] = item
    
    def pop(self):
        """Pop item from stack"""
        if self.is_empty():
            raise IndexError("Stack underflow")
        
        item = self.data[self.top_index]
        self.data[self.top_index] = None
        self.top_index -= 1
        return item
    
    def peek(self):
        """Peek at top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.data[self.top_index]
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        for i in range(self.top_index, -1, -1):
            print(f"  {self.data[i]}")


class StackNode:
    """Node class for linked list stack"""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    """Stack implementation using linked list"""
    
    def __init__(self):
        self.head = None
        self.stack_size = 0
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.head is None
    
    def size(self):
        """Return current size of stack"""
        return self.stack_size
    
    def push(self, item):
        """Push item onto stack"""
        new_node = StackNode(item)
        new_node.next = self.head
        self.head = new_node
        self.stack_size += 1
    
    def pop(self):
        """Pop item from stack"""
        if self.is_empty():
            raise IndexError("Stack underflow")
        
        item = self.head.data
        self.head = self.head.next
        self.stack_size -= 1
        return item
    
    def peek(self):
        """Peek at top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.head.data
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        current = self.head
        while current:
            print(f"  {current.data}")
            current = current.next


class PythonListStack:
    """Stack implementation using Python's built-in list"""
    
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.data) == 0
    
    def size(self):
        """Return current size of stack"""
        return len(self.data)
    
    def push(self, item):
        """Push item onto stack"""
        self.data.append(item)
    
    def pop(self):
        """Pop item from stack"""
        if self.is_empty():
            raise IndexError("Stack underflow")
        
        return self.data.pop()
    
    def peek(self):
        """Peek at top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.data[-1]
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        for i in range(len(self.data) - 1, -1, -1):
            print(f"  {self.data[i]}")


class StackApplications:
    """Various stack applications and algorithms"""
    
    @staticmethod
    def is_balanced_parentheses(expression):
        """Check if parentheses are balanced using stack"""
        stack = PythonListStack()
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in pairs:  # Opening bracket
                stack.push(char)
            elif char in pairs.values():  # Closing bracket
                if stack.is_empty():
                    return False
                
                opening = stack.pop()
                if pairs[opening] != char:
                    return False
        
        return stack.is_empty()
    
    @staticmethod
    def infix_to_postfix(expression):
        """Convert infix expression to postfix using stack"""
        stack = PythonListStack()
        postfix = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
        for char in expression:
            if char.isalnum():  # Operand
                postfix.append(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove '('
            elif char in precedence:  # Operator
                while (not stack.is_empty() and 
                       stack.peek() != '(' and 
                       stack.peek() in precedence and
                       precedence[stack.peek()] >= precedence[char]):
                    postfix.append(stack.pop())
                stack.push(char)
        
        while not stack.is_empty():
            postfix.append(stack.pop())
        
        return ''.join(postfix)
    
    @staticmethod
    def evaluate_postfix(expression):
        """Evaluate postfix expression using stack"""
        stack = PythonListStack()
        
        for char in expression:
            if char.isdigit():
                stack.push(int(char))
            elif char in '+-*/':
                if stack.size() < 2:
                    raise ValueError("Invalid postfix expression")
                
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if char == '+':
                    result = operand1 + operand2
                elif char == '-':
                    result = operand1 - operand2
                elif char == '*':
                    result = operand1 * operand2
                elif char == '/':
                    if operand2 == 0:
                        raise ValueError("Division by zero")
                    result = operand1 / operand2
                
                stack.push(result)
        
        if stack.size() != 1:
            raise ValueError("Invalid postfix expression")
        
        return stack.pop()
    
    @staticmethod
    def next_greater_element(arr):
        """Find next greater element for each element using stack"""
        stack = PythonListStack()
        result = [-1] * len(arr)
        
        for i in range(len(arr) - 1, -1, -1):
            # Pop elements smaller than current element
            while not stack.is_empty() and stack.peek() <= arr[i]:
                stack.pop()
            
            # If stack is not empty, top is the next greater element
            if not stack.is_empty():
                result[i] = stack.peek()
            
            # Push current element
            stack.push(arr[i])
        
        return result
    
    @staticmethod
    def largest_rectangle_histogram(heights):
        """Find largest rectangle in histogram using stack"""
        stack = PythonListStack()
        max_area = 0
        index = 0
        
        while index < len(heights):
            if stack.is_empty() or heights[index] >= heights[stack.peek()]:
                stack.push(index)
                index += 1
            else:
                top = stack.pop()
                width = index if stack.is_empty() else index - stack.peek() - 1
                area = heights[top] * width
                max_area = max(max_area, area)
        
        while not stack.is_empty():
            top = stack.pop()
            width = index if stack.is_empty() else index - stack.peek() - 1
            area = heights[top] * width
            max_area = max(max_area, area)
        
        return max_area
    
    @staticmethod
    def reverse_string(s):
        """Reverse a string using stack"""
        stack = PythonListStack()
        
        for char in s:
            stack.push(char)
        
        reversed_str = ""
        while not stack.is_empty():
            reversed_str += stack.pop()
        
        return reversed_str
    
    @staticmethod
    def decimal_to_binary(decimal):
        """Convert decimal to binary using stack"""
        if decimal == 0:
            return "0"
        
        stack = PythonListStack()
        
        while decimal > 0:
            stack.push(decimal % 2)
            decimal //= 2
        
        binary = ""
        while not stack.is_empty():
            binary += str(stack.pop())
        
        return binary


def test_stack_implementations():
    """Test all stack implementations"""
    print("=== Testing Stack Implementations ===\n")
    
    # Test Array Stack
    print("=== Array-based Stack ===")
    array_stack = ArrayStack(5)
    
    print("Pushing elements: 10, 20, 30")
    array_stack.push(10)
    array_stack.push(20)
    array_stack.push(30)
    array_stack.display()
    print(f"Size: {array_stack.size()}")
    print(f"Top element: {array_stack.peek()}")
    print()
    
    print("Popping elements:")
    while not array_stack.is_empty():
        popped = array_stack.pop()
        print(f"Popped: {popped}")
    print()
    
    # Test Linked List Stack
    print("=== Linked List-based Stack ===")
    ll_stack = LinkedListStack()
    
    print("Pushing elements: A, B, C")
    ll_stack.push('A')
    ll_stack.push('B')
    ll_stack.push('C')
    ll_stack.display()
    print(f"Size: {ll_stack.size()}")
    print(f"Top element: {ll_stack.peek()}")
    print()
    
    # Test Python List Stack
    print("=== Python List-based Stack ===")
    py_stack = PythonListStack()
    
    print("Pushing elements: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        py_stack.push(i)
    py_stack.display()
    print()


def test_stack_applications():
    """Test stack applications"""
    print("=== Testing Stack Applications ===\n")
    
    apps = StackApplications()
    
    # Test balanced parentheses
    print("=== Balanced Parentheses ===")
    test_expressions = [
        "((()))",
        "()[]{}", 
        "(((",
        "({[]})",
        "([)]"
    ]
    
    for expr in test_expressions:
        result = apps.is_balanced_parentheses(expr)
        print(f"'{expr}' is {'balanced' if result else 'not balanced'}")
    print()
    
    # Test infix to postfix conversion
    print("=== Infix to Postfix Conversion ===")
    infix_expressions = [
        "A+B*C",
        "(A+B)*C", 
        "A+B*C-D",
        "A*(B+C)-D"
    ]
    
    for expr in infix_expressions:
        postfix = apps.infix_to_postfix(expr)
        print(f"Infix: {expr} -> Postfix: {postfix}")
    print()
    
    # Test postfix evaluation
    print("=== Postfix Evaluation ===")
    postfix_expressions = [
        "231*+9-",  # ((2+(3*1))-9) = -4
        "123+*8-",  # ((1*(2+3))-8) = -3
    ]
    
    for expr in postfix_expressions:
        try:
            result = apps.evaluate_postfix(expr)
            print(f"Postfix: {expr} = {result}")
        except Exception as e:
            print(f"Error evaluating {expr}: {e}")
    print()
    
    # Test next greater element
    print("=== Next Greater Element ===")
    test_arrays = [
        [4, 5, 2, 25],
        [13, 7, 6, 12],
        [1, 2, 3, 4, 5]
    ]
    
    for arr in test_arrays:
        result = apps.next_greater_element(arr)
        print(f"Array: {arr}")
        print(f"Next Greater: {result}")
        print()
    
    # Test largest rectangle in histogram
    print("=== Largest Rectangle in Histogram ===")
    histograms = [
        [6, 2, 5, 4, 5, 1, 6],
        [2, 1, 5, 6, 2, 3]
    ]
    
    for hist in histograms:
        area = apps.largest_rectangle_histogram(hist)
        print(f"Heights: {hist}")
        print(f"Largest rectangle area: {area}")
        print()
    
    # Test utility functions
    print("=== Utility Functions ===")
    test_string = "Hello World"
    reversed_str = apps.reverse_string(test_string)
    print(f"Original: {test_string}")
    print(f"Reversed: {reversed_str}")
    
    decimal_num = 42
    binary_str = apps.decimal_to_binary(decimal_num)
    print(f"Decimal {decimal_num} = Binary {binary_str}")


if __name__ == "__main__":
    test_stack_implementations()
    print("\n" + "="*50 + "\n")
    test_stack_applications()
