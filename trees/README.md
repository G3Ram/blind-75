# Trees

Binary trees are hierarchical data structures where each node has at most two children. They're essential for many algorithms and data structure implementations.

## Key Concepts

- **Tree Traversal**: Inorder, preorder, postorder, level-order
- **Recursion**: Most tree problems have elegant recursive solutions
- **Binary Search Tree (BST)**: Left subtree < node < right subtree
- **Tree Height**: Maximum depth from root to leaf
- **Balanced Trees**: Height difference between subtrees is limited

## Common Patterns

1. **DFS (Depth-First Search)**: Recursive exploration of paths
2. **BFS (Breadth-First Search)**: Level-order traversal using queue
3. **Divide and Conquer**: Process left and right subtrees separately
4. **Path Sum Problems**: Track values along root-to-leaf paths
5. **Tree Construction**: Build trees from traversal arrays
6. **Tree Serialization**: Convert tree to/from string representation

## Problems in This Category (13)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Invert Binary Tree | Easy | DFS Recursion |
| Maximum Depth of Binary Tree | Easy | DFS/BFS |
| Same Tree | Easy | DFS Comparison |
| Subtree of Another Tree | Easy | DFS with Tree Comparison |
| Lowest Common Ancestor of BST | Easy | BST Properties |
| Validate Binary Search Tree | Medium | DFS with Range Checking |
| Kth Smallest Element in BST | Medium | Inorder Traversal |
| Binary Tree Level Order Traversal | Medium | BFS with Queue |
| Construct Binary Tree from Traversals | Medium | Recursion with Index Mapping |
| Serialize and Deserialize Binary Tree | Hard | BFS/DFS Encoding |
| Binary Tree Maximum Path Sum | Hard | DFS with Global Maximum |
| Implement Trie | Medium | Tree Structure |
| Add and Search Word | Medium | Trie + DFS with Wildcards |

## Tips

- Base case for recursion: typically when node is None
- For BST problems, leverage the ordering property
- Level-order traversal needs a queue (BFS)
- Depth-first problems often use recursion (DFS)
- Consider both top-down and bottom-up approaches
- Helper functions with extra parameters are often useful
- Track information in return values or global variables
- Draw small examples to visualize the problem

## Common Edge Cases

- Empty tree (root is None)
- Single node tree
- Unbalanced tree (essentially a linked list)
- All nodes in left or right subtree
- Negative values
- Duplicate values

## Tree Traversals

```
    1
   / \
  2   3
 / \
4   5
```

- **Preorder** (Root, Left, Right): 1, 2, 4, 5, 3
- **Inorder** (Left, Root, Right): 4, 2, 5, 1, 3
- **Postorder** (Left, Right, Root): 4, 5, 2, 3, 1
- **Level-order** (BFS): 1, 2, 3, 4, 5

## Resources

- [LeetCode Tree Patterns](https://leetcode.com/tag/tree/)
- [Binary Tree Visualization](https://visualgo.net/en/bst)
- [Tree Traversal Methods](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
