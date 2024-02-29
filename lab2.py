class QueueCapacityTypeError(Exception):
    """
    This exception gets raised when the queue is given the wrong type.
    """
    pass

class QueueCapacityBoundError(Exception):
    """
    This exception gets raised when the queue is given a negative or 0 value.
    """
    pass

class StackCapacityBoundError(Exception):
    """
    This exception gets raised when the stack is given a negative or 0 value.
    """
    pass

class StackCapacityTypeError(Exception):
    """
    This exception gets raised when the stack is given the wrong type.
    """
    pass

class QueueIsFull(Exception):
    """
    This exception is raised when the queue is full.
    """
    pass

class QueueIsEmpty(Exception):
    """
    This exception is raised when the queue is empty.
    """
    pass

class StackIsFull(Exception):
    """
    This exception is raised when the queue is full.
    """
    pass

class StackIsEmpty(Exception):
    """
    This exception is raised when the queue is empty.
    """
    pass


class PriorityQueue():
    """
    Description: The priority queue class. Implements the core methods.
    """

    def __init__(self, capacity) :
        """
        Constructor for the class.
        Inputs: size <- integer value for the size of the queue.
        """
        if (type(capacity) != int):
            raise QueueCapacityTypeError("Error: The capacity must be of type int.")
        elif(capacity < 0):
            raise QueueCapacityBoundError("Error: The capacity must be a positive int.")

        ######### YOUR CODE STARTS HERE #########
        self._heap = []
        self.capacity = capacity
        self.currentSize = 0

    def isEmpty(self):
        """
        Description: Return true when the priority queue is empty
        Usage: <PQ>.isEmpty()
        """
        ######### YOUR CODE STARTS HERE #########
        return self.currentSize == 0

    def isFull(self):
        """
        Description: Returns true if the queue is full else false.
        Usage: <PQ>.isFull()
        """
        ######### YOUR CODE STARTS HERE #########
        return self.currentSize == self.capacity

    def getParent(self, pos):
        """ Get parent of node at position <pos>. """
        ######### YOUR CODE STARTS HERE #########
        return (pos - 1) // 2

    def getLeftChild(self, pos):
        """ Get left child of node at position <pos>. """
        ######### YOUR CODE STARTS HERE #########
        return 2 * pos + 1

    def getRightChild(self, pos):
        """ Get right child of node at position <pos>. """
        ######### YOUR CODE STARTS HERE #########
        return 2 * pos + 2

    def swap(self, childPos, parentPos):
        """
        A helper method for restructuring the heap.
        Returns True if the node that was swapped or False if unchanged.
        Usage: self.swap(i, j)
        """
        ######### YOUR CODE STARTS HERE #########
        child = self._heap[childPos]
        self._heap[childPos] = self._heap[parentPos]
        self._heap[parentPos] = child

    def heapify(self, index):
        """
        Description: Bubbles down the node at index
        Usage: self.heapify(<index>)
        """
        ######### YOUR CODE STARTS HERE #########
        l = self.getLeftChild(index)
        r = self.getRightChild(index)

        if l < self.currentSize and self._heap[l][0] > self._heap[index][0]:
            largest = l
        else:
            largest = index

        if r < self.currentSize and self._heap[r][0] > self._heap[index][0]:
            largest = r

        if largest != index:
            self.swap(largest, index)
            self.heapify(largest)

    def insert(self, item):
        """
        Description: Insert a new item into the queue.
        An item = (priority, value) is a tuple.
        """
        ######### YOUR CODE STARTS HERE #########
        self._heap.append(item)
        currentIndex = self.currentSize

        parentIndex = self.getParent(currentIndex)

        while parentIndex >= 0 and self._heap[currentIndex][0] > self._heap[parentIndex][0]:
            self.swap(currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = self.getParent(currentIndex)

        self.currentSize += 1
        return True

    def extractMax(self):
        """
        Description: Remove and return the maximum item from the heap.
        Usage: returnValue = <PQ>.extractMax()
        """
        ######### YOUR CODE STARTS HERE #########
        returnValue = self._heap[0]
        lastNodePos = self.currentSize - 1
        self._heap[0] = self._heap[lastNodePos]
        self._heap.pop()
        self.currentSize -= 1
        self.heapify(0)
        return returnValue

    def peekMax(self):
        """
        Description: Returns the maximum item from the heap.
        Usage: bool = <pq>.peekMax()
        """
        ######### YOUR CODE STARTS HERE #########
        if self.isEmpty():
            return False
        else:
            return self._heap[0]
