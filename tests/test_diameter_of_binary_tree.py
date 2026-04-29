from trees.diameter_of_binary_tree import DiameterOfBinaryTree, TreeNode

def build_tree():
    # [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def test_diameter_basic():
    sol = DiameterOfBinaryTree()
    assert sol.diameterOfBinaryTree(build_tree()) == 3