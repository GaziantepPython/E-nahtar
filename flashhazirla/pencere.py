from tkinter import messagebox
from tkinter import Tk

class Pencere:
    def __init__(self):
        self.pencere = None
        pass

    def pencere_olustur(self):
        self.pencere = Tk()

    def pencere_destroy(self):
        if self.pencere:
            self.pencere.destroy()
            self.pencere = None

    def sor_kapat(self):
        if messagebox.askokcancel("Çıkış", "Programdan Çıkmak üzeresiniz!!"):
            self.pencere_destroy()

    def pencere_ortala(self):
        # pencere gizle
        self.pencere.withdraw()
        self.pencere.update_idletasks()

        # Hem ekran genişliğinin / yüksekliğinin yarısını hem de pencere genişliğini / yüksekliğini alır
        sagPozisyon = int(self.pencere.winfo_screenwidth() / 2 - self.pencere.winfo_reqwidth() / 2)
        altPozisyon = int(self.pencere.winfo_screenheight() / 2 - self.pencere.winfo_reqheight() / 2)

        self.pencere.geometry("+{}+{}".format(sagPozisyon, altPozisyon))

        # pencere goster
        self.pencere.deiconify()

    def pencere_ac(self):
        self.pencere.mainloop()

    def mesaj(self, mesaj):
        messagebox.showwarning("Hata", mesaj)