from timer import Timer

class GameClock(object):

    def __init__(self, counter = 20, fischer = 0):
        self.init(counter, fischer)

    def init(self, counter = 20, fischer = 0):
        self.timer1 = Timer(counter, fischer)
        self.timer2 = Timer(counter, fischer)

    def start(self):
        self.timer1.start()

    def next(self):
        if(self.timer1.time == self.timer2.time == None):
            self.timer1.start()
        else:
            self.timer1.start_stop()
            self.timer2.start_stop()

    def interrupt(self):
        self.timer1.interrupt()
        self.timer2.interrupt()

    def get_counters(self):
        return [ self.timer1.get_formatted_counter(),
                 self.timer2.get_formatted_counter(),
                 self.turn_id() ]

    def turn_id(self):
        if self.timer1.time == None:
            if self.timer2.time == None:
                return 1
            else:
                return 2
        else:
            if self.timer2.time == None:
                return 1

        raise Warning('The 2 timers are started at the same time')





