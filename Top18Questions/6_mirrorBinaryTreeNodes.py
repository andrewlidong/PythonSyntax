'''
6. Mirror binary tree nodes

Given the root node of a binary tree, swap the ‘left’ and ‘right’ children for each node. The below example shows how the mirrored binary tree should look like.

Solution: 

This problem is quite straightforward. For this algorithm, we will utilize a post order traversal of the binary tree. For each node, we will swap its left and right child.

# Time: O(N)
# Space: O(N)
'''


def mirror_tree_node(node):
