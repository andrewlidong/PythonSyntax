'''
13. LRU

Least Recently Used (LRU) is a common caching strategy. It defines the policy to evict elements from the cache to make room for new elements when the cache is full, meaning it discards the least recently used items first.

Example

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Solution:

To implement an LRU cache we use two data structures: a hashmap and a doubly linked list. A doubly linked list helps in maintaining the eviction order and a hashmap helps with O(1) lookup of cached keys. Here goes the algorithm for LRU cache.

If the element exists in hashmap
    move the accessed element to the tail of the linked list
Otherwise,
    if eviction is needed i.e. cache is already full
        Remove the head element from doubly linked list and delete its hashmap entry
    Add the new element at the tail of linked list and in hashmap
Get from Cache and Return

Note that the doubly linked list is used to keep track of the most recently accessed elements. The element at the tail of the doubly linked list is the most recently accessed element. All newly inserted elements (in put) go the tail of the list. Similarly, any element accessed (in get operation) goes to the tail of the list.

Time:
Get: O(N)
Set: O(1)
Deletion at Head: O(1)
Search for deleting and adding to tail: O(N)

Space: O(N)
'''

# Linked list operations
# insert_at_tail(self, key, data)
# remove(self, data)
# remove_node(self, node)
# remove_head(self)
# remove_tail(self)
# get_head(self)
# get_tail(self)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.cache_vals = LinkedList()

    def set(self, key, value):
        node = self.get(value)
        if node is None:
            if self.cache_vals > self.capacity:
                self.cache_vals.insert_at_tail(key, value)
                self.cache.add(value)
                self.cache.remove(self.cache_vals.get_head().data)
                self.cach_vals.remove_head()
            else:
                self.cache_vals.insert_at_tail(key, value)
                self.cache.add(value)

        else:
            self.cache_vals.remove(value)
            self.cache_vals.insert_at_tail(key, value)

    def get(self, value):
        if value not in self.cache:
            return None
        else:
            i = self.cache.get_head()
            while i is not None:
                if i.data is value:
                    return i
                i = i.next

    def printcache(self):
        node = self.cache_vals.get_head()
        while node != None:
        print("(" + str(node.key) + "," + str(node.data) + ")", end="")
        node = node.next
        print()


cache1 = LRUCache(2)
cache1.Set(10, 20)
cache1.printcache()

cache1.Set(15, 25)
cache1.printcache()

cache1.Set(20, 30)
cache1.printcache()

cache1.Set(25, 35)
cache1.printcache()

cache1.Set(5, 25)
cache1.printcache()
