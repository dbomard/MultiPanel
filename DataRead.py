from threading import Thread
import time


class DataRead(Thread):

    def __init__(self, hid):
        Thread.__init__(self)
        self._parentHid = hid

    def run(self):
        run = True
        while run:
            self._parentHid.set_nonblocking(1)
            buf = self._parentHid.read(4)
            if len(buf) > 0:
                msg = buf[0] + buf[1] << 9 + buf[2] << 18
                print("{0:032b}".format(msg))
                if buf[0] == 16:
                    run = False
                    self._parentHid.set_nonblocking(0)
            time.sleep(.1)
