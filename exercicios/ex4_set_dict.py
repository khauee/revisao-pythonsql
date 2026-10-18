# Exercício 4: dict e set

# a) Frequência de cada palavra
# O(n) tempo, O(k) memória (k = palavras diferentes)
def contagem_palavras(palavras):
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem


# b) Remover duplicatas mantendo a ordem
# O(n) tempo, O(n) memória
def remove_duplicata(valores):
    resultado = []
    vistos = set()
    for valor in valores:
        if valor not in vistos:
            vistos.add(valor)
            resultado.append(valor)
    return resultado


# c) Interseção de duas listas (sem repetidos)
# Versão com set: O(n + m) tempo
def interseccao(lista1, lista2):
    conjunto = set(lista2)
    resultado = []
    for numero in lista1:
        if numero in conjunto and numero not in resultado:
            resultado.append(numero)
    return resultado


# Versão ingênua com dois for: O(n * m) tempo
def interseccao_ingenua(lista1, lista2):
    resultado = []
    for numero1 in lista1:
        for numero2 in lista2:
            if numero1 == numero2 and numero1 not in resultado:
                resultado.append(numero1)
    return resultado


print("a) Contagem:", contagem_palavras(["a", "b", "a", "c", "a"]))
print("a) Lista vazia:", contagem_palavras([]))
print("b) Sem duplicatas:", remove_duplicata([3, 1, 3, 2, 1]))
print("c) Interseção (set):", interseccao([1, 2, 2, 3], [2, 2, 3]))
print("c) Interseção (ingênua):", interseccao_ingenua([1, 2, 2, 3], [2, 2, 3]))