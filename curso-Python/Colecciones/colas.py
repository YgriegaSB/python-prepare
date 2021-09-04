# colas
# el primero en entrar, primero en Salir

cola = ["maria", "andres", "felipe", "francisco"]
#agregar
cola.append("carla")
print(cola)
cola.append("flor")
print(cola)

#eliminar por el principio
n = cola.pop(0)
print(f"estan atendiendo a {n}")
print(cola)