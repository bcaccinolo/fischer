from timer import Timer

class GameClock(object):

    def __init__(self):
        self.timer1 = Timer()
        self.timer2 = Timer()

    def start(self):
        self.timer1.start()
        print 'game starts now'

    def next(self):
        print 'next to move'



