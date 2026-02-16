# Arrays

Arrays are fundamental data structures that store elements in contiguous memory locations. Understanding array manipulation is essential for solving many coding problems efficiently.

## Key Concepts

- **Two Pointers**: Use two pointers moving at different speeds or directions
- **Sliding Window**: Maintain a window of elements that satisfies certain conditions
- **Prefix Sum**: Precompute cumulative sums for quick range queries
- **Binary Search**: Find elements in O(log n) time in sorted arrays
- **Hash Tables**: Trade space for time to achieve O(1) lookups

## Common Patterns

1. **Two Sum Pattern**: Use hash table to find complements
2. **Kadane's Algorithm**: Maximum subarray problems
3. **Dutch National Flag**: Three-way partitioning
4. **Modified Binary Search**: Search in rotated/modified sorted arrays

## Problems in This Category (10)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Two Sum | Easy | Hash Table |
| Best Time to Buy and Sell Stock | Easy | One Pass |
| Contains Duplicate | Easy | Hash Set |
| Product of Array Except Self | Medium | Prefix/Suffix Products |
| Maximum Subarray | Medium | Kadane's Algorithm |
| Maximum Product Subarray | Medium | Dynamic Programming |
| Find Minimum in Rotated Sorted Array | Medium | Binary Search |
| Search in Rotated Sorted Array | Medium | Modified Binary Search |
| 3Sum | Medium | Two Pointers |
| Container With Most Water | Medium | Two Pointers |

## Tips

- Always consider edge cases: empty arrays, single elements, duplicates
- Think about time-space tradeoffs: can you use extra space for better time complexity?
- For sorted arrays, consider binary search or two-pointer techniques
- For unsorted arrays, consider hash tables or sorting first
- Watch out for integer overflow in product/sum problems

## Resources

- [LeetCode Array Patterns](https://leetcode.com/tag/array/)
- [Two Pointers Technique](https://leetcode.com/articles/two-pointer-technique/)
- [Sliding Window Pattern](https://leetcode.com/tag/sliding-window/)
