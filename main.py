from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from telas.tela_inicial import Ui_Tela_Inicio
from telas.tela_cadastro import Ui_Tela_Cadastro
from telas.tela_cadastro_livro import Ui_Tela_Cadastro_Livro
from telas.tela_principal import Ui_Tela_Principal
import sys
import os
from PyQt5.QtCore import pyqtSlot
from fireBaseSD import FireBaseSD

config = {
    'apiKey': "AIzaSyDZYQ53lbRVwuuUhQ0qCsCPGE2tiNPSDO4",
    'authDomain': "sd-livros.firebaseapp.com",
    'databaseURL': "https://sd-livros.firebaseio.com",
    'projectId': "sd-livros",
    'storageBucket': "sd-livros.appspot.com",
    'messagingSenderId': "1035059556229",
    'appId': "1:1035059556229:web:abf74498a46063c4"
}


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_inicio = Ui_Tela_Inicio()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro = Ui_Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_principal = Ui_Tela_Principal()
        self.tela_principal.setupUi(self.stack2)

        self.tela_cadastro_livro = Ui_Tela_Cadastro_Livro()
        self.tela_cadastro_livro.setupUi(self.stack3)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.firebase = FireBaseSD(config)
        self.user = None
        self.setupUi(self)

        self.tela_inicio.botao_entrar.clicked.connect(self.entrar)
        self.tela_inicio.botao_criar_conta.clicked.connect(self.openCriarConta)

        self.tela_cadastro.botao_salvar.clicked.connect(self.criarConta)
        self.tela_cadastro.toolButton.clicked.connect(self.voltarInicio)

    def openCriarConta(self):
        self.QtStack.setCurrentIndex(1)

    def entrar(self):
        self.user = self.firebase.login(self.tela_inicio.e_mail_login.text(), 
                                    self.tela_inicio.senha_login.text())
        if self.user != None:
            dados = self.firebase.buscarUsuario(self.user['localId'])
            # print(dados['nome'])
            self.tela_principal.label.setText('Olá, '+str(dados['nome']))
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.about(self, 'Atenção', 'E-mail ou senha inválidos')

    
    def criarConta(self):

        self.user, dados = self.firebase.creatUser({
            'nome': self.tela_cadastro.nome.text(),
            'email': self.tela_cadastro.e_mail.text(),
            'password': self.tela_cadastro.senha.text(),
            })

        if self.user != None:
            QMessageBox.about(self, 'Atenção', 'Cadastro realizado com sucesso!')
            self.QtStack.setCurrentIndex(0)
            # print('usuario criado '+self.user['email'])
        else:
            QMessageBox.about(self, 'Atenção', 'Desculpe, não foi possível completar seu cadastro!')

    def voltarInicio(self):
        self.QtStack.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())