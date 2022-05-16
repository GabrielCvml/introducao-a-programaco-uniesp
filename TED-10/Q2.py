import random 
vet = []
repetidos = []
for numero in range (0,51):
  vet.append(random.randint(1,10))
print(vet)
for i in vet:
  if i not in repetidos:
    print('numero repetido:', i)
    repetidos.append(i)