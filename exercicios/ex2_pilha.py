# Exercício 2: escrever uma função que recebe uma string e diz se os parênteses, colchetes e chaves estão balanceados.
#"{[()]}" → True
#"{[(])}" → False
#"(()" → False

# O(n) tempo, O(n) memória no pior caso

def balanceador(texto):
    abridor = "([{"
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = []

    for caractere in texto:
        if caractere in abridor:
            pilha.append(caractere)
        elif caractere in pares:
            if len(pilha) == 0:
                return False
            topo = pilha.pop()
            if topo != pares[caractere]:
                return False

    return len(pilha) == 0


print("Válido:", balanceador("{[()]}"))       
print("Ordem errada:", balanceador("{[(])}"))  
print("Sobrou abridor:", balanceador("(()"))   
print("Fechador sem abridor:", balanceador(")"))  

