import pyhidapi as hid

hid.hid_init()


class HidMultiPanel:

    def __init__(self):
        try:
            print('opening device')
            self._h = hid.hid_open(0x06a3, 0x0d06)
            buf = [0x0] * 13
            res = hid.hid_get_feature_report(self._h, buf)
            print(res)
            hid.hid_set_nonblocking(self._h, True)
            bufread = [0] * 4
            res = hid.hid_read(self._h, bufread)
            print("{0:08b} {1:08b} {2:08b}".format(res[0], res[1], res[2]))
            hid.hid_set_nonblocking(self._h, False)
            hid.hid_close(self._h)
        except IOError as ex:
            print(ex)
            self._h.close()


if __name__ == '__main__':
    MPanel = HidMultiPanel()

    print()
