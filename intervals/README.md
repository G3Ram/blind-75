# Intervals

Interval problems involve working with ranges [start, end] and often require sorting, merging, or finding overlaps.

## Key Concepts

- **Interval Representation**: [start, end] or (start, end)
- **Sorting**: Usually sort by start time (sometimes by end time)
- **Overlap Detection**: Check if intervals intersect
- **Merging**: Combine overlapping intervals
- **Greedy Algorithms**: Make locally optimal choices

## Common Patterns

1. **Sort and Merge**: Sort intervals, then merge overlapping ones
2. **Sweep Line**: Process start and end points separately
3. **Interval Scheduling**: Greedy selection of non-overlapping intervals
4. **Priority Queue**: Track active intervals with min/max heap
5. **Binary Search**: Find insertion position or search in sorted intervals

## Problems in This Category (6)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Insert Interval | Medium | Linear Scan with Merge |
| Merge Intervals | Medium | Sort + Linear Scan |
| Non-overlapping Intervals | Medium | Greedy (Sort by End Time) |
| Meeting Rooms | Easy | Sort + Check Overlap |
| Meeting Rooms II | Medium | Min Heap or Sweep Line |
| Minimum Interval to Include Each Query | Hard | Sort + Priority Queue |

## Tips

- Always consider sorting first (usually by start time)
- Two intervals [a,b] and [c,d] overlap if: max(a,c) < min(b,d)
- For merging: compare current interval's start with previous interval's end
- Greedy approach often works for interval scheduling
- Use min heap to track earliest ending meetings
- Consider both open and closed interval interpretations
- Draw timeline diagrams to visualize overlaps

## Overlap Detection

Two intervals [a, b] and [c, d] overlap if:
```python
max(a, c) < min(b, d)
# OR equivalently:
a < d and c < b
```

## Merging Intervals

```python
if current.start <= last.end:
    # Overlapping - merge
    last.end = max(last.end, current.end)
else:
    # Non-overlapping - add new interval
    result.append(current)
```

## Common Edge Cases

- Empty intervals list
- Single interval
- All intervals overlap
- No intervals overlap
- Point intervals [x, x]
- Intervals with same start/end times

## Sorting Strategies

- **By start time**: Most common, for merging and insertion
- **By end time**: For interval scheduling (maximize non-overlapping)
- **By duration**: For specific optimization problems

## Resources

- [LeetCode Interval Problems](https://leetcode.com/tag/intervals/)
- [Interval Scheduling](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)
- [Sweep Line Algorithm](https://www.geeksforgeeks.org/interval-tree/)
