"""
Problem: Valid Anagram (LeetCode #242)
Difficulty: Easy
Category: Strings

Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Examples:
Input: s = 'anagram', t = 'nagaram'
Output: true
Input: s = 'rat', t = 'car'
Output: false

Constraints:
- 1 <= s.length, t.length <= 5*10^4
- s and t consist of lowercase English letters

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

def valid_anagram(s: str, t: str) -> bool:
    """
    TODO: Implement your solution here

    Args:
        s: First string
        t: Second string to check if it's an anagram of s

    Returns:
        True if t is an anagram of s, False otherwise
    """
    pass


# Test Cases
def test_valid_anagram():
    """Test cases for valid_anagram"""

    test_cases = [
        {
            "name": "Test case 1: Valid anagram",
            "input": ("anagram", "nagaram"),
            "expected": True
        },
        {
            "name": "Test case 2: Not an anagram",
            "input": ("rat", "car"),
            "expected": False
        },
        {
            "name": "Test case 3: Different lengths",
            "input": ("hello", "world"),
            "expected": False
        },
        {
            "name": "Test case 4: Single character - same",
            "input": ("a", "a"),
            "expected": True
        },
        {
            "name": "Test case 5: Single character - different",
            "input": ("a", "b"),
            "expected": False
        },
        {
            "name": "Edge case: Empty strings",
            "input": ("", ""),
            "expected": True
        },
        {
            "name": "Edge case: Repeated characters",
            "input": ("aabbcc", "abcabc"),
            "expected": True
        }
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: s = '{test['input'][0]}', t = '{test['input'][1]}'")
        print(f"  Expected: {test['expected']}")

        try:
            result = valid_anagram(test['input'][0], test['input'][1])

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
    test_valid_anagram()
