'''
Exercicio: Crie uma função para verificar se uma palavra é palíndrome. Retorna true se for uma palavra palíndrome, e false se não for.
Exemplos de palavras palindromes: ovo, arara
'arara' -> [0], [1], [2]
'''

def palindrome(palavra): return palavra == palavra[::-1]


print(palindrome('arara'))

print(palindrome('murilo'))
print(palindrome('OVO'))


        
def contaAte1000():
    for i in range(1000):
        print(i)

contaAte1000()
        
