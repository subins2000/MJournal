from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import qApp, QMainWindow, QStyle

from mjournal.app.ui import Ui_Home


class Home(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.initMenubar()

    def initUI(self):
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        self.browserView = QWebEngineView()
        self.centralWidget.addWidget(self.browserView)

        self.browserView.load(QtCore.QUrl('http://127.0.0.1:8786'))

        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                qApp.desktop().availableGeometry()
            )
        )

        self.show()

    def initMenubar(self):
        self.ui.quitAction.triggered.connect(qApp.quit)
