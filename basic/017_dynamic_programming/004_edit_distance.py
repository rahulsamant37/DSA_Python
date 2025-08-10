"""
004 - Edit Distance (Levenshtein Distance)
==========================================

Dynamic Programming solution for computing the minimum edit distance
between two strings using insertions, deletions, and substitutions.

The edit distance is the minimum number of single-character edits
needed to transform one string into another.

Time Complexity: O(m * n) where m, n are string lengths
Space Complexity: O(m * n) or O(min(m, n)) with optimization

Applications:
- Spell checkers and auto-correction
- DNA sequence analysis
- Plagiarism detection
- Fuzzy string matching
- Data deduplication
"""

from typing import List, Tuple, Optional, Dict
from enum import Enum


class EditOperation(Enum):
    """Types of edit operations"""
    MATCH = "MATCH"
    INSERT = "INSERT"
    DELETE = "DELETE"
    SUBSTITUTE = "SUBSTITUTE"


def edit_distance(str1: str, str2: str) -> int:
    """
    Compute minimum edit distance between two strings
    
    Args:
        str1: Source string
        str2: Target string
    
    Returns:
        Minimum number of edits needed
    """
    m, n = len(str1), len(str2)
    
    # DP table: dp[i][j] = edit distance between str1[0:i] and str2[0:j]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from str1
    
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters to reach str2
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                # Characters match - no edit needed
                dp[i][j] = dp[i-1][j-1]
            else:
                # Choose minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # Delete from str1
                    dp[i][j-1],      # Insert into str1
                    dp[i-1][j-1]     # Substitute in str1
                )
    
    return dp[m][n]


