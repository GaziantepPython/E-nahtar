import subprocess

class UsbDetay:
    def __init__(self, baglantiYolu):
        """
        @baglantiYolu
            verilen usb baglanti konumuna göre  usb ozellikleri ile
            detay verileri aliyoruz
        """
        # print("baglantiYolu : ", baglantiYolu)

        cikti = self.depolamaDetayAl(baglantiYolu)
        try:
            # verirleri istenilen formatta isliyoruz
            s = str(cikti).split('\n')[1].split()

            self.device, self.size, self.used, self.available, self.percent = s[:5]
            self.mountpoint = " ".join(s[5:])
        except Exception as ex:
            # ~ print(str(cikti))
            # ~ print(str(cikti).split('\n')[1].split())
            # ~ exit()
            pass

        return

    def depolamaDetayAl(self, baglantiYolu):
        """
        konsol ekranindan komut calitirarak ciktisini verir
        """
        df = subprocess.Popen(["df", "-h", baglantiYolu], stdout=subprocess.PIPE)
        return df.communicate()[0].decode("utf-8")


if __name__ == '__main__':
    # ~ UsbDetay()
    print("enahtar.py yi çalıştırın")
