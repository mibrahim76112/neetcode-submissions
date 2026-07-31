# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        best = 0
        heights = {None: 0}
        stack = [(root,False)]

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            
            if not visited:
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left,False))
            else:
                lh = heights[node.left]
                rh = heights[node.right]
                best = max(best, lh + rh)
                heights[node] = 1 + max(lh, rh)
            
        return best

            
            


