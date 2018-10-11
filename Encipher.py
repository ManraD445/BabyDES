################################################################
#                                                              #
#   En esta ocacion trato de hacer un programa que cifre       #
#   deacuerdo con el algoritmo DES                             #
#                                                              #
################################################################


Mensaje = "Hola es un gusto saber de ti"

bloques=[] #Creo una lista para guardar los bloques de 64 bits.


x=8
y=0

for i in range(4): 
    bloques.append(Mensaje[y:x])
    x=x+8
    y=y+8

print(bloques)
