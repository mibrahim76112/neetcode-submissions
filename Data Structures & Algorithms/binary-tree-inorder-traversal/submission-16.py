# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        curr = root
        arr = []
        s = []
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            print(curr.val)
            arr.append(curr.val)
            curr = curr.right
  
       
        return arr


