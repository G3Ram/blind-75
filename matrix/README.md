# Matrix

Matrix problems involve 2D arrays and require understanding of row/column operations, traversals, and transformations.

## Key Concepts

- **2D Array Indexing**: matrix[row][col]
- **In-place Modification**: Modify matrix without extra space
- **Matrix Traversal**: Row-wise, column-wise, diagonal, spiral
- **Coordinate Transformation**: Rotation, reflection, transposition
- **Boundary Tracking**: Track edges during spiral/boundary traversal

## Common Patterns

1. **Spiral Traversal**: Process elements in spiral order
2. **In-place Rotation**: Transform matrix using mathematical formulas
3. **DFS/BFS on Grid**: Treat matrix as graph
4. **Marking Visited**: Use matrix itself or separate visited array
5. **Layer-by-Layer Processing**: Process outer layers first

## Problems in This Category (4)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Set Matrix Zeroes | Medium | In-place Marking |
| Spiral Matrix | Medium | Boundary Tracking |
| Rotate Image | Medium | Transpose + Reverse |
| Word Search | Medium | DFS with Backtracking |

## Tips

- Draw small examples to visualize transformations
- For rotation: consider transpose + reverse operations
- Use markers in the matrix itself to save space
- Track boundaries (top, bottom, left, right) for spiral traversal
- For DFS/BFS: mark visited cells or use a visited set
- Watch out for index out of bounds errors
- Consider directions array: [(0,1), (1,0), (0,-1), (-1,0)]

## Common Operations

### Matrix Rotation (90° clockwise)
1. Transpose: matrix[i][j] ↔ matrix[j][i]
2. Reverse each row

### Spiral Traversal
- Track 4 boundaries: top, bottom, left, right
- Move right → down → left → up
- Shrink boundaries after each direction

### DFS on Grid
```python
directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
for dx, dy in directions:
    new_row, new_col = row + dx, col + dy
```

## Common Edge Cases

- Empty matrix
- 1×1 matrix
- Single row or single column
- Non-square matrices
- All elements are the same

## Resources

- [LeetCode Matrix Problems](https://leetcode.com/tag/matrix/)
- [Matrix Rotation Visualization](https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/)
- [Spiral Matrix Pattern](https://leetcode.com/problems/spiral-matrix/solution/)
