from threading import Thread

class DataRead(Thread):
    def __init__(self, hid):
        Thread.__init__(self)
        self._parentHid = hid

    def run(self):
        while True:
            buf = self._parentHid.read(4)
            pass