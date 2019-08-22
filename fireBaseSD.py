import pyrebase
import socket
import json
import os

path_cache = 'cache/'
path_imgs = 'images/'
cacheImgs = path_cache + path_imgs

confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']

def initFb(config):
    return FireBaseSD(config) 

def check_host():
    global confiaveis
    for host in confiaveis:
        a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.settimeout(.5)
        try:
            b=a.connect_ex((host, 80))
            if b==0:
                return True
        except:
            pass
        a.close()
    return False

class FireBaseSD:
    def __init__(self, config):
        self._firebase = pyrebase.initialize_app(config)
        self._db = self._firebase.database()
        self._auth = self._firebase.auth()
        self._storage = self._firebase.storage()
        self.books = []
        if 'cache' not in os.listdir():
            os.makedirs(cacheImgs)

    def creatUser(self, dados):
        if not check_host():
            return 'Não conectado'
        dado = None
        try:
            _email = dados['email']
            _password = dados['password']
            del dados['password']
            self._user = self._auth.create_user_with_email_and_password(_email, _password)
            self._db.child('users').child(self._user['localId']).set(dados)
            dado = self._db.child('users').child(self._user['localId']).get().val()
            return self._user, dado
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']['message']
            if _error == 'INVALID_EMAIL':
                dado = 'E-mail invalido'
            elif _error == 'EMAIL_EXISTS':
                dado = 'E-mail já cadastrado'
            elif _error == 'WEAK_PASSWORD : Password should be at least 6 characters':
                dado = 'Senha fraca: Senha com menos de 6 caracteres'
            else:
                dado = _error
            return None, dado

    def login(self, email, password):
        if not check_host():
            return 'Não conectado'
        try:
            self._user = self._auth.sign_in_with_email_and_password(email, password)
            return self._user
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return None

    def updateUserDados(self, dados):
        if not check_host():
            return 'Não conectado'
        try:
            self._db.child('users').child(self._user['localId']).update(dados)
            return 'Ok'
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return _error['message']

    def desativaUser(self):
        if not check_host():
            return 'Não conectado'
        return self.updateUserDados({'ativo': False})

    def ativaUser(self):
        if not check_host():
            return 'Não conectado'
        return self.updateUserDados({'ativo': True})

    def listarUsers(self):
        if check_host():
            return 'Não conectado'
        all_users = self._db.child("users").get()
        return [user.val()['nome'] for user in all_users.each()]

    def buscaUser(self, dados): # nome ou email mudar
        if not check_host():
            return 'Não conectado'
        all_users = self._db.child("users").get()
        keys = dados.keys()
        for user in all_users.each():
            userV = user.val()
            if 'nome' in keys:
                if userV['nome'].lower() == dados['nome'].lower():
                    return userV
            if 'email' in keys:
                if userV['email'] == dados['email']:
                    return userV
        return None

    def addBook(self, dados):
        # if check_host():
        #     return 'Não conectado'
        try:
            isbn = dados['isbn']
            del dados['isbn']
            if 'visible' not in dados.keys(): dados['visible'] = True
            if 'pathCapa' in list(dados.keys()):
                self.addCapa('images/books/'+isbn+'.png', dados['pathCapa'])
                dados['pathCapa'] = 'images/books/'+isbn+'.png'
            self._db.child('books').child(isbn).set(dados)
            return True
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return False
    
    def addCapa(self, pathFB, pathPC):
        if not check_host():
            return 'Não conectado'
        try:
            self._storage.child(pathFB).put(pathPC)
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return _error['message']

    def listarBooks(self):
        if not check_host():
            return 'Não conectado'
        all_books = self._db.child("books").get()
        tem = False
        for book in all_books.each():
            bookV = book.val()
            bookV['isbn'] = book.key()

            for bookCache in self.books:
                if bookCache['isbn'] == bookV['isbn']:
                    tem = True
                    break

            if not tem:
                self._storage.child(bookV['pathCapa']).download(cacheImgs+bookV['isbn']+".jpg")
                bookV['pathCapa'] = cacheImgs+bookV['isbn']+".jpg"
                self.books.append(bookV)
                tem = False
        return 'Ok'

    def buscaBook(self, dados, invisibles=False):
        if not check_host():
            return 'Não conectado'
        all_books = self._db.child("books").get()
        keys = dados.keys()
        for book in all_books.each():
            bookV = book.val()
            bookV['isbn'] = book.key()
            if 'nome' in keys:
                if (bookV['nome'].lower() == dados['nome'].lower()) & ((bookV['visible']) | (invisibles)):
                    return bookV
            if 'isbn' in keys:
                if (bookV['isbn'] == dados['isbn']) & ((bookV['visible']) | (invisibles)):
                    return bookV
        return None

    def updateBook(self, dados):
        if not check_host():
            return 'Não conectado'
        busca = {}
        if 'isbn' in dados.keys():
            busca['isbn'] = dados['isbn']
            del dados['isbn']
        # if 'titulo' in dados.keys(): busca['titulo'] = dados['titulo']
        # if len(dados.keys()) == 1 & dados.keys[0] == 'titulo':
            
        book = self.buscaBook(busca)
        if book == None:
            return 'Livro não disponivel'
        try:
            if 'pathCapa' in list(dados.keys()):
                self.addCapa('images/books/'+dados['isbn']+'.png', dados['pathCapa'])
                dados['pathCapa'] = 'images/books/'+dados['isbn']+'.png'
            self._db.child('books').child(book['isbn']).update(dados)
            return 'Ok'
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return _error['message']
        
    def setBookInvisible(self, dados):
        if not check_host():
            return 'Não conectado'
        book = self.buscaBook(dados)
        if book == None:
            return 'Livro não disponivel'
        self._db.child('books').child(book['isbn']).update({'visible': False})

    def setBookVisible(self, dados):
        if not check_host():
            return 'Não conectado'
        book = self.buscaBook(dados, True)
        if book == None:
            return 'Livro não disponivel'
        self._db.child('books').child(book['isbn']).update({'visible': True})

    def buscarUsuario(self, id):
        return self._db.child('users/'+str(id)).get().val()

    def buscarAllBooks(self):
        return self._db.child('books').get().val()

    def buscarOneBook(self, isbn):
        return self._db.child('books/'+str(isbn)+'/pathCapa').get().val()

    def buscarPorTitulo(self, titulo):
        pass

    def getCapa(self, path, isbn):
        try:
            self._storage.child(str(path)).download('images/downloaded_'+str(isbn)+'.png')
            return 'images/downloaded_'+str(isbn)+'.png'
        except:
            return ''

    def buscarPeloIsbn(self, isbn):
        return self._db.child('books/'+str(isbn)).get().val()
    def editarLivro(self, dados):
        try:
            if dados['capaEdited']:
                self.addCapa('images/books/'+dados['isbn']+'.png', dados['pathCapa'])
                dados['pathCapa'] = 'images/books/'+dados['isbn']+'.png'
                del dados['capaEdited']
            self._db.child('books/'+dados['isbn']).update(dados)
            return True
        except:
            return False
    
    def excluirLivro(self, isbn, path):
        try:
            self._db.child('books/'+isbn).remove()
            return True
        except:
            return False

# Inicio validação

# Fim validação
''' 
-- User
String - nome
Bool - admin
Bool - ativo
{'email':'', 'password':'', 'nome':'', 'ativo':'', 'admin':''}

-- Books
String - titulo
String - pathCapa
Bool - visible
String - ISBN  --- 10 ou 13
{'ISBN':'', 'titulo':'', 'visible':'', 'pathCapa':''}
'''