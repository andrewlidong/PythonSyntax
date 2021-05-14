'''
4. Delete node with a given key

We are given the head of a linked list and a key. We have to delete the node that contains this given key. The following two examples elaborate on this problem further.

Example

Input: head = [4,5,1,9], key = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Solution:

First, we have to find the key in the linked list. We’ll keep two pointers, current and previous, as we iterate the linked list.

If the key is found in the linked list, then the current pointer would be pointing to the node containing the key to be deleted. The previous should be pointing to the node before the key node.

This can be done in a linear scan and we can simply update current and previous pointers as we iterate through the linked list.

Time: O(N)
Space: O(1)
'''


def delete_node(head, key):
    prev = None
    current = head

    while (current != None):
        if current.data == key:
            if current == head:
                head = head.next
                current = head
            else:
                prev.next = current.next
                current = current.next
        else:
            prev = current
            current = current.next

    # if key not found in list
    if current == None:
        return head

    return head


list_head = create_random_list(10)
print("Original:")
display(list_head)

lst = to_list(list_head)

print("\nDeleting " + str(lst[5]), end="")
list_head = delete_node(list_head, lst[5])
print("\nAfter Delete LinkedListNode:")
display(list_head)

print("\nDeleting (Non-Existing) " + str(101), end="")
list_head = delete_node(list_head, 101)
print("\nAfter Delete LinkedListNode:")
display(list_head)

print("\nDeleting 1st node:" + str(lst[0]), end="")
list_head = delete_node(list_head, lst[0])
print("\nAfter Delete 1st LinkedListNode:")
display(list_head)

lst = to_list(list_head)
print("\nDeleting last node:" + str(lst[-1]), end="")
list_head = delete_node(list_head, lst[-1])
print("\nAfter Delete last LinkedListNode:")
display(list_head)
