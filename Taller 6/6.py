futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),
(14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"),
(7, "Villa")]
futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print(futbolistasTup)
nums = [(4,9),(7,9),(11,0),(4,9),(5,11),(7,3)]
nums.sort(key=lambda numero: numero[0])
print(nums)
#a)Ordena las tuplas de "futbolistasTup" con respecto al primer elemento de ellas, el cual es un numero entero, por ejemplo: (1,"casillas") es el primero y luego le sigue (3,"Pique") y asi sucesivamente
#b)Estamos especificando que el vamos a ordenar las tuplas con respecto al primer elemento, por eso ponemos "Futbolistas[0]", si pusieramos por ejemplo "Futbolistas[1]" estariamos ordenando
#con respecto al segundo elemento que en este caso es un String  
#c) 
uno = [4,7,11,4,9,5,11,7,3,5]
uno.sort(key=lambda numero: numero)
print("Lista 1: ",uno)
tres = [47,3,21,32.56,92]
tres.sort(key=lambda numero: numero)
print("Lista tres: ",tres)
cuatro = [8,43,17,6,40,16,18,97,11,7]
cuatro.sort(key=lambda numero: numero)
print("lista 4: ",cuatro)
#La conclusion que se obtiene es que primero, al ser listas normales y no tuplas, hay que modificar un poco .sort para que no salgan errores ya que el original esta pensado para ordenar con respecto
#al primer elemento de la tupla.
#La segunda conclusion es que es inutil utilizar este metodo cuando se quiere ordenar una lista normal
#d)(1 es el peor y 100 es el mejor)
mejoresInventos = [("HTC Vive Pro Eye",50),("Hamburguesa vegetariana",1),("Dron Subacuatico",75),("Una silla",35),("Protesis con IA",90)]
mejoresInventos.sort(key=lambda inventos: inventos[1])
print(mejoresInventos)