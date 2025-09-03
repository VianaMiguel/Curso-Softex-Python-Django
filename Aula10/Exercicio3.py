acessos=[("Pedro","sucesso"), ("Ana","falha"),("Maria","sucesso"), ("Pedro", "falha"),("Ana","falha") ]

usuarios_sucesso = set()
usuarios_falha = set()

for login, tentativa in acessos:
    if tentativa == "sucesso":
        usuarios_sucesso.add(login)

    elif tentativa == "falha":
        usuarios_falha.add(login)

com_falha = usuarios_falha.difference(usuarios_sucesso)

print(usuarios_sucesso)
print(com_falha)