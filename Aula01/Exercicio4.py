"""EXERCICIOS - 4

Sistema de Login Básico (while e break):

○ Defina um nome de usuário e uma senha corretos (ex: admin, 1234).
○ Use um loop while True para pedir ao usuário que digite o nome de usuário e a
senha.
○ Se ambos estiverem corretos, imprima "Login bem-sucedido!" e use break para
sair do loop.
○ Se estiverem incorretos, imprima "Login inválido. Tente novamente. """

#Defino login correto:
def_login = "admin"
#Defino senha correta:
def_senha = "1234"
#Uso While True (True tem que ser com maiusculo):
while True:
  #Peço o Login de entrada:
  login = input("Entre com seu Login: ")
  #Peço a Senha de entrada tbm:
  senha = input("Entre com sua Senha: ")
  #Condiciono as duas entradas com AND para serem vdd:
  if login == def_login and senha == def_senha:
    #Se ambas certas login aceito:
    print("Login bem-sucedido!")
    #Com isso paro o Loop:
    break
  #Se não:
  else:
    #O loop continua até login ter sucesso:
    print("Login inválido. Tente novamente.")