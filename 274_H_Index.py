'''

274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.

Thoughts:
    Sorting is needed to reduce the time complexity. The best way is to use a counting sort, because we already know
    the upper limit of the groups, so this sorting's time complexity is reduced to O(n + n) = O(n), which is faster
    than a normal sorting algorithm with complexity of O(nlogn).
'''


# function definition
def hIndex(citations):  # given a list of numbers as citations, return the h-index

    # first decide the groups, and since we already know the upper limit is the length of the citation array we can
    # simply write out the groups
    groups = [0] * (len(citations)+1)

    # fill the groups with occurances
    for c in citations:
        if c > len(citations):
            groups[len(citations)] += 1
        else:
            groups[c] += 1

    # make the reference map
    for i in range(1, len(citations)+1):
        groups[i] = groups[i-1] + groups[i]

    # create the sorted array
    rst = [0] * (len(citations))
    for c in citations:
        if c <= len(citations):
            groups[c] -= 1
            rst[groups[c]] = c
        else:
            groups[len(citations)] -= 1
            rst[groups[len(citations)]] = c

    # check the h-index
    for i, c in enumerate(rst):
        if c >= len(citations) - i:
            return len(citations) - i

    return 0


# main test run
if __name__ == "__main__":
    test_input = [0, 5, 8, 2, 4, 7]
    print(hIndex(test_input))
