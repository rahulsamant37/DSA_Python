"""
003 - Longest Common Subsequence (LCS)
======================================

Dynamic Programming solution for finding the Longest Common Subsequence
between two strings/sequences.

A subsequence is derived by deleting some (or no) characters without 
changing the order of remaining characters.

Time Complexity: O(m * n) where m, n are string lengths
Space Complexity: O(m * n) or O(min(m, n)) with optimization

Applications:
- DNA sequence alignment in bioinformatics
- Text comparison and diff algorithms
- Version control systems
- Plagiarism detection
"""

from typing import List, Tuple, Optional


def lcs_length(str1: str, str2: str) -> int:
    """
    Find length of Longest Common Subsequence
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        Length of LCS
    """
    m, n = len(str1), len(str2)
    
    # DP table: dp[i][j] = LCS length of str1[0:i] and str2[0:j]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


def lcs_string(str1: str, str2: str) -> str:
    """
    Find the actual Longest Common Subsequence string
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        LCS string
    """
    m, n = len(str1), len(str2)
    
    # Build DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtrack to construct LCS
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))


def lcs_all_sequences(str1: str, str2: str) -> List[str]:
    """
    Find all Longest Common Subsequences
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        List of all LCS strings
    """
    m, n = len(str1), len(str2)
    
    # Build DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Find all LCS using backtracking
    def find_all_lcs(i: int, j: int, current_lcs: str) -> List[str]:
        if i == 0 or j == 0:
            return [current_lcs[::-1]]  # Reverse since we built backwards
        
        result = []
        
        if str1[i-1] == str2[j-1]:
            # Characters match - must include in LCS
            result.extend(find_all_lcs(i-1, j-1, current_lcs + str1[i-1]))
        else:
            # Characters don't match - try both directions
            if dp[i-1][j] == dp[i][j]:
                result.extend(find_all_lcs(i-1, j, current_lcs))
            if dp[i][j-1] == dp[i][j]:
                result.extend(find_all_lcs(i, j-1, current_lcs))
        
        return result
    
    all_lcs = find_all_lcs(m, n, "")
    return list(set(all_lcs))  # Remove duplicates


def lcs_space_optimized(str1: str, str2: str) -> int:
    """
    Space-optimized LCS (only returns length)
    
    Space Complexity: O(min(m, n))
    """
    # Make str1 the shorter string for space optimization
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    m, n = len(str1), len(str2)
    
    # Use only two rows
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str2[j-1] == str1[i-1]:
                curr[i] = prev[i-1] + 1
            else:
                curr[i] = max(prev[i], curr[i-1])
        
        # Swap rows
        prev, curr = curr, prev
    
    return prev[m]


def lcs_with_positions(str1: str, str2: str) -> Tuple[str, List[int], List[int]]:
    """
    Find LCS with positions in both strings
    
    Returns:
        Tuple of (lcs_string, positions_in_str1, positions_in_str2)
    """
    m, n = len(str1), len(str2)
    
    # Build DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtrack to get LCS and positions
    lcs = []
    pos1 = []
    pos2 = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            pos1.append(i-1)
            pos2.append(j-1)
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Reverse since we built backwards
    lcs.reverse()
    pos1.reverse()
    pos2.reverse()
    
    return ''.join(lcs), pos1, pos2


def lcs_diff(str1: str, str2: str) -> Tuple[List[str], List[str]]:
    """
    Create a diff-like output showing additions and deletions
    
    Returns:
        Tuple of (operations_str1, operations_str2)
        where each operation is either the character or a marker
    """
    lcs, pos1, pos2 = lcs_with_positions(str1, str2)
    
    diff1 = []
    diff2 = []
    
    # Process str1
    lcs_idx = 0
    for i, char in enumerate(str1):
        if lcs_idx < len(pos1) and i == pos1[lcs_idx]:
            diff1.append(char)  # Common character
            lcs_idx += 1
        else:
            diff1.append(f"-{char}")  # Deleted from str1
    
    # Process str2
    lcs_idx = 0
    for i, char in enumerate(str2):
        if lcs_idx < len(pos2) and i == pos2[lcs_idx]:
            diff2.append(char)  # Common character
            lcs_idx += 1
        else:
            diff2.append(f"+{char}")  # Added in str2
    
    return diff1, diff2


