'''
46. Permutations
    Given a collection of distinct integers, return all possible permutations.

Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

Thoughts:
    Since this problem is asking about "ALL" possible combinations, it is a backtracking problem.
'''


# function definition
def permute(nums):  # the input is a list of integers, the return is a list of a list of integers
    res = []
    helper(nums, [], res)  # using the helper function to achieve backtracking
    return res


def helper(rem, cur, res):  # the funtion's inputs are the left numbers to permute, the current combination,
    # and the result. The result is passed by reference so it's always changing. But the other two inputs should be
    # passed by values to ensure all possible permutations

    # this is the base case. When there is no chance for permutation, add the current combination to the result.
    if not rem:
        res.append(cur)

    # if there is any chance for permutation, make sure to exploit all chances by iterating over all remaining numbers.
    for i in range(len(rem)):
        remain = rem[:i] + rem[i + 1:]
        acc = cur + [rem[i]]
        helper(remain, acc, res)  # essentially perform depth first search, pass the first two inputs new values and
        # the last one by its reference to update it in place


# main test run
if __name__ == "__main__":
    test_input = [3, 5, 7, 8]
    print(permute(test_input))
