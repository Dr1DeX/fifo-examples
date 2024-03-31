import unittest
from Fifo.library.classic_queue import ClassicQueue
from Fifo.library.deque import Deque


class TestClassicQueue(unittest.TestCase):
    def test_runner_classic_queue(self):
        corner_case = [
            (3, [1, 2, 3], [1, 2, 3]),
        ]

        for n, params, expected in corner_case:
            with self.subTest(n=n, params=params, expected=expected):
                queue_instance = ClassicQueue(n)
                queue_instance.push(params)
                self.assertEqual(queue_instance.pop(), expected)

    def test_empty_buffer(self):
        corner_case = [
            (1, None)
        ]

        for n, expected in corner_case:
            with self.subTest(n=n, expected=expected):
                queue_instance = ClassicQueue(n)
                self.assertEqual(queue_instance.pop(), expected)


class TestDeque(unittest.TestCase):
    def test_push(self):
        corner_case = [
            (2, [1, 2], [1, 2]),
        ]

        for n, params, expected in corner_case:
            with self.subTest(n=n, params=params, expected=expected):
                deque_instance = Deque(n)
                deque_instance.push(params)
                self.assertEqual(deque_instance.pop(), expected)

    def test_push_back(self):
        corner_case = [
            (2, [1, 2], [1, 2]),
        ]

        for n, params, expected in corner_case:
            with self.subTest(n=n, params=params, expected=expected):
                deque_instance = Deque(n)
                deque_instance.push(params)
                self.assertEqual(deque_instance.pop_back(), expected)


if __name__ == '__main__':
    unittest.main()
