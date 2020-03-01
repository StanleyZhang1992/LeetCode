'''

55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

Thoughts:
    From the rear go to the front, record the current last step and update it if the previous position can reach to
    the current last step. Finally, check if the first position is the current last step (if it is, then it can reach the last step)
'''


# function definition
def canJump(nums):

    # edge cases
    if not nums:
        return False

    if len(nums) < 2:
        return True

    # initialize the last step and the log index
    last = len(nums) - 1
    i = len(nums) - 2

    # rules to update the last step (indicates the ability to reach the last step)
    while i >= 0:
        if nums[i] + i >= last:
            last = i
        i -= 1

    # The last step is to check if the first position can reach to the last step
    return last == 0

# main test run
if __name__ == "__main__":
    test_input = [3, 2, 1, 1, 4]
    print(canJump(test_input))
