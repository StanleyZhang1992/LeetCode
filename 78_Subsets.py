'''

78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Thoughts:
    We use backtracking to solve this problem.
'''


# function definition
def subsets(nums):

    # DFS helper using recursion
    def helper(res, cur, nums, index):

        if index == len(nums):
            res.append(cur.copy())
            return

        # include nums[index] in the result
        cur.append(nums[index])
        helper(res, cur, nums, index + 1)
        # exclude nums[index] in the result
        cur.pop()
        helper(res, cur, nums, index + 1)

    # null case
    if not nums:
        return []

    res = []
    helper(res, [], nums, 0)

    return res


# main test run
if __name__ == "__main__":
    test_input = nums = [1,2,3]
    print(subsets(test_input))
