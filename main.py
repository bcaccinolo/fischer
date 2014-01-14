from __future__ import print_function
import time
import sys

from game_clock import GameClock

class Fischer(object):

    @classmethod
    def start(self):
        clock = GameClock()
        clock.start()
        while True:
            time.sleep(0.5)

            counters = clock.get_counters()
            str = "timer1: {} - timer2: {}".format(counters[0], counters[1])

            sys.stdout.write("\r")
            sys.stdout.write(str)
            sys.stdout.flush()

if __name__ == '__main__':
    Fischer.start()


