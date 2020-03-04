'''

221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

Thoughts:
    Since this problem is asking for the maximum sub-square's area, we use dynamic programming.
'''


# function definition
def maximalSquare(matrix) -> int:

    # null case
    if not matrix:
        return 0

    # initialization
    max_area = 0
    dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        dp[i][0] = int(matrix[i][0])
    for j in range(len(matrix[0])):
        dp[0][j] = int(matrix[0][j])

    # build up the record table
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if int(matrix[i][j]) == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    # get the max area
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            max_area = max(max_area, dp[i][j])

    return max_area ** 2


# main test run
if __name__ == "__main__":
    test_input = [0, 5, 8, 2, 4, 7]
    print(hIndex(test_input))
