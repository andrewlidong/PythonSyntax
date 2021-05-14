'''
5. Copy linked list with arbitrary pointer

You are given a linked list where the node has two pointers. The first is the regular next pointer. The second pointer is called arbitrary_pointer and it can point to any node in the linked list. Your job is to write code to make a deep copy of the given linked list. Here, deep copy means that any operations on the original list (inserting, modifying and removing) should not affect the copied list.

Example

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Solution: 


For this problem, we will use a map to track the arbitrary nodes pointed by the original list. Then, we create a deep copy of the original linked list in two passes.

For the first pass, we create a copy of the original linked list. When create the new copy, use the same values for data and arbitrary_pointer in the copied list. Furthermore, it’s important to keep updating the map with entries where the key is the address to the old node and the value is the address of the new node.

Once we’ve created the copy, again we’ll pass the copied linked list and update the arbitrary pointers to the new address created in the first pass.

Time: O(N)
Space: O(N)
'''


def deep_copy_arbitrary_pointer(head):
   #TODO: Write - Your - Code
    return None
