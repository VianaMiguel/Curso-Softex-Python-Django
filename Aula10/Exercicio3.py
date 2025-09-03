acessos=[("Pedro","sucesso"), ("Ana","falha"),("Maria","sucesso"), ("Pedro", "falha"),("Ana","falha") ]

usuarios_sucesso = set()
usuarios_falha = set()

for login, tentativa in acessos:
    if acessos == "sucesso":
        usuarios_sucesso.add(login)

    elif acessos == "falha":
        usuarios_falha.add(login)

com_falha = usuarios_falha.difference(usuarios_sucesso)

print(com_falha)
