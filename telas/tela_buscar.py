# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_buscar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_Tela_Buscar(object):
    def setupUi(self, Tela_Buscar):
        Tela_Buscar.setObjectName("Tela_Buscar")
        Tela_Buscar.resize(926, 547)
        self.numLinhas = 1
        self.centralwidget = QtWidgets.QWidget(Tela_Buscar)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_buscar.setGeometry(QtCore.QRect(800, 80, 99, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/images/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_buscar.setIcon(icon)
        self.botao_buscar.setObjectName("botao_buscar")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 421, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 80, 85, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 20, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 881, 331))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.numLinhas)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 293)
        self.tableWidget.setColumnWidth(1, 293)
        self.tableWidget.setColumnWidth(2, 165)
        self.tableWidget.setColumnWidth(3, 127)

        self.tableWidget.setHorizontalHeaderLabels(['Título', 'Autor', 'Nº de páginas', 'Ano'])

        pica = {'1234': {'titulo':'Sexo anal', 'autor':'Daniel Taradão', 'paginas':10, 'ano':90}, '1235': {'titulo':'Sexo Sem Rola', 'autor':'Daniel Pensador', 'paginas':100, 'ano':1996}}
        self.numLinhas = len(pica)
        for i, value in enumerate(pica):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(pica[value]['titulo']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(pica[value]['autor']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(pica[value]['paginas'])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(pica[value]['ano'])))

        Tela_Buscar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Buscar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 25))
        self.menubar.setObjectName("menubar")
        Tela_Buscar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Buscar)
        self.statusbar.setObjectName("statusbar")
        Tela_Buscar.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Buscar)
        QtCore.QMetaObject.connectSlotsByName(Tela_Buscar)

    def retranslateUi(self, Tela_Buscar):
        _translate = QtCore.QCoreApplication.translate
        Tela_Buscar.setWindowTitle(_translate("Tela_Buscar", "MainWindow"))
        self.botao_buscar.setText(_translate("Tela_Buscar", "BUSCAR"))
        self.comboBox.setItemText(0, _translate("Tela_Buscar", "TÍTULO"))
        self.comboBox.setItemText(1, _translate("Tela_Buscar", "AUTOR"))
        self.label_3.setText(_translate("Tela_Buscar", "BUSCAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Buscar = QtWidgets.QMainWindow()
    ui = Ui_Tela_Buscar()
    ui.setupUi(Tela_Buscar)
    Tela_Buscar.show()
    sys.exit(app.exec_())
