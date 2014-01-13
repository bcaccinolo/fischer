import time

class Timer(object):

    def __init__(self):
        self.counter = 20
        self.time = time.time()

    def get_counter(self):
        now = time.time()
        since = int(round(now - self.time))
        now_counter = self.counter - since
        return(0 if (now_counter < 0) else now_counter)

    def show(self):
        print self.get_counter()

    def start(self):
        self.time = time.time()

    def stop(self):
        self.counter = self.get_counter()


### UNIT TESTS ###############################################

import unittest
import time

class TestTimer(unittest.TestCase):

    def test_init(self):
        timer = Timer()
        time.sleep(5)
        self.assertEqual(timer.get_counter(),15)

    def test_stop(self):
        timer = Timer()
        time.sleep(5)
        timer.stop()
        time.sleep(3)
        timer.start()
        time.sleep(5)
        self.assertEqual(timer.get_counter(),10)



if __name__== '__main__':
    unittest.main()


