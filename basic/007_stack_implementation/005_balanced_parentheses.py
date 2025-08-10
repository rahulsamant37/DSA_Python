"""
005 - Stack Applications - Balanced Parentheses
===============================================

Check if parentheses/brackets are balanced using stack.

Time Complexity: O(n)
Space Complexity: O(n)

Common application of stack in expression parsing.
"""

from python_list_stack_004 import PythonListStack


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


def demo_balanced_parentheses():
    """Demonstrate balanced parentheses checking"""
    print("=== Balanced Parentheses Demo ===")
    
    test_cases = [
        "()",
        "(())",
        "()[]{}",
        "([{}])",
        "(((",
        "())",
        "([)]",
        "{[}]"
    ]
    
    for expression in test_cases:
        result = is_balanced_parentheses(expression)
        print(f"'{expression}' -> {'Balanced' if result else 'Not Balanced'}")


if __name__ == "__main__":
    demo_balanced_parentheses()
