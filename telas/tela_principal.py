# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 70, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ver_acervo = QtWidgets.QPushButton(self.centralwidget)
        self.ver_acervo.setGeometry(QtCore.QRect(300, 310, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.ver_acervo.setFont(font)
        self.ver_acervo.setObjectName("ver_acervo")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 10, 511, 451))
        self.textBrowser.setObjectName("textBrowser")
        self.cadastrar_novo_livro = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrar_novo_livro.setGeometry(QtCore.QRect(300, 220, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.cadastrar_novo_livro.setFont(font)
        self.cadastrar_novo_livro.setObjectName("cadastrar_novo_livro")
        self.sair = QtWidgets.QPushButton(self.centralwidget)
        self.sair.setGeometry(QtCore.QRect(820, 450, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.sair.setFont(font)
        self.sair.setObjectName("sair")
        self.textBrowser.raise_()
        self.label.raise_()
        self.ver_acervo.raise_()
        self.cadastrar_novo_livro.raise_()
        self.sair.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Olá,"))
        self.ver_acervo.setText(_translate("MainWindow", "VER ACERVO"))
        self.cadastrar_novo_livro.setText(_translate("MainWindow", "CADASTAR NOVO LIVRO"))
        self.sair.setText(_translate("MainWindow", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
