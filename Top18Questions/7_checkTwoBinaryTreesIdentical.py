'''
7. Check if two binary trees are identical
Given the roots of two binary trees, determine if these trees are identical or not. Identical trees have the same layout and data at each node.

Example

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

Solution: 

This problem can be tackled using recursion. The base case of the recursive solution would be when both nodes being compared are null or one of them is null.

Two trees being compared are identical if:

data on their roots is the same
the left sub-tree of ‘A’ is identify to the left sub-tree of ‘B’
the right sub-tree of ‘A’ is identical to the right sub-tree of ‘B’
Using recursion, we can solve this problem through a depth-first traversal on both trees simultaneously while comparing the data at each node.

Time: O(N)
Space: O(N)
'''


def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        return (root1.data and root2.data and are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right))

    return False


arr1 = [100, 50, 200, 25, 125, 350]
arr2 = [1, 2, 10, 50, 180, 199]
root1 = create_BST(arr1)
display_level_order(root1)
root2 = create_BST(arr2)

display_level_order(root2)
if(are_identical(root1, root2)):
    print("The trees are identical")
else:
    print("The trees are not identical")
