import sys

from Fifo.library.BaseQueue import BaseQueue
from Fifo.utils.exceptions import FullArrException, EmptyArrException


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
        if self.is_empty():
            return False
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        return x

    def __interface_commander(self):
        for _ in range(self.max_size):
            print('Введите команду и число: ')
            try:
                line = sys.stdin.readline().rstrip().split(' ')
                cmd = line[0]
                if len(line) > 1:
                    val = int(line[-1])
                    if cmd == 'push':
                        try:
                            self.push(val)
                        except FullArrException:
                            print('error: full queue')
                elif cmd == 'pop':
                    try:
                        print(self.pop())
                    except EmptyArrException:
                        print('error: empty queue')
                else:
                    print(f'Команда "{cmd}" не распознана')
            except Exception as e:
                print(e)

    def runner(self):
        return self.__interface_commander()
