# Blind 75 - LeetCode Problems for Interview Prep

A comprehensive collection of 75 curated LeetCode problems covering essential data structures and algorithms patterns for coding interviews. This repository is designed for daily practice with structured learning paths and progress tracking.

## 📚 What is Blind 75?

The **Blind 75** is a curated list of 75 LeetCode problems originally compiled by a Facebook engineer. These problems cover the most important patterns and concepts needed to excel in coding interviews at top tech companies. The list focuses on:

- **Quality over quantity**: 75 carefully selected problems vs. thousands available
- **Pattern recognition**: Problems grouped by similar techniques and approaches
- **Interview relevance**: Frequently asked at FAANG and other top companies
- **Comprehensive coverage**: All major data structures and algorithm paradigms

## 🗂️ Repository Structure

```
blind-75/
├── README.md                     # This file
├── CLAUDE.md                     # Instructions for Claude Code
├── progress_tracker.py           # Interactive progress tracker
├── .gitignore                    # Python artifacts
│
├── arrays/                       # 10 problems
├── strings/                      # 10 problems
├── linked_lists/                 # 6 problems
├── trees/                        # 13 problems
├── graphs/                       # 8 problems
├── dynamic_programming/          # 11 problems
├── matrix/                       # 4 problems
├── intervals/                    # 6 problems
├── binary/                       # 5 problems
└── heap/                         # 2 problems
```

Each category folder contains:
- Individual problem files with stubs and test cases
- `README.md` explaining concepts, patterns, and tips

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd blind-75
```

### 2. View Your Progress Dashboard

```bash
python progress_tracker.py
```

This shows:
- Overall completion percentage
- Category-wise breakdown
- Current streak
- Recommended next problem

### 3. Start Solving Problems

Pick a problem from the dashboard or browse categories:

```bash
# View problems in a category
python progress_tracker.py --category arrays

# Mark a problem as started
python progress_tracker.py --start two_sum

# Open the problem file
code arrays/two_sum.py  # or use your preferred editor
```

### 4. Test Your Solution

Each problem file includes test cases. Run them with:

```bash
python arrays/two_sum.py
```

### 5. Mark as Complete

```bash
python progress_tracker.py --complete two_sum
```

## 📊 Progress Tracker Features

The interactive CLI tracker (`progress_tracker.py`) helps you stay organized:

```bash
# Show dashboard with statistics
python progress_tracker.py

# List all problems
python progress_tracker.py --list

# Filter by category
python progress_tracker.py --category trees

# Filter by status
python progress_tracker.py --status completed

# Mark problem as started
python progress_tracker.py --start problem_name

# Mark problem as completed
python progress_tracker.py --complete problem_name

# View detailed statistics
python progress_tracker.py --stats

