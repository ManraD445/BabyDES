
Mensaje="Hola es un gusto saber de ti"
Key="rabalero"
print("Texto plano »»",Mensaje,"\n")
print("la longitud de la cadena es de:",len(Mensaje),"caracteres")

bloque64=[]
x=8
y=0
for i in range(4):
    bloque64.append(Mensaje[y:x])
    x=x+8
    y=y+8

print("Se dibide el mensaje en bloques de 64bits »»",bloque64)
bloque64_0 = bloque64[0]
print("\nEl primer bloque contiene los caracteres\n«««««««»»»»»»»")
y=0
for i in bloque64_0:
    print(bloque64_0[y])
    y=y+1
print("««««««««»»»»»»»»")
y=0
bloque64_0Ascii=[]
for i in bloque64_0:
    auxAscii = str(ord(bloque64_0[y]))
    bloque64_0Ascii.append(auxAscii)
    y=y+1




bloque64_0Binario=[]
y=0
for i in range(8):
    auxBloque64_0Ascii=int(bloque64_0Ascii[y])
    binario=(bin(auxBloque64_0Ascii))
    binario = binario.replace("b", "")
    bloque64_0Binario.append(binario)
    y=y+1




print("\nlos valores en ascii y binario del primer bloque de 64 bits\n«««««««««»»»»»»»»»")
y=0
for i in range(8):
    print(bloque64_0Ascii[y],"  ««»»  ",bloque64_0Binario[y])
    y=y+1
print("««««««««»»»»»»»»")

###############################################################################################################################
key ="rabalero"
print("La llave es: ",key," & sus valores binario son »» ")

key_0Ascii=[]
y=0
for i in key:
    auxAscii = str(ord(key[y]))
    key_0Ascii.append(auxAscii)
    y=y+1


key_0Binario=[]
allBits_key=[]


for i in range(8):                              #el indece ira de 1 a 8
    auxkey_0Ascii=int(key_0Ascii[i])            #se toma el valir i de key_0Ascii & se le asigna a auxkey_0Ascii (Convertido en tipo entero... ya que estos datos estan guardados en tipo string)
    binario=(bin(auxkey_0Ascii))                #auxkey_0Ascii se convierte en binario (Este lo convierte en tipo cadena)
    binario = binario.replace("b", "")          #borramos la letra b que nos pone por defecto la funcion bin()...
    key_0Binario.append(binario)                #binario se guarda en key_0Binario (en grupos de 8 bits)

print("\nlos valores en ascii y binario de la llave son\n«««««««««»»»»»»»»»")
y=0
for i in range(8):
    print(key_0Ascii[y],"  ««»»  ",key_0Binario[y])
    y=y+1
print("««««««««»»»»»»»»")

for i in range(8):
    auxallBits_key=key_0Binario[i]
    for i in range(8):
        allBits_key.append(auxallBits_key[i])

print("Todos los bits de la llave »\n",allBits_key)
PC1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

keyplus=[]
y=0
for x in range(56):
    i=PC1[y]
    keyplus.append(allBits_key[i])
    y=y+1

print("\nK+ (key permutada) »",keyplus,"\n")

c_0=keyplus[:28:]
d_0=keyplus[28::]

print("C_0» ",c_0)
print("D_0» ",d_0)



#_----------------------------------------------------------------------------------------------
