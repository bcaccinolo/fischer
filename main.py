from __future__ import print_function
import time
import sys
import curses

from game_clock import GameClock

class Fischer(object):

    @classmethod
    def curses_init(self):
        self.win = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        self.win.nodelay(1)

    @classmethod
    def start(self):
        self.curses_init()
        clock = GameClock()
        while True:
            time.sleep(0.2)

            counters = clock.get_counters()
            str = "\rtimer1: {} - timer2: {}   ".format(counters[0], counters[1])

            sys.stdout.write(str)
            sys.stdout.flush()

            ch = self.win.getch()
            if(ch == 32): clock.next()

if __name__ == '__main__':
    Fischer.start()


