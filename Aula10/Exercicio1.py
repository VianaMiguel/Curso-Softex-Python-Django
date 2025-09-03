vendas=[("Teclado",50,2), ("Mouse", 25.50,4), ("Monitor", 300,1),("Fone", 45, 1), ("Webcam", 75.20,2)] 

vendas_filtradas= list() #[] tambem podemos usar
produtos_unicos= set() # Conjunto Vacio

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        vendas_filtradas.append((produto, valor, quantidade))
    
    produtos_unicos.add(produto)

print("Vendas Filtradas (valor total >= 100:)")
print(vendas_filtradas)
print("\nProdutos únicos:")
print(produtos_unicos)