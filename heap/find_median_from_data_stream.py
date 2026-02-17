"""
Problem: Find Median from Data Stream (LeetCode #295)
Difficulty: Hard
Category: Heap

Description:
Design a data structure that supports adding integers and finding the median of all elements.
The median is the middle value in an ordered integer list. If the size of the list is even,
the median is the mean of the two middle values.

Examples:
Input: Operations: ['MedianFinder','addNum','addNum','findMedian','addNum','findMedian']
       Values:     [[], [1], [2], [], [3], []]
Output: [null, null, null, 1.5, null, 2.0]

Constraints:
- -10^5 <= num <= 10^5
- At most 5*10^4 calls to addNum and findMedian
- There will be at least one element in the data structure before calling findMedian

Time Complexity Target: O(log n) for addNum, O(1) for findMedian
Space Complexity Target: O(n)
"""


class MedianFinder:
    """
    TODO: Implement your solution here.

    Hint: Use two heaps — a max-heap for the lower half and a min-heap for the upper half.
    """

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


# Test Cases
def test_median_finder():
    """Test cases for MedianFinder"""

    test_cases = [
        {
            "name": "Test case 1: basic example from problem description",
            "operations": ["addNum", "addNum", "findMedian", "addNum", "findMedian"],
            "values": [1, 2, None, 3, None],
            "expected": [None, None, 1.5, None, 2.0],
        },
        {
            "name": "Test case 2: single element",
            "operations": ["addNum", "findMedian"],
            "values": [5, None],
            "expected": [None, 5.0],
        },
        {
            "name": "Test case 3: even count — median is average of two middles",
            "operations": ["addNum", "addNum", "findMedian"],
            "values": [2, 3, None],
            "expected": [None, None, 2.5],
        },
        {
            "name": "Test case 4: descending order insertions",
            "operations": ["addNum", "addNum", "addNum", "findMedian"],
            "values": [5, 3, 1, None],
            "expected": [None, None, None, 3.0],
        },
        {
            "name": "Test case 5: all same values",
            "operations": ["addNum", "addNum", "addNum", "findMedian"],
            "values": [7, 7, 7, None],
            "expected": [None, None, None, 7.0],
        },
        {
            "name": "Test case 6: negative numbers",
            "operations": ["addNum", "addNum", "addNum", "findMedian"],
            "values": [-1, -2, -3, None],
            "expected": [None, None, None, -2.0],
        },
        {
            "name": "Test case 7: mixed positive and negative",
            "operations": ["addNum", "addNum", "addNum", "addNum", "findMedian"],
            "values": [-1, 3, -2, 4, None],
            "expected": [None, None, None, None, 1.0],
        },
        {
            "name": "Test case 8: multiple findMedian calls",
            "operations": ["addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
            "values": [10, None, 20, None, 15, None],
            "expected": [None, 10.0, None, 15.0, None, 15.0],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Operations: {test['operations']}")
        print(f"  Values:     {test['values']}")
        print(f"  Expected:   {test['expected']}")

        try:
            finder = MedianFinder()
            results = []
            not_implemented = False

            for op, val in zip(test["operations"], test["values"]):
                if op == "addNum":
                    finder.addNum(val)
                    results.append(None)
                elif op == "findMedian":
                    median = finder.findMedian()
                    if median is None:
                        not_implemented = True
                    results.append(median)

            if not_implemented:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
                continue

            if results == test["expected"]:
                print(f"  ✓ PASSED: {results}")
                passed += 1
            else:
                print(f"  ✗ FAILED: Got {results}")
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
    test_median_finder()
