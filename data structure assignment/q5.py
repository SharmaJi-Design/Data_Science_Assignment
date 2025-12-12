# Tree (Binary Tree using Class)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)


print("Root value:", root.value)
print("Left child:", root.left.value)
print("Right child:", root.right.value)