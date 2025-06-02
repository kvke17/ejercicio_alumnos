#ejercicio de los alumnos:
import os, msvcrt


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
        pass
    elif opc =="2":
        pass
    elif opc =="3":
        print("fin del programa")
        break
    else:
        print("opcion incorrecta")
    print("\n.... presione una tecla para coninuar.....")
    msvcrt.getch()