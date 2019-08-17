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

fb = fireBaseSD.initFb(config)

# print('Criar User')
# print(fb.creatUser({'email':'', 'password':'', 'nome':'', 'ativo':'', 'admin':''})

# print('Login')
# print(fb.login('teste@csada.com', '1233sd3'))

# print('Update')
# print(fb.updateUserDados(dados))

# print('Desativa')
# print(fb.desativaUser())

# print('Busca')
# print(fb.buscaUser({'nome':'teste'}))

# print('add Livro')
# print(fb.addBook({'ISBN':'', 'titulo':'', 'visible':'', 'pathCapa':''}))

# print('listar')
# print(fb.listarBooks())

# print('Busca Livro')
# print(fb.buscaBook({'isbn':'6125913153'}))

# print('Atualizar Livro')
# print(fb.updateBook(dados))

# print('Invisible livro')
# print(fb.setBookInvisible({'isbn': '6125913153'}))
