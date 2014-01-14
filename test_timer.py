from timer import Timer

import unittest
import time

class TestTimer(unittest.TestCase):

    def test_init(self):
        timer = Timer()
        time.sleep(5)
        self.assertEqual(timer.get_counter(),20)

    # no fischer amount
    def test_stop(self):
        timer = Timer()
        time.sleep(5)
        timer.stop()
        time.sleep(3)
        timer.start()
        time.sleep(5)
        self.assertEqual(timer.get_counter(),10)

    def test_get_counter(self):
        timer = Timer()
        timer.start()
        time.sleep(5)
        timer.stop()
        self.assertEqual(timer.get_counter(), 15)

    # with fischer amount
    def test_stop_with_fischer(self):
        timer = Timer(20, 20)
        timer.start()
        time.sleep(5)
        timer.stop()
        self.assertEqual(timer.get_counter(), 35)

    def test_start_stop(self):
        timer = Timer()
        timer.start_stop()
        self.assertNotEqual(timer.time, None)
        timer.start_stop()
        self.assertEqual(timer.time, None)



