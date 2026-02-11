"""
Problem: Course Schedule (LeetCode #207)
Difficulty: Medium
Category: Graphs

Description:
Given numCourses and a list of prerequisites where prerequisites[i] = [ai, bi] indicates you must take course bi first to take course ai, return true if you can finish all courses.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: Take course 0, then course 1

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- All pairs are unique

Time Complexity Target: O(V+E)
Space Complexity Target: O(V+E)
"""

from typing import List


def course_schedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        numCourses: Total number of courses (labeled 0 to numCourses-1)
        prerequisites: List of [ai, bi] pairs meaning course bi must be taken before ai

    Returns:
        True if it is possible to finish all courses, False otherwise
    """
    pass


# Test Cases
def test_course_schedule():
    """Test cases for course_schedule"""

    test_cases = [
        {
            "name": "Test case 1: simple dependency, no cycle",
            "input": {"numCourses": 2, "prerequisites": [[1, 0]]},
            "expected": True
        },
        {
            "name": "Test case 2: direct cycle",
            "input": {"numCourses": 2, "prerequisites": [[1, 0], [0, 1]]},
            "expected": False
        },
        {
            "name": "Test case 3: chain of dependencies",
            "input": {"numCourses": 3, "prerequisites": [[1, 0], [2, 1]]},
            "expected": True
        },
        {
            "name": "Test case 4: indirect cycle",
            "input": {"numCourses": 4, "prerequisites": [[1, 0], [2, 1], [3, 2], [1, 3]]},
            "expected": False
        },
        {
            "name": "Edge case: single course no prerequisites",
            "input": {"numCourses": 1, "prerequisites": []},
            "expected": True
        },
        {
            "name": "Edge case: multiple courses no prerequisites",
            "input": {"numCourses": 5, "prerequisites": []},
            "expected": True
        },
        {
            "name": "Edge case: self-loop",
            "input": {"numCourses": 2, "prerequisites": [[0, 0]]},
            "expected": False
        },
        {
            "name": "Edge case: two disconnected components, both valid",
            "input": {"numCourses": 4, "prerequisites": [[1, 0], [3, 2]]},
            "expected": True
        },
        {
            "name": "Edge case: two components, one has cycle",
            "input": {"numCourses": 4, "prerequisites": [[1, 0], [2, 3], [3, 2]]},
            "expected": False
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  numCourses: {test['input']['numCourses']}")
        print(f"  prerequisites: {test['input']['prerequisites']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = course_schedule(
                test['input']['numCourses'],
                test['input']['prerequisites']
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
    test_course_schedule()
