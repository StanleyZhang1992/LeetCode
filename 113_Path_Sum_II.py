'''

113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

Thoughts:
    Use DFS to solve this problem.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# function definition
def pathSum(root, s):
    if not root:
        return []

    stack = []
    cur = [root.val]
    stack.append((root, cur))
    res = []

    while stack:

        node, cur_array = stack.pop()

        if not node.left and not node.right:
            # dfs reaches a leaf
            if sum(cur_array) == s:
                res.append(cur_array.copy())

        if node.right:
            apd = cur_array + [node.right.val]
            stack.append((node.right, apd))

        if node.left:
            apd = cur_array + [node.left.val]
            stack.append((node.left, apd))

    return res


# main test run
if __name__ == "__main__":
    n5 = TreeNode(5)
    n3 = TreeNode(3)
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n0 = TreeNode(0)

    n5.left = n3
    n5.right = n2
    n3.right = n1
    n2.left = n0

    print(pathSum(n5, 7))