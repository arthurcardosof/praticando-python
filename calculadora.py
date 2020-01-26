# comentario em linha
'''
comentario
em
varias linhas
'''

''' Crie uma calculadora em Python usando funções:
Essas funções serão chamadas do jeito:
soma(a,b)
subtracao(a,b)
divisao(a,b)
multiplicacao(a,b)
Desafio extra: quando ser feita a divisão, não pode dividir por 0;
'''

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def divisao(a,b):
    if b > 0:
        return a // b
    return 'Erro'

def multiplicacao(a,b):
    return a * b

def resto(a,b):
    return a % b

print(soma(-20, 2)) # -18
print(subtracao(1, -1)) # 2 
print(divisao(10,2))
print(multiplicacao(20, 3)) #60

print(divisao(10,0))
