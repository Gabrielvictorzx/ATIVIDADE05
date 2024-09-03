lista = [1,54,7,2,645,87,32,45,3]

print[0]
print[0:5]

lista.sort()
lista.sort(reverse=True)
print(f'Lista ordena {lista}')

lista.remove(8)
lista.pop(7)
del lista[2:5]

nome = 'tavin'
lista.append(nome)
print(lista)

# inserção
lista.insert(1, 'victor')
print(lista)

# substituição
lista[2] = 'jean'
print(lista)

print('tavin' in lista)

if 'tavin' in lista:
    # esse bloco so sera executado quando a condicao é true
    print('Sim, o tavin esta na lista')
else:
    # esse bloco so sera executado quando a condicao é false
    print('Nao, o tavin nao esta na lista')   

print(20*'-', ' BOLETIM ESCOLAR ',20*'-')
