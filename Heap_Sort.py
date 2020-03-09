'''

Self-developed heap sort algorithm

Time Complexity: O(nlogn)

This algorithm uses the heap structure to sort an array. The hard part is to maintain the heap structure.

'''

import random

# function definition
def heap_sort(nums):

    if not nums:
        return []

    last_idx = len(nums) - 1
    while last_idx > 0:
        helper(nums, last_idx)
        nums[0], nums[last_idx] = nums[last_idx], nums[0]
        last_idx -= 1

    return nums


def helper(nums, k):
    # maintain the heap strcuture
    last_parent = (k - 1) // 2
    while last_parent >= 0:
        sift(nums, last_parent, k)
        last_parent -= 1


def sift(nums, par, limit):
    # if par still has children/child
    while par * 2 + 1 <= limit:
        lc = par * 2 + 1
        rc = par * 2 + 2

        # if the right child exists
        if rc <= limit:
            if nums[par] >= max(nums[lc], nums[rc]):
                break
            else:
                if nums[lc] >= nums[rc]:
                    nums[par], nums[lc] = nums[lc], nums[par]
                    par = lc
                else:
                    nums[par], nums[rc] = nums[rc], nums[par]
                    par = rc

        else: # if only has the left child
            if nums[par] >= nums[lc]:
                break
            else:
                nums[par], nums[lc] = nums[lc], nums[par]
                par = lc


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
        test_result = heap_sort(test_input)
        check_result = sorted(input_copy)
        if not check_equal(test_result, check_result):
            return False
    return True


# main test run
if __name__ == "__main__":
    print(run_test(20, 30))

