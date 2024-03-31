from Fifo.library.deque import Deque


def runner_deque():
    try:
        max_size = int(input('Размер очереди: '))
        deque = Deque(max_size)

        deque.runner()
    except ValueError:
        print('Что-то пошло не так....')


if __name__ == '__main__':
    runner_deque()
