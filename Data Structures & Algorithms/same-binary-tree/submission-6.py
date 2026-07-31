# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack1 = [p]
        stack2 = [q]
        while stack1 or stack2:
            s1 = stack1.pop()
            s2 = stack2.pop()

            if not s1 and not s2:
                continue
            if not s1 or not s2:
                return False

            if s1.val != s2.val:
                return False
            
            stack1.append(s1.left)
            stack1.append(s1.right)
            stack2.append(s2.left)
            stack2.append(s2.right)
        return len(stack1) == len(stack2)


      
            

        