'''

Self-developed merge sort algorithm

Time Complexity: O(nlogn)
Space Complexity: O(n)

This algorithm is the most popular sorting algorithm that is widely used in the source code of Java, Python,
etc (as a matter of fact, the real one being used is called Tim Sort, but it is based on the merge sort algorithm).
It implements the concept of divide and conquer.

'''

import random

# function definition
# divide step
def merge_sort(nums):

    # null case
    if not nums:
        return None

    if len(nums) == 1:
        return nums

    # divide the array into two halves
    lo, hi = 0, len(nums) - 1
    mid = lo + (hi - lo) // 2
    left = nums[: mid+1]
    right = nums[mid+1 :]

    # merge the two halves
    return merge(merge_sort(left), merge_sort(right))

# conquer step
def merge(left, right):
    i, j, k = 0, 0, 0
    res = [0] * (len(left) + len(right))

    # merge the items in two halves one by one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res[k] = left[i]
            i += 1
            k += 1
        else:
            res[k] = right[j]
            j += 1
            k += 1

    # if one half is done, merge the rest of another half into the result
    if i == len(left):
        res[k :] = right[j :]
    else:
        res[k :] = left[i :]

    return res


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
        test_result = merge_sort(test_input)
        check_result = sorted(input_copy)
        if not check_equal(test_result, check_result):
            return False
    return True


# main test run
if __name__ == "__main__":
    print(run_test(20, 50))

