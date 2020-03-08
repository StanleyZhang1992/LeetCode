'''

Self-developed quick sort algorithm

Time Complexity: O(nlogn)
Worst Complexity: O(n^2)
Space Complexity: O(logn)

This algorithm is a popular sorting algorithm that is being used in the source code of some programming languages. It uses the concepts of pivot and partition.

'''

import random

# function definition
def quick_sort(nums):

    # null case
    if not nums:
        return None

    # edge case
    if len(nums) == 1:
        return nums

    # main part -- pivot and partition
    partition(nums, 0, len(nums)-1)

    return nums


# partition step
def partition(nums, lo, hi): # the first input always being the whole array, the other two inputs define the part of
    # the array that is being manipulated/sorted

    # boundary condition
    if lo >= hi:
        return

    # randomly pick the pivot
    pivot_ptr = random.randint(lo, hi)
    nums[pivot_ptr], nums[hi] = nums[hi], nums[pivot_ptr]
    pivot = nums[hi]
    i = lo
    j = hi

    while True:
        while i < hi:
            if nums[i] <= pivot:
                i += 1
            else:
                break
        while j > lo:
            if nums[j] >= pivot:
                j -= 1
            else:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        else:
            nums[i], nums[hi] = nums[hi], nums[i]
            break

    # recursively sort the array
    partition(nums, lo, i-1)
    partition(nums, i+1, hi)


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


def run_test(times, array_len):
    for _ in range(times):
        # generate an array of random numbers
        test_input = []
        for _ in range(array_len):
            test_input.append(random.randint(-10, 10))
        # make a copy for verification
        input_copy = test_input.copy()
        # test my own method by comparing with the python sorting method
        test_result = quick_sort(test_input)
        check_result = sorted(input_copy)
        if not check_equal(test_result, check_result):
            return False
    return True


# main test run
if __name__ == "__main__":
    print(run_test(100, 35))

