'''

Self-developed selection sort algorithm

Time Complexity: O(n^2)
Space Complexity: O(1)

This algorithm is the most natural sorting algorithm. Therefore, it has a "brute force" nature. It's easy to think
of, but it has the worst performance in terms of time complexity in all kinds of sorting algorithms.

'''

import random

# function definition
def selection_sort(nums):

    # null case
    if not nums:
        return None

    for i in range(len(nums) - 1):
        min_ptr = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_ptr]:
                min_ptr = j
        nums[i], nums[min_ptr] = nums[min_ptr], nums[i]

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
    for _ in range(10):
        test_input.append(random.randint(-10, 10))
    input_copy = test_input.copy()

    test_result = selection_sort(test_input)
    check_result = sorted(input_copy)

    print(check_equal(test_result, check_result))

