"""
Write a recursive function that returns the frequency of a key given as input in a Binary Tree.

"""

class TreeNode(object):
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def get_count(root,key):
    if root is None:
        return 0
    if root.val==key:
         return 1+get_count(root.left,key)+get_count(root.right,key)
    else:
         return get_count(root.left,key)+get_count(root.right,key)


root= TreeNode(5)
left_node=TreeNode(1)
right_node=TreeNode(5)
right_node.left=TreeNode(50)
root.left=left_node
root.right=right_node
print(get_count(root,5))
