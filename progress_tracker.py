#!/usr/bin/env python3
"""
Blind 75 Progress Tracker
Interactive CLI tool to track your progress through the Blind 75 problems
"""

import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

# ANSI color codes
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Complete list of Blind 75 problems organized by category
PROBLEMS = {
    "arrays": [
        "two_sum",
        "best_time_to_buy_and_sell_stock",
        "contains_duplicate",
        "product_of_array_except_self",
        "maximum_subarray",
        "maximum_product_subarray",
        "find_minimum_in_rotated_sorted_array",
        "search_in_rotated_sorted_array",
        "3sum",
        "container_with_most_water"
    ],
    "strings": [
        "valid_anagram",
        "group_anagrams",
        "valid_parentheses",
        "longest_substring_without_repeating_characters",
        "longest_repeating_character_replacement",
        "minimum_window_substring",
        "palindromic_substrings",
        "encode_and_decode_strings",
        "valid_palindrome",
        "longest_palindromic_substring"
    ],
    "linked_lists": [
        "reverse_linked_list",
        "detect_cycle",
        "merge_two_sorted_lists",
        "merge_k_sorted_lists",
        "remove_nth_node_from_end_of_list",
        "reorder_list"
    ],
    "trees": [
        "invert_binary_tree",
        "maximum_depth_of_binary_tree",
        "same_tree",
        "subtree_of_another_tree",
        "lowest_common_ancestor_of_bst",
        "validate_binary_search_tree",
        "kth_smallest_element_in_bst",
        "binary_tree_level_order_traversal",
        "construct_binary_tree_from_preorder_and_inorder",
        "serialize_and_deserialize_binary_tree",
        "binary_tree_maximum_path_sum",
        "implement_trie",
        "add_and_search_word"
    ],
    "graphs": [
        "number_of_islands",
        "clone_graph",
        "pacific_atlantic_water_flow",
        "course_schedule",
        "longest_consecutive_sequence",
        "alien_dictionary",
        "graph_valid_tree",
        "number_of_connected_components"
    ],
    "dynamic_programming": [
        "climbing_stairs",
        "house_robber",
        "house_robber_ii",
        "coin_change",
        "coin_change_ii",
        "longest_increasing_subsequence",
        "combination_sum_iv",
        "decode_ways",
        "unique_paths",
        "jump_game",
        "word_break"
    ],
    "matrix": [
        "set_matrix_zeroes",
        "spiral_matrix",
        "rotate_image",
        "word_search"
    ],
    "intervals": [
        "insert_interval",
        "merge_intervals",
        "non_overlapping_intervals",
        "meeting_rooms",
        "meeting_rooms_ii",
        "minimum_interval_to_include_each_query"
    ],
    "binary": [
        "sum_of_two_integers",
        "number_of_1_bits",
        "counting_bits",
        "missing_number",
        "reverse_bits"
    ],
    "heap": [
        "top_k_frequent_elements",
        "find_median_from_data_stream"
    ]
}

PROGRESS_FILE = Path(".progress.json")


