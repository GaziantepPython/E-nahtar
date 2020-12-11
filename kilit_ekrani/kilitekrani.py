#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webview
from threading import Thread


class KilitEkrani:
    sablonlar = {
        "varsayilan": "template/index.html",
        "webadresi": "http://sahinbeyktl.meb.k12.tr/tema/icerik.php?KATEGORINO=192972",
        "pano": "http://127.0.0.1/~sef/proje/bilgepano/bilgepano24042017/"
    }

    def __init__(self):
        self.window = webview.create_window("ETAP E-Nahtar",
                                            self.sablonlar.get("varsayilan"),
                                            width=800,
                                            height=600,
                                            fullscreen=True
                                            )
        webview.start()


if __name__ == '__main__':
    KilitEkrani()
