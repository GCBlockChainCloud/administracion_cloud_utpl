import os

nombre = os.getenv("NOMBRE", "estudiante")
entorno = os.getenv("ENTORNO", "desarrollo")

print(f"Hola {nombre}, este contenedor esta en el entorno: {entorno}")
