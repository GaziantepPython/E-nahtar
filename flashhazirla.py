#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ import threading
import webview
from .jsapi import *

class UsbAnahtarOlustur:
    """ Class doc """

    def __init__(self):
        """ Class initialiser """
        self.window = None
        pass

    def start(self):
        # javascript icin kullanilacak api nesnesi olusturuluyor
        api = JSApi(self.getWindow)

        # webview icin pencere olustur
        self.window = webview.create_window(
            'E-nahtar USB Bellek Hazırla',
            url="template/index.html",
            js_api=api,
            width=450,
            height=350,
            frameless=True,
            resizable=False
        )

        # webview pencere kapandiginda bir islem yapmak gerekirse kullanabiliriz
        self.window.closed += self.on_closed

        # webview baslat
        # webview.start(self.on_evulatejs, self.window)
        webview.start()

    def on_evulatejs(self):
        print("on_evulatejs : ")
        pass

    def on_closed(self):
        print('on_closed: webview penceresi kapatıldı !')

    def getWindow(self):
        return self.window


if __name__ == '__main__':
    """
    webview.create_window(title, url='', html='', js_api=None, width=800, height=600,
                          x=None, y=None, resizable=True, fullscreen=False,
                          min_size=(200, 100), hidden=False, frameless=False,
                          minimized=False, on_top=False, confirm_close=False,
                          background_color='#FFF', text_select=False)
    """
    # UsbAnahtarOlustur().start()
    print("enahtar.py yi çalıştırın")
