def mostrar_menu():
    print("**MENU**")
    print("1. Añadir Tarea")
    print("2. Ver Tareas")
    print("3. Eliminar Tarea")
    print("4. Marcar como Completado")
    print("5. Salir")


def ejecutar_lista_tareas():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            tarea = input("Agrega una nueva tarea: ")
            tareas.append(tarea)
        elif opcion == "2":
            print("Tareas: \n")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            print("\n")
        elif opcion == "3":
            indice = (
                int(input("Indique el numero de la tarea a eliminar: ")) - int("1"))
            if 0 <= indice < len(tareas):
                tareas.pop(indice)
            else:
                print("numero de tarea no valido.")
        elif opcion == "4":
            indice2 = int(input("Que tarea has completado: ")) - int("1")
            if 0 <= indice2 < len(tareas):
                tareas[indice2] = tareas[indice2] + " - COMPLETADO"
            else:
                print("Opcion no valida!")
                break
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida!")


ejecutar_lista_tareas()
