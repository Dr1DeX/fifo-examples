import sys
from Fifo.library.classic_queue import ClassicQueue


def main():
    try:
        n = int(input('Размер очереди: '))
        queue = ClassicQueue(n)
    except TypeError:
        print('Что то пошло не так...')


if __name__ == '__main__':
    main()
