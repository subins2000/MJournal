#!/usr/bin/python3

import sys

from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import QApplication, QWidget

from mjournal_app.app.Home import Home


class App:

    app = None

    def run(self):
        self.app = QApplication(sys.argv)

        qtTranslator = QTranslator()
        qtTranslator.load('mjournal_' + QLocale.system().name(),
                          QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        self.app.installTranslator(qtTranslator)

        ex = Home()

        sys.exit(self.app.exec_())
