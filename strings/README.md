# Strings

String manipulation problems are common in coding interviews. They often involve pattern matching, character frequency analysis, and substring operations.

## Key Concepts

- **Character Frequency**: Count character occurrences using hash maps
- **Sliding Window**: Maintain a window for substring problems
- **Two Pointers**: Compare or manipulate strings from both ends
- **Palindrome Checking**: Expand around center or two-pointer approach
- **String Matching**: Pattern matching algorithms (KMP, Rabin-Karp)

## Common Patterns

1. **Anagram Problems**: Use character frequency maps or sorted strings
2. **Palindrome Detection**: Expand around center or dynamic programming
3. **Substring Search**: Sliding window with hash map
4. **Parentheses Matching**: Stack-based validation
5. **String Building**: Use StringBuilder/list for efficiency

## Problems in This Category (10)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Valid Anagram | Easy | Hash Map |
| Group Anagrams | Medium | Hash Map with Sorted Key |
| Valid Parentheses | Easy | Stack |
| Longest Substring Without Repeating Characters | Medium | Sliding Window + Hash Set |
| Longest Repeating Character Replacement | Medium | Sliding Window |
| Minimum Window Substring | Hard | Sliding Window + Hash Map |
| Palindromic Substrings | Medium | Expand Around Center |
| Encode and Decode Strings | Medium | Length Encoding |
| Valid Palindrome | Easy | Two Pointers |
| Longest Palindromic Substring | Medium | Expand Around Center |

## Tips

- Strings are immutable in Python - use lists for building strings
- Consider ASCII vs Unicode when working with character arrays
- Empty strings and single characters are common edge cases
- For palindrome problems, consider both odd and even length palindromes
- Sliding window is your friend for substring problems
- Stack is perfect for matching/validating paired characters

## Resources

- [LeetCode String Patterns](https://leetcode.com/tag/string/)
- [Sliding Window Technique](https://leetcode.com/tag/sliding-window/)
- [KMP Algorithm](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)
