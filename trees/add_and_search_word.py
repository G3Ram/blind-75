"""
Problem: Design Add and Search Words Data Structure (LeetCode #211)
Difficulty: Medium
Category: Trees

Description:
Design a data structure that supports adding new words and finding if a string matches any previously added string. Search can use '.' to represent any letter.

Examples:
Input: Operations: ['WordDictionary','addWord','search']
Output: [null,null,true,false,true]

Constraints:
- 1 <= word.length <= 25
- word consists of lowercase English letters
- queries consist of lowercase English letters or '.'
- At most 10^4 calls will be made

Time Complexity Target: O(m)
Space Complexity Target: O(m)
"""


class WordDictionary:
    def __init__(self):
        """
        TODO: Initialize your data structure here
        """
        pass

    def addWord(self, word: str) -> None:
        """
        TODO: Implement your solution here

        Adds word to the data structure.

        Args:
            word: The word to add
        """
        pass

    def search(self, word: str) -> bool:
        """
        TODO: Implement your solution here

        Returns true if there is any string in the data structure that matches word.
        '.' matches any single letter.

        Args:
            word: The pattern to search (may contain '.' wildcards)

        Returns:
            True if any stored word matches the pattern, False otherwise
        """
        pass


# Test Cases
def test_add_and_search_word():
    """Test cases for WordDictionary"""

    test_cases = [
        {
            "name": "Test case 1: Exact match",
            "adds": ["bad", "dad", "mad"],
            "query": "bad",
            "expected": True
        },
        {
            "name": "Test case 2: No match",
            "adds": ["bad", "dad", "mad"],
            "query": "pad",
            "expected": False
        },
        {
            "name": "Test case 3: Wildcard matches first character",
            "adds": ["bad", "dad", "mad"],
            "query": ".ad",
            "expected": True
        },
        {
            "name": "Test case 4: All wildcards",
            "adds": ["bad"],
            "query": "...",
            "expected": True
        },
        {
            "name": "Edge case: Search empty dictionary",
            "adds": [],
            "query": "any",
            "expected": False
        },
        {
            "name": "Edge case: Single character exact match",
            "adds": ["a"],
            "query": "a",
            "expected": True
        },
        {
            "name": "Edge case: Single character wildcard",
            "adds": ["a"],
            "query": ".",
            "expected": True
        },
        {
            "name": "Edge case: Wildcard no match (length mismatch)",
            "adds": ["bad"],
            "query": "..",
            "expected": False
        },
        {
            "name": "Edge case: Wildcard in middle",
            "adds": ["bat", "ball", "bad"],
            "query": "b.t",
            "expected": True
        },
        {
            "name": "Edge case: Multiple wildcards, no match",
            "adds": ["cat", "dog"],
            "query": "b.t",
            "expected": False
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: adds={test['adds']}, search('{test['query']}')")
        print(f"  Expected: {test['expected']}")

        try:
            wd = WordDictionary()
            for word in test['adds']:
                wd.addWord(word)

            result = wd.search(test['query'])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            elif result == test['expected']:
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
    test_add_and_search_word()
