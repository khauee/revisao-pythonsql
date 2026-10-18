produtos = [
    {"nome": "Mouse", "preco": 45.0, "categoria": "perifericos"},
    {"nome": "Teclado", "preco": 120.0, "categoria": "perifericos"},
    {"nome": "Monitor", "preco": 800.0, "categoria": "video"},
    {"nome": "Cabo HDMI", "preco": 30.0, "categoria": "video"},
]

# Exercício 1: a) Função que retorna só os produtos com preço acima de um valor passado.
# O(n) tempo, O(n) memória no pior caso

def produtos_preco_acima(produtos, valor):
    resultado = []
    for item in produtos:
        if item["preco"] > valor:
            resultado.append(item)

    return resultado


# Exercício 1: b) Função que retorna a lista de nomes dos produtos de uma categoria.
# O(n) tempo, O(n) memória no pior caso

def nome_por_categoria(produtos, categoria):
    resultado = []

    for item in produtos:
        if item["categoria"] == categoria:
            resultado.append(item["nome"])

    return resultado
        

# Exercício 1: c) Função que retorna o produto mais caro, sem usar max(). 
# O(n) tempo, O(1) memória

def produto_mais_caro(produtos):
    if len(produtos) == 0:
        return None
    
    produto_caro = produtos[0]

    for item in produtos:
        if item["preco"] > produto_caro["preco"]:
            produto_caro = item

    return produto_caro

print("Acima de 100:",produtos_preco_acima(produtos, 100))
print("Categoria video:", nome_por_categoria(produtos, "video"))
print("Mais caro:", produto_mais_caro(produtos))

