﻿#!/usr/bin/python
# -*- coding: utf-8 -*-
"""QssStylesheetEditor app start module

Create QApplication and show splash. Include minimal module to accelerate spalsh load.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from splash import SplashScreen
from i18n.language import Language
try:
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
except Exception:
    print('__file__ of app.py load err')


class App(QApplication):
    """Application to load splash and mainwindow"""
    def __init__(self):
        super().__init__(sys.argv)
        self.windows = {}
        # sys.setrecursionlimit(1500)

    def run(self, pytest=False):
        """run the app
        :param pytest: if run is true start event loop, else just for test
        """
        print("starting...")
        Language.setTrans()
        splash = SplashScreen("res/splash.png")
        splash.loadProgress()
        from ui.mainwin import MainWin
        self.windows["main"] = MainWin()
        self.windows["main"].show()
        splash.finish(self.windows["main"])
        if not pytest:
            sys.exit(self.exec_())


def main():
    App().run()


if __name__ == "__main__":
    main()
