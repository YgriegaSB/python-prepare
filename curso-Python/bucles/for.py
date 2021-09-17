# Bucle for

for i in [1,2,3,4,5]:
    print("hola mundo")

print("---------------------------")
coleccion = {"nicolas": 1, "veronica": 2, "alejandro": 3}
for i in coleccion:
    print(f"Elemento: {coleccion[i]}")

for i in coleccion:
    print(f"Elemento: {i}")

for i in coleccion:
    print(f"{i} -> {coleccion[i]}")

print("---------------------------")

# una forma mucho mejor .items

for clave,valor in coleccion.items():
    print(f"{clave} -> {valor}")

print("---------------------------")
# imprimo todo de corrido
for calve,valor in coleccion.items():
    print(f"{calve} -> {valor}", end=" || ")

print("---------------------------")
print("\tVerificacion Email")
email=False

for i in "nicolas@informatica.com":
    if i=="@" or i==".":
        email = True
if email == True:
    print("Email es correcto")
else:
    print("El email no es correcto")

# Range

for i in range(5):
    print(f"{i} hola")
