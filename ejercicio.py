#ejercicio de los alumnos:
import os, msvcrt

alumnos=[]

menu="""Menu
1. agregar alumno
2. ver alumnos
3. salir"""

while True:
    os.system("cls")
    print(menu)
    opc=input("ingrese opcion: ")
    os.system("cls")
    if opc =="1":
        print("Agregar alumno")
        codigo = input("ingrese código: ")
        Edad = int(input("ingrese edad: "))
        nombre = input("ingrese nombre: ")
        alumno={
            "codigo": codigo,
            "nombre": nombre,
            "edad": Edad
        }
        alumnos.append(alumno)
        print("alumnos guardado con éxito")
    elif opc =="2":
        print("Ver Alumnos")
        for a in alumnos:
            print(f"El alumno {a["nombre"]} de codigo {a["codigo"]} tiene {a["edad"]} años")
            #print(a)
    elif opc =="3":
        print("fin del programa")
        break
    else:
        print("opcion incorrecta")
    print("\n.... presione una tecla para coninuar.....")
    msvcrt.getch()