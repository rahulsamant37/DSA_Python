"""
Backtracking Pattern

Backtracking is an algorithmic technique that considers searching every possible 
combination in order to solve computational problems. It builds candidates to the 
solutions incrementally and abandons candidates (backtracks) as soon as it is 
determined that they cannot possibly be extended to a valid solution.

Time Complexity: Often exponential O(2^n) or O(n!)
Space Complexity: O(depth of recursion)

Common Problems:
- Subsets
- Permutations
- Combination Sum
- N-Queens
- Sudoku Solver
- Word Search
- Generate Parentheses
"""

def find_subsets(nums):
    """
    Find all possible subsets of a given set.
    
    Args:
        nums: list of unique integers
    
    Returns:
        list of all subsets
    """
    subsets = []
    backtrack_subsets(0, nums, [], subsets)
    return subsets


def backtrack_subsets(start, nums, path, subsets):
    """Helper function for find_subsets."""
    # Add current subset to result
    subsets.append(list(path))
    
    # Try adding each remaining number
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack_subsets(i + 1, nums, path, subsets)
        path.pop()  # Backtrack


def find_subsets_with_duplicates(nums):
    """
    Find all possible subsets of a given set with duplicates.
    
    Args:
        nums: list of integers (may contain duplicates)
    
    Returns:
        list of all unique subsets
    """
    subsets = []
    nums.sort()  # Sort to handle duplicates
    backtrack_subsets_with_duplicates(0, nums, [], subsets)
    return subsets


def backtrack_subsets_with_duplicates(start, nums, path, subsets):
    """Helper function for find_subsets_with_duplicates."""
    subsets.append(list(path))
    
    for i in range(start, len(nums)):
        # Skip duplicates: if current element is same as previous and 
        # we haven't used the previous element in current recursion level
        if i > start and nums[i] == nums[i - 1]:
            continue
        
        path.append(nums[i])
        backtrack_subsets_with_duplicates(i + 1, nums, path, subsets)
        path.pop()


def find_permutations(nums):
    """
    Find all permutations of a given set.
    
    Args:
        nums: list of unique integers
    
    Returns:
        list of all permutations
    """
    result = []
    backtrack_permutations(nums, [], result)
    return result


def backtrack_permutations(nums, path, result):
    """Helper function for find_permutations."""
    # If path length equals nums length, we have a complete permutation
    if len(path) == len(nums):
        result.append(list(path))
        return
    
    # Try adding each unused number
    for num in nums:
        if num not in path:
            path.append(num)
            backtrack_permutations(nums, path, result)
            path.pop()  # Backtrack


def find_permutations_with_duplicates(nums):
    """
    Find all permutations of a given set with duplicates.
    
    Args:
        nums: list of integers (may contain duplicates)
    
    Returns:
        list of all unique permutations
    """
    result = []
    nums.sort()  # Sort to handle duplicates
    used = [False] * len(nums)
    backtrack_permutations_with_duplicates(nums, [], used, result)
    return result


def backtrack_permutations_with_duplicates(nums, path, used, result):
    """Helper function for find_permutations_with_duplicates."""
    if len(path) == len(nums):
        result.append(list(path))
        return
    
    for i in range(len(nums)):
        if used[i]:
            continue
        
        # Skip duplicates: if current element is same as previous and 
        # previous element is not used
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue
        
        path.append(nums[i])
        used[i] = True
        backtrack_permutations_with_duplicates(nums, path, used, result)
        path.pop()
        used[i] = False


def combination_sum(candidates, target):
    """
    Find all unique combinations where candidates sum to target.
    Numbers can be used multiple times.
    
    Args:
        candidates: list of distinct positive integers
        target: target sum
    
    Returns:
        list of all unique combinations
    """
    result = []
    candidates.sort()
    backtrack_combination_sum(candidates, target, 0, [], result)
    return result


def backtrack_combination_sum(candidates, target, start, path, result):
    """Helper function for combination_sum."""
    if target == 0:
        result.append(list(path))
        return
    
    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break  # No point in continuing as array is sorted
        
        path.append(candidates[i])
        # Note: we pass i (not i+1) because we can reuse same elements
        backtrack_combination_sum(candidates, target - candidates[i], i, path, result)
        path.pop()


def combination_sum_ii(candidates, target):
    """
    Find all unique combinations where candidates sum to target.
    Each number can only be used once.
    
    Args:
        candidates: list of integers (may contain duplicates)
        target: target sum
    
    Returns:
        list of all unique combinations
    """
    result = []
    candidates.sort()
    backtrack_combination_sum_ii(candidates, target, 0, [], result)
    return result


