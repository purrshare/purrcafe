import threading
import time
import unittest

from _rwlock import RWLock  # Import your RWLock implementation


class TestRWLock(unittest.TestCase):

    def test_reader_writer_exclusion(self):
        lock = RWLock()
        data = 0

        def reader(expected: int) -> None:
            nonlocal self, data
            with lock.reader:
                self.assertEqual(data, expected)  # Ensure data is not modified by a writer

        def writer() -> None:
            nonlocal data
            with lock.writer:
                current_data = data
                time.sleep(0.05)
                current_data += 1
                time.sleep(0.05)
                data = current_data

        thread_groups = [
            [threading.Thread(target=writer) for _ in range(4)],
            [threading.Thread(target=reader, args=(2,)) for _ in range(3)]
        ]

        for thread_group in thread_groups:
            for thread in thread_group:
                thread.start()

            for thread in thread_group:
                thread.join()

    def test_multiple_writers(self):
        lock = RWLock()
        counter = 0

        def writer():
            nonlocal counter
            with lock.writer:
                counter_data = counter
                time.sleep(0.1)  # Simulate some work
                counter = counter_data + 1

        threads = [threading.Thread(target=writer) for _ in range(10)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(10, counter)  # Ensure readers don't interfere with each other

    def test_writer_starvation_prevention(self):
        lock = RWLock()
        data = 0

        def reader():
            nonlocal data
            while True:
                with lock.reader:
                    time.sleep(0.1)  # Simulate long-running readers

                time.sleep(0.1)

        def writer():
            nonlocal data
            with lock.writer:
                data += 1

        reader_thread = threading.Thread(target=reader)
        reader_thread.start()

        writer_threads = [threading.Thread(target=writer) for _ in range(5)]

        start_time = time.time()
        for thread in writer_threads:
            thread.start()

        for thread in writer_threads:
            thread.join(timeout=5)

        reader_thread.join()

        end_time = time.time()
        self.assertLess(end_time - start_time, 5)  # Ensure writers don't starve
        self.assertEqual(5, data)


if __name__ == '__main__':
    unittest.main()
