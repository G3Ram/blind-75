"""
Problem: Word Search (LeetCode #79)
Difficulty: Medium
Category: Matrix

Description:
Given an m x n grid of characters and a string word, return true if word exists in the grid. Word can be constructed from sequentially adjacent cells (horizontally or vertically).

Examples:
Input: board = [['A','B','C'],['S','F','C'],['A','D','E']], word = 'ABCCED'
Output: true

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consist of only lowercase and uppercase English letters

Time Complexity Target: O(m*n*4^L)
Space Complexity Target: O(L)
"""

from typing import List


def word_search(board: List[List[str]], word: str) -> bool:
    """
    TODO: Implement your solution here

    Args:
        board: m x n grid of characters
        word: target word to search for

    Returns:
        True if word exists in the grid, False otherwise
    """
    pass


# Test Cases
def test_word_search():
    """Test cases for word_search"""

    test_cases = [
        {
            "name": "Test case 1: word exists diagonally adjacent",
            "board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "word": "ABCCED",
            "expected": True,
        },
        {
            "name": "Test case 2: word exists at end",
            "board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "word": "SEE",
            "expected": True,
        },
        {
            "name": "Test case 3: word does not exist (revisit required)",
            "board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "word": "ABCB",
            "expected": False,
        },
        {
            "name": "Edge case: single cell board, word matches",
            "board": [["A"]],
            "word": "A",
            "expected": True,
        },
        {
            "name": "Edge case: single cell board, word does not match",
            "board": [["A"]],
            "word": "B",
            "expected": False,
        },
        {
            "name": "Edge case: word longer than board cells",
            "board": [["A"]],
            "word": "AB",
            "expected": False,
        },
        {
            "name": "Edge case: word wraps entire board",
            "board": [["A", "B"], ["C", "D"]],
            "word": "ABDC",
            "expected": True,
        },
        {
            "name": "Edge case: all same characters, word not possible",
            "board": [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"]],
            "word": "AAAB",
            "expected": False,
        },
        {
            "name": "Edge case: word is single character present multiple times",
            "board": [["A", "B"], ["C", "A"]],
            "word": "A",
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Board: {test['board']}")
        print(f"  Word: {test['word']!r}")
        print(f"  Expected: {test['expected']}")

        try:
            result = word_search(test["board"], test["word"])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            elif result == test["expected"]:
                print(f"  ✓ PASSED: {result}")
                passed += 1
            else:
                print(f"  ✗ FAILED: Got {result}")
                failed += 1

        except Exception as e:
            print(f"  ✗ FAILED: {type(e).__name__}: {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")

    if failed == 0:
        print("✓ All test cases passed!")
    else:
        print("✗ Some test cases failed. Please review the implementation.")


if __name__ == "__main__":
    test_word_search()
