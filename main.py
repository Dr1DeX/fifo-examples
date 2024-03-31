from Fifo.utils.runner_classic_queue import runner_classic_queue
from Fifo.utils.runner_deque import runner_deque


class AcceptMethods:
    ClassicQueue = 1
    Deque = 2


def main():
    msg = """
Доступные FIFO-методы:
[1] Классическая очередь(Queue)
[2] Двухсторонняя очередь(Deque)\n
"""

    print(msg)
    try:
        cmd = int(input('Ввод команды: '))

        if cmd == AcceptMethods.ClassicQueue:
            runner_classic_queue()
        elif cmd == AcceptMethods.Deque:
            runner_deque()
    except ValueError:
        print('Ожидалось целое число!')


if __name__ == '__main__':
    main()
