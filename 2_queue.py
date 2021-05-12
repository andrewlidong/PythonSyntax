from queue import Queue

# Initializing a queue
q = Queue(maxSize=3)

# qsize() give the maxsize of the Queue
q.qsize()

# Adding of element to a queue
q.put('a')

# Return boolean for full queue
q.full()

# Removing element from queue
q.get()

# Return Boolean for empty Queue
q.empty()
