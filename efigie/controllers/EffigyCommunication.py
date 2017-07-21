#-*- coding: utf-8 -*-
# import gettext 
# import locale

# nameFileTraduction ='django'# nome do arquivo de traducao 
# namefolderLocationFileTraduction ='locale'# localizacao inicial do arquivo de traducao, a localizacao completa é locale\pt_BR\LC_MESSAGES 
# language = gettext.translation(nameFileTraduction, namefolderLocationFileTraduction, languages=['pt']) 
# language.install() # instalacao da Linguagem requerida 
# _ = language.ugettext # renomeando o gettext para _ 


IMAGE_BLANK = ('A imagem esta em branco.')

name_EXIST = ('Identificador ja cadastrado.')
name_BLANK = ('Identificador esta em branco.')

MESSAGE_BLANK      = ('A mensagem esta em branco.')
MESSAGE_BLANK_SIZE = ('A quantidade de vezes que a mensagem pode ser lida deve ser um numero maior que 0 ou deixada em branco')
MESSAGE_NOT_FOUND  = ('Nenhuma mensagem encontrada')
MESSAGE_LIMIT      = ('A mensagem ja excedeu o numero maximo de vezes que poderia ser lida')
MESSAGE_WRITE      = ('A mensagem foi gerada com sucesso.')
MESSAGE_SEARCH     = ('Como nenhuma imagem foi selecionada, busque uma abaixo')

KEY = ('A chave: ')
KEY_DELETE     = (' foi excluida com sucesso.')
KEY_DELETE_TITLE = ('Deletar a chave: ')
KEY_DELETE_DESCRIPTION = ('Voce tem certeza que deseja deletar a chave: ')
KEY_DELETE_BUTTON = ('Deletar')
KEY_NOT_DELETE = (' nao pode ser excluida.')
KEY_IMPORT     = (' foi importada com sucesso.') 
KEY_NOT_IMPORT = (' nao pode ser importada.') 
KEY_NEW        = (' foi criada com sucesso.') 
KEY_NOT_EXPORT = (' nao pode ser exportada.') 
KEY_EDIT       = (' nao pode ser editada.') 
KEY_NOT_EDIT   = (' nao pode ser alterada.') 
KEY_NOT_SHOW   = (' escolhida nao pode ser exibida.')
KEY_NOT_FOUND  = ('Nenhuma chave encontrada.')
KEY_BLANK_SIZE = ('Tamanho da chave nao esta selecionado.')



USER_ALREADY_REGISTER = ('Usuario ja cadastrado.')
USER_CONFIRMATION     = ('Uma confirmacao foi enviada para o seu endereco de e-mail, para realizar o login e necessario realizar a confirmacao antes.')
USER_CONFIRMATION_SUCCESS = ('Confirmacao de e-mail realizada com sucesso.')
USER_CONFIRMATION_DANGER = ('Confirmacao de e-mail nao encontrada.')
USER_CONFIRMATION_EXPIRED = ('Esta confirmacao de e-mail expirou.')
USER_NOT_DELETE       = ('Usuario nao pode ser excluido.')
USER_DELETE           = ('Usuario excluido com sucesso.')
USER_DELETE_TITLE       = ('Deletar seu usuario')
USER_DELETE_DESCRIPTION = ('Voce tem certeza que deseja deletar a sua conta de usuario? Todas as chaves relacionadas somentes a voce tambem serao apagadas')
USER_DELETE_BUTTON      = ('Deletar')
USER_FORGET_PASSWORD = ('Enviamos um e-mail com instrucoes.')
USER_LOGOUT           = ('Logout realizado com sucesso.')
USER_NOT_FOUND        = ('Usuario nao encontrado')
USER_INVALID          = ('Username/e-mail ou senha invalidos')
USER_NOT_EDIT         = ('Usuario nao pode ser alterado.')

PASSWORD_EDIT = ('Senha alterada com sucesso.')
PASSWORD_NOT_MATCH = ('Senhas nao correspondentes.')
PASSWORD_INVALID   = ('Senha atual invalida')

TOKEN_CREATE     = ('Segunda verificacao de login ativada com sucesso.')
TOKEN_NOT_CREATE = ('Segunda verificacao de login desativada com sucesso.')
TOKEN_INVALID    = ('Codigo invalido.')