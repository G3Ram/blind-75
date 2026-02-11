"""
Problem: Clone Graph (LeetCode #133)
Difficulty: Medium
Category: Graphs

Description:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node contains a value and a list of neighbors.

Examples:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Constraints:
- The number of nodes is in range [0, 100]
- 1 <= Node.val <= 100
- Node.val is unique
- No repeated edges and no self-loops

Time Complexity Target: O(N+E)
Space Complexity Target: O(N)
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    TODO: Implement your solution here

    Args:
        node: Reference to a node in a connected undirected graph

    Returns:
        Deep copy of the graph (reference to the cloned node)
    """
    pass


# Helper functions for testing
def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    """Build graph from adjacency list (1-indexed node values)."""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    """Convert graph back to adjacency list (sorted, 1-indexed)."""
    if not node:
        return []
    visited = {}
    queue = [node]
    while queue:
        curr = queue.pop(0)
        if curr.val not in visited:
            visited[curr.val] = sorted(n.val for n in curr.neighbors)
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
    return [visited[i] for i in sorted(visited)]


def graphs_are_independent(original: Optional[Node], clone: Optional[Node]) -> bool:
    """Verify clone shares no node objects with original."""
    if original is None and clone is None:
        return True
    orig_nodes = set()
    queue = [original]
    while queue:
        curr = queue.pop(0)
        if id(curr) not in orig_nodes:
            orig_nodes.add(id(curr))
            queue.extend(curr.neighbors)
    clone_queue = [clone]
    while clone_queue:
        curr = clone_queue.pop(0)
        if id(curr) in orig_nodes:
            return False
        clone_queue.extend(curr.neighbors)
    return True


# Test Cases
def test_clone_graph():
    """Test cases for clone_graph"""

    test_cases = [
        {
            "name": "Test case 1: four-node cycle graph",
            "adj_list": [[2, 4], [1, 3], [2, 4], [1, 3]],
            "expected_adj": [[2, 4], [1, 3], [2, 4], [1, 3]]
        },
        {
            "name": "Test case 2: two-node graph",
            "adj_list": [[2], [1]],
            "expected_adj": [[2], [1]]
        },
        {
            "name": "Test case 3: three-node fully connected",
            "adj_list": [[2, 3], [1, 3], [1, 2]],
            "expected_adj": [[2, 3], [1, 3], [1, 2]]
        },
        {
            "name": "Edge case: single node no neighbors",
            "adj_list": [[]],
            "expected_adj": [[]]
        },
        {
            "name": "Edge case: empty graph (null node)",
            "adj_list": [],
            "expected_adj": []
        },
        {
            "name": "Edge case: linear chain",
            "adj_list": [[2], [1, 3], [2]],
            "expected_adj": [[2], [1, 3], [2]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input adj_list: {test['adj_list']}")
        print(f"  Expected adj_list: {test['expected_adj']}")

        try:
            original = build_graph(test['adj_list'])
            result = clone_graph(original)

            if result is None and test['expected_adj']:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            elif result is None and not test['expected_adj']:
                # Empty graph case - None is correct
                print(f"  ✓ PASSED: None (empty graph)")
                passed += 1
            else:
                result_adj = graph_to_adj_list(result)
                if result_adj == test['expected_adj']:
                    if graphs_are_independent(original, result):
                        print(f"  ✓ PASSED: {result_adj} (deep copy verified)")
                        passed += 1
                    else:
                        print(f"  ✗ FAILED: Adjacency matches but not a deep copy (shared nodes)")
                        failed += 1
                else:
                    print(f"  ✗ FAILED: Got {result_adj}")
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
    test_clone_graph()
