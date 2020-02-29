'''

80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.

Thoughts:
    Similar to Problem 26 and 27, we consider to use two pointers method to solve this problem
'''


# function definition
def removeDuplicates(nums):  # changes should be done in place, and return the length of the result array

    # allow one duplicate, so the first two elements (if exist) will never change
    if len(nums) <= 2:
        return len(nums)

    # start from the third element
    i, j = 2, 2

    # iterate over the entire array
    while j < len(nums):
        # if the previous two elements are not the same, change the log element and move on
        if nums[i-1] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
            j += 1
        else:
            # if the previous two elements are the same, and the current element is equal to them, there is no need
            # to change the log value
            if nums[j] == nums[i-1]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1

    return i

# main test run
if __name__ == "__main__":
    test_input = [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    i = removeDuplicates(test_input)
    print(test_input[:i])
