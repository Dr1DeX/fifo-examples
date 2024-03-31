import sys

from Fifo.library.BaseQueue import BaseQueue
from Fifo.utils.exceptions import EmptyArrException


class ClassicQueue(BaseQueue):
    queue: list[int]  # type hint
    max_size: int
    tail: int
    head: int
    size: int

    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.tail = 0
        self.head = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def pop(self):
        try:
            if self.is_empty():
                raise EmptyArrException
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            return x
        except EmptyArrException:
            print('error: empty queue')

    def __parser_commander(self):
        for _ in range(self.max_size):
            print('Введите команду: ')
            line = sys.stdin.readline().rstrip().split(' ')
            cmd = line[0]
            if len(line) > 1:
                val = int(line[-1])
                if cmd == 'push':
                    self.push(val)
            elif cmd == 'pop':
                res = self.pop()
                if res is not None:
                    print(res)
                else:
                    print('error: empty queue')
            else:
                print(f'Команда "{cmd}" не распознана')

    def runner(self):
        return self.__parser_commander()
