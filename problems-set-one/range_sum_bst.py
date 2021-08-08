class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def get_sum_range(root,low,high):
    sum=0
    stack =[root]
    while stack:
        current_node = stack.pop()
        if current_node:
            if current_node.val >= low and current_node.val <= high:
                sum += current_node.val
            if current_node.val > low:
                stack.append(current_node.left)
            if current_node.val < high:
                stack.append(current_node.right)
    return sum

root= TreeNode(5)
left_node=TreeNode(1)
right_node=TreeNode(10)
root.left=left_node
root.right=right_node
print(get_sum_range(root,2,10))
