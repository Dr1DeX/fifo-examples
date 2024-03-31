import unittest
from Fifo.library.classic_queue import ClassicQueue


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


if __name__ == '__main__':
    unittest.main()
