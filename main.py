from __future__ import print_function
import time
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
            if counters[2] == 1:
                marker1 = '>'
                marker2 = ' '
            else:
                marker1 = ' '
                marker2 = '>'
            str = " {} timer1: {} - {} timer2: {}   ".format(marker1, counters[0],
                                                           marker2, counters[1])
            self.win.addstr(5, 5, str)

            ch = self.win.getch()
            if(ch == 32): clock.next()

if __name__ == '__main__':
    Fischer.start()

