from tkinter import *
# import anamenu
from yonetim import Yonetim
from pencere import Pencere
from veritabani import Veritabani
from flashhazirla.flashhazirla import UsbAnahtarOlustur

class Enahtar(Pencere):
    def __init__(self):
        super(Enahtar, self).__init__()
        pass

    def anahtarolustur(self):
        # Formdaki nesnelere göre genişlik ve yükseklik alınıyor.
        self.pencere_destroy()
        UsbAnahtarOlustur().start()
        self.anamenu_pencere()

    def yonetim_pencere(self):
        self.pencere_destroy()
        Yonetim().yonetim_pencere()
        self.anamenu_pencere()

    def giris_pencere(self):
        self.pencere_destroy()
        self.pencere_olustur()

        self.pencere.title("E-nahtar - Kullancı Giriş")
        icon = PhotoImage(file="resim/user3.gif")
        Label(self.pencere, image=icon, bg="#fce876").grid(row=0, column=0, columnspan=2, sticky=N, padx=80)
        self.pencere.configure(background='#fce876')

        Label(self.pencere, text="Kullanıcı Adı", bg="#fce876", fg="#2d6c9b",
              font="Verdana 10").grid(row=1, sticky=E, pady=10)
        Label(self.pencere, text="Şifre", bg="#fce876", fg="#2d6c9b", font="Verdana 10").grid(row=2, sticky=E)

        self.entry_kad = Entry(self.pencere, width=30)
        self.entry_kad.grid(row=1, column=1, sticky=E, padx=10)
        self.entry_sifre = Entry(self.pencere, width=30, show="*")
        self.entry_sifre.grid(row=2, column=1, sticky=E, padx=10)

        Button(self.pencere, text="Giriş Yap", width=15, bg="#5ba0d5", fg="black",
               command=self.kontrolet).grid(row=3, column=0, columnspan=2, sticky=N, pady=10)

        Button(self.pencere, text="Çıkış", bg="#2d6c9b", fg="#fce876",
               command=self.sor_kapat).grid(row=3, column=1, sticky=E, padx=10)

        Label(self.pencere, text="E-nahtar Versiyon: 1.0.0", bg="#fce876", fg="#000000",
              font="Verdana 6").grid(row=4, column=1, sticky=E)

        self.pencere_ortala()

        self.pencere_ac()

    def anamenu_pencere(self):
        self.pencere_destroy()
        self.pencere_olustur()

        self.pencere.title("E-nahtar - Ana Menü")
        self.pencere.configure(background='#ec69a4')

        icon = PhotoImage(file=r"resim/logo.gif")
        Label(self.pencere, image=icon,
              background="#ec69a4").grid(row=0, column=0, rowspan=3, sticky=N, pady=10, padx=15)

        photoolustur = PhotoImage(file=r"resim/usb1.png")
        Button(self.pencere, text="Anahtar Flash Oluştur", command=self.anahtarolustur, image=photoolustur,
               compound=TOP, width=200, font="Verdana 13", bg="#e7b864",
               fg="black").grid(row=0, column=1, columnspan=2, sticky=N, pady=10, padx=30)

        photokullanici = PhotoImage(file=r"resim/ekle.png")
        Button(self.pencere, text="Kullanıcı İşlemleri", command=self.yonetim_pencere, image=photokullanici, compound=TOP,
               width=200, font="Verdana 13", bg="#71a0c7",
               fg="black").grid(row=1, column=1, columnspan=2, sticky=N, padx=30)

        photocikis = PhotoImage(file=r"resim/cikisana.png")
        Button(self.pencere, text="Çıkış", image=photocikis, compound=TOP, width=200, font="Verdana 13", bg="#a29e9d",
               fg="red", command=self.sor_kapat).grid(row=2, column=1, columnspan=2, sticky=N, pady=10, padx=30)

        Label(self.pencere, text="E-nahtar Versiyon: 1.0.0", bg="#ec69a4", fg="#FFFFFF",
              font="Verdana 6").grid(row=4, column=0, sticky=SW)

        self.pencere_ortala()

        self.pencere_ac()

    def kontrolet(self):
        if Veritabani().girisKontrol(self.entry_kad.get(), self.entry_sifre.get()):
            # self.pencere.pencere_destroy()
            self.anamenu_pencere()
        else:
            self.mesaj("Kullancı Adı veya Şifre Yanlış")


enahtar = Enahtar()
enahtar.giris_pencere()
