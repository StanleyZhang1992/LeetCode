'''

Self-developed counting sort algorithm

Time Complexity: O(n * k), when k is small, this is O(n), which is better than merge sort or quick sort.
Space Complexity: O(n * k)

This algorithm is one of the "bucket sort" algorithms. It does not compare numbers. Instead, it uses a map to store
the number of appearance of each number, and then use this information to get the order of a certain number in the
array. When the range of the numbers is small and you have a lot of numbers, this algorithm is preferable than other
sorting algorithms.
To extend this algorithm, there is radix sort, which is based on this sorting algorithm, but solves more complicated
problems in which there are multiple element/radix(s) to be dealt with.

'''

import random

# function definition
def counting_sort(nums):

    # null case
    if not nums:
        return None

    res = []

    # create the buckets
    buckets = [0] * (max(nums) - min(nums) + 1)
    diff = 0 - min(nums)
    for n in nums:
        buckets[n + diff] += 1

    for i in range(len(buckets)):
        for j in range(buckets[i]):
            res.append(i - diff)

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
        test_result = counting_sort(test_input)
        check_result = sorted(input_copy)
        if not check_equal(test_result, check_result):
            return False
    return True


# main test run
if __name__ == "__main__":
    print(run_test(100, 5000))

