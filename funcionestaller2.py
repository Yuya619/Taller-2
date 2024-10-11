import random 
from datetime import datetime
def add_m(du:str,dic:dict)-> list:
    lista=du.split("|") # separa el dato que ingresa el usuario con el caracter |
    codigo=lista[1].upper()+ "%03d" % random.randint(1,999) # extrae el tipo de mascota y le asigna un numero aleatorio 
    hora=datetime.now().time() # utiliza el modulo datetime para asignar la hora de ingreso de la mascota,toma la hora inmediata al registro
    lista.append(hora) # agrega la hora a la lista de datos ingresados por teclado 
    while codigo in dic: # verifica que el codigo(clave) no se repita en el diccionario, si se repite asignara uno nuevo, el ciclo me garantiza que se verifique las veces que sea necesario
        codigo=lista[1].upper()+ "%03d" % random.randint(1,999)
   
    print(lista)
    dic[codigo]=lista # agrega un registro con el codigo y los valores ingresados por el usuario
    return lista
print("lalal")
