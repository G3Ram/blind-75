"""
Problem: Top K Frequent Elements (LeetCode #347)
Difficulty: Medium
Category: Heap

Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Examples:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- k is in range [1, number of unique elements]
- Answer is guaranteed to be unique

Time Complexity Target: O(n log k)
Space Complexity Target: O(n)
"""

from typing import List


def top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        nums: Input integer array
        k: Number of top frequent elements to return

    Returns:
        List of k most frequent elements
    """
    pass


# Test Cases
def test_top_k_frequent_elements():
    """Test cases for top_k_frequent_elements"""

    test_cases = [
        {
            "name": "Test case 1: basic example with k=2",
            "nums": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2],
        },
        {
            "name": "Test case 2: single element",
            "nums": [1],
            "k": 1,
            "expected": [1],
        },
        {
            "name": "Test case 3: all same elements",
            "nums": [3, 3, 3, 3],
            "k": 1,
            "expected": [3],
        },
        {
            "name": "Test case 4: k equals number of unique elements",
            "nums": [1, 2, 3],
            "k": 3,
            "expected": [1, 2, 3],
        },
        {
            "name": "Test case 5: negative numbers",
            "nums": [-1, -1, -2, -2, -2, 3],
            "k": 2,
            "expected": [-2, -1],
        },
        {
            "name": "Test case 6: clear winner for k=1",
            "nums": [1, 1, 2, 2, 3, 3, 3],
            "k": 1,
            "expected": [3],
        },
        {
            "name": "Test case 7: larger input",
            "nums": [4, 4, 4, 5, 5, 6, 6, 6, 6, 7],
            "k": 2,
            "expected": [6, 4],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums={test['nums']}, k={test['k']}")
        print(f"  Expected: {sorted(test['expected'])}")

        try:
            result = top_k_frequent_elements(test["nums"], test["k"])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if sorted(result) == sorted(test["expected"]):
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
    test_top_k_frequent_elements()