class ProgressTracker:
    def __init__(self):
        self.data = self.load_progress()

    def load_progress(self) -> Dict:
        """Load progress from JSON file"""
        if PROGRESS_FILE.exists():
            with open(PROGRESS_FILE, 'r') as f:
                return json.load(f)
        else:
            # Initialize new progress data
            return {
                "problems": {},
                "streak": 0,
                "last_practice_date": None,
                "started_date": datetime.now().isoformat()
            }

    def save_progress(self):
        """Save progress to JSON file"""
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(self.data, indent=2, fp=f)

    def get_problem_status(self, category: str, problem: str) -> str:
        """Get status of a problem: 'not_started', 'in_progress', 'completed'"""
        key = f"{category}/{problem}"
        if key not in self.data["problems"]:
            return "not_started"
        return self.data["problems"][key].get("status", "not_started")

    def set_problem_status(self, category: str, problem: str, status: str):
        """Set status of a problem"""
        key = f"{category}/{problem}"
        if key not in self.data["problems"]:
            self.data["problems"][key] = {}

        self.data["problems"][key]["status"] = status
        self.data["problems"][key]["last_updated"] = datetime.now().isoformat()

        # Update streak if completing a problem
        if status == "completed":
            self.update_streak()

        self.save_progress()

    def update_streak(self):
        """Update the daily practice streak"""
        today = datetime.now().date()
        last_date_str = self.data.get("last_practice_date")

        if last_date_str:
            last_date = datetime.fromisoformat(last_date_str).date()
            days_diff = (today - last_date).days

            if days_diff == 0:
                # Same day, no change to streak
                pass
            elif days_diff == 1:
                # Consecutive day, increment streak
                self.data["streak"] = self.data.get("streak", 0) + 1
            else:
                # Streak broken, reset to 1
                self.data["streak"] = 1
        else:
            # First practice day
            self.data["streak"] = 1

        self.data["last_practice_date"] = datetime.now().isoformat()

    def get_statistics(self) -> Dict:
        """Calculate statistics"""
        stats = {
            "total": 75,
            "completed": 0,
            "in_progress": 0,
            "not_started": 0,
            "by_category": {}
        }

        for category, problems in PROBLEMS.items():
            cat_stats = {
                "total": len(problems),
                "completed": 0,
                "in_progress": 0,
                "not_started": 0
            }

            for problem in problems:
                status = self.get_problem_status(category, problem)
                stats[status] += 1
                cat_stats[status] += 1

            stats["by_category"][category] = cat_stats

        stats["percentage"] = (stats["completed"] / stats["total"]) * 100
        return stats

    def display_dashboard(self):
        """Display the main dashboard"""
        stats = self.get_statistics()

        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}🎯 BLIND 75 PROGRESS TRACKER{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.RESET}\n")

        # Overall statistics
        print(f"{Colors.BOLD}Overall Progress:{Colors.RESET}")
        print(f"  {Colors.GREEN}✓ Completed:{Colors.RESET} {stats['completed']}/75 ({stats['percentage']:.1f}%)")
        print(f"  {Colors.YELLOW}◐ In Progress:{Colors.RESET} {stats['in_progress']}")
        print(f"  {Colors.RED}○ Not Started:{Colors.RESET} {stats['not_started']}")

        # Progress bar
        completed_blocks = int(stats['completed'] / 75 * 40)
        progress_bar = f"{Colors.GREEN}{'█' * completed_blocks}{Colors.RESET}{'░' * (40 - completed_blocks)}"
        print(f"\n  [{progress_bar}] {stats['percentage']:.1f}%\n")

        # Streak
        streak = self.data.get("streak", 0)
        if streak > 0:
            print(f"{Colors.BOLD}🔥 Current Streak:{Colors.RESET} {streak} day{'s' if streak != 1 else ''}")

        last_practice = self.data.get("last_practice_date")
        if last_practice:
            last_date = datetime.fromisoformat(last_practice).strftime("%Y-%m-%d")
            print(f"{Colors.BOLD}📅 Last Practice:{Colors.RESET} {last_date}")

        print(f"\n{Colors.BOLD}{'─'*70}{Colors.RESET}\n")

        # Category breakdown
        print(f"{Colors.BOLD}Progress by Category:{Colors.RESET}\n")

        for category, cat_stats in stats["by_category"].items():
            cat_display = category.replace('_', ' ').title()
            completed = cat_stats["completed"]
            total = cat_stats["total"]
            percentage = (completed / total * 100) if total > 0 else 0

            # Category progress bar
            cat_blocks = int(completed / total * 20) if total > 0 else 0
            cat_bar = f"{Colors.GREEN}{'█' * cat_blocks}{Colors.RESET}{'░' * (20 - cat_blocks)}"

            print(f"  {cat_display:30} [{cat_bar}] {completed}/{total} ({percentage:.0f}%)")

        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.RESET}\n")

        # Next recommended problem
        self.suggest_next_problem(stats)

    def suggest_next_problem(self, stats: Dict):
        """Suggest next problem to work on"""
        # Find category with lowest completion percentage
        min_percentage = 100
        target_category = None

        for category, cat_stats in stats["by_category"].items():
            if cat_stats["not_started"] > 0 or cat_stats["in_progress"] > 0:
                percentage = (cat_stats["completed"] / cat_stats["total"]) * 100
                if percentage < min_percentage:
                    min_percentage = percentage
                    target_category = category

        if target_category:
            # Find first not started problem in that category
            for problem in PROBLEMS[target_category]:
                status = self.get_problem_status(target_category, problem)
                if status == "not_started":
                    problem_display = problem.replace('_', ' ').title()
                    cat_display = target_category.replace('_', ' ').title()
                    print(f"{Colors.BOLD}💡 Recommended Next Problem:{Colors.RESET}")
                    print(f"   {Colors.MAGENTA}{problem_display}{Colors.RESET}")
                    print(f"   Category: {cat_display}")
                    print(f"   File: {target_category}/{problem}.py\n")
                    return

    def list_problems(self, category: Optional[str] = None, status_filter: Optional[str] = None):
        """List all problems with their status"""
        categories_to_show = [category] if category else PROBLEMS.keys()

        print(f"\n{Colors.BOLD}Problem List:{Colors.RESET}\n")

        for cat in categories_to_show:
            if cat not in PROBLEMS:
                print(f"{Colors.RED}Unknown category: {cat}{Colors.RESET}")
                continue

            cat_display = cat.replace('_', ' ').title()
            print(f"{Colors.BOLD}{Colors.CYAN}{cat_display}:{Colors.RESET}")

            for problem in PROBLEMS[cat]:
                status = self.get_problem_status(cat, problem)

                if status_filter and status != status_filter:
                    continue

                status_icon = {
                    "completed": f"{Colors.GREEN}✓{Colors.RESET}",
                    "in_progress": f"{Colors.YELLOW}◐{Colors.RESET}",
                    "not_started": f"{Colors.RED}○{Colors.RESET}"
                }[status]

                problem_display = problem.replace('_', ' ').title()
                print(f"  {status_icon} {problem_display}")

            print()

    def start_problem(self, problem_identifier: str):
        """Mark a problem as in progress"""
        category, problem = self.parse_problem_identifier(problem_identifier)
        if category and problem:
            self.set_problem_status(category, problem, "in_progress")
            problem_display = problem.replace('_', ' ').title()
            print(f"\n{Colors.YELLOW}Started:{Colors.RESET} {problem_display}")
            print(f"File: {category}/{problem}.py\n")

    def complete_problem(self, problem_identifier: str):
        """Mark a problem as completed"""
        category, problem = self.parse_problem_identifier(problem_identifier)
        if category and problem:
            self.set_problem_status(category, problem, "completed")
            problem_display = problem.replace('_', ' ').title()
            print(f"\n{Colors.GREEN}✓ Completed:{Colors.RESET} {problem_display}")

            # Show updated stats
            stats = self.get_statistics()
            print(f"Total Progress: {stats['completed']}/75 ({stats['percentage']:.1f}%)")
            print(f"🔥 Streak: {self.data.get('streak', 0)} days\n")

    def parse_problem_identifier(self, identifier: str) -> tuple:
        """Parse problem identifier (category/problem or just problem name)"""
        if '/' in identifier:
            parts = identifier.split('/')
            category = parts[0]
            problem = parts[1].replace('.py', '')
        else:
            # Search for problem in all categories
            problem = identifier.replace('.py', '').replace('-', '_').replace(' ', '_').lower()
            category = None

            for cat, problems in PROBLEMS.items():
                if problem in problems:
                    category = cat
                    break

        if not category:
            print(f"{Colors.RED}Problem not found: {identifier}{Colors.RESET}")
            return None, None

        if problem not in PROBLEMS[category]:
            print(f"{Colors.RED}Problem not found in category {category}: {problem}{Colors.RESET}")
            return None, None

        return category, problem

    def reset_progress(self, confirm: bool = False):
        """Reset all progress"""
        if not confirm:
            response = input(f"{Colors.YELLOW}Are you sure you want to reset all progress? (yes/no): {Colors.RESET}")
            if response.lower() != 'yes':
                print("Reset cancelled.")
                return

        self.data = {
            "problems": {},
            "streak": 0,
            "last_practice_date": None,
            "started_date": datetime.now().isoformat()
        }
        self.save_progress()
        print(f"{Colors.GREEN}Progress reset successfully.{Colors.RESET}")


