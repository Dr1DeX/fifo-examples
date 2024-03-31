from Fifo.library.classic_queue import ClassicQueue


def runner_classic_queue():
    try:
        n = int(input('Размер очереди: '))
        queue = ClassicQueue(n)
        queue.runner()
    except ValueError:
        print('Что то пошло не так...')


if __name__ == '__main__':
    runner_classic_queue()
