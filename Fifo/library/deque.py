import sys

from Fifo.library.BaseQueue import BaseQueue
from Fifo.utils.exceptions import (FullArrException,
                                   EmptyArrException,
                                   UnknownCommand)


class Deque(BaseQueue):
    queue: list[int]  # type hint
    max_size: int
    front_q: int
    back_q: int

    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front_q = -1
        self.back_q = - 1

    def is_empty(self):
        return self.front_q == -1

    def __is_full_queue(self):
        return (self.back_q + 1) % self.max_size == self.front_q

    def push(self, x):
        if self.__is_full_queue():
            raise FullArrException
        elif self.is_empty():
            self.front_q = 0
            self.back_q = 0
            self.queue[self.front_q] = x
        else:
            self.front_q = (self.front_q - 1 + self.max_size) % self.max_size
            self.queue[self.front_q] = x

    def push_back(self, x):
        if self.__is_full_queue():
            raise FullArrException
        elif self.is_empty():
            self.front_q = 0
            self.back_q = 0
            self.queue[self.back_q] = x
        else:
            self.back_q = (self.back_q + 1) % self.max_size
            self.queue[self.back_q] = x

    def pop(self):
        if self.is_empty():
            raise EmptyArrException
        elif self.front_q == self.back_q:
            x = self.queue[self.front_q]
            self.front_q = -1
            self.back_q = -1
            return x
        else:
            x = self.queue[self.front_q]
            self.front_q = (self.front_q + 1) % self.max_size
            return x

    def pop_back(self):
        if self.is_empty():
            raise EmptyArrException
        elif self.front_q == self.back_q:
            x = self.queue[self.back_q]
            self.front_q = -1
            self.back_q = -1
            return x
        else:
            x = self.queue[self.back_q]
            self.back_q = (self.back_q - 1 + self.max_size) % self.max_size
            return x

    def __parser_commander(self):
        for _ in range(self.max_size):
            line = sys.stdin.readline().rstrip().split(' ')
            cmd = line[0]
            try:
                if len(line) > 1:
                    val = int(line[-1])
                    if cmd == 'push':
                        try:
                            self.push(val)
                        except FullArrException:
                            print('error: full queue')
                    elif cmd == 'push_back':
                        try:
                            self.push_back(val)
                        except FullArrException:
                            print('error: full queue')
                elif cmd == 'pop':
                    try:
                        print(self.pop())
                    except EmptyArrException:
                        print('error: empty queue')
                elif cmd == 'pop_back':
                    try:
                        print(self.pop_back())
                    except EmptyArrException:
                        print('error: empty queue')
                else:
                    raise UnknownCommand
            except UnknownCommand:
                print(f'Команда {cmd} не распознана')

    def runner(self):
        return self.__parser_commander()
