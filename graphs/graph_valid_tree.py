"""
Problem: Graph Valid Tree (LeetCode #261)
Difficulty: Medium
Category: Graphs

Description:
Given n nodes labeled from 0 to n-1 and a list of undirected edges, check if these edges form a valid tree.

Examples:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2

Time Complexity Target: O(V+E)
Space Complexity Target: O(V+E)
"""

from typing import List


def graph_valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        n: Number of nodes labeled from 0 to n-1
        edges: List of undirected edges [u, v]

    Returns:
        True if the edges form a valid tree, False otherwise
    """
    pass


# Test Cases
def test_graph_valid_tree():
    """Test cases for graph_valid_tree"""

    test_cases = [
        {
            "name": "Test case 1: valid tree (star shape)",
            "input": {"n": 5, "edges": [[0, 1], [0, 2], [0, 3], [1, 4]]},
            "expected": True
        },
        {
            "name": "Test case 2: cycle present",
            "input": {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]},
            "expected": False
        },
        {
            "name": "Test case 3: valid tree (chain)",
            "input": {"n": 3, "edges": [[0, 1], [0, 2]]},
            "expected": True
        },
        {
            "name": "Test case 4: disconnected graph",
            "input": {"n": 4, "edges": [[0, 1], [2, 3]]},
            "expected": False
        },
        {
            "name": "Edge case: single node no edges",
            "input": {"n": 1, "edges": []},
            "expected": True
        },
        {
            "name": "Edge case: two nodes one edge",
            "input": {"n": 2, "edges": [[0, 1]]},
            "expected": True
        },
        {
            "name": "Edge case: two nodes no edges (disconnected)",
            "input": {"n": 2, "edges": []},
            "expected": False
        },
        {
            "name": "Edge case: extra edge causes cycle",
            "input": {"n": 3, "edges": [[0, 1], [1, 2], [0, 2]]},
            "expected": False
        },
        {
            "name": "Edge case: five nodes fully connected chain",
            "input": {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [3, 4]]},
            "expected": True
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
            result = graph_valid_tree(
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
    test_graph_valid_tree()