def lcs_three_strings(str1: str, str2: str, str3: str) -> str:
    """
    Find LCS of three strings
    
    Time Complexity: O(m * n * p)
    Space Complexity: O(m * n * p)
    """
    m, n, p = len(str1), len(str2), len(str3)
    
    # 3D DP table
    dp = [[[0 for _ in range(p + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, p + 1):
                if str1[i-1] == str2[j-1] == str3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )
    
    # Backtrack to get LCS
    lcs = []
    i, j, k = m, n, p
    
    while i > 0 and j > 0 and k > 0:
        if str1[i-1] == str2[j-1] == str3[k-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
            k -= 1
        elif dp[i-1][j][k] == dp[i][j][k]:
            i -= 1
        elif dp[i][j-1][k] == dp[i][j][k]:
            j -= 1
        else:
            k -= 1
    
    return ''.join(reversed(lcs))


def demo_basic_lcs():
    """Demonstrate basic LCS functionality"""
    print("=== Basic LCS Demo ===")
    
    str1 = "ABCDGH"
    str2 = "AEDFHR"
    
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    
    # Length only
    length = lcs_length(str1, str2)
    print(f"LCS length: {length}")
    
    # Actual LCS
    lcs = lcs_string(str1, str2)
    print(f"LCS string: '{lcs}'")
    
    # LCS with positions
    lcs_str, pos1, pos2 = lcs_with_positions(str1, str2)
    print(f"LCS: '{lcs_str}'")
    print(f"Positions in str1: {pos1}")
    print(f"Positions in str2: {pos2}")
    
    # Visualize positions
    print(f"String 1: {str1}")
    print(f"Matches:  {' '.join('*' if i in pos1 else ' ' for i in range(len(str1)))}")
    print(f"String 2: {str2}")
    print(f"Matches:  {' '.join('*' if i in pos2 else ' ' for i in range(len(str2)))}")


def demo_multiple_lcs():
    """Demonstrate multiple LCS strings"""
    print("\n=== Multiple LCS Demo ===")
    
    str1 = "ABCDEF"
    str2 = "ACEF"
    
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    
    # All possible LCS
    all_lcs = lcs_all_sequences(str1, str2)
    print(f"All LCS ({len(all_lcs)} total):")
    for i, lcs in enumerate(all_lcs, 1):
        print(f"  {i}: '{lcs}'")


def demo_diff_algorithm():
    """Demonstrate diff-like functionality"""
    print("\n=== Diff Algorithm Demo ===")
    
    str1 = "HELLO"
    str2 = "HELP"
    
    print(f"Original: {str1}")
    print(f"Modified: {str2}")
    
    diff1, diff2 = lcs_diff(str1, str2)
    
    print(f"Diff view:")
    print(f"Original: {' '.join(diff1)}")
    print(f"Modified: {' '.join(diff2)}")
    
    # More complex example
    print(f"\nComplex diff example:")
    text1 = "The quick brown fox"
    text2 = "The slow brown cat"
    
    print(f"Text 1: {text1}")
    print(f"Text 2: {text2}")
    
    lcs = lcs_string(text1, text2)
    print(f"Common: '{lcs}'")


def demo_three_string_lcs():
    """Demonstrate LCS of three strings"""
    print("\n=== Three String LCS Demo ===")
    
    str1 = "ABCD"
    str2 = "ACBD"
    str3 = "ACD"
    
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print(f"String 3: {str3}")
    
    lcs = lcs_three_strings(str1, str2, str3)
    print(f"LCS of all three: '{lcs}'")
    
    # Pairwise comparisons
    lcs12 = lcs_string(str1, str2)
    lcs13 = lcs_string(str1, str3)
    lcs23 = lcs_string(str2, str3)
    
    print(f"Pairwise LCS:")
    print(f"  {str1} & {str2}: '{lcs12}'")
    print(f"  {str1} & {str3}: '{lcs13}'")
    print(f"  {str2} & {str3}: '{lcs23}'")


def demo_dna_alignment():
    """Demonstrate DNA sequence alignment"""
    print("\n=== DNA Sequence Alignment Demo ===")
    
    dna1 = "AGTGATG"
    dna2 = "GTTAG"
    
    print(f"DNA Sequence 1: {dna1}")
    print(f"DNA Sequence 2: {dna2}")
    
    lcs, pos1, pos2 = lcs_with_positions(dna1, dna2)
    print(f"Common subsequence: {lcs}")
    print(f"Similarity: {len(lcs)}/{max(len(dna1), len(dna2))} = {len(lcs)/max(len(dna1), len(dna2)):.2%}")
    
    # Create alignment visualization
    print(f"\nAlignment:")
    alignment1 = ""
    alignment2 = ""
    
    i1 = i2 = 0
    lcs_idx = 0
    
    while i1 < len(dna1) or i2 < len(dna2):
        if (lcs_idx < len(pos1) and i1 == pos1[lcs_idx] and 
            lcs_idx < len(pos2) and i2 == pos2[lcs_idx]):
            # Match
            alignment1 += dna1[i1]
            alignment2 += dna2[i2]
            i1 += 1
            i2 += 1
            lcs_idx += 1
        elif i1 < len(dna1) and (i2 >= len(dna2) or 
                                (lcs_idx < len(pos1) and i1 < pos1[lcs_idx])):
            # Gap in sequence 2
            alignment1 += dna1[i1]
            alignment2 += "-"
            i1 += 1
        else:
            # Gap in sequence 1
            alignment1 += "-"
            alignment2 += dna2[i2]
            i2 += 1
    
    print(f"Seq1: {alignment1}")
    print(f"Seq2: {alignment2}")


def lcs_applications():
    """Discuss LCS applications and variations"""
    print("\n=== LCS Applications and Variations ===")
    
    print("Applications:")
    print("1. DNA/Protein sequence alignment in bioinformatics")
    print("2. Text comparison and diff utilities (git diff)")
    print("3. Plagiarism detection")
    print("4. Data compression algorithms")
    print("5. Version control systems")
    print("6. Spell checkers and auto-correction")
    
    print("\nVariations:")
    print("1. Longest Common Substring (continuous)")
    print("2. Edit Distance (Levenshtein Distance)")
    print("3. Shortest Common Supersequence")
    print("4. Longest Increasing Subsequence")
    print("5. Weighted LCS (different character costs)")
    print("6. LCS with constraints")
    
    print("\nComplexity:")
    print("• Time: O(m * n) for two strings")
    print("• Space: O(m * n) or O(min(m, n)) optimized")
    print("• Three strings: O(m * n * p)")
    print("• K strings: O(n^k) - exponential!")


if __name__ == "__main__":
    demo_basic_lcs()
    demo_multiple_lcs()
    demo_diff_algorithm()
    demo_three_string_lcs()
    demo_dna_alignment()
    lcs_applications()
