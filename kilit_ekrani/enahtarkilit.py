#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pyudev
import time
import os
import hashlib
import subprocess
import time
class getUsbDetay:
    def __init__(self, bagKonum):
        time.sleep(1)
        df = subprocess.Popen(["df", "-h", bagKonum], stdout=subprocess.PIPE)
        output = df.communicate()[0].decode("utf-8")
        s = str(output).split('\n')[1].split()
        self.device, self.size, self.used, self.available, self.percent = s[:5]
        self.mountpoint = " ".join(s[5:])
        return

class USBDetector:
    """ Monitor udev for detection of usb """
    def __init__(self, usbCheck):
        """ Runs the actual loop to detect the events """
        print("init usbdetector")
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='block')
        self.observer = pyudev.MonitorObserver(self.monitor, usbCheck)
        self.observer.start()

class EtapKilit(USBDetector):
    """
    """
    kilitID = None
    sifreKodla = "deneme"  # varsayilan sifre olustururken kullanilan kod

    def __init__(self):
        super(EtapKilit, self).__init__(self.usbKontrol)
        self.kilitle()

        return

    def usbKontrol(self, action, device):
        """
        usb aygıt takılıp çıkarıldığında çalışır
        """
        print(action)
        if self.isFlash(device):
            if device.action == 'add':
                self.kilitAc(device)

            if device.action == 'remove':
                self.kilitle()

    def isFlash(self, device):
        return device.get('ID_USB_DRIVER') == 'usb-storage' and device.get('ID_FS_TYPE') is not None and device.get(
            'ID_FS_UUID') is not None

    def kilitle(self):
        """
        """
        if self.kilitID is None:
            for device in self.context.list_devices(subsystem='block'):
                if self.isFlash(device):
                    if self.anahtarTakili(self.sifreKodla, device):
                        return False

            self.kilitID = subprocess.Popen(['python3', 'kilitekrani.py'])
            time.sleep(2)
            os.system('wmctrl -r "ETAP E-Nahtar" -b add,above')
            print("kilitle")

        return

    def kilitAc(self, device):
        """
        """
        if self.anahtarTakili(self.sifreKodla, device):
            if self.kilitID is not None:
                subprocess.Popen.terminate(self.kilitID)
                self.kilitID = None
                print("kilitAc")
        return

    def anahtarTakili(self, anahtarkodu, device):
        """
        anahtar olarak tanimli flash bellek takilimi kontrol edelim
        """
        try:
            usbBellek = getUsbDetay(device.device_node)
            dosyaismi = ".enahtar.dat"
            dosyaTamKonumu = usbBellek.mountpoint + "/" + dosyaismi
            # ~ print(dosyaTamKonumu)
            dosya = open(dosyaTamKonumu, "r")
            anahtar = dosya.read()
            dosya.close()
            durum = hashlib.sha224(
                anahtarkodu.encode("utf-8") + device.get('ID_FS_UUID').encode("utf-8")).hexdigest() == anahtar
            return durum
        except Exception as ex:
            print(ex)
        return False


ek = EtapKilit()
while True:
    time.sleep(1)
    pass