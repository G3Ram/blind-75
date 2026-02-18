"""
Problem: Implement Trie (Prefix Tree) (LeetCode #208)
Difficulty: Medium
Category: Trees

Description:
A trie or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Implement the Trie class with insert, search, and startsWith methods.

Examples:
Input: Operations: ['Trie', 'insert', 'search', 'startsWith']
Output: [null, null, true, true]

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters
- At most 3*10^4 calls will be made to insert, search, and startsWith

Time Complexity Target: O(m)
Space Complexity Target: O(m)
"""


class Trie:
    def __init__(self):
        """
        TODO: Initialize your data structure here
        """
        pass

    def insert(self, word: str) -> None:
        """
        TODO: Implement your solution here

        Inserts the string word into the trie.

        Args:
            word: The word to insert
        """
        pass

    def search(self, word: str) -> bool:
        """
        TODO: Implement your solution here

        Returns true if the string word is in the trie, false otherwise.

        Args:
            word: The word to search for

        Returns:
            True if the word exists in the trie, False otherwise
        """
        pass

    def startsWith(self, prefix: str) -> bool:
        """
        TODO: Implement your solution here

        Returns true if there is a previously inserted word that has the prefix.

        Args:
            prefix: The prefix to check

        Returns:
            True if any word in the trie starts with prefix, False otherwise
        """
        pass


# Test Cases
def test_implement_trie():
    """Test cases for Trie"""

    test_cases = [
        {
            "name": "Test case 1: Search existing word",
            "inserts": ["apple"],
            "method": "search",
            "query": "apple",
            "expected": True
        },
        {
            "name": "Test case 2: Search non-existing word",
            "inserts": ["apple"],
            "method": "search",
            "query": "app",
            "expected": False
        },
        {
            "name": "Test case 3: startsWith existing prefix",
            "inserts": ["apple"],
            "method": "startsWith",
            "query": "app",
            "expected": True
        },
        {
            "name": "Test case 4: Search after inserting prefix as word",
            "inserts": ["apple", "app"],
            "method": "search",
            "query": "app",
            "expected": True
        },
        {
            "name": "Edge case: Search empty trie",
            "inserts": [],
            "method": "search",
            "query": "any",
            "expected": False
        },
        {
            "name": "Edge case: startsWith with no matching prefix",
            "inserts": ["apple"],
            "method": "startsWith",
            "query": "xyz",
            "expected": False
        },
        {
            "name": "Edge case: Search single character word",
            "inserts": ["a"],
            "method": "search",
            "query": "a",
            "expected": True
        },
        {
            "name": "Edge case: startsWith full word",
            "inserts": ["hello"],
            "method": "startsWith",
            "query": "hello",
            "expected": True
        },
        {
            "name": "Edge case: Multiple words, search one",
            "inserts": ["the", "a", "there", "answer", "any", "by", "bye", "their"],
            "method": "search",
            "query": "there",
            "expected": True
        },
        {
            "name": "Edge case: Multiple words, search non-existing",
            "inserts": ["the", "a", "there", "answer", "any"],
            "method": "search",
            "query": "these",
            "expected": False
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: inserts={test['inserts']}, {test['method']}('{test['query']}')")
        print(f"  Expected: {test['expected']}")

        try:
            trie = Trie()
            for word in test['inserts']:
                trie.insert(word)

            if test['method'] == 'search':
                result = trie.search(test['query'])
            else:
                result = trie.startsWith(test['query'])

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
    test_implement_trie()
