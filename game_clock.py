from timer import Timer

class GameClock(object):

    def __init__(self, counter = 20, fischer = 0):
        self.timer1 = Timer(counter, fischer)
        self.timer2 = Timer(counter, fischer)

    def start(self):
        self.timer1.start()
        print 'game starts now'

    def next(self):
        self.timer1.start_stop()
        self.timer2.start_stop()
        print 'next to move'



