from hidapi import Device
from DataRead import DataRead

# button Messages
MP_BTN_DWN = 0
MP_BTN_UP = 1

MP_APBTN_BITPOS = 0
MP_HDGBTN_BITPOS = 1
MP_NAVBTN_BITPOS = 2
MP_IASBTN_BITPOS = 3
MP_ALTBTN_BITPOS = 4
MP_VSBTN_BITPOS = 5
MP_APRBTN_BITPOS = 6
MP_REVBTN_BITPOS = 7
MP_READ_KNOB_MODE_MASK = 0x0000001F
MP_READ_BTNS_MASK = 0x00007F80
MP_READ_FLAPS_MASK = 0x00030000
MP_READ_TRIM_MASK = 0x000C0000
MP_READ_TUNING_MASK = 0x00000060
MP_READ_THROTTLE_MASK = 0x00008000
MP_READ_KNOB_ALT = 0x00000001
MP_READ_KNOB_VS = 0x00000002
MP_READ_KNOB_IAS = 0x00000004
MP_READ_KNOB_HDG = 0x00000008
MP_READ_KNOB_CRS = 0x00000010
MP_READ_TUNING_RIGHT = 0x00000020
MP_READ_TUNING_LEFT = 0x00000040
MP_READ_AP_BTN = 0x00000080
MP_READ_HDG_BTN = 0x00000100
MP_READ_NAV_BTN = 0x00000200
MP_READ_IAS_BTN = 0x00000400
MP_READ_ALT_BTN = 0x00000800
MP_READ_VS_BTN = 0x00001000
MP_READ_APR_BTN = 0x00002000
MP_READ_REV_BTN = 0x00004000
MP_READ_THROTTLE_ON = 0x00008000
MP_READ_THROTTLE_OFF = 0x00000000
MP_READ_FLAPS_UP = 0x00010000
MP_READ_FLAPS_DN = 0x00020000
MP_READ_TRIM_DOWN = 0x00040000
MP_READ_TRIM_UP = 0x00080000
MP_READ_NOMSG = 0xFFFFFFFF


class Mpanel():
    def __init__(self):
        # call parent class with ref to Multi Panel
        try:
            self._hid = Device(vendor_id=0x06a3, product_id=0x0d06, blocking=False)
            self._launchDataRead()
        except IOError:
            print("No Multi Panel found")
            exit(1)


    def __del__(self):
        self._loop.join()
        self._hid.close()

    def _launchDataRead(self):
        self._loop = DataRead(self._hid)
        self._loop.start()

    def Btn_down(self):
        pass
        # TODO : Gestion d
