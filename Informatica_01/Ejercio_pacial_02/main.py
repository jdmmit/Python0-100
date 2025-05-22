import student_module


def main():
    while True:
        print("\n ===== MENU GESTION DE ESTUDIANTES =====")
        print("1. Agregar Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Calcular Promedio de notas")
        print("4. Salir")

        option = input("\n Seleccione una opción del (1 - 4): ")
        if option == "1":
            student_module.add_student()
        elif option == "2":
            student_module.show_students()

        elif option == "3":
            student_module.calculate_average()
        elif option == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


if __name__ == "__main__":
    main()
