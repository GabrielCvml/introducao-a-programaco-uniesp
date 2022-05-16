#lista = [] Primeira Tentativa 
#for n in range(1,21): 
#    lista.append(n)
#print(lista)
#lista.reverse
#print(lista)

# Segunda tentativa 
lista = []
for n in range(20): 
 numeros = int(input('Digite seu número: '))
 lista.append(numeros)
print('Essa é a sua lista: ' ,lista )

SorN = str(input('Você que ver a lista na forma reversa ? ( Sim ou Não): '))

if SorN == 'Sim':
  lista.reverse()
  print(f'Essa é a sua lista {lista}')
else:
  print('Tudo OK')
 