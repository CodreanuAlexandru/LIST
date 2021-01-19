lista1=list(eval(input('Introduceti lista de numere:')))
print(lista1)
lista2=sorted(lista1)
print(lista2)
lista3=sorted(lista1,reverse=True)
print(lista3)
print(len(lista1))
print(max(lista1),min(lista1),sep="\n")
lista4=lista1+[111]
print(lista4)
lista5=lista1
lista5.insert(1, 222)
print(lista5)