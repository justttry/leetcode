#encoding:UTF-8
#author:justry
import os
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def hasLeftChild(self):
        return self.left
    
    def hasRightChild(self):
        return self.right
    
def insert(node, x):
    if x is None:
        return
    if x <= node.val:
        if node.hasLeftChild():
            insert(node.left, x)
        else:
            node.left = TreeNode(x)
    else:
        if node.hasRightChild():
            insert(node.right, x)
        else:
            node.right = TreeNode(x)
            
def print_tree(node):
    if node.val is not None:
        print(node.val)
    else:
        print('null')
    if node.hasLeftChild():
        print_tree(node.left)
    if node.hasRightChild():
        print_tree(node.right)
        

def rangeSumBST(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """
    if root is None or root.val is None:
        return 0
    else:
        in_range = L <= root.val <= R
    if root.left is None and root.right is None:
        sub_sum = 0
    elif root.left is None:
        sub_sum = rangeSumBST(root.right, L, R)
    elif root.right is None:
        sub_sum = rangeSumBST(root.left, L, R)
    else:
        sub_sum = rangeSumBST(root.left, L, R) +\
        rangeSumBST(root.right, L, R)
    if in_range:
        return root.val + sub_sum
    else:
        return sub_sum
    
            
class TreeNodeTest(unittest.TestCase):
    def test_0(self):
        l = [10,5,15,3,7,None,18]
        root = None
        for i in l:
            if root is None:
                root = TreeNode(i)
            else:
                insert(root, i)
        print_tree(root)
        ret = rangeSumBST(root, 7, 15)
        self.assertEqual(ret, 32)
        
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TreeNodeTest('test_0'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')