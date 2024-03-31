import abc


class BaseQueue(abc.ABC):

    @abc.abstractmethod
    def is_empty(self):
        pass

    @abc.abstractmethod
    def push(self, x):
        pass

    @abc.abstractmethod
    def pop(self):
        pass
