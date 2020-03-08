'''

Self-developed bubble sort algorithm

Time Complexity: O(n^2)
Best Time Complexity: O(n)
Space Complexity: O(1)

One thing to notice is that the best time for this algorithm can be achieved by using a little tweak shown in this
file to get O(n) complexity if the input is already sorted.

'''

import random

# function definition
def bubble_sort(nums):

    # null case
    if not nums:
        return None

    for i in range(len(nums) - 1):
        flag = True
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = False
        if flag:
            return nums

    return nums


def check_equal(nums1, nums2):
    if nums1 and nums2:
        if len(nums1) != len(nums2):
            return False
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                return False
        return True
    else:
        return nums1 == nums2


# main test run
if __name__ == "__main__":
    # generate an array of random numbers
    test_input = []
    for _ in range(1000):
        test_input.append(random.randint(-10, 10))
    input_copy = test_input.copy()

    test_result = bubble_sort(test_input)
    check_result = sorted(input_copy)

    print(check_equal(test_result, check_result))

