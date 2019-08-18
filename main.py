from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from telas.tela_inicial import Ui_Tela_Inicio
from telas.tela_cadastro import Ui_Tela_Cadastro
from telas.tela_cadastro_livro import Ui_Tela_Cadastro_Livro

from PyQt5.QtCore import pyqtSlot
import fireBaseSD

config = {
    'apiKey': "AIzaSyDZYQ53lbRVwuuUhQ0qCsCPGE2tiNPSDO4",
    'authDomain': "sd-livros.firebaseapp.com",
    'databaseURL': "https://sd-livros.firebaseio.com",
    'projectId': "sd-livros",
    'storageBucket': "sd-livros.appspot.com",
    'messagingSenderId': "1035059556229",
    'appId': "1:1035059556229:web:abf74498a46063c4"
}


class Tela_Inicio(QMainWindow):

    def __init__(self):
        super().__init__()
        self.firebase = fireBaseSD.initFb(config)
        self.ui = Ui_Tela_Inicio()
        self.ui.setupUi(self)
        self.ui.botao_entrar.clicked.connect(self.entrar)
        self.ui.botao_criar_conta.clicked.connect(self.abrir_criar_conta)
        self.show()


    def entrar(self):
        if(self.firebase.login(self.ui.e_mail_login.text(), self.ui.senha_login.text()) == 'Ok'):
            print('login feito')
        else:
            print('erro')
        
    def abrir_criar_conta(self):
        Tela_Cadastro().__init__()
        # self.ui.setupUi(self)

class Tela_Cadastro(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tela = Ui_Tela_Cadastro()
        self.tela.setupUi(self)
        self.showw()
        self.show()
    # def cirar_conta(self):

    def showw(self):
        print('aqui')


# class Tela_Cadastro_Livro(QMainWindow):
#     def __init__(self):
#         super().__init__()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Inicio()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())