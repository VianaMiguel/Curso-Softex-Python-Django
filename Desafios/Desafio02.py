""" Desafio: Analise de dados de acessos(Usuario , status, duração em minutos)"""

registros_acessos = []
sucesso = set()
minuto=0

while True:
    usuario = input(" Digite o nome de usuario (ou 'parar' para sair): ")
    if usuario=='parar':
        break

    status = int (input("digite '1' para 'sucesso' e '2' para 'falha':"))
    if status > 2:
        print(" Responda com 1 ou 2 apenas")
        continue

    try:
        duracao = int (input("Digite a duração da sessão em minutos: "))  
    except ValueError:
        print("Digite numeração de tempo")
        continue

    if status == 1:
        status_texto = "sucesso"
        sucesso.add(usuario)
        minuto += duracao
    else:
        status_texto= "falha"
    registros_acessos.append((usuario, status_texto, duracao))

print("Registro de acessos:", registros_acessos)
print("Usuarios com acesso bem-sucedido:", sucesso)
print("Tempo total de sessões bem-sucedidas:", minuto, "minutos")