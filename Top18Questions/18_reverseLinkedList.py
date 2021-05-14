'''
18. Reverse a linked list
Reverse a singly linked list. See the example below.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Let’s take a look at the iterative approach.

If the linked list has 0 or 1 nodes, then the current list can be returned as is. If there are two or more nodes, then the iterative approach starts with two pointers:

reversed_list: A pointer to already reversed linked list.

list_to_do: A pointer to the remaining list.

Then, we set reversed_list->next to NULL. This becomes the last node of the reversed linked list.

For each iteration, the list_to_do pointer moves forward. The current node becomes the new head of the reversed linked list. The loop terminates when we hit NULL.

Time: O(N)
Space: O(1)

'''


def reverse(head):
    reversed_list = head
    #TODO: Write - Your - Code
    return reversed_list