def main():
    parser = argparse.ArgumentParser(
        description="Track your progress through the Blind 75 coding problems",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python progress_tracker.py                    # Show dashboard
  python progress_tracker.py --list             # List all problems
  python progress_tracker.py --start two_sum    # Mark problem as started
  python progress_tracker.py --complete arrays/two_sum  # Mark as completed
  python progress_tracker.py --category arrays  # Show arrays problems
  python progress_tracker.py --stats            # Show statistics
        """
    )

    parser.add_argument('--start', metavar='PROBLEM', help='Start working on a problem')
    parser.add_argument('--complete', metavar='PROBLEM', help='Mark a problem as completed')
    parser.add_argument('--list', action='store_true', help='List all problems')
    parser.add_argument('--category', metavar='CATEGORY', help='Filter by category')
    parser.add_argument('--status', choices=['completed', 'in_progress', 'not_started'],
                       help='Filter by status')
    parser.add_argument('--stats', action='store_true', help='Show detailed statistics')
    parser.add_argument('--reset', action='store_true', help='Reset all progress')

    args = parser.parse_args()
    tracker = ProgressTracker()

    if args.start:
        tracker.start_problem(args.start)
    elif args.complete:
        tracker.complete_problem(args.complete)
    elif args.list:
        tracker.list_problems(args.category, args.status)
    elif args.reset:
        tracker.reset_progress()
    elif args.stats:
        tracker.display_dashboard()
    else:
        # Default: show dashboard
        tracker.display_dashboard()


if __name__ == "__main__":
    main()
