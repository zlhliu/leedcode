# 此处的left和right都是Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif not p.val != q.val:
            return False
        return Solution.isSameTree(p.right, q.right) and Solution.isSameTree(p.left, q.left)



if __name__ == '__main__':
    a = TreeNode()
    b = TreeNode()
    a.val = 1


    print(Solution.isSameTree(b, a, c))