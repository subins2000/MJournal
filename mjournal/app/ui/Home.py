# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/Home.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(537, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
        Home.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Home.setIconSize(QtCore.QSize(48, 48))
        self.centralWidget = QtWidgets.QWidget(Home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(537, 0))
        self.centralWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.noWebEngineInfo = QtWidgets.QTextBrowser(self.centralWidget)
        self.noWebEngineInfo.setOpenExternalLinks(True)
        self.noWebEngineInfo.setObjectName("noWebEngineInfo")
        self.verticalLayout.addWidget(self.noWebEngineInfo)
        Home.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(Home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 20))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        Home.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(Home)
        self.statusBar.setObjectName("statusBar")
        Home.setStatusBar(self.statusBar)
        self.settingsAction = QtWidgets.QAction(Home)
        self.settingsAction.setObjectName("settingsAction")
        self.quitAction = QtWidgets.QAction(Home)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.quitAction.setIcon(icon)
        self.quitAction.setObjectName("quitAction")
        self.menuFile.addAction(self.quitAction)
        self.menuEdit.addAction(self.settingsAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "MJournal"))
        self.noWebEngineInfo.setHtml(_translate("Home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">MJournal</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Your system doesn\'t have PyQt5.QtWebEngineWidgets.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://127.0.0.1:8786\"><span style=\" text-decoration: underline; color:#0000ff;\">Open MJournal In Browser</span></a></p></body></html>"))
        self.menuFile.setTitle(_translate("Home", "File"))
        self.menuEdit.setTitle(_translate("Home", "Edit"))
        self.settingsAction.setText(_translate("Home", "Settings"))
        self.quitAction.setText(_translate("Home", "Quit"))
        self.quitAction.setShortcut(_translate("Home", "Ctrl+Q"))

