# Dynamic Programming

Dynamic Programming (DP) is an optimization technique that solves complex problems by breaking them into simpler subproblems and storing results to avoid redundant calculations.

## Key Concepts

- **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
- **Overlapping Subproblems**: Same subproblems are solved multiple times
- **Memoization**: Top-down approach with caching (recursion + memo)
- **Tabulation**: Bottom-up approach with table (iterative)
- **State Transition**: Relationship between current and previous states

## Common Patterns

1. **1D DP**: Single array, depends on previous elements (Fibonacci, climbing stairs)
2. **2D DP**: Matrix, depends on previous rows/columns (edit distance, LCS)
3. **Knapsack**: Include/exclude decisions (0/1 knapsack, subset sum)
4. **Path Problems**: Count/find paths in grid or sequence
5. **String DP**: Palindromes, subsequences, pattern matching
6. **Stock Problems**: State machine with buy/sell/cooldown states

## Problems in This Category (11)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Climbing Stairs | Easy | 1D DP (Fibonacci) |
| House Robber | Medium | 1D DP (Include/Exclude) |
| House Robber II | Medium | Circular Array DP |
| Coin Change | Medium | Unbounded Knapsack |
| Coin Change II | Medium | Combination Sum DP |
| Longest Increasing Subsequence | Medium | 1D DP or Binary Search |
| Combination Sum IV | Medium | Order Matters DP |
| Decode Ways | Medium | 1D DP with Decision Tree |
| Unique Paths | Medium | 2D Grid DP |
| Jump Game | Medium | Greedy or DP |
| Word Break | Medium | 1D DP with Dictionary |

## Tips

- Identify if problem has optimal substructure and overlapping subproblems
- Start with brute force recursive solution
- Add memoization to recursive solution (top-down DP)
- Convert to iterative tabulation (bottom-up DP)
- Optimize space by keeping only necessary previous states
- Define state clearly: what information do you need?
- Write the recurrence relation before coding
- Consider base cases carefully
- Test with small examples first

## DP Problem-Solving Steps

1. **Define the state**: What does dp[i] represent?
2. **Find the recurrence**: How does dp[i] relate to previous states?
3. **Initialize base cases**: What are dp[0], dp[1], etc.?
4. **Determine iteration order**: Bottom-up or top-down?
5. **Optimize space**: Can you use O(1) or O(n) instead of O(n²)?

## Common DP Patterns

### 1D Array DP
```python
dp[i] = function(dp[i-1], dp[i-2], ...)
```

### 2D Grid DP
```python
dp[i][j] = function(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

### Knapsack DP
```python
dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
```

## Space Optimization

- 1D DP with constant space: Keep only last few values
- 2D DP to 1D: Use rolling array (keep only previous row)
- In-place DP: Modify input array if allowed

## Resources

- [LeetCode DP Patterns](https://leetcode.com/tag/dynamic-programming/)
- [DP for Beginners](https://www.geeksforgeeks.org/dynamic-programming/)
- [Common DP Patterns](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
