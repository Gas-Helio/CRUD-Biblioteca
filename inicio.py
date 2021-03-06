from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from telas.tela_inicial import Ui_Tela_Inicio
from telas.tela_cadastro import Ui_Tela_Cadastro
from telas.tela_cadastro_livro import Ui_Tela_Cadastro_Livro
from telas.tela_buscar import Ui_Tela_Buscar
from telas.tela_principal import Ui_Tela_Principal
from telas.tela_acervo import Ui_Tela_Acervo
from telas.tela_buscar import Ui_Tela_Buscar
from telas.tela_editar_livro import Ui_Tela_Editar_Livro
from PyQt5.QtGui import QPixmap
import PyQt5
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
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_inicio = Ui_Tela_Inicio()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro = Ui_Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_principal = Ui_Tela_Principal()
        self.tela_principal.setupUi(self.stack2)

        self.tela_cadastro_livro = Ui_Tela_Cadastro_Livro()
        self.tela_cadastro_livro.setupUi(self.stack3)

        self.tela_acervo = Ui_Tela_Acervo()
        self.tela_acervo.setupUi(self.stack4)

        self.tela_buscar = Ui_Tela_Buscar()
        self.tela_buscar.setupUi(self.stack5)

        self.tela_editar_livro = Ui_Tela_Editar_Livro()
        self.tela_editar_livro.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.firebase = FireBaseSD(config)
        self.user = None
        self.capaEdited = False
        self.setupUi(self)

        self.tela_inicio.botao_entrar.clicked.connect(self.entrar)
        self.tela_inicio.botao_criar_conta.clicked.connect(self.openCriarConta)

        self.tela_cadastro.botao_salvar.clicked.connect(self.criarConta)
        self.tela_cadastro.toolButton.clicked.connect(self.voltarInicio)

        self.tela_principal.cadastrar_novo_livro.clicked.connect(self.openCadastrarLivro)
        self.tela_principal.ver_acervo.clicked.connect(self.openAcervoLivro)
        self.tela_principal.sair.clicked.connect(self.voltarInicio)

        self.tela_cadastro_livro.botao_selecionar_img.clicked.connect(self.selecionarImagem)
        self.tela_cadastro_livro.botao_salvar_livro.clicked.connect(self.cadastrarLivro)
        self.tela_cadastro_livro.buttonVoltar.clicked.connect(self.voltarPrincipal)

        self.tela_buscar.botao_voltar.clicked.connect(self.voltarPrincipal)
        self.tela_buscar.tableWidget.cellClicked.connect(self.celulaClicada)
        self.tela_buscar.pushButton.clicked.connect(self.buscar)

        self.tela_editar_livro.botao_editar_livro.clicked.connect(self.editarLivro)
        self.tela_editar_livro.botao_selecionar_img.clicked.connect(self.selecionarImagemEditar)
        self.tela_editar_livro.botao_excluir_livro.clicked.connect(self.excluirLivro)
        self.tela_editar_livro.botao_voltar.clicked.connect(self.openAcervoLivro)

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
            print(dados)
            QMessageBox.about(self, 'Atenção', 'Desculpe, não foi possível completar seu cadastro!')

    def voltarInicio(self):
        self.tela_inicio.e_mail_login.setText('') 
        self.tela_inicio.senha_login.setText('')
        self.user != None
        self.QtStack.setCurrentIndex(0)

    def voltarPrincipal(self):
        self.QtStack.setCurrentIndex(2)

    def openCadastrarLivro(self):
        self.QtStack.setCurrentIndex(3)

    def openAcervoLivro(self):
        dados_livros = self.firebase.buscarAllBooks()

        self.tela_buscar.tableWidget.setColumnWidth(0, 95)
        self.tela_buscar.tableWidget.setColumnWidth(1, 273)
        self.tela_buscar.tableWidget.setColumnWidth(2, 273)
        self.tela_buscar.tableWidget.setColumnWidth(3, 125)
        self.tela_buscar.tableWidget.setColumnWidth(4, 100)

        if dados_livros != None:
            self.tela_buscar.tableWidget.setRowCount(len(dados_livros))
            for i, value in enumerate(dados_livros):
                self.tela_buscar.tableWidget.setItem(i, 0, QTableWidgetItem(str(value)))
                self.tela_buscar.tableWidget.setItem(i, 1, QTableWidgetItem(str(dados_livros[value]['titulo'])))
                self.tela_buscar.tableWidget.setItem(i, 2, QTableWidgetItem(str(dados_livros[value]['autor'])))
                self.tela_buscar.tableWidget.setItem(i, 3, QTableWidgetItem(str(dados_livros[value]['quantPaginas'])))
                self.tela_buscar.tableWidget.setItem(i, 4, QTableWidgetItem(str(dados_livros[value]['ano'])))
        else:
            for _ in range(self.tela_buscar.tableWidget.rowCount()):
                self.tela_buscar.tableWidget.removeRow(_)
        self.QtStack.setCurrentIndex(5)
    
    def selecionarImagem(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '/home', "PNG (*.png);;JPEG  (*.jpeg);;JPG  (*.jpg)")
        pixmap = QPixmap(self.fileName)
        pixmap1 = pixmap.scaled(161, 201)
        self.tela_cadastro_livro.colocar_imagem.setPixmap(pixmap1)
        self.capaEdited = True

    def cadastrarLivro(self):
        dados_livro = {
            'titulo': self.tela_cadastro_livro.titulo.text(),
            'isbn': self.tela_cadastro_livro.isbn.text(),
            'quantPaginas': self.tela_cadastro_livro.qtd_pag.text(),
            'autor': self.tela_cadastro_livro.autor.text(),
            'ano': self.tela_cadastro_livro.ano_publi.text(),
        }
        if self.capaEdited:
            dados_livro['pathCapa'] = self.fileName
        self.capaEdited = False
        if self.validar(dados_livro):
            self.tela_cadastro_livro.titulo.setText('')
            self.tela_cadastro_livro.isbn.setText('')
            self.tela_cadastro_livro.qtd_pag.setText('')
            self.tela_cadastro_livro.autor.setText('')
            self.tela_cadastro_livro.ano_publi.setText('')
            if self.firebase.addBook(dados_livro):
                QMessageBox.about(self, 'Atenção', 'Livro cadastrado com sucesso!')
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, 'Atenção', 'Erro ao cadastrar livro!')
            self.fileName = 'images/nada.png'
            pixmap = QPixmap(self.fileName)
            pixmap1 = pixmap.scaled(161, 201)
            self.tela_cadastro_livro.colocar_imagem.setPixmap(pixmap1)

    def celulaClicada(self):
        row = self.tela_buscar.tableWidget.currentRow()
        
        dados_livro = {
            'isbn': self.tela_buscar.tableWidget.item(row, 0).text(),
            'titulo': self.tela_buscar.tableWidget.item(row, 1).text(),
            'autor': self.tela_buscar.tableWidget.item(row, 2).text(),
            'quantPaginas': self.tela_buscar.tableWidget.item(row, 3).text(),
            'ano': self.tela_buscar.tableWidget.item(row, 4).text()
        }
        path_img = self.firebase.buscarOneBook(self.tela_buscar.tableWidget.item(row, 0).text())
        self.tela_editar_livro.titulo.setText(dados_livro['titulo'])
        self.tela_editar_livro.ano_publi.setText(dados_livro['ano'])
        self.tela_editar_livro.autor.setText(dados_livro['autor'])
        self.tela_editar_livro.qtd_pag.setText(dados_livro['quantPaginas'])
        self.tela_editar_livro.isbn.setText(dados_livro['isbn'])
        pixmap = QPixmap(self.firebase.getCapa(path_img, dados_livro['isbn']))
        pixmap1 = pixmap.scaled(161, 201)
        self.tela_editar_livro.colocar_imagem.setPixmap(pixmap1)
        self.tela_editar_livro.caminho_img = path_img
        self.QtStack.setCurrentIndex(6)

    def buscar(self):
        if self.tela_buscar.lineEdit.text() == '':
                QMessageBox.about(self, "Atenção", "Campo em branco")
        else:
            if self.tela_buscar.comboBox.currentText() == 'ISBN':
                dados_livros = self.firebase.buscarPeloIsbn(self.tela_buscar.lineEdit.text())
                if dados_livros != None:
                    for _ in range(self.tela_buscar.tableWidget.rowCount()):
                        self.tela_buscar.tableWidget.removeRow(_)
                    self.tela_buscar.tableWidget.setRowCount(1)
                    self.tela_buscar.tableWidget.setItem(0, 0, QTableWidgetItem(str(self.tela_buscar.lineEdit.text())))
                    self.tela_buscar.tableWidget.setItem(0, 1, QTableWidgetItem(str(dados_livros['titulo'])))
                    self.tela_buscar.tableWidget.setItem(0, 2, QTableWidgetItem(str(dados_livros['autor'])))
                    self.tela_buscar.tableWidget.setItem(0, 3, QTableWidgetItem(str(dados_livros['quantPaginas'])))
                    self.tela_buscar.tableWidget.setItem(0, 4, QTableWidgetItem(str(dados_livros['ano'])))
                else:
                    QMessageBox.about(self, "Atenção", "Não foi encontrado nenhum livro com: "+self.tela_buscar.lineEdit.text())
            elif self.tela_buscar.comboBox.currentText() == 'Titulo':
                dados_livros = self.firebase.buscaBook({'titulo':self.tela_buscar.lineEdit.text()})
                if dados_livros != None:
                    for _ in range(self.tela_buscar.tableWidget.rowCount()):
                        self.tela_buscar.tableWidget.removeRow(_)
                    self.tela_buscar.tableWidget.setRowCount(1)
                    print(dados_livros)
                    self.tela_buscar.tableWidget.setItem(0, 0, QTableWidgetItem(str(self.tela_buscar.lineEdit.text())))
                    self.tela_buscar.tableWidget.setItem(0, 1, QTableWidgetItem(str(dados_livros['titulo'])))
                    self.tela_buscar.tableWidget.setItem(0, 2, QTableWidgetItem(str(dados_livros['autor'])))
                    self.tela_buscar.tableWidget.setItem(0, 3, QTableWidgetItem(str(dados_livros['quantPaginas'])))
                    self.tela_buscar.tableWidget.setItem(0, 4, QTableWidgetItem(str(dados_livros['ano'])))
                else:
                    QMessageBox.about(self, "Atenção", "Não foi encontrado nenhum livro com: "+self.tela_buscar.lineEdit.text())

    def editarLivro(self):
        self.editar_livro = {
            'isbn': str(self.tela_editar_livro.isbn.text()),
            'titulo': str(self.tela_editar_livro.titulo.text()),
            'autor': str(self.tela_editar_livro.autor.text()),
            'quantPaginas': str(self.tela_editar_livro.qtd_pag.text()),
            'ano': str(self.tela_editar_livro.ano_publi.text()),
            'pathCapa': str(self.tela_editar_livro.caminho_img),
            'capaEdited': self.capaEdited
        }

        if self.validar(self.editar_livro):
            if self.firebase.editarLivro(self.editar_livro): 
                QMessageBox.about(self,'Atenção', 'Livro editado com sucesso!!')
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self,'Atenção', 'Livro não editado!!')
                self.QtStack.setCurrentIndex(2)
        self.capaEdited = False

    def selecionarImagemEditar(self):
        self.fileNameEditar, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '/home', "PNG (*.png);;JPEG  (*.jpeg);;JPG  (*.jpg)")
        pixmap = QPixmap(self.fileNameEditar)
        pixmap1 = pixmap.scaled(161, 201)
        self.tela_editar_livro.caminho_img = self.fileNameEditar
        self.capaEdited = True
        self.tela_editar_livro.colocar_imagem.setPixmap(pixmap1)

    def excluirLivro(self):
        if self.firebase.excluirLivro(self.tela_editar_livro.isbn.text(), self.tela_editar_livro.caminho_img):
            QMessageBox.about(self,'Atenção', 'Livro excluido com sucesso!!')
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.about(self,'Atenção', 'Livro não excluido!!')
            self.QtStack.setCurrentIndex(2)

    def validar(self, dados):
        keys = list(dados.keys())
        if 'isbn' in keys:
            if ((len(dados['isbn']) != 11) == (len(dados['isbn']) != 13)) or not self.isNumero(dados['isbn']):
                QMessageBox.about(self,'Atenção', 'ISBN invalido!!')
                return False
        if 'quantPaginas' in keys:
            if self.isNumero(dados['quantPaginas']):
                if int(dados['quantPaginas']) < 0:
                    QMessageBox.about(self,'Atenção', 'Quantidade de paginas invalida: Número negativo!!')
                    return False
            else:
                QMessageBox.about(self,'Atenção', 'Quantidade de paginas invalida: Não é número!!')
                return False
        if 'ano' in keys:
            if not self.isNumero(dados['ano']):
                QMessageBox.about(self,'Atenção', 'Ano de publicação invalido invalido!!')
                return False
        return True

    def isNumero(self, dado):
        try:
            s = int(dado)
            return True
        except:
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())