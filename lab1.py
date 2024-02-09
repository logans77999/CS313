class QueueCapacityTypeError(Exception):
    pass


class QueueCapacityBoundError(Exception):
    pass


class QueueIsFull(Exception):
    pass


class QueueIsEmpty(Exception):
    pass


class StackCapacityTypeError(Exception):
    pass


class StackIsFull(Exception):
    pass


class StackIsEmpty(Exception):
    pass


class StackCapacityBoundError(Exception):
    pass


class Node:

    def __init__(self, data=None):
        """

        """
        ####### YOUR CODE STARTS HERE #######
        self.data = data
        self.next = None

class Queue:

    def __init__(self, capacity):
        """

        """
        if type(capacity) != int:
            raise QueueCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise QueueCapacityBoundError('Invalid capacity')
        else:
            ####### YOUR CODE STARTS HERE #######
            self.head = None
            self.tail = None
            self.capacity = capacity
            self.currentSize = 0

    def enqueue(self, item):
        ####### YOUR CODE STARTS HERE #######
        if self.isFull():
            #return False
            raise QueueIsFull("Queue is full. Cannot enqueue!.")
        else:
            new_node = Node(data=item)
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            self.currentSize += 1
            return True

    def dequeue(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            raise QueueIsEmpty("Queue is Empty")
        else:
            data = self.head.data

            if self.currentSize == 1:
                self.head = None
                self.tail = None
            else:
                old_head = self.head
                self.head = old_head.next
                old_head.next = None
            
            self.currentSize -= 1
          
            return data

    def front(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            return False
        else:
            return self.head.data

    def isEmpty(self):
        ####### YOUR CODE STARTS HERE #######
        if self.currentSize == 0:
        	return True
        else:
        	return False

    def isFull(self):
        ####### YOUR CODE STARTS HERE #######
        if self.currentSize == self.capacity:
        	return True
        else:
        	return False

class Stack:

    def __init__(self, capacity):
        """

        """
        if type(capacity) != int:
            raise StackCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise StackCapacityBoundError('Invalid capacity')
        else:
            ####### YOUR CODE STARTS HERE #######
            self.head = None
            self.capacity = capacity
            self.currentSize = 0

    def push(self, item):
        ####### YOUR CODE STARTS HERE #######
        if self.isFull():
            raise StackIsFull("Stack is full")
        else:
            new_node = Node(data=item)
        
            if self.isEmpty():
                self.head = new_node
            else:
                new_node.next = self.head
 
                self.head = new_node

            self.currentSize += 1
            return True

    def pop(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            raise StackIsEmpty("Stack is Empty")
        else:
            data = self.head.data

            if self.currentSize == 1:
                self.head = None
         
            else:
                old_head = self.head
                self.head = old_head.next
                old_head.next = None

            self.currentSize -= 1

            return data

    def peek(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            return False
        else:
            return self.head.data

    def isEmpty(self):
        ####### YOUR CODE STARTS HERE #######
        return self.currentSize == 0

    def isFull(self):
        ####### YOUR CODE STARTS HERE #######
        return self.currentSize == self.capacity

