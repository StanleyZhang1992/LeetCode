'''

209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Thoughts:
    This is a good chance to use the two pointers method to reduce the time complexity. We only need to go through
    the entire list once.
'''


def minSubArrayLen(s: int, nums):

    # null case
    if not nums:
        return 0

    # initialize
    i, j = 0, 0
    cur_sum = 0
    min_len = float("inf")
    flag = 1

    # iterate over the whole list
    while j < len(nums):
        # cur_sum depends on the flag
        if flag > 0:
            cur_sum += nums[j]
        else:
            cur_sum -= nums[i-1]

        # according to cur_sum and s values, decide the min_len's change, i and j's moves, and the flag's change
        if cur_sum >= s:
            min_len = min(j - i + 1, min_len)
            i += 1
            flag = -1
        else:
            j += 1
            flag = 1

    # return 0 if there is no valid cases
    return 0 if min_len == float("inf") else min_len

if __name__ == "__main__":
    print(minSubArrayLen(s = 7, nums = [2, 3, 1, 2, 4, 3]))