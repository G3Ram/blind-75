# Graphs

Graphs are non-linear data structures consisting of vertices (nodes) and edges (connections). They model relationships and are used in many real-world applications.

## Key Concepts

- **Graph Representation**: Adjacency list, adjacency matrix, edge list
- **DFS (Depth-First Search)**: Explore as far as possible before backtracking
- **BFS (Breadth-First Search)**: Explore level by level
- **Cycle Detection**: Find cycles using visited tracking
- **Topological Sort**: Linear ordering of vertices in a DAG
- **Union Find**: Track connected components efficiently

## Common Patterns

1. **DFS for Connectivity**: Find connected components, detect cycles
2. **BFS for Shortest Path**: Unweighted shortest path problems
3. **Topological Sort**: Course scheduling, dependency resolution
4. **Union Find**: Dynamic connectivity, MST algorithms
5. **Graph Coloring**: Bipartite checking, conflict detection

## Problems in This Category (8)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Number of Islands | Medium | DFS/BFS Grid Traversal |
| Clone Graph | Medium | DFS/BFS with Hash Map |
| Pacific Atlantic Water Flow | Medium | DFS from Boundaries |
| Course Schedule | Medium | Topological Sort (Cycle Detection) |
| Longest Consecutive Sequence | Medium | Union Find or Hash Set |
| Alien Dictionary | Hard | Topological Sort |
| Graph Valid Tree | Medium | DFS/BFS + Cycle Detection |
| Number of Connected Components | Medium | DFS/BFS or Union Find |

## Tips

- Always track visited nodes to avoid infinite loops
- Choose representation based on graph density (sparse vs dense)
- DFS uses stack (recursion), BFS uses queue
- For cycle detection in directed graphs, track "currently visiting"
- Topological sort only works on DAGs (Directed Acyclic Graphs)
- Grid problems are often graph problems in disguise
- Consider both recursive and iterative implementations
- Union Find is perfect for dynamic connectivity

## Graph Representations

**Adjacency List** (preferred for sparse graphs):
```python
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}
```

**Adjacency Matrix** (good for dense graphs):
```python
matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
```

## Common Edge Cases

- Empty graph
- Single node
- Disconnected components
- Self-loops
- Cycles
- Directed vs undirected graphs

## DFS vs BFS

**Use DFS when:**
- Finding any path
- Detecting cycles
- Topological sorting
- Finding connected components

**Use BFS when:**
- Finding shortest path (unweighted)
- Level-order processing
- Finding all nodes at distance k

## Resources

- [LeetCode Graph Patterns](https://leetcode.com/tag/graph/)
- [Graph Algorithms Visualization](https://visualgo.net/en/dfsbfs)
- [Union Find Explained](https://www.geeksforgeeks.org/union-find/)
