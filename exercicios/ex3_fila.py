#Exercicio 3: Fila
from collections import deque

print("------------Usando lista------------")

fila = []

def atender():
    if len(fila) == 0:
        return None
    return fila.pop(0)  # O(n): desloca os outros itens

def chegar(nome):
    fila.append(nome)

def tamanho():
    return len(fila)

chegar("Ana")
chegar("Bruno")
chegar("Carla")
print("Atendeu:", atender())   
print("Tamanho:", tamanho())   
print("Atendeu:", atender())   
print("Tamanho:", tamanho())  
print("Atendeu:", atender())   
print("Tamanho:", tamanho()) 
print("Atendeu:", atender()) 

print("------------Usando Deque------------")

fila1 = deque()

def chegar1(nome):
    fila1.append(nome)

def atender1():
    if len(fila1) == 0:
        return None
    return fila1.popleft()  # O(1)

def tamanho1():
    return len(fila1)

chegar1("Ana")
chegar1("Bruno")
chegar1("Carla")
print("Atendeu:", atender1())   
print("Tamanho:", tamanho1())   
print("Atendeu:", atender1())   
print("Tamanho:", tamanho1())  
print("Atendeu:", atender1())   
print("Tamanho:", tamanho1()) 
print("Atendeu:", atender1()) 