def edit_distance_with_operations(str1: str, str2: str) -> Tuple[int, List[Tuple[EditOperation, int, str]]]:
    """
    Compute edit distance and return the sequence of operations
    
    Args:
        str1: Source string
        str2: Target string
    
    Returns:
        Tuple of (distance, operations_list)
        Each operation is (operation_type, position, character)
    """
    m, n = len(str1), len(str2)
    
    # DP table with parent tracking
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    parent = [[None for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
        if i > 0:
            parent[i][0] = (EditOperation.DELETE, i-1, str1[i-1])
    
    for j in range(n + 1):
        dp[0][j] = j
        if j > 0:
            parent[0][j] = (EditOperation.INSERT, j-1, str2[j-1])
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                parent[i][j] = (EditOperation.MATCH, i-1, str1[i-1])
            else:
                delete_cost = dp[i-1][j] + 1
                insert_cost = dp[i][j-1] + 1
                substitute_cost = dp[i-1][j-1] + 1
                
                min_cost = min(delete_cost, insert_cost, substitute_cost)
                dp[i][j] = min_cost
                
                if min_cost == delete_cost:
                    parent[i][j] = (EditOperation.DELETE, i-1, str1[i-1])
                elif min_cost == insert_cost:
                    parent[i][j] = (EditOperation.INSERT, j-1, str2[j-1])
                else:
                    parent[i][j] = (EditOperation.SUBSTITUTE, i-1, f"{str1[i-1]}->{str2[j-1]}")
    
    # Backtrack to get operations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if parent[i][j] is None:
            break
        
        op, pos, char = parent[i][j]
        operations.append((op, pos, char))
        
        if op == EditOperation.DELETE or op == EditOperation.SUBSTITUTE:
            i -= 1
        if op == EditOperation.INSERT or op == EditOperation.SUBSTITUTE:
            j -= 1
        if op == EditOperation.MATCH:
            i -= 1
            j -= 1
    
    operations.reverse()
    return dp[m][n], operations


def edit_distance_space_optimized(str1: str, str2: str) -> int:
    """
    Space-optimized edit distance (only returns distance)
    
    Space Complexity: O(min(m, n))
    """
    # Make str1 the shorter string
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    m, n = len(str1), len(str2)
    
    # Use only two rows
    prev = list(range(m + 1))
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        curr[0] = j
        
        for i in range(1, m + 1):
            if str1[i-1] == str2[j-1]:
                curr[i] = prev[i-1]
            else:
                curr[i] = 1 + min(prev[i], curr[i-1], prev[i-1])
        
        prev, curr = curr, prev
    
    return prev[m]


def weighted_edit_distance(str1: str, str2: str, 
                          insert_cost: float = 1.0,
                          delete_cost: float = 1.0,
                          substitute_cost: float = 1.0) -> float:
    """
    Edit distance with custom operation costs
    
    Args:
        str1: Source string
        str2: Target string
        insert_cost: Cost of insertion
        delete_cost: Cost of deletion
        substitute_cost: Cost of substitution
    
    Returns:
        Minimum weighted edit distance
    """
    m, n = len(str1), len(str2)
    
    dp = [[0.0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i * delete_cost
    
    for j in range(n + 1):
        dp[0][j] = j * insert_cost
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No cost for match
            else:
                dp[i][j] = min(
                    dp[i-1][j] + delete_cost,      # Delete
                    dp[i][j-1] + insert_cost,      # Insert
                    dp[i-1][j-1] + substitute_cost # Substitute
                )
    
    return dp[m][n]


def edit_distance_with_transposition(str1: str, str2: str) -> int:
    """
    Damerau-Levenshtein distance including transposition
    
    Allows four operations: insert, delete, substitute, transpose
    """
    m, n = len(str1), len(str2)
    
    # Character alphabet for transposition tracking
    chars = set(str1 + str2)
    da = {char: 0 for char in chars}
    
    # Extended DP table
    max_dist = m + n
    dp = [[max_dist for _ in range(n + 2)] for _ in range(m + 2)]
    
    dp[0][0] = max_dist
    for i in range(0, m + 1):
        dp[i+1][0] = max_dist
        dp[i+1][1] = i
    for j in range(0, n + 1):
        dp[0][j+1] = max_dist
        dp[1][j+1] = j
    
    for i in range(1, m + 1):
        db = 0
        for j in range(1, n + 1):
            k = da[str2[j-1]]
            l = db
            cost = 1
            
            if str1[i-1] == str2[j-1]:
                cost = 0
                db = j
            
            dp[i+1][j+1] = min(
                dp[i][j] + cost,        # Substitute or match
                dp[i+1][j] + 1,         # Insert
                dp[i][j+1] + 1,         # Delete
                dp[k][l] + (i-k-1) + 1 + (j-l-1)  # Transpose
            )
        
        da[str1[i-1]] = i
    
    return dp[m+1][n+1]


def similarity_ratio(str1: str, str2: str) -> float:
    """
    Calculate similarity ratio based on edit distance
    
    Returns:
        Similarity ratio between 0.0 and 1.0
    """
    if not str1 and not str2:
        return 1.0
    
    max_len = max(len(str1), len(str2))
    if max_len == 0:
        return 1.0
    
    distance = edit_distance(str1, str2)
    return 1.0 - (distance / max_len)


def fuzzy_match(target: str, candidates: List[str], threshold: float = 0.8) -> List[Tuple[str, float]]:
    """
    Find fuzzy matches for target string in candidate list
    
    Args:
        target: String to match
        candidates: List of candidate strings
        threshold: Minimum similarity threshold
    
    Returns:
        List of (candidate, similarity) pairs above threshold
    """
    matches = []
    
    for candidate in candidates:
        similarity = similarity_ratio(target, candidate)
        if similarity >= threshold:
            matches.append((candidate, similarity))
    
    # Sort by similarity (descending)
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches


def demo_basic_edit_distance():
    """Demonstrate basic edit distance functionality"""
    print("=== Basic Edit Distance Demo ===")
    
    test_cases = [
        ("kitten", "sitting"),
        ("saturday", "sunday"),
        ("intention", "execution"),
        ("", "abc"),
        ("abc", ""),
        ("same", "same")
    ]
    
    for str1, str2 in test_cases:
        distance = edit_distance(str1, str2)
        similarity = similarity_ratio(str1, str2)
        
        print(f"'{str1}' -> '{str2}':")
        print(f"  Edit distance: {distance}")
        print(f"  Similarity: {similarity:.2%}")
        print()


def demo_edit_operations():
    """Demonstrate edit operations tracking"""
    print("=== Edit Operations Demo ===")
    
    str1 = "kitten"
    str2 = "sitting"
    
    print(f"Transforming '{str1}' to '{str2}':")
    
    distance, operations = edit_distance_with_operations(str1, str2)
    print(f"Edit distance: {distance}")
    print(f"Operations:")
    
    for i, (op, pos, char) in enumerate(operations, 1):
        if op == EditOperation.MATCH:
            print(f"  {i}. {op.value}: '{char}' at position {pos}")
        elif op == EditOperation.INSERT:
            print(f"  {i}. {op.value}: '{char}' at position {pos}")
        elif op == EditOperation.DELETE:
            print(f"  {i}. {op.value}: '{char}' from position {pos}")
        elif op == EditOperation.SUBSTITUTE:
            print(f"  {i}. {op.value}: '{char}' at position {pos}")


def demo_weighted_edit_distance():
    """Demonstrate weighted edit distance"""
    print("\n=== Weighted Edit Distance Demo ===")
    
    str1 = "cat"
    str2 = "bat"
    
    print(f"Strings: '{str1}' -> '{str2}'")
    
    # Standard costs
    standard = weighted_edit_distance(str1, str2)
    print(f"Standard costs (1,1,1): {standard}")
    
    # Make substitution cheaper
    cheap_sub = weighted_edit_distance(str1, str2, 
                                     insert_cost=2, delete_cost=2, substitute_cost=0.5)
    print(f"Cheap substitution (2,2,0.5): {cheap_sub}")
    
    # Make insertion expensive
    expensive_insert = weighted_edit_distance(str1, str2,
                                            insert_cost=3, delete_cost=1, substitute_cost=1)
    print(f"Expensive insertion (3,1,1): {expensive_insert}")


def demo_fuzzy_matching():
    """Demonstrate fuzzy string matching"""
    print("\n=== Fuzzy String Matching Demo ===")
    
    # Dictionary of words
    dictionary = [
        "apple", "application", "appreciate", "approach",
        "banana", "band", "hand", "land", "sand",
        "computer", "complete", "company", "compare"
    ]
    
    # Misspelled words
    misspelled = ["aple", "applicaton", "compter", "comany"]
    
    print("Dictionary:", dictionary)
    print()
    
    for word in misspelled:
        print(f"Fuzzy matches for '{word}':")
        matches = fuzzy_match(word, dictionary, threshold=0.6)
        
        if matches:
            for candidate, similarity in matches[:3]:  # Top 3 matches
                print(f"  {candidate}: {similarity:.2%}")
        else:
            print("  No matches found")
        print()


def demo_dna_analysis():
    """Demonstrate edit distance for DNA analysis"""
    print("\n=== DNA Sequence Analysis Demo ===")
    
    dna1 = "AGTGATG"
    dna2 = "AGCGATC"
    
    print(f"DNA Sequence 1: {dna1}")
    print(f"DNA Sequence 2: {dna2}")
    
    distance = edit_distance(dna1, dna2)
    similarity = similarity_ratio(dna1, dna2)
    
    print(f"Edit distance: {distance}")
    print(f"Similarity: {similarity:.2%}")
    
    # Show operations
    _, operations = edit_distance_with_operations(dna1, dna2)
    print(f"\nMutations needed:")
    
    for i, (op, pos, char) in enumerate(operations, 1):
        if op != EditOperation.MATCH:
            print(f"  {i}. {op.value}: {char}")


def demo_spell_checker():
    """Demonstrate spell checker application"""
    print("\n=== Spell Checker Demo ===")
    
    # Simple dictionary
    dictionary = [
        "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog",
        "hello", "world", "python", "programming", "algorithm", "computer"
    ]
    
    # Text with typos
    text = "the quik browm fox jums over the lasy dog"
    words = text.split()
    
    print(f"Original text: {text}")
    print(f"Corrections:")
    
    corrected_words = []
    for word in words:
        if word in dictionary:
            corrected_words.append(word)
            print(f"  '{word}' -> OK")
        else:
            matches = fuzzy_match(word, dictionary, threshold=0.7)
            if matches:
                suggestion = matches[0][0]  # Best match
                corrected_words.append(suggestion)
                print(f"  '{word}' -> '{suggestion}' ({matches[0][1]:.2%})")
            else:
                corrected_words.append(f"[{word}]")  # Mark as unknown
                print(f"  '{word}' -> [UNKNOWN]")
    
    corrected_text = " ".join(corrected_words)
    print(f"\nCorrected text: {corrected_text}")


def compare_algorithms():
    """Compare different edit distance algorithms"""
    print("\n=== Algorithm Comparison ===")
    
    print("Standard Edit Distance (Levenshtein):")
    print("✓ Three operations: insert, delete, substitute")
    print("✓ O(m*n) time, O(m*n) or O(min(m,n)) space")
    print("✓ Most commonly used")
    
    print("\nDamerau-Levenshtein Distance:")
    print("✓ Four operations: + transposition")
    print("✓ Handles adjacent character swaps")
    print("✓ More realistic for typing errors")
    print("✗ Slightly more complex")
    
    print("\nWeighted Edit Distance:")
    print("✓ Custom costs for different operations")
    print("✓ Domain-specific optimization")
    print("✓ Can model real-world error probabilities")
    
    print("\nApplications:")
    print("• Spell checkers and auto-correction")
    print("• DNA/protein sequence alignment")
    print("• Plagiarism detection")
    print("• Data deduplication")
    print("• Fuzzy string matching")
    print("• Version control (diff algorithms)")


if __name__ == "__main__":
    demo_basic_edit_distance()
    demo_edit_operations()
    demo_weighted_edit_distance()
    demo_fuzzy_matching()
    demo_dna_analysis()
    demo_spell_checker()
    compare_algorithms()
