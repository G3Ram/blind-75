# Heap (Priority Queue)

Heaps are tree-based data structures that maintain a partial ordering, allowing efficient access to the minimum (min-heap) or maximum (max-heap) element.

## Key Concepts

- **Min Heap**: Parent ≤ children (root is minimum)
- **Max Heap**: Parent ≥ children (root is maximum)
- **Priority Queue**: Abstract data type implemented using heaps
- **Heapify**: Convert array to heap in O(n) time
- **Time Complexity**: Insert O(log n), Extract-Min/Max O(log n), Peek O(1)

## Common Patterns

1. **Top K Elements**: Use min-heap of size K
2. **Kth Largest/Smallest**: Maintain heap of K elements
3. **Running Median**: Two heaps (max-heap and min-heap)
4. **Merge K Sorted**: Use heap to track smallest from each list
5. **Frequency Problems**: Combine with hash map for counting

## Problems in This Category (2)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Top K Frequent Elements | Medium | Hash Map + Min Heap |
| Find Median from Data Stream | Hard | Two Heaps (Max + Min) |

## Tips

- Python's heapq module implements min-heap by default
- For max-heap in Python: negate values or use (-value, item) tuples
- Heaps are perfect for "top K" or "Kth largest/smallest" problems
- Two-heap pattern (max-heap + min-heap) for running median
- Consider heap when you need repeated min/max operations
- Building a heap from array is O(n), not O(n log n)
- Heaps don't support efficient search or arbitrary deletion

## Python heapq Operations

```python
import heapq

# Create heap from list
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)  # O(n)

# Push element
heapq.heappush(heap, 2)  # O(log n)

# Pop smallest element
smallest = heapq.heappop(heap)  # O(log n)

# Peek at smallest (without removing)
smallest = heap[0]  # O(1)

# Push and pop in one operation
heapq.heappushpop(heap, 6)  # O(log n)

# Get K largest/smallest
largest_k = heapq.nlargest(k, heap)  # O(n log k)
smallest_k = heapq.nsmallest(k, heap)  # O(n log k)
```

## Max Heap in Python

Since Python only has min-heap, create max-heap by negating values:

```python
# Max heap using negation
max_heap = []
heapq.heappush(max_heap, -value)  # Negate on push
max_value = -heapq.heappop(max_heap)  # Negate on pop

# Or use tuples with negated priority
heapq.heappush(max_heap, (-priority, item))
```

## Two Heap Pattern (Running Median)

Maintain two heaps:
- **Max heap** (lower half): Stores smaller half of numbers
- **Min heap** (upper half): Stores larger half of numbers

**Invariants:**
1. Size difference ≤ 1
2. All elements in max-heap ≤ all elements in min-heap

**Median:**
- If equal size: average of both tops
- If different size: top of larger heap

## Top K Pattern

For finding top K frequent elements:
1. Count frequencies using hash map
2. Use min-heap of size K
3. For each element:
   - If heap size < K: add to heap
   - Else if frequency > heap top: remove top, add current
4. Final heap contains top K elements

## Common Edge Cases

- Empty heap
- Single element
- All elements equal
- K = 1 or K = n
- Negative numbers
- Duplicate values

## When to Use Heaps

**Good for:**
- Finding top K elements
- Merging sorted sequences
- Running median/statistics
- Scheduling/priority systems

**Not good for:**
- Searching for arbitrary elements
- Need to maintain sorted order of all elements
- Frequent arbitrary deletions

## Resources

- [LeetCode Heap Problems](https://leetcode.com/tag/heap-priority-queue/)
- [Heap Data Structure](https://en.wikipedia.org/wiki/Heap_(data_structure))
- [Python heapq Documentation](https://docs.python.org/3/library/heapq.html)
