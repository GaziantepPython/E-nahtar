import tkinter
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import messagebox
import os
from veritabani import Veritabani
from pencere import Pencere


class Yonetim(Pencere):
    def __init__(self):
        super(Yonetim, self).__init__()
        self.id = None
        pass

    def form_kontrol(self):
        veri = {
            "adi": self.entry_ad.get(),
            "sadi": self.entry_sad.get(),
            "kadi": self.entry_kad.get(),
            "sifre": self.entry_sifre.get(),
            "sifretekrar": self.entry_sifretekrar.get()
        }
        if veri["adi"] == "" or veri["sadi"] == "" or veri["kadi"] == "" or veri["sifre"] == "":
            self.mesaj("Lütfen Tüm Bilgileri Eksiksiz giriniz")
            return False
        elif veri["sifre"] != veri["sifretekrar"]:
            self.mesaj("Şifre ile Şifre tekrar aynı olmalıdır.")
            return False
        return veri

    def entrytemizle(self):
        # Entry nesnesini temizler
        self.entry_ad.delete(0, END)
        self.entry_sad.delete(0, END)
        self.entry_kad.delete(0, END)
        self.entry_sifre.delete(0, END)
        self.entry_sifretekrar.delete(0, END)
        self.id = None

    def tiklananveri(self, event):
        # datalist tıklanınca veriler entry lere aktırılıyor
        secim = self.liste.selection()
        if len(secim) == 0:
            return
        self.id = self.liste.item(secim[0])['text']

        ad = self.liste.item(secim[0])['values'][0]
        soy = self.liste.item(secim[0])['values'][1]
        kadi = self.liste.item(secim[0])['values'][2]
        ksifre = self.liste.item(secim[0])['values'][3]

        self.entry_ad.delete(0, END)  # Entry nesnesini temizler
        self.entry_ad.insert(0, ad)

        self.entry_sad.delete(0, END)
        self.entry_sad.insert(0, soy)

        self.entry_kad.delete(0, END)
        self.entry_kad.insert(0, kadi)

        self.entry_sifre.delete(0, END)
        self.entry_sifre.insert(0, ksifre)

    def listele(self):
        self.liste.delete(*self.liste.get_children())
        for i in Veritabani().listele():
            self.liste.insert("", 0, text=i["id"], values=(i["adi"], i["soyadi"], i["kullaniciadi"], i["sifre"]))

    def veriguncelle(self):
        veri = self.form_kontrol()
        if veri:
            if Veritabani().kayit_guncelle(self.id, veri):
                self.mesaj("Kayıt başarı ile güncellendi")
                self.listele()
                self.entrytemizle()
            else:
                self.mesaj("Kayıt ekleme başarısız")

    def kaydet(self):
        veri = self.form_kontrol()
        if veri:
            if Veritabani().kayit_ekle(veri):
                self.mesaj("Kayıt başarı ile eklendi")
                self.listele()
                self.entrytemizle()
            else:
                self.mesaj("Kayıt ekleme başarısız")

    def verisil(self):
        if self.id != 1:
            Veritabani().kayit_sil(self.id)
            self.listele()
        else:
            self.mesaj("İlk kayıt silinemez")

        self.entrytemizle()

    def yonetim_pencere(self):
        self.pencere_olustur()
        self.pencere.title("E-nahtar - Kullanıcı İşlemleri")
        icon = PhotoImage(file=r"resim/yonetim2.png")
        Label(self.pencere, image= icon, bg="#ec69a4").grid(row=0, rowspan=6, sticky=SW, padx=10)
        self.pencere.configure(background='#ec69a4')
    
        Label(self.pencere, text="KULLANICININ :", bg="White", fg="Red", font="Verdana 16").grid(row=1, column=1, sticky=SW,
                                                                                            pady=10)
        Label(self.pencere, text="* Adı", bg="#ec69a4", fg="#014da3", font="Verdana 12").grid(row=2, column=1, sticky=SW,
                                                                                         pady=10)
        Label(self.pencere, text="* Soyadı", bg="#ec69a4", fg="#014da3", font="Verdana 12").grid(row=3, column=1, sticky=SW)
        Label(self.pencere, text="* Kullanıcı Adı", bg="#ec69a4", fg="#014da3", font="Verdana 12").grid(row=4, column=1,
                                                                                                   sticky=SW, pady=10)
        Label(self.pencere, text="* Şifre", bg="#ec69a4", fg="#014da3", font="Verdana 12").grid(row=5, column=1, sticky=SW,
                                                                                           pady=10)
        Label(self.pencere, text="* Şifre Tekrar", bg="#ec69a4", fg="#014da3", font="Verdana 12").grid(row=6, column=1,
                                                                                                  sticky=SW, pady=10)

        self.entry_ad = Entry(self.pencere, font="Verdana 12")
        self.entry_ad.grid(row=2, column=1, sticky=SW, pady=10, padx=150)
        self.entry_sad = Entry(self.pencere, font="Verdana 12")
        self.entry_sad.grid(row=3, column=1, sticky=SW, pady=10, padx=150)
        self.entry_kad = Entry(self.pencere, font="Verdana 12")
        self.entry_kad.grid(row=4, column=1, sticky=SW, pady=10, padx=150)
        self.entry_sifre = Entry(self.pencere, font="Verdana 12", show="*")
        self.entry_sifre.grid(row=5, column=1, sticky=SW, pady=10, padx=150)
        self.entry_sifretekrar = Entry(self.pencere, font="Verdana 12", show="*")
        self.entry_sifretekrar.grid(row=6, column=1, sticky=SW, pady=10, padx=150)
    
        photokayit = PhotoImage(file=r"resim/kayit.png")
        btn_kayit = Button(self.pencere, text="Kayıt", image=photokayit, compound=TOP, width=70, bg="#faa54d", fg="black",
                           command=self.kaydet)
        btn_kayit.grid(row=1, rowspan=2, column=1, sticky=E, pady=15)
    
        photoguncelle = PhotoImage(file=r"resim/guncelle.png")
        btn_guncelle = Button(self.pencere, text="Güncelle", image=photoguncelle, compound=TOP, width=70, height=270,
                              bg="#3ceee9", fg="black", command=self.veriguncelle)
        btn_guncelle.grid(row=1, rowspan=6, column=2, sticky=E, pady=15, padx=10)
    
        photosil = PhotoImage(file=r"resim/sil.png")
        btn_sil = Button(self.pencere, text="Sil", image=photosil, compound=TOP, width=70, bg="#f8aef9", fg="Black",
                         command=self.verisil)
        btn_sil.grid(row=3, rowspan=2, column=1, sticky=E, pady=10)
    
        photocikis = PhotoImage(file=r"resim/cikis.png")
        btn_cikis = Button(self.pencere, text="Çıkış", image=photocikis, compound=TOP, width=70, bg="#6789fd", fg="red",
                           command=self.pencere_destroy)
        btn_cikis.grid(row=5, rowspan=2, column=1, sticky=E, pady=10)
    
        style = ttk.Style()
        style.configure("liste.Treeview", highlightthickness=0, bd=0, font=('Calibri', 14))  # Modify the font of the body
        style.configure("liste.Treeview.Heading", font=('Calibri', 16, 'bold'))  # Modify the font of the headings
        style.layout("liste.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.liste = Treeview(self.pencere, height=5, style="liste.Treeview")
        self.liste["columns"] = ("sut1", "sut2", "sut3", "sut4")
        self.liste.grid(row=8, column=0, columnspan=3, sticky=SW, padx=20, pady=20)  # nesnenin ekrandaki pozisyonu
    
        self.liste.heading("#0", text="Id")
        self.liste.heading("sut1", text="Adı")
        self.liste.heading("sut2", text="Soyadı")
        self.liste.heading("sut3", text="Kullanıcı Adı")
        self.liste.heading("sut4", text="Şifre")
        # liste.insert("", 0,  values=("Gaziantep", "Python","Admin","Admin"))
        self.liste.bind('<ButtonRelease-1>', self.tiklananveri)  # Tıklanan veriyi alma

        self.listele()
        self.pencere_ortala()

        self.pencere_ac()


if __name__ == '__main__':
    print("enahtar.py yi çalıştırın")
