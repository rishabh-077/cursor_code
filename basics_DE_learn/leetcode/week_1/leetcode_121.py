"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem
  Given prices[i] = stock price on day i, pick ONE buy day and ONE sell day (sell after buy).
  Return maximum profit. If no profit possible, return 0.

Pattern
  Track the **lowest price seen so far** (best buy) and max profit if you sell today.

Key rule
  Buy must happen on an **earlier day** than sell — you cannot use global min and global max
  from the whole array (e.g. [2, 4, 1] → min=1, max=4 but 1 comes after 4).

Approach comparison (n = len(prices))
  | Approach              | Time  | Space | Notes                                    |
  |-----------------------|-------|-------|------------------------------------------|
  | Brute force (pairs)   | O(n²) | O(1)  | TLE on LeetCode                          |
  | Global min + max      | Wrong | —     | Ignores buy-before-sell order            |
  | Two pointers buy/sell | O(n)  | O(1)  | buy index moves to cheaper day           |
  | One pass (cur_min)    | O(n)  | O(1)  | Preferred — submit as Solution           |

LeetCode: submit ONE class named Solution (one-pass cur_min below).
"""

from typing import List


# --- Approach 1: Brute force — every (buy, sell) pair with j > i ---
class SolutionBruteForce:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit
    # Time: O(n²)
    # Space: O(1)


# --- Approach 2: Global min/max — WRONG (do not submit) ---
# Fails when cheapest day is AFTER the best sell day.
# Example: [2, 4, 1] → global min=1, max=4 looks like profit 3, but you cannot buy on day 3 and sell on day 2.
class SolutionGlobalMinMax:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = min(prices)
        sell = max(prices)
        if prices.index(buy) < prices.index(sell):
            return sell - buy
        for i in range(prices.index(buy) + 1, len(prices)):
            if prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit


# --- Approach 3: Two pointers — buy index + sell index scan ---
class SolutionTwoPointers:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            else:
                # No profit selling today — move buy to cheaper day (current sell)
                buy = sell
            sell += 1
        return max_profit
    # Time: O(n) — sell visits each index once; buy only moves forward
    # Space: O(1)


# --- Approach 4: One pass — track min price so far (submit this as Solution) ---
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float("inf")  # cheapest buy price seen so far
        max_prof = 0

        for p in prices:
            cur_min = min(cur_min, p)           # best buy up to today
            max_prof = max(max_prof, p - cur_min)  # best profit if we sell today

        return max_prof
    # Time: O(n)
    # Space: O(1)
    #
    # Walkthrough: [7, 1, 5, 3, 6, 4]
    #   p=7: cur_min=7, profit=0
    #   p=1: cur_min=1, profit=0
    #   p=5: cur_min=1, profit=4  (buy@1 sell@5)
    #   ... max_prof ends at 5 (buy@1 sell@6)


if __name__ == "__main__":
    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),  # buy@2 sell@4 — global min/max approach fails here
    ]
    for prices, expected in tests:
        got = Solution().maxProfit(prices)
        print(f"{prices} -> {got} (expected {expected})")