# Reset progress (requires confirmation)
python progress_tracker.py --reset
```

**Features:**
- ✅ Track completion status (not started, in progress, completed)
- 📊 Visual progress bars for each category
- 🔥 Daily practice streak counter
- 💡 Smart problem recommendations
- 🎨 Color-coded terminal output
- 💾 Progress saved locally in `.progress.json`

## 🎯 Learning Paths

### Path 1: By Difficulty (Recommended for Beginners)

**Week 1-2: Easy Problems** (Build fundamentals)
1. Two Sum, Contains Duplicate, Valid Anagram
2. Valid Parentheses, Valid Palindrome
3. Reverse Linked List, Merge Two Sorted Lists
4. Invert Binary Tree, Maximum Depth, Same Tree
5. Best Time to Buy and Sell Stock, Climbing Stairs

**Week 3-5: Medium Problems** (Core interview prep)
- Focus on arrays, strings, and trees
- Move to graphs and dynamic programming
- Practice matrix and interval problems

**Week 6+: Hard Problems** (Advanced preparation)
- Merge K Sorted Lists
- Binary Tree Maximum Path Sum
- Serialize and Deserialize Binary Tree
- Find Median from Data Stream

### Path 2: By Category (Recommended for Focused Study)

**Week 1**: Arrays (10 problems)
**Week 2**: Strings (10 problems)
**Week 3**: Linked Lists (6) + Binary (5)
**Week 4**: Trees (13 problems)
**Week 5**: Graphs (8 problems) + Matrix (4)
**Week 6**: Dynamic Programming (11 problems)
**Week 7**: Intervals (6) + Heap (2) + Review

### Path 3: Interview Prep Sprint (4 weeks)

**Week 1**: Top patterns (Two Sum, Valid Parentheses, Merge Two Lists, Invert Tree, DFS/BFS basics)
**Week 2**: Medium difficulty across categories (breadth over depth)
**Week 3**: Dynamic programming and graph problems
**Week 4**: Hard problems + review weak areas

## 📋 Problem Categories

| Category | Count | Key Concepts |
|----------|-------|--------------|
| **Arrays** | 10 | Two pointers, sliding window, binary search |
| **Strings** | 10 | Hash maps, sliding window, palindromes |
| **Linked Lists** | 6 | Two pointers, reversal, fast/slow pointers |
| **Trees** | 13 | DFS, BFS, recursion, BST properties |
| **Graphs** | 8 | DFS, BFS, topological sort, union find |
| **Dynamic Programming** | 11 | Memoization, tabulation, state transitions |
| **Matrix** | 4 | 2D traversal, in-place operations |
| **Intervals** | 6 | Sorting, merging, greedy algorithms |
| **Binary** | 5 | Bit manipulation, XOR properties |
| **Heap** | 2 | Priority queue, top K problems |

## 💡 Study Tips

### General Strategy
1. **Understand before coding**: Read the problem carefully, identify the pattern
2. **Start simple**: Begin with brute force, then optimize
3. **Think out loud**: Practice explaining your approach
4. **Test thoroughly**: Include edge cases in your tests
5. **Review solutions**: Learn from optimal solutions even if you solved it
6. **Practice consistently**: Better to do 1 problem/day than 10 in one day

### Problem-Solving Framework
1. **Clarify**: Ask questions, understand constraints
2. **Examples**: Work through examples, identify patterns
3. **Approach**: Discuss multiple approaches and trade-offs
4. **Code**: Write clean, working code
5. **Test**: Run through test cases, including edge cases
6. **Optimize**: Analyze time/space complexity, improve if possible

### Interview Tips
- Communicate clearly throughout
- State assumptions explicitly
- Consider edge cases out loud
- Explain your thought process
- Don't be afraid to ask for hints
- Test your code before saying you're done

## 🔥 Maintaining Streaks

Build the habit of daily practice:
- Set a consistent time for solving problems
- Start with easier problems to build confidence
- Use the tracker to maintain motivation
- Join study groups or find an accountability partner
- Celebrate milestones (25%, 50%, 75%, 100%)

## 📖 Additional Resources

### Practice Platforms
- [LeetCode](https://leetcode.com/) - Original problem source
- [NeetCode](https://neetcode.io/) - Video explanations for Blind 75
- [AlgoExpert](https://www.algoexpert.io/) - Structured courses

### Learning Resources
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualgo](https://visualgo.net/) - Algorithm visualizations
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Detailed explanations

### Books
- *Cracking the Coding Interview* by Gayle Laakmann McDowell
- *Elements of Programming Interviews* by Adnan Aziz
- *Introduction to Algorithms* (CLRS) for deep dives

## 🤝 Contributing

While this repository contains problem stubs for practice:
1. Keep solutions private to yourself (don't commit them)
2. Feel free to add more test cases
3. Report issues or suggest improvements
4. Share your learning journey and tips

## 📝 File Structure

Each problem file follows this template:

```python
"""
Problem: [Name] (LeetCode #[number])
Difficulty: [Easy/Medium/Hard]
Category: [Category Name]

Description:
[Full problem description]

Examples:
[Input/output examples]

Constraints:
[Problem constraints]

Time Complexity Target: O(...)
Space Complexity Target: O(...)
"""

def solution_function(params):
    """
    TODO: Implement your solution here
    """
    pass

def test_solution():
    """Test cases"""
    # Test implementations
    pass

if __name__ == "__main__":
    test_solution()
```

## ⚙️ Configuration

Progress is stored in `.progress.json` (git-ignored). This file tracks:
- Problem completion status
- Last practice date
- Current streak
- Started date

To sync progress across machines, manually copy the `.progress.json` file.

## 🎓 Success Stories

Complete this challenge to:
- Build confidence for technical interviews
- Recognize common patterns quickly
- Improve problem-solving speed
- Master essential data structures and algorithms
- Develop a systematic approach to coding problems

## 📅 Timeline Suggestions

- **Intensive**: 2-3 problems/day = ~1 month
- **Moderate**: 1-2 problems/day = ~2 months
- **Relaxed**: 1 problem every 2 days = ~5 months
- **Long-term**: 2-3 problems/week = ~6 months

Choose based on your interview timeline and experience level.

## 🏆 Milestones

- ✨ **25% (19 problems)**: Foundation built
- 🌟 **50% (38 problems)**: Pattern recognition strong
- 💫 **75% (57 problems)**: Interview-ready
- 🎯 **100% (75 problems)**: Master level!

## 📞 Getting Help

- Read the category README.md for concepts and patterns
- Search LeetCode discussions for the specific problem
- Watch NeetCode video explanations
- Join coding communities (Reddit, Discord, etc.)
- Practice explaining solutions to others

## 📄 License

This repository is for educational purposes. Problems are from LeetCode.com. Please respect their terms of service.

---

**Ready to start?** Run `python progress_tracker.py` and begin your journey! 🚀

*Good luck with your interview preparation!* 💪