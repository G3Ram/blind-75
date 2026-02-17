"""
Problem: Group Anagrams (LeetCode #49)
Difficulty: Medium
Category: Strings

Description:
Given an array of strings strs, group the anagrams together. Return the groups in any order.

Examples:
Input: strs = ['eat','tea','tan','ate','nat','bat']
Output: [['bat'],['nat','tan'],['ate','eat','tea']]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

Time Complexity Target: O(n*k)
Space Complexity Target: O(n*k)
"""

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    TODO: Implement your solution here

    Args:
        strs: List of strings to group by anagram

    Returns:
        List of groups where each group contains strings that are anagrams of each other
    """
    pass


# Test Cases
def test_group_anagrams():
    """Test cases for group_anagrams"""

    test_cases = [
        {
            "name": "Test case 1: Mixed anagram groups",
            "input": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        },
        {
            "name": "Test case 2: Single string",
            "input": ["a"],
            "expected": [["a"]]
        },
        {
            "name": "Test case 3: All same string",
            "input": ["abc", "abc", "abc"],
            "expected": [["abc", "abc", "abc"]]
        },
        {
            "name": "Test case 4: No anagrams",
            "input": ["abc", "def", "ghi"],
            "expected": [["abc"], ["def"], ["ghi"]]
        },
        {
            "name": "Edge case: Single character strings",
            "input": ["a", "b", "a"],
            "expected": [["a", "a"], ["b"]]
        },
        {
            "name": "Edge case: Empty strings",
            "input": ["", ""],
            "expected": [["", ""]]
        },
        {
            "name": "Edge case: All anagrams",
            "input": ["eat", "tea", "ate"],
            "expected": [["eat", "tea", "ate"]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = group_anagrams(test['input'])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                # Normalize: sort each group and sort the list of groups for comparison
                result_sorted = sorted([sorted(g) for g in result])
                expected_sorted = sorted([sorted(g) for g in test['expected']])
                if result_sorted == expected_sorted:
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
    test_group_anagrams()
