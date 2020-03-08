'''

Self-developed insertion sort algorithm

Time Complexity: O(n^2)
Best Time Complexity: O(n)
Space Complexity: O(1)

This algorithm is very similar to the bubble sort algorithm.

'''

import random

# function definition
def insertion_sort(nums):

    # null case
    if not nums:
        return None

    for i in range(1, len(nums)):
        temp = nums[i]
        flag = False
        for j in range(i, 0, -1):
            if temp < nums[j-1]:
                nums[j] = nums[j-1]
            else:
                flag = True
                break
        # different replacement for cases when the comparing loop is broken or not
        if flag:
            nums[j] = temp
        else:
            nums[j-1] = temp


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


def run_test(times, array_len):
    for _ in range(times):
        # generate an array of random numbers
        test_input = []
        for _ in range(array_len):
            test_input.append(random.randint(-10, 10))
        # make a copy for verification
        input_copy = test_input.copy()
        # test my own method by comparing with the python sorting method
        test_result = insertion_sort(test_input)
        check_result = sorted(input_copy)
        if not check_equal(test_result, check_result):
            return False
    return True


# main test run
if __name__ == "__main__":
    print(run_test(20, 50))
