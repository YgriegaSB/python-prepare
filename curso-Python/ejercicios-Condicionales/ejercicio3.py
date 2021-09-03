# pide un caracter, indica si es vocal o no

vocal = input('Digite una letra -> ').lower()
 # metodo lower transforma a minusculas las mayusculas
#forma muy larga - comentario propio
if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
    print(f"{vocal} -> es una vocal")
else:
    print(f"{vocal} -> no es una vocal")
