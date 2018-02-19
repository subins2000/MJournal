from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import qApp, QMainWindow, QStyle

from mjournal_app.app.ui import Ui_Home


class Home(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.initMenubar()

    def initUI(self):
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        '''
        Check if Qt WebEngine is available
        '''
        try:
            from PyQt5.QtWebEngineWidgets import QWebEngineView

            self.webEngineView()
        except:
            self.noWebEngineView()

        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                qApp.desktop().availableGeometry()
            )
        )

        self.show()

    def webEngineView(self):
        self.ui.noWebEngineInfo.hide()

        self.ui.browserView = QWebEngineView()
        self.ui.centralWidget.addWidget(self.browserView)

        self.ui.browserView.load(QtCore.QUrl('http://127.0.0.1:8786'))

    def noWebEngineView(self):
        self.ui.noWebEngineInfo.show()

    def initMenubar(self):
        self.ui.quitAction.triggered.connect(qApp.quit)
