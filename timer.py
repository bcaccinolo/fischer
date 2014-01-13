import time

class Timer(object):

    def __init__(self, counter = 20, fischer = 0):
        self.counter = counter
        self.fischer = fischer
        self.time = time.time()

    def get_counter(self):
        if (self.time == None): return self.counter
        now = time.time()
        since = int(round(now - self.time))
        now_counter = self.counter - since
        return(0 if (now_counter < 0) else now_counter)

    def show(self):
        print self.get_counter()

    def start(self):
        self.time = time.time()

    def stop(self):
        self.counter = self.get_counter() + self.fischer
        self.time = None

