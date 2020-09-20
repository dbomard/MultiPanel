import hidapi as hid

if __name__ == '__main__':
    MPanel = hid.Device(vendor_id=0x06a3, product_id=0x0d06)
    datas = MPanel.read(4, blocking=False)
    datas = [0,1,2,3,4,5,6,7,8,9,1,2,3,0]
    buf = bytearray(datas)
    featurerpt = MPanel.send_feature_report(bytes(buf),report_id=bytes(1))
    print(MPanel)
    MPanel.close()
