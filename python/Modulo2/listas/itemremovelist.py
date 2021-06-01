#EL metodo remove() elimina el item especificado.
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#El metodo pop() remueve un index especifico.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#SI lo no indicas nada remueve el ultimo valor.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#EL metodo delete elimina la lista:

thislist = ["apple", "banana", "cherry"]
del thislist

#El metodo clear limpia la lista.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

