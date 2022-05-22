from random import randint

m = []
l = soma = 0
for x in range(1,11):
  a = []
  for y in range(1,11):
    numero = randint(10, 50)
    soma = soma+numero 
    a.append(numero)
  print(a)
  l += 1
  m.append(a)

print('==========+=============+===========') 

soma_t = 0
for linha in m:
  for coluna in linha:
    soma_t = soma_t+coluna 
print(f"o valor total é {soma_t}")

print('==========+=============+===========') 

b = []
for linha in m:
  c = []
  for coluna in linha:
    nu_3 = coluna*3
    c.append(nu_3)
  b.append(c)
  print(c)
