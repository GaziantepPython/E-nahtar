import sqlite3 as sql
import os


class Veritabani:
    __db_path = 'db/'
    __db_name = 'enahtardb.sqlite'
    __tablo_adi = 'tbl_kullanici'

    def __init__(self):
        # baslangicta veri tabanini kontrol et varsa baglan yoksa olustur ve baglan
        self.veritabanikontrol()

    def vt_baglanti(self):
        self.vt = sql.connect(self.__db_path + self.__db_name)
        self.imlec = self.vt.cursor()

    def veritabanikontrol(self):
        if os.path.exists(self.__db_path + self.__db_name):
            self.vt_baglanti()
        else:
            self.vt_baglanti()
            self.veritabaniolustur()

    def veritabaniolustur(self):
        self.imlec.execute(
            "CREATE TABLE IF NOT EXISTS tbl_kullanici(id INTEGER PRIMARY KEY AUTOINCREMENT, adi,soyadi,kadi,sifre)")
        # Veritabanı ilk defa oluşuyorsa Gaziantep Python kullanıcısı ekleniyor
        sorgu = "INSERT INTO {}(adi, soyadi, kadi, sifre) VALUES(?,?,?,?)".format(self.__tablo_adi)
        veri = ["Gaziantep", "Python", "admin", "admin"]
        self.imlec.execute(sorgu, veri)
        self.vt.commit()

    # Kullancı Adı ve Şifre Kontrol Ediliyor
    def girisKontrol(self, kullanici_adi, sifre):
        self.imlec.execute(
            """SELECT * FROM """ + self.__tablo_adi + """ WHERE kadi = '%s' AND sifre = '%s'""" % (
            kullanici_adi, sifre))
        return self.imlec.fetchone()

    def kayit_guncelle(self, id, veri):
        sorgu = "UPDATE tbl_kullanici SET adi='%s',soyadi='%s',kadi='%s',sifre='%s' WHERE id='%s' " % (
            veri["adi"], veri["sadi"], veri["kadi"], veri["sifre"], id)
        self.imlec.execute(sorgu)
        self.vt.commit()
        return True

    def kayit_sil(self, id):
        self.imlec.execute("""DELETE FROM """ + self.__tablo_adi + """ WHERE id = '%s' """ % (id))
        self.vt.commit()
        return True

    def kayit_ekle(self, veri):
        sorgu = """INSERT INTO """ + self.__tablo_adi + """(adi, soyadi, kadi, sifre) VALUES(?,?,?,?)"""
        self.imlec.execute(sorgu, [veri["adi"], veri["sadi"], veri["kadi"], veri["sifre"]])
        self.vt.commit()
        return True

    def listele(self):
        sorgu = """SELECT * FROM """ + self.__tablo_adi + """ ORDER BY Id DESC"""
        self.imlec.execute(sorgu)
        results = self.imlec.fetchall()
        data = list()
        for row in results:
            data.append({
                "id": row[0],
                "adi": row[1],
                "soyadi": row[2],
                "kullaniciadi": row[3],
                "sifre": row[4]
            })
        return data

    def __delete__(self, instance):
        self.vt.close()
