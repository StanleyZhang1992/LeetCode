'''

120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Thoughts:
    It asks for the "minimum sum" of a path to the bottom. It is a sign that we can use a dynamic programming algorithm.
'''


def minimumTotal(triangle) -> int:

    # null case
    if not triangle:
        return None

    # initialize the record table
    record = []
    for _ in range (len(triangle)):
        record.append([])

    for j in range(len(triangle)):
        for _ in range(0, j + 1):
            record[j].append(0)

    record[0][0] = triangle[0][0]

    # build the table
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j - 1 >= 0 and j < i:
                record[i][j] = min(record[i - 1][j - 1] + triangle[i][j], record[i - 1][j] + triangle[i][j])
            else:
                if j - 1 < 0:
                    record[i][j] = record[i - 1][j] + triangle[i][j]
                else:
                    record[i][j] = record[i - 1][j - 1] + triangle[i][j]

    # return the result
    return min(record[len(triangle) - 1])

if __name__ == "__main__":
    test_input = [
                     [2],
                    [3,4],
                   [6,5,7],
                  [4,1,8,3]
                ]
    print(minimumTotal(test_input))