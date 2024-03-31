import abc


class BaseQueue(abc.ABC):
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.tail = 0
        self.head = 0
        self.size = 0

    @abc.abstractmethod
    def is_empty(self):
        pass

    @abc.abstractmethod
    def push(self, x):
        pass

    @abc.abstractmethod
    def pop(self):
        pass

