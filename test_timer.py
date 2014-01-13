from timer import Timer

import unittest
import time

class TestTimer(unittest.TestCase):

    def test_init(self):
        timer = Timer()
        time.sleep(5)
        self.assertEqual(timer.get_counter(),15)

    # no fischer amount
    def test_stop(self):
        timer = Timer()
        time.sleep(5)
        timer.stop()
        time.sleep(3)
        timer.start()
        time.sleep(5)
        self.assertEqual(timer.get_counter(),10)

    # with fischer amount
    def test_init_fischer(self):
        timer = Timer(20, 20)
    # def test_stop_with_fischer(self):
    #     timer = Timer()

