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
        self.timer1.start_stop()
        self.timer2.start_stop()

    def interrupt(self):
        self.timer1.interrupt()
        self.timer2.interrupt()

    def get_counters(self):
        return [ self.timer1.get_counter(), self.timer2.get_counter() ]




