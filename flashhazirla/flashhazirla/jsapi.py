import pyudev
import webview
import hashlib
import time
import json
from .usbdetay import *

class USBDetector:
    """ Monitor udev for detection of usb """

    def __init__(self, usbCheck):
        """ Runs the actual loop to detect the events """
        # print("init usbdetector")
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='usb')
        self.observer = pyudev.MonitorObserver(self.monitor, usbCheck)
        self.observer.start()


class JSApi(USBDetector):
    """
    pywebview ile javascript uzerinden bu sinifa erisilebilir
    """

    def __init__(self, window):

        self.getWindow = window
        self.usbListe = list()

        super(JSApi, self).__init__(self.usbKontrol)
        return

    def isFlash(self, device):
        return device.get('ID_USB_DRIVER') == 'usb-storage' and device.get('ID_FS_TYPE') is not None and device.get(
            'ID_FS_UUID') is not None

    def usbKontrol(self, action, device):
        """
        usb aygıt takılıp çıkarıldığında çalışır
        """
        print(action)
        if device.action == 'bind' or device.action == 'remove':
            self.getUsbListesi()
            try:
                self.getWindow().evaluate_js(r"""usbListesiGuncelle({});""".format(json.dumps(self.usbListe)))
            except Exception as err:
                print("Hata 1:" + err)

    def getUsbListesi(self):
        """
        sistemde takılı olan usb bellek listesini oluşturur
        """
        time.sleep(1)

        # listeyi baslangicta temizle
        self.usbListe.clear()
        try:
            # ~ for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
            for device in self.context.list_devices(subsystem='block'):
                # print(device.get('ID_FS_LABEL',"NO NAME"),device.get('ID_USB_DRIVER'))
                if self.isFlash(device):
                    usbBellek = UsbDetay(device.device_node)
                    # print(device.device_node, usbBellek.mountpoint)
                    self.usbListe.append({
                        "id": device.get('ID_FS_UUID'),
                        "value": usbBellek.mountpoint,
                        "name": device.get('DEVNAME'),
                        "label": device.get('ID_FS_LABEL', "NO NAME"),
                        "filesistem": device.get('ID_FS_TYPE'),
                        "size": usbBellek.size
                    })
        except Exception as e:
            print("getUsbListesi: ")
            print(e)
        return self.usbListe

    def sifreOlustur(self, anahtarkodu, usbid):
        return hashlib.sha224(anahtarkodu.encode("utf-8") + usbid.encode("utf-8")).hexdigest()

    def flashHazirla(self, hedef, anahtarkodu):
        try:
            if hedef.strip() == "":
                return {"mesaj": "Anahtar seçilmedi", "renk": "kirmizi"}
            elif anahtarkodu.strip() == "":
                return {"mesaj": "Şifre için anahtar belirtilmedi", "renk": "kirmizi"}
            else:
                usbid = None
                for i in self.usbListe:
                    if i["value"] == hedef:
                        usbid = i["id"]

                if usbid is None:
                    return {"mesaj": "Şifre için id bulunamadı", "renk": "kirmizi"}

                dosyaismi = ".enahtar.dat"
                dosyaTamKomunu = hedef + "/" + dosyaismi
                dosya = open(dosyaTamKomunu, "w")
                dosya.write(self.sifreOlustur(anahtarkodu, usbid))
                dosya.close()
                return {"mesaj": "Anahtar oluşturuldu !", "renk": "yesil"}
        except Exception as e:
            return {"mesaj": "Dosya yazılamadı : " + str(e), "renk": "kirmizi"}

    def error(self, e):
        self.log(e)
        raise Exception('Hata oluştu !'+e)

    def log(self, e):
        print("log : ")
        print(e)

    def exit(self):
        self.getWindow().destroy()


if __name__ == '__main__':
    """
    bu alanda JSApi yi test edebiliriz
    """
    # ~ api = JSApi(None)
    # ~ print(api.getUsbListesi())
    print("enahtar.py yi çalıştırın")
