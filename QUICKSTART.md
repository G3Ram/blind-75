# Quick Start Guide

Welcome to your Blind 75 practice repository! Here's how to get started.

## 🚀 First Steps

### 1. View Your Dashboard
```bash
python progress_tracker.py
```

### 2. Pick Your First Problem
Start with the recommended problem (usually Two Sum):
```bash
# Mark it as started
python progress_tracker.py --start two_sum

# Open the file
code arrays/two_sum.py  # or vim, nano, etc.
```

### 3. Solve the Problem
- Read the problem description at the top of the file
- Implement the solution in the function stub
- The function currently just has `pass` - replace it with your solution

### 4. Test Your Solution
```bash
python arrays/two_sum.py
```

### 5. Mark as Complete
```bash
python progress_tracker.py --complete two_sum
```

## 📊 Useful Commands

```bash
# View dashboard
python progress_tracker.py

# List all problems
python progress_tracker.py --list

# View specific category
python progress_tracker.py --category arrays

# Filter by completion status
python progress_tracker.py --status completed
python progress_tracker.py --status in_progress
python progress_tracker.py --status not_started
```

## 📁 Repository Layout

```
blind-75/
├── arrays/              # 10 array problems
├── strings/             # 10 string problems
├── linked_lists/        # 6 linked list problems
├── trees/               # 13 tree problems
├── graphs/              # 8 graph problems
├── dynamic_programming/ # 11 DP problems
├── matrix/              # 4 matrix problems
├── intervals/           # 6 interval problems
├── binary/              # 5 bit manipulation problems
└── heap/                # 2 heap problems
```

## 💡 Tips

1. **Start Easy**: Begin with arrays and strings
2. **Be Consistent**: Solve 1-2 problems daily rather than 10 in one day
3. **Use the READMEs**: Each category folder has a README.md with patterns and tips
4. **Test Edge Cases**: Make sure to test empty inputs, single elements, etc.
5. **Track Progress**: Use the progress tracker to maintain motivation

## 🎯 Learning Path Suggestions

### Beginner Path (2 months)
- Week 1-2: Arrays (10) + Strings Easy problems
- Week 3: Strings (remaining) + Linked Lists (6)
- Week 4: Trees Easy (6 problems)
- Week 5: Trees Medium (7) + Binary (5)
- Week 6: Dynamic Programming Easy (3)
- Week 7: Graphs (8) + Matrix (4)
- Week 8: DP remaining + Intervals (6) + Heap (2)

### Intensive Path (1 month)
- Solve 2-3 problems per day
- Focus on Easy problems first, then Medium
- Save Hard problems for the final week

## 📖 Resources

- **Category READMEs**: Each folder has patterns and tips
- **Root README.md**: Complete guide with learning paths
- **CLAUDE.md**: Instructions for working with Claude Code

## 🎉 Getting Help

If a problem is tricky:
1. Read the category README for patterns
2. Try solving a simpler problem in the same category first
3. Look up the problem on LeetCode for hints
4. Watch NeetCode video explanations

---

**Ready to start?** Run `python progress_tracker.py` and pick your first problem! 🚀
