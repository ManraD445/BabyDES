
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

print()

print("\nlos valores en ascii del primer bloque de 64 bits\n«««««««««»»»»»»»»»")
y=0
for i in bloque64_0:
    print(bloque64_0Ascii[y])
    y=y+1
print("««««««««»»»»»»»»")


bloque64_0Binario=[]
y=0
for i in range(8):
    auxBloque64_0Ascii=int(bloque64_0Ascii[y])
    binario=(bin(auxBloque64_0Ascii))
    binario = binario.replace("b", "")
    bloque64_0Binario.append(binario)
    y=y+1

print("\nlos valores en binario del primer bloque de 64 bits\n«««««««««»»»»»»»»»")
y=0
for i in range(8):
    print(bloque64_0Binario[y])
    y=y+1
print("««««««««»»»»»»»»")


print("\nlos valores en ascii y binario del primer bloque de 64 bits\n«««««««««»»»»»»»»»")
y=0
for i in range(8):
    print(bloque64_0Ascii[y],"  ««»»  ",bloque64_0Binario[y])
    y=y+1
print("««««««««»»»»»»»»")
