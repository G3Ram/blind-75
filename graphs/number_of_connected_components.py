"""
Problem: Number of Connected Components in an Undirected Graph (LeetCode #323)
Difficulty: Medium
Category: Graphs

Description:
Given n nodes labeled from 0 to n-1 and a list of undirected edges, return the number of connected components in the graph.

Examples:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2

Time Complexity Target: O(V+E)
Space Complexity Target: O(V)
"""

from typing import List


def number_of_connected_components(n: int, edges: List[List[int]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: Number of nodes labeled from 0 to n-1
        edges: List of undirected edges [u, v]

    Returns:
        Number of connected components in the graph
    """
    pass


# Test Cases
def test_number_of_connected_components():
    """Test cases for number_of_connected_components"""

    test_cases = [
        {
            "name": "Test case 1: two connected components",
            "input": {"n": 5, "edges": [[0, 1], [1, 2], [3, 4]]},
            "expected": 2
        },
        {
            "name": "Test case 2: all nodes connected in one component",
            "input": {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [3, 4]]},
            "expected": 1
        },
        {
            "name": "Test case 3: two pairs plus one isolated node",
            "input": {"n": 5, "edges": [[0, 2], [1, 3]]},
            "expected": 3
        },
        {
            "name": "Edge case: single node no edges",
            "input": {"n": 1, "edges": []},
            "expected": 1
        },
        {
            "name": "Edge case: all isolated nodes",
            "input": {"n": 4, "edges": []},
            "expected": 4
        },
        {
            "name": "Edge case: two nodes one edge",
            "input": {"n": 2, "edges": [[0, 1]]},
            "expected": 1
        },
        {
            "name": "Edge case: two nodes no edges",
            "input": {"n": 2, "edges": []},
            "expected": 2
        },
        {
            "name": "Edge case: star graph (all connected to center)",
            "input": {"n": 5, "edges": [[0, 1], [0, 2], [0, 3], [0, 4]]},
            "expected": 1
        },
        {
            "name": "Edge case: three separate pairs",
            "input": {"n": 6, "edges": [[0, 1], [2, 3], [4, 5]]},
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  n: {test['input']['n']}")
        print(f"  edges: {test['input']['edges']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = number_of_connected_components(
                test['input']['n'],
                test['input']['edges']
            )

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if result == test['expected']:
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
    test_number_of_connected_components()
