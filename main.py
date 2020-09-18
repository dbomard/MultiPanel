import pywinusb.hid as hid
from ctypes import c_ubyte


def inputHandle(self):
    pass


class MPDevice():

    def __init__(self):
        # search for a panel connected
        hidPanel = hid.HidDeviceFilter(vendor_id=0x06A3, product_id=0x0D06).get_devices()[0]
        # if panel found, initialize
        if hidPanel:
            hidPanel.open()
            physicalDescriptor = hidPanel.get_physical_descriptor()
            nbFeatureReports = hidPanel.count_all_feature_reports()
            featReports = hidPanel.find_feature_reports()
            dt = [c_ubyte(0x00)] * 13
            for report in featReports:
                report.set_raw_data(dt)
                report.send()
                print(report.get())
            hidPanel.add_event_handler(hid.get_full_usage_id(0x08,0x00), inputHandle)
            hidPanel.close()


if __name__ == '__main__':
    myDevice = MPDevice()
    print(myDevice)
