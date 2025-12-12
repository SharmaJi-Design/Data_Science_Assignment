# Tree (Scratch Binary Search Tree)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

print("Inorder traversal of tree:")
inorder(root)
print()