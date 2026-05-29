#Listas, mutables
frutas = ["manzana", "banana", "naranja"]
print (frutas[0])
print (frutas[-1])

#agregar
frutas.append("uva")
#INSERTAR
frutas.insert(1,"pera")
print (frutas)

#remover
frutas.remove("banana")
#sacar ultimo elemento
ultimo = frutas.pop()
print("elemento eliminado",ultimo)
del frutas[0]

