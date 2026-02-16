#!/usr/bin/env python3
"""
Script to generate all 75 Blind 75 problem files
"""

from pathlib import Path

# Problem metadata: (file_name, problem_name, leetcode_number, difficulty, description, examples, constraints, time_complexity, space_complexity)
PROBLEM_DATA = {
    "arrays": [
        ("two_sum", "Two Sum", "1", "Easy",
         "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
         [("nums = [2,7,11,15], target = 9", "[0,1]", "nums[0] + nums[1] == 9")],
         ["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "Only one valid answer exists"],
         "O(n)", "O(n)"),

        ("best_time_to_buy_and_sell_stock", "Best Time to Buy and Sell Stock", "121", "Easy",
         "You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize profit by choosing a single day to buy and one day in the future to sell. Return the maximum profit, or 0 if no profit.",
         [("prices = [7,1,5,3,6,4]", "5", "Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5")],
         ["1 <= prices.length <= 10^5", "0 <= prices[i] <= 10^4"],
         "O(n)", "O(1)"),

        ("contains_duplicate", "Contains Duplicate", "217", "Easy",
         "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
         [("nums = [1,2,3,1]", "true", ""), ("nums = [1,2,3,4]", "false", "")],
         ["1 <= nums.length <= 10^5", "-10^9 <= nums[i] <= 10^9"],
         "O(n)", "O(n)"),

        ("product_of_array_except_self", "Product of Array Except Self", "238", "Medium",
         "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements of nums except nums[i]. Must run in O(n) time without using division.",
         [("nums = [1,2,3,4]", "[24,12,8,6]", "")],
         ["2 <= nums.length <= 10^5", "-30 <= nums[i] <= 30", "Product fits in 32-bit integer", "Must be O(n) without division"],
         "O(n)", "O(1)"),

        ("maximum_subarray", "Maximum Subarray", "53", "Medium",
         "Given an integer array nums, find the subarray with the largest sum, and return its sum.",
         [("nums = [-2,1,-3,4,-1,2,1,-5,4]", "6", "Subarray [4,-1,2,1] has the largest sum 6")],
         ["1 <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4"],
         "O(n)", "O(1)"),

        ("maximum_product_subarray", "Maximum Product Subarray", "152", "Medium",
         "Given an integer array nums, find a subarray that has the largest product, and return the product.",
         [("nums = [2,3,-2,4]", "6", "Subarray [2,3] has product 6")],
         ["1 <= nums.length <= 2*10^4", "-10 <= nums[i] <= 10"],
         "O(n)", "O(1)"),

        ("find_minimum_in_rotated_sorted_array", "Find Minimum in Rotated Sorted Array", "153", "Medium",
         "Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the rotated array, return the minimum element. Must run in O(log n) time.",
         [("nums = [3,4,5,1,2]", "1", ""), ("nums = [4,5,6,7,0,1,2]", "0", "")],
         ["n == nums.length", "1 <= n <= 5000", "-5000 <= nums[i] <= 5000", "All integers are unique"],
         "O(log n)", "O(1)"),

        ("search_in_rotated_sorted_array", "Search in Rotated Sorted Array", "33", "Medium",
         "Given the array nums after rotation and an integer target, return the index of target if it is in nums, or -1 if not. Must achieve O(log n) runtime.",
         [("nums = [4,5,6,7,0,1,2], target = 0", "4", "")],
         ["1 <= nums.length <= 5000", "-10^4 <= nums[i] <= 10^4", "All values are unique"],
         "O(log n)", "O(1)"),

        ("3sum", "3Sum", "15", "Medium",
         "Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that i != j != k and nums[i] + nums[j] + nums[k] == 0.",
         [("nums = [-1,0,1,2,-1,-4]", "[[-1,-1,2],[-1,0,1]]", "")],
         ["3 <= nums.length <= 3000", "-10^5 <= nums[i] <= 10^5"],
         "O(n²)", "O(n)"),

        ("container_with_most_water", "Container With Most Water", "11", "Medium",
         "Given n non-negative integers representing vertical lines on a chart, find two lines that together with the x-axis form a container with the most water.",
         [("height = [1,8,6,2,5,4,8,3,7]", "49", "")],
         ["n == height.length", "2 <= n <= 10^5", "0 <= height[i] <= 10^4"],
         "O(n)", "O(1)"),
    ],

    "strings": [
        ("valid_anagram", "Valid Anagram", "242", "Easy",
         "Given two strings s and t, return true if t is an anagram of s, and false otherwise.",
         [("s = 'anagram', t = 'nagaram'", "true", ""), ("s = 'rat', t = 'car'", "false", "")],
         ["1 <= s.length, t.length <= 5*10^4", "s and t consist of lowercase English letters"],
         "O(n)", "O(1)"),

        ("group_anagrams", "Group Anagrams", "49", "Medium",
         "Given an array of strings strs, group the anagrams together. Return the groups in any order.",
         [("strs = ['eat','tea','tan','ate','nat','bat']", "[['bat'],['nat','tan'],['ate','eat','tea']]", "")],
         ["1 <= strs.length <= 10^4", "0 <= strs[i].length <= 100", "strs[i] consists of lowercase English letters"],
         "O(n*k)", "O(n*k)"),

        ("valid_parentheses", "Valid Parentheses", "20", "Easy",
         "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. Brackets must close in the correct order.",
         [("s = '()'", "true", ""), ("s = '()[]{}'", "true", ""), ("s = '(]'", "false", "")],
         ["1 <= s.length <= 10^4", "s consists of parentheses only '()[]{}'"],
         "O(n)", "O(n)"),

        ("longest_substring_without_repeating_characters", "Longest Substring Without Repeating Characters", "3", "Medium",
         "Given a string s, find the length of the longest substring without repeating characters.",
         [("s = 'abcabcbb'", "3", "Answer is 'abc' with length 3"), ("s = 'bbbbb'", "1", "Answer is 'b'")],
         ["0 <= s.length <= 5*10^4", "s consists of English letters, digits, symbols and spaces"],
         "O(n)", "O(min(m,n))"),

        ("longest_repeating_character_replacement", "Longest Repeating Character Replacement", "424", "Medium",
         "Given a string s and an integer k, you can choose any character and change it to any other uppercase English character at most k times. Return the length of the longest substring containing the same letter you can get after performing the operations.",
         [("s = 'ABAB', k = 2", "4", "Replace the two 'A's with 'B's or vice versa")],
         ["1 <= s.length <= 10^5", "s consists of only uppercase English letters", "0 <= k <= s.length"],
         "O(n)", "O(1)"),

        ("minimum_window_substring", "Minimum Window Substring", "76", "Hard",
         "Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If no such substring exists, return empty string.",
         [("s = 'ADOBECODEBANC', t = 'ABC'", "'BANC'", "")],
         ["m == s.length, n == t.length", "1 <= m, n <= 10^5", "s and t consist of uppercase and lowercase English letters"],
         "O(m+n)", "O(m+n)"),

        ("palindromic_substrings", "Palindromic Substrings", "647", "Medium",
         "Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward.",
         [("s = 'abc'", "3", "Three palindromic substrings: 'a', 'b', 'c'"), ("s = 'aaa'", "6", "'a', 'a', 'a', 'aa', 'aa', 'aaa'")],
         ["1 <= s.length <= 1000", "s consists of lowercase English letters"],
         "O(n²)", "O(1)"),

        ("encode_and_decode_strings", "Encode and Decode Strings", "271", "Medium",
         "Design an algorithm to encode a list of strings to a string and decode it back. The encoded string is then sent over the network and decoded back to the original list of strings.",
         [("strs = ['Hello','World']", "'Hello', 'World'", "Encode to a single string, then decode back")],
         ["1 <= strs.length <= 200", "0 <= strs[i].length <= 200", "strs[i] contains any possible characters"],
         "O(n)", "O(1)"),

        ("valid_palindrome", "Valid Palindrome", "125", "Easy",
         "Given a string s, return true if it is a palindrome, otherwise false. Consider only alphanumeric characters and ignore cases.",
         [("s = 'A man, a plan, a canal: Panama'", "true", ""), ("s = 'race a car'", "false", "")],
         ["1 <= s.length <= 2*10^5", "s consists only of printable ASCII characters"],
         "O(n)", "O(1)"),

        ("longest_palindromic_substring", "Longest Palindromic Substring", "5", "Medium",
         "Given a string s, return the longest palindromic substring in s.",
         [("s = 'babad'", "'bab' or 'aba'", "Both are valid"), ("s = 'cbbd'", "'bb'", "")],
         ["1 <= s.length <= 1000", "s consist of only digits and English letters"],
         "O(n²)", "O(1)"),
    ],

    "linked_lists": [
        ("reverse_linked_list", "Reverse Linked List", "206", "Easy",
         "Given the head of a singly linked list, reverse the list and return the reversed list.",
         [("head = [1,2,3,4,5]", "[5,4,3,2,1]", "")],
         ["The number of nodes is in range [0, 5000]", "-5000 <= Node.val <= 5000"],
         "O(n)", "O(1)"),

        ("detect_cycle", "Linked List Cycle", "141", "Easy",
         "Given head, the head of a linked list, determine if the linked list has a cycle in it. Return true if there is a cycle, false otherwise.",
         [("head = [3,2,0,-4], pos = 1", "true", "Tail connects to 2nd node (index 1)")],
         ["The number of nodes is in range [0, 10^4]", "-10^5 <= Node.val <= 10^5"],
         "O(n)", "O(1)"),

        ("merge_two_sorted_lists", "Merge Two Sorted Lists", "21", "Easy",
         "Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.",
         [("list1 = [1,2,4], list2 = [1,3,4]", "[1,1,2,3,4,4]", "")],
         ["The number of nodes in both lists is in range [0, 50]", "-100 <= Node.val <= 100", "Both lists are sorted in non-decreasing order"],
         "O(n+m)", "O(1)"),

        ("merge_k_sorted_lists", "Merge k Sorted Lists", "23", "Hard",
         "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
         [("lists = [[1,4,5],[1,3,4],[2,6]]", "[1,1,2,3,4,4,5,6]", "")],
         ["k == lists.length", "0 <= k <= 10^4", "0 <= lists[i].length <= 500", "-10^4 <= lists[i][j] <= 10^4"],
         "O(N log k)", "O(k)"),

        ("remove_nth_node_from_end_of_list", "Remove Nth Node From End of List", "19", "Medium",
         "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
         [("head = [1,2,3,4,5], n = 2", "[1,2,3,5]", "")],
         ["The number of nodes is sz", "1 <= sz <= 30", "0 <= Node.val <= 100", "1 <= n <= sz"],
         "O(n)", "O(1)"),

        ("reorder_list", "Reorder List", "143", "Medium",
         "Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→… You may not modify the values, only nodes themselves may be changed.",
         [("head = [1,2,3,4]", "[1,4,2,3]", ""), ("head = [1,2,3,4,5]", "[1,5,2,4,3]", "")],
         ["The number of nodes is in range [1, 5*10^4]", "1 <= Node.val <= 1000"],
         "O(n)", "O(1)"),
    ],

    "trees": [
        ("invert_binary_tree", "Invert Binary Tree", "226", "Easy",
         "Given the root of a binary tree, invert the tree and return its root.",
         [("root = [4,2,7,1,3,6,9]", "[4,7,2,9,6,3,1]", "")],
         ["The number of nodes is in range [0, 100]", "-100 <= Node.val <= 100"],
         "O(n)", "O(h)"),

        ("maximum_depth_of_binary_tree", "Maximum Depth of Binary Tree", "104", "Easy",
         "Given the root of a binary tree, return its maximum depth. Maximum depth is the number of nodes along the longest path from root to the farthest leaf.",
         [("root = [3,9,20,null,null,15,7]", "3", "")],
         ["The number of nodes is in range [0, 10^4]", "-100 <= Node.val <= 100"],
         "O(n)", "O(h)"),

        ("same_tree", "Same Tree", "100", "Easy",
         "Given the roots of two binary trees p and q, check if they are the same or not. Two trees are same if they are structurally identical and nodes have the same value.",
         [("p = [1,2,3], q = [1,2,3]", "true", "")],
         ["The number of nodes in both trees is in range [0, 100]", "-10^4 <= Node.val <= 10^4"],
         "O(n)", "O(h)"),

        ("subtree_of_another_tree", "Subtree of Another Tree", "572", "Easy",
         "Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values as subRoot, false otherwise.",
         [("root = [3,4,5,1,2], subRoot = [4,1,2]", "true", "")],
         ["The number of nodes in root is in range [1, 2000]", "The number of nodes in subRoot is in range [1, 1000]", "-10^4 <= root.val <= 10^4"],
         "O(m*n)", "O(h)"),

        ("lowest_common_ancestor_of_bst", "Lowest Common Ancestor of a Binary Search Tree", "235", "Easy",
         "Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. The LCA is the lowest node that has both nodes as descendants.",
         [("root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8", "6", "")],
         ["The number of nodes is in range [2, 10^5]", "-10^9 <= Node.val <= 10^9", "All Node.val are unique", "p != q"],
         "O(h)", "O(h)"),

        ("validate_binary_search_tree", "Validate Binary Search Tree", "98", "Medium",
         "Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST has left subtree nodes < node < right subtree nodes for all nodes.",
         [("root = [2,1,3]", "true", ""), ("root = [5,1,4,null,null,3,6]", "false", "")],
         ["The number of nodes is in range [1, 10^4]", "-2^31 <= Node.val <= 2^31 - 1"],
         "O(n)", "O(h)"),

        ("kth_smallest_element_in_bst", "Kth Smallest Element in a BST", "230", "Medium",
         "Given the root of a binary search tree and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.",
         [("root = [3,1,4,null,2], k = 1", "1", ""), ("root = [5,3,6,2,4,null,null,1], k = 3", "3", "")],
         ["The number of nodes is n", "1 <= k <= n <= 10^4", "0 <= Node.val <= 10^4"],
         "O(n)", "O(h)"),

        ("binary_tree_level_order_traversal", "Binary Tree Level Order Traversal", "102", "Medium",
         "Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).",
         [("root = [3,9,20,null,null,15,7]", "[[3],[9,20],[15,7]]", "")],
         ["The number of nodes is in range [0, 2000]", "-1000 <= Node.val <= 1000"],
         "O(n)", "O(n)"),

        ("construct_binary_tree_from_preorder_and_inorder", "Construct Binary Tree from Preorder and Inorder Traversal", "105", "Medium",
         "Given two integer arrays preorder and inorder, construct and return the binary tree.",
         [("preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]", "[3,9,20,null,null,15,7]", "")],
         ["1 <= preorder.length <= 3000", "inorder.length == preorder.length", "-3000 <= preorder[i], inorder[i] <= 3000", "All values are unique"],
         "O(n)", "O(n)"),

        ("serialize_and_deserialize_binary_tree", "Serialize and Deserialize Binary Tree", "297", "Hard",
         "Design an algorithm to serialize and deserialize a binary tree. Serialization converts a tree to a string, deserialization converts the string back to the tree structure.",
         [("root = [1,2,3,null,null,4,5]", "[1,2,3,null,null,4,5]", "")],
         ["The number of nodes is in range [0, 10^4]", "-1000 <= Node.val <= 1000"],
         "O(n)", "O(n)"),

        ("binary_tree_maximum_path_sum", "Binary Tree Maximum Path Sum", "124", "Hard",
         "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge. A path does not need to pass through the root. Return the maximum path sum of any non-empty path.",
         [("root = [1,2,3]", "6", "Path is 2 -> 1 -> 3"), ("root = [-10,9,20,null,null,15,7]", "42", "Path is 15 -> 20 -> 7")],
         ["The number of nodes is in range [1, 3*10^4]", "-1000 <= Node.val <= 1000"],
         "O(n)", "O(h)"),

        ("implement_trie", "Implement Trie (Prefix Tree)", "208", "Medium",
         "A trie or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Implement the Trie class with insert, search, and startsWith methods.",
         [("Operations: ['Trie', 'insert', 'search', 'startsWith']", "[null, null, true, true]", "")],
         ["1 <= word.length, prefix.length <= 2000", "word and prefix consist only of lowercase English letters", "At most 3*10^4 calls will be made to insert, search, and startsWith"],
         "O(m)", "O(m)"),

        ("add_and_search_word", "Design Add and Search Words Data Structure", "211", "Medium",
         "Design a data structure that supports adding new words and finding if a string matches any previously added string. Search can use '.' to represent any letter.",
         [("Operations: ['WordDictionary','addWord','search']", "[null,null,true,false,true]", "")],
         ["1 <= word.length <= 25", "word consists of lowercase English letters", "queries consist of lowercase English letters or '.'", "At most 10^4 calls will be made"],
         "O(m)", "O(m)"),
    ],

    "graphs": [
        ("number_of_islands", "Number of Islands", "200", "Medium",
         "Given an m x n 2D grid of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.",
         [("grid = [['1','1','0'],['1','1','0'],['0','0','1']]", "2", "")],
         ["m == grid.length", "n == grid[i].length", "1 <= m, n <= 300", "grid[i][j] is '0' or '1'"],
         "O(m*n)", "O(m*n)"),

        ("clone_graph", "Clone Graph", "133", "Medium",
         "Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node contains a value and a list of neighbors.",
         [("adjList = [[2,4],[1,3],[2,4],[1,3]]", "[[2,4],[1,3],[2,4],[1,3]]", "")],
         ["The number of nodes is in range [0, 100]", "1 <= Node.val <= 100", "Node.val is unique", "No repeated edges and no self-loops"],
         "O(N+E)", "O(N)"),

        ("pacific_atlantic_water_flow", "Pacific Atlantic Water Flow", "417", "Medium",
         "Given an m x n matrix of heights representing an island, return coordinates of cells where water can flow to both Pacific (top/left edges) and Atlantic (bottom/right edges) oceans.",
         [("heights = [[1,2,3],[8,9,4],[7,6,5]]", "[[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]", "")],
         ["m == heights.length", "n == heights[r].length", "1 <= m, n <= 200", "0 <= heights[r][c] <= 10^5"],
         "O(m*n)", "O(m*n)"),

        ("course_schedule", "Course Schedule", "207", "Medium",
         "Given numCourses and a list of prerequisites where prerequisites[i] = [ai, bi] indicates you must take course bi first to take course ai, return true if you can finish all courses.",
         [("numCourses = 2, prerequisites = [[1,0]]", "true", "Take course 0, then course 1")],
         ["1 <= numCourses <= 2000", "0 <= prerequisites.length <= 5000", "All pairs are unique"],
         "O(V+E)", "O(V+E)"),

        ("longest_consecutive_sequence", "Longest Consecutive Sequence", "128", "Medium",
         "Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. Must run in O(n) time.",
         [("nums = [100,4,200,1,3,2]", "4", "The sequence is [1,2,3,4]")],
         ["0 <= nums.length <= 10^5", "-10^9 <= nums[i] <= 10^9"],
         "O(n)", "O(n)"),

        ("alien_dictionary", "Alien Dictionary", "269", "Hard",
         "Given a sorted dictionary of an alien language with unique letters, derive the order of letters in this language. If order is invalid, return empty string.",
         [("words = ['wrt','wrf','er','ett','rftt']", "'wertf'", "")],
         ["1 <= words.length <= 100", "1 <= words[i].length <= 100", "words[i] consists of only lowercase English letters"],
         "O(C)", "O(1)"),

        ("graph_valid_tree", "Graph Valid Tree", "261", "Medium",
         "Given n nodes labeled from 0 to n-1 and a list of undirected edges, check if these edges form a valid tree.",
         [("n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]", "true", "")],
         ["1 <= n <= 2000", "0 <= edges.length <= 5000", "edges[i].length == 2"],
         "O(V+E)", "O(V+E)"),

        ("number_of_connected_components", "Number of Connected Components in an Undirected Graph", "323", "Medium",
         "Given n nodes labeled from 0 to n-1 and a list of undirected edges, return the number of connected components in the graph.",
         [("n = 5, edges = [[0,1],[1,2],[3,4]]", "2", "")],
         ["1 <= n <= 2000", "0 <= edges.length <= 5000", "edges[i].length == 2"],
         "O(V+E)", "O(V)"),
    ],

    "dynamic_programming": [
        ("climbing_stairs", "Climbing Stairs", "70", "Easy",
         "You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
         [("n = 2", "2", "1+1, or 2"), ("n = 3", "3", "1+1+1, 1+2, or 2+1")],
         ["1 <= n <= 45"],
         "O(n)", "O(1)"),

        ("house_robber", "House Robber", "198", "Medium",
         "You are a robber planning to rob houses along a street. Each house has money, but adjacent houses have security systems connected. Find maximum money you can rob without robbing adjacent houses.",
         [("nums = [1,2,3,1]", "4", "Rob house 1 (money = 1) then house 3 (money = 3)"), ("nums = [2,7,9,3,1]", "12", "Rob houses 1, 3, and 5")],
         ["1 <= nums.length <= 100", "0 <= nums[i] <= 400"],
         "O(n)", "O(1)"),

        ("house_robber_ii", "House Robber II", "213", "Medium",
         "All houses are arranged in a circle. Adjacent houses have security systems. Find maximum money you can rob without alerting police.",
         [("nums = [2,3,2]", "3", "Cannot rob house 1 and 3"), ("nums = [1,2,3,1]", "4", "")],
         ["1 <= nums.length <= 100", "0 <= nums[i] <= 1000"],
         "O(n)", "O(1)"),

        ("coin_change", "Coin Change", "322", "Medium",
         "Given coins of different denominations and a total amount, return the fewest number of coins needed to make up that amount. Return -1 if impossible.",
         [("coins = [1,2,5], amount = 11", "3", "11 = 5 + 5 + 1")],
         ["1 <= coins.length <= 12", "1 <= coins[i] <= 2^31 - 1", "0 <= amount <= 10^4"],
         "O(n*amount)", "O(amount)"),

        ("coin_change_ii", "Coin Change II", "518", "Medium",
         "Given coins of different denominations and a total amount, return the number of combinations that make up that amount.",
         [("amount = 5, coins = [1,2,5]", "4", "5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1")],
         ["1 <= coins.length <= 300", "1 <= coins[i] <= 5000", "0 <= amount <= 5000"],
         "O(n*amount)", "O(amount)"),

        ("longest_increasing_subsequence", "Longest Increasing Subsequence", "300", "Medium",
         "Given an integer array nums, return the length of the longest strictly increasing subsequence.",
         [("nums = [10,9,2,5,3,7,101,18]", "4", "LIS is [2,3,7,101]")],
         ["1 <= nums.length <= 2500", "-10^4 <= nums[i] <= 10^4"],
         "O(n log n)", "O(n)"),

        ("combination_sum_iv", "Combination Sum IV", "377", "Medium",
         "Given an array of distinct integers and a target, return the number of possible combinations that add up to target. Different sequences count as different combinations.",
         [("nums = [1,2,3], target = 4", "7", "[1,1,1,1], [1,1,2], [1,2,1], [1,3], [2,1,1], [2,2], [3,1]")],
         ["1 <= nums.length <= 200", "1 <= nums[i] <= 1000", "All elements are unique", "1 <= target <= 1000"],
         "O(target*n)", "O(target)"),

        ("decode_ways", "Decode Ways", "91", "Medium",
         "A message containing letters A-Z can be encoded as numbers where 'A'=1, 'B'=2, ..., 'Z'=26. Given encoded message containing digits, return the number of ways to decode it.",
         [("s = '12'", "2", "Can be decoded as 'AB' (1 2) or 'L' (12)"), ("s = '226'", "3", "'BZ', 'VF', or 'BBF'")],
         ["1 <= s.length <= 100", "s contains only digits", "s may contain leading zeros"],
         "O(n)", "O(1)"),

        ("unique_paths", "Unique Paths", "62", "Medium",
         "A robot on an m x n grid starts at top-left and wants to reach bottom-right. The robot can only move down or right. How many unique paths are there?",
         [("m = 3, n = 7", "28", ""), ("m = 3, n = 2", "3", "")],
         ["1 <= m, n <= 100"],
         "O(m*n)", "O(n)"),

        ("jump_game", "Jump Game", "55", "Medium",
         "Given an array nums where each element represents your maximum jump length at that position, determine if you can reach the last index.",
         [("nums = [2,3,1,1,4]", "true", "Jump 1 step to index 1, then 3 steps to last index"), ("nums = [3,2,1,0,4]", "false", "")],
         ["1 <= nums.length <= 10^4", "0 <= nums[i] <= 10^5"],
         "O(n)", "O(1)"),

        ("word_break", "Word Break", "139", "Medium",
         "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.",
         [("s = 'leetcode', wordDict = ['leet','code']", "true", "Can be segmented as 'leet code'")],
         ["1 <= s.length <= 300", "1 <= wordDict.length <= 1000", "1 <= wordDict[i].length <= 20", "All strings consist of lowercase English letters"],
         "O(n²)", "O(n)"),
    ],

    "matrix": [
        ("set_matrix_zeroes", "Set Matrix Zeroes", "73", "Medium",
         "Given an m x n matrix, if an element is 0, set its entire row and column to 0. Must do it in-place.",
         [("matrix = [[1,1,1],[1,0,1],[1,1,1]]", "[[1,0,1],[0,0,0],[1,0,1]]", "")],
         ["m == matrix.length", "n == matrix[0].length", "1 <= m, n <= 200", "-2^31 <= matrix[i][j] <= 2^31 - 1"],
         "O(m*n)", "O(1)"),

        ("spiral_matrix", "Spiral Matrix", "54", "Medium",
         "Given an m x n matrix, return all elements of the matrix in spiral order (clockwise from outside to inside).",
         [("matrix = [[1,2,3],[4,5,6],[7,8,9]]", "[1,2,3,6,9,8,7,4,5]", "")],
         ["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 10", "-100 <= matrix[i][j] <= 100"],
         "O(m*n)", "O(1)"),

        ("rotate_image", "Rotate Image", "48", "Medium",
         "Given an n x n 2D matrix representing an image, rotate the image by 90 degrees clockwise. Must rotate the matrix in-place.",
         [("matrix = [[1,2,3],[4,5,6],[7,8,9]]", "[[7,4,1],[8,5,2],[9,6,3]]", "")],
         ["n == matrix.length == matrix[i].length", "1 <= n <= 20", "-1000 <= matrix[i][j] <= 1000"],
         "O(n²)", "O(1)"),

        ("word_search", "Word Search", "79", "Medium",
         "Given an m x n grid of characters and a string word, return true if word exists in the grid. Word can be constructed from sequentially adjacent cells (horizontally or vertically).",
         [("board = [['A','B','C'],['S','F','C'],['A','D','E']], word = 'ABCCED'", "true", "")],
         ["m == board.length", "n == board[i].length", "1 <= m, n <= 6", "1 <= word.length <= 15", "board and word consist of only lowercase and uppercase English letters"],
         "O(m*n*4^L)", "O(L)"),
    ],

    "intervals": [
        ("insert_interval", "Insert Interval", "57", "Medium",
         "Given a set of non-overlapping intervals sorted by start time, insert a new interval and merge if necessary.",
         [("intervals = [[1,3],[6,9]], newInterval = [2,5]", "[[1,5],[6,9]]", "")],
         ["0 <= intervals.length <= 10^4", "intervals[i].length == 2", "newInterval.length == 2", "Intervals are sorted by start time"],
         "O(n)", "O(n)"),

        ("merge_intervals", "Merge Intervals", "56", "Medium",
         "Given an array of intervals, merge all overlapping intervals and return an array of non-overlapping intervals.",
         [("intervals = [[1,3],[2,6],[8,10],[15,18]]", "[[1,6],[8,10],[15,18]]", "[1,3] and [2,6] overlap")],
         ["1 <= intervals.length <= 10^4", "intervals[i].length == 2", "0 <= starti <= endi <= 10^4"],
         "O(n log n)", "O(n)"),

        ("non_overlapping_intervals", "Non-overlapping Intervals", "435", "Medium",
         "Given an array of intervals, return the minimum number of intervals you need to remove to make the rest non-overlapping.",
         [("intervals = [[1,2],[2,3],[3,4],[1,3]]", "1", "Remove [1,3] to make rest non-overlapping")],
         ["1 <= intervals.length <= 10^5", "intervals[i].length == 2", "-5*10^4 <= starti < endi <= 5*10^4"],
         "O(n log n)", "O(1)"),

        ("meeting_rooms", "Meeting Rooms", "252", "Easy",
         "Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings.",
         [("intervals = [[0,30],[5,10],[15,20]]", "false", "Meetings overlap")],
         ["0 <= intervals.length <= 10^4", "intervals[i].length == 2"],
         "O(n log n)", "O(1)"),

        ("meeting_rooms_ii", "Meeting Rooms II", "253", "Medium",
         "Given an array of meeting time intervals, return the minimum number of conference rooms required.",
         [("intervals = [[0,30],[5,10],[15,20]]", "2", "Need 2 rooms at time 5-10")],
         ["1 <= intervals.length <= 10^4", "0 <= starti < endi <= 10^6"],
         "O(n log n)", "O(n)"),

        ("minimum_interval_to_include_each_query", "Minimum Interval to Include Each Query", "1851", "Hard",
         "Given intervals and queries arrays, for each query find the size of the smallest interval containing it. Return -1 if no interval contains the query.",
         [("intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]", "[3,3,1,4]", "")],
         ["1 <= intervals.length <= 10^5", "1 <= queries.length <= 10^5", "intervals[i].length == 2", "1 <= lefti <= righti <= 10^7"],
         "O(n log n + q log q)", "O(n + q)"),
    ],

    "binary": [
        ("sum_of_two_integers", "Sum of Two Integers", "371", "Medium",
         "Given two integers a and b, return the sum of the two integers without using the + or - operators.",
         [("a = 1, b = 2", "3", ""), ("a = 2, b = 3", "5", "")],
         ["-1000 <= a, b <= 1000"],
         "O(1)", "O(1)"),

        ("number_of_1_bits", "Number of 1 Bits", "191", "Easy",
         "Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).",
         [("n = 11", "3", "Binary: 00000000000000000000000000001011"), ("n = 128", "1", "Binary: 00000000000000000000000010000000")],
         ["1 <= n <= 2^31 - 1"],
         "O(1)", "O(1)"),

        ("counting_bits", "Counting Bits", "338", "Easy",
         "Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.",
         [("n = 2", "[0,1,1]", "0 has 0 ones, 1 has 1 one, 2 (10) has 1 one"), ("n = 5", "[0,1,1,2,1,2]", "")],
         ["0 <= n <= 10^5"],
         "O(n)", "O(n)"),

        ("missing_number", "Missing Number", "268", "Easy",
         "Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.",
         [("nums = [3,0,1]", "2", "Range is [0,3], missing number is 2"), ("nums = [9,6,4,2,3,5,7,0,1]", "8", "")],
         ["n == nums.length", "1 <= n <= 10^4", "0 <= nums[i] <= n", "All numbers are unique"],
         "O(n)", "O(1)"),

        ("reverse_bits", "Reverse Bits", "190", "Easy",
         "Reverse bits of a given 32 bits unsigned integer.",
         [("n = 00000010100101000001111010011100", "00111001011110000010100101000000", "964176192")],
         ["Input is a binary string of length 32"],
         "O(1)", "O(1)"),
    ],

    "heap": [
        ("top_k_frequent_elements", "Top K Frequent Elements", "347", "Medium",
         "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.",
         [("nums = [1,1,1,2,2,3], k = 2", "[1,2]", ""), ("nums = [1], k = 1", "[1]", "")],
         ["1 <= nums.length <= 10^5", "k is in range [1, number of unique elements]", "Answer is guaranteed to be unique"],
         "O(n log k)", "O(n)"),

        ("find_median_from_data_stream", "Find Median from Data Stream", "295", "Hard",
         "Design a data structure that supports adding integers and finding the median of all elements. Median is the middle value in an ordered list.",
         [("Operations: ['MedianFinder','addNum','addNum','findMedian']", "[null,null,null,1.5]", "")],
         ["-10^5 <= num <= 10^5", "At most 5*10^4 calls to addNum and findMedian"],
         "O(log n)", "O(n)"),
    ]
}


def create_problem_file(category: str, file_name: str, problem_name: str, leetcode_num: str,
                       difficulty: str, description: str, examples: list, constraints: list,
                       time_complexity: str, space_complexity: str):
    """Create a single problem file"""

    # Build examples section
    examples_text = "\n".join([
        f"Input: {ex[0]}\nOutput: {ex[1]}" + (f"\nExplanation: {ex[2]}" if ex[2] else "")
        for ex in examples
    ])

    # Build constraints section
    constraints_text = "\n".join([f"- {c}" for c in constraints])

    # Create function name from file name
    func_name = file_name

    # Determine basic parameters based on category
    if category == "linked_lists":
        params = "head: Optional[ListNode]"
        return_type = "Optional[ListNode]"
        param_desc = "head: Head of the linked list"
        return_desc = "Modified or new linked list head"
    elif category == "trees":
        params = "root: Optional[TreeNode]"
        return_type = "Optional[TreeNode]" if "construct" in file_name or "serialize" in file_name else "bool"
        param_desc = "root: Root of the binary tree"
        return_desc = "Result based on problem requirements"
    elif category == "graphs":
        params = "graph: List[List[int]]"
        return_type = "int"
        param_desc = "graph: Graph representation"
        return_desc = "Result based on problem requirements"
    else:
        params = "nums: List[int]"
        return_type = "int"
        param_desc = "nums: Input array or parameters"
        return_desc = "Result based on problem requirements"

    content = f'''"""
Problem: {problem_name} (LeetCode #{leetcode_num})
Difficulty: {difficulty}
Category: {category.replace("_", " ").title()}

Description:
{description}

Examples:
{examples_text}

Constraints:
{constraints_text}

Time Complexity Target: {time_complexity}
Space Complexity Target: {space_complexity}
"""

from typing import List, Optional


def {func_name}({params}) -> {return_type}:
    """
    TODO: Implement your solution here

    Args:
        {param_desc}

    Returns:
        {return_desc}
    """
    pass


# Test Cases
def test_{func_name}():
    """Test cases for {func_name}"""

    # Test case 1
    print("Test case 1...")
    # TODO: Add test case implementation

    # Test case 2
    print("Test case 2...")
    # TODO: Add test case implementation

    # Edge cases
    print("Edge case tests...")
    # TODO: Add edge case tests

    print("✓ All test cases passed!")


if __name__ == "__main__":
    test_{func_name}()
'''

    file_path = Path(category) / f"{file_name}.py"
    file_path.write_text(content)
    print(f"Created: {file_path}")


def main():
    """Generate all problem files"""
    total_created = 0

    for category, problems in PROBLEM_DATA.items():
        print(f"\nGenerating {category} problems...")
        for problem in problems:
            create_problem_file(category, *problem)
            total_created += 1

    print(f"\n{'='*60}")
    print(f"✓ Successfully created {total_created} problem files!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
