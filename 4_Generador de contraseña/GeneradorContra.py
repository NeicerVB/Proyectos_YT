# ¿Qué necesito?
# 0. Tamaño de la contraseña
# 1. Las letras, números y simbolos especiales
# 2. Tenemos que elegir de manera aleatoria un elemento de un conjunto de elementos

import random
import string

size_password = int(input("Digite la cantidad de carácteres que va a querer: "))

CHARACTERS = string.ascii_letters + string.digits + "!#$%&"
password = ""
password_force = True

print(CHARACTERS)

# Creamos un bucle para que la contraseña siempre tenga ciertos carácteres
# while password_force:
    
#     for i in range(0, size_password):
#         password += random.choice(CHARACTERS)
        
#     if 

# print(password)
# print(len(password))