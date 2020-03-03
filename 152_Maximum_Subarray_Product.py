'''

152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Thoughts:
    Looking for the "maximum" product. Thus, we can use dynamic programming. Figure out the state transfer function
    and we will be able to solve it. It's a little tricky because in this case we need to keep track of two records
    since the sign of a current number can affect the product significantly.
'''


# function definition
def maxProduct(nums) -> int:

    # edge cases
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    # two cache tables for two records, also need to keep track of the maximum product
    max_prod = [None] * len(nums)
    min_prod = [None] * len(nums)
    max_prod[0], min_prod[0], rtn = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        # use the state transfer functions here
        max_prod[i] = max(max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i], nums[i])
        min_prod[i] = min(max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i], nums[i])
        rtn = max(rtn, max_prod[i]) # update the maximum product

    return rtn


# main test run
if __name__ == "__main__":
    test_input = [0, 5, 8, -2, 4, -7]
    print(maxProduct(test_input))
