#Imprimiendo un valor indexado
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#banana
#Imprimiendo un rango de valores Indexados
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Cherry orange

#Comparación
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Si esta dentro de la tupla")

#Recorrido con for:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


