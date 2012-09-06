import os, sys
from collections import deque

#
# The trouble with Python is that its list implementation is so damned good
# that you have to work very hard to need a double-headed list/queue/stack
# except for slight convenience.
#

#
# Implement Stack or Queue
#
class Stack(object):

    def __init__(self):
        self._deque = deque()

    def push(self, item):
        self._deque.append(item)

    def pop(self):
        return self._deque.pop()

class Queue(object):

    def __init__(self):
        self._deque = deque()

    def push(self, item):
        self._deque.appendleft(item)

    def pop(self):
        return self._deque.pop()

