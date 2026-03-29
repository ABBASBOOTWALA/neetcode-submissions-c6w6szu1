# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = [[root]]
        row_index = 0

        while(1):
            child_node = []
            for node in result[row_index]:
                if node.left:
                    child_node.append(node.left)
                if node.right:
                    child_node.append(node.right)
            if child_node:
                result.append(child_node)
                row_index += 1
            else:
                break
        
        for idx, row in enumerate(result):
            result[idx] = [node.val for node in row]

        return result
            



