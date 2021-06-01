#Para remover un iter de un set se usa el metodo remove(), o  el metodo discard().
#Usando el metodo remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Remover "banana" usando el metodo discard():
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Remover el ultimo item usando el metodo pop():
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(thisset)

#Metodo  clear() para vacial el set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)




