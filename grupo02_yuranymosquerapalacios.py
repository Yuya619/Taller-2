
from funcionestaller2 import add_m
dic={}
while True:
    print("\n\n1.ingresar info de mascota\n2.editar informacion\n3.eliminar informacion\n4.ver informacion\n5.buscar mascota\n6.salir\n\n")
    mn=int(input("seleccione una opcion: "))
    if mn==1:
        datos=input("ingrese los datos de la mascota siguiendo este formato: nombre|tipo(P=perro,G=gato,A=ave,T=tortuga|edad|razon de visita|diagnostico: ")
        add_m(datos,dic)
    if mn==6:
        break
    
        
print(dic)