def backtrack_combination_sum_ii(candidates, target, start, path, result):
    """Helper function for combination_sum_ii."""
    if target == 0:
        result.append(list(path))
        return
    
    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break
        
        # Skip duplicates
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        
        path.append(candidates[i])
        backtrack_combination_sum_ii(candidates, target - candidates[i], i + 1, path, result)
        path.pop()


def solve_n_queens(n):
    """
    Solve the N-Queens problem.
    
    Args:
        n: size of the chessboard (n x n)
    
    Returns:
        list of all solutions (each solution is a list of strings)
    """
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check diagonal (top-right to bottom-left)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack_n_queens(board, row, result):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack_n_queens(board, row + 1, result)
                board[row][col] = '.'  # Backtrack
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack_n_queens(board, 0, result)
    return result


def generate_parentheses(n):
    """
    Generate all combinations of well-formed parentheses.
    
    Args:
        n: number of pairs of parentheses
    
    Returns:
        list of all valid parentheses combinations
    """
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    result = []
    backtrack('', 0, 0)
    return result


def word_search(board, word):
    """
    Search for a word in a 2D board.
    
    Args:
        board: 2D grid of characters
        word: word to search for
    
    Returns:
        True if word exists in board, False otherwise
    """
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        if index == len(word):
            return True
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            board[row][col] != word[index]):
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Search in all four directions
        found = (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1))
        
        # Restore original character (backtrack)
        board[row][col] = temp
        
        return found
    
    # Try starting from each cell
    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True
    
    return False


def letter_combinations(digits):
    """
    Find all possible letter combinations that the number could represent.
    
    Args:
        digits: string containing digits 2-9
    
    Returns:
        list of all possible letter combinations
    """
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return
        
        letters = phone[digits[index]]
        for letter in letters:
            backtrack(index + 1, path + letter)
    
    result = []
    backtrack(0, '')
    return result


def palindrome_partitioning(s):
    """
    Partition string such that every substring is a palindrome.
    
    Args:
        s: input string
    
    Returns:
        list of all possible palindrome partitionings
    """
    def is_palindrome(string):
        return string == string[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(list(path))
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result


# Example usage and test cases
if __name__ == "__main__":
    # Test find_subsets
    print("=== Subsets ===")
    nums = [1, 3]
    result = find_subsets(nums)
    print(f"Input: {nums}")
    print(f"Subsets: {result}")  # [[], [1], [3], [1, 3]]
    
    # Test find_subsets_with_duplicates
    print("\n=== Subsets with Duplicates ===")
    nums = [1, 5, 3, 3]
    result = find_subsets_with_duplicates(nums)
    print(f"Input: {nums}")
    print(f"Unique subsets: {result}")
    
    # Test find_permutations
    print("\n=== Permutations ===")
    nums = [1, 3, 5]
    result = find_permutations(nums)
    print(f"Input: {nums}")
    print(f"Permutations: {result}")
    
    # Test combination_sum
    print("\n=== Combination Sum ===")
    candidates = [2, 3, 6, 7]
    target = 7
    result = combination_sum(candidates, target)
    print(f"Candidates: {candidates}, Target: {target}")
    print(f"Combinations: {result}")  # [[2, 2, 3], [7]]
    
    # Test solve_n_queens
    print("\n=== N-Queens (n=4) ===")
    n = 4
    result = solve_n_queens(n)
    print(f"N = {n}")
    print(f"Number of solutions: {len(result)}")
    if result:
        print("First solution:")
        for row in result[0]:
            print(row)
    
    # Test generate_parentheses
    print("\n=== Generate Parentheses ===")
    n = 3
    result = generate_parentheses(n)
    print(f"n = {n}")
    print(f"Valid parentheses: {result}")
    
    # Test word_search
    print("\n=== Word Search ===")
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    result = word_search([row[:] for row in board], word)  # Copy board
    print(f"Board: {board}")
    print(f"Word: {word}")
    print(f"Found: {result}")  # True
    
    # Test letter_combinations
    print("\n=== Letter Combinations ===")
    digits = "23"
    result = letter_combinations(digits)
    print(f"Digits: {digits}")
    print(f"Letter combinations: {result}")
    
    # Test palindrome_partitioning
    print("\n=== Palindrome Partitioning ===")
    s = "aab"
    result = palindrome_partitioning(s)
    print(f"String: {s}")
    print(f"Palindrome partitions: {result}")  # [['a', 'a', 'b'], ['aa', 'b']]
