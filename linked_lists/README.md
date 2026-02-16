# Linked Lists

Linked lists are linear data structures where elements are stored in nodes, and each node points to the next. They're fundamental for understanding pointer manipulation and memory management.

## Key Concepts

- **Node Structure**: Each node contains data and a reference to the next node
- **Pointers**: Master pointer manipulation (slow/fast pointers, previous/current)
- **In-place Operations**: Modify the list without using extra space
- **Dummy Nodes**: Simplify edge cases by using a dummy head
- **Two Pointers**: Fast/slow pointers for cycle detection and middle finding

## Common Patterns

1. **Two Pointer (Slow/Fast)**: Find middle, detect cycles
2. **Reversal**: Reverse entire list or portions
3. **Merging**: Merge sorted lists
4. **Dummy Head**: Simplify operations on head node
5. **Runner Technique**: Use two pointers at different speeds

## Problems in This Category (6)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Reverse Linked List | Easy | Iterative/Recursive Reversal |
| Detect Cycle | Easy | Floyd's Cycle Detection |
| Merge Two Sorted Lists | Easy | Two Pointers |
| Merge K Sorted Lists | Hard | Min Heap or Divide & Conquer |
| Remove Nth Node From End of List | Medium | Two Pass or Two Pointers |
| Reorder List | Medium | Find Middle + Reverse + Merge |

## Tips

- Always check for null/None pointers before dereferencing
- Draw diagrams to visualize pointer changes
- Use dummy nodes to handle edge cases with the head
- Consider both iterative and recursive approaches
- Remember to update all necessary pointers when modifying links
- Fast/slow pointer technique is powerful for finding the middle
- Be careful with cycles - they can cause infinite loops

## Common Edge Cases

- Empty list (head is None)
- Single node list
- Two node list
- Lists with cycles
- Operations on the head node

## Resources

- [LeetCode Linked List Patterns](https://leetcode.com/tag/linked-list/)
- [Floyd's Cycle Detection](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare)
- [Linked List Visualization](https://visualgo.net/en/list)
