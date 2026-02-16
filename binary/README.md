# Binary (Bit Manipulation)

Bit manipulation involves working directly with binary representations of numbers using bitwise operators. These problems are often elegant and efficient.

## Key Concepts

- **Bitwise Operators**: AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>)
- **Bit Masking**: Use masks to manipulate specific bits
- **Two's Complement**: Negative number representation
- **Properties of XOR**: a ^ a = 0, a ^ 0 = a, commutative and associative
- **Bit Counting**: Count set bits (1s) in a number

## Common Patterns

1. **XOR Properties**: Find unique elements, detect differences
2. **Bit Masking**: Set, clear, or check specific bits
3. **Power of Two**: Check using n & (n-1) == 0
4. **Counting Bits**: Brian Kernighan's algorithm
5. **Bit Shifts**: Multiply/divide by powers of 2

## Problems in This Category (5)

| Problem | Difficulty | Key Technique |
|---------|-----------|---------------|
| Sum of Two Integers | Medium | Bitwise Addition (XOR + AND) |
| Number of 1 Bits | Easy | Brian Kernighan's Algorithm |
| Counting Bits | Easy | DP with Bit Pattern |
| Missing Number | Easy | XOR or Math |
| Reverse Bits | Easy | Bit Manipulation |

## Tips

- XOR is your friend for finding unique/missing elements
- Use bit shifts for efficient multiplication/division by 2
- n & (n-1) clears the lowest set bit
- n & 1 checks if number is odd
- Practice converting between decimal and binary
- Watch for integer overflow (especially in Java/C++)
- Python handles arbitrary precision integers automatically
- Use bin() in Python to see binary representation

## Bitwise Operations Cheat Sheet

### Basic Operations
```python
# Check if bit i is set
is_set = (n & (1 << i)) != 0

# Set bit i
n |= (1 << i)

# Clear bit i
n &= ~(1 << i)

# Toggle bit i
n ^= (1 << i)

# Get lowest set bit
lowest = n & (-n)

# Clear lowest set bit
n &= (n - 1)
```

### XOR Properties
```python
a ^ a = 0       # Number XOR itself is 0
a ^ 0 = a       # Number XOR 0 is itself
a ^ b ^ a = b   # XOR is associative and commutative
```

### Useful Bit Patterns
- Power of 2: `n & (n-1) == 0` (and n != 0)
- Even number: `n & 1 == 0`
- Odd number: `n & 1 == 1`
- Multiply by 2: `n << 1`
- Divide by 2: `n >> 1`
- Negate: `~n + 1` (two's complement)

## Common Tricks

### Count Set Bits (Brian Kernighan)
```python
count = 0
while n:
    n &= (n - 1)  # Clear lowest set bit
    count += 1
```

### Check Power of Two
```python
return n > 0 and (n & (n - 1)) == 0
```

### Find Single Unique Number
```python
result = 0
for num in nums:
    result ^= num  # All pairs cancel out
return result
```

## Common Edge Cases

- Zero (0)
- Negative numbers (two's complement)
- Integer overflow/underflow
- All bits set (e.g., -1 in two's complement)
- Powers of 2

## Resources

- [LeetCode Bit Manipulation](https://leetcode.com/tag/bit-manipulation/)
- [Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html)
- [Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement)
