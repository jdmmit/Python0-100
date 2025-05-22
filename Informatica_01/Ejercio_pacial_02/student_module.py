def add_student():
    id_student = input("Ingrese el ID del estudiante: ")

    with open("database_student.txt", "a+") as database:
        database.seek(0)
        ids = database.read().splitlines()
        if id_student in ids:
            print("El ID ya existe. No se puede agregar el estudiante.")
            return

        name = input("Ingrese el nombre del estudiante: ")
        age = input("Ingrese la edad del estudiante: ")
        career = input("Ingrese la carrera del estudiante: ")
        grade = input("Ingrese la nota del estudiante: ")

        database.write(f"{id_student},{name},{age},{career},{grade}\n")

        print("Estudiante agregado exitosamente.")

        with open(f"{id_student}.txt", "w") as student_file:
            student_file.write(f"ID: {id_student}\n")
            student_file.write(f"Nombre: {name}\n")
            student_file.write(f"Edad: {age}\n")
            student_file.write(f"Carrera: {career}\n")
            student_file.write(f"Nota: {grade}\n")

        print(f"Estudiante {name} registrado con exito.")


def show_students():
    id_student = input("Ingrese el ID del estudiante: ")

    try:
        with open(f"{id_student}.txt", "r") as student_file:
            info = student_file.read()
            print("\n ====== INFORMACION DEL ESTUDIANTE ======")
            print(info)
    except FileNotFoundError:
        print("Estudiante no encontrado.")


def calculate_average():
    try:
        with open("database_student.txt", "r") as database:
            lines = database.read().splitlines()

        if not lines:
            print("No hay estudiantes registrados.")
            return

        total_grades = 0
        count = 0

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 5:
                try:
                    grade = float(parts[4])
                    total_grades += grade
                    count += 1
                except ValueError:
                    continue

        if count > 0:
            average = total_grades / count
            print(f"El promedio de notas es: {average:.2f}")
        else:
            print("No se encontraron notas para calcular.")
    except FileNotFoundError:
        print("No hay estudiantes registrados.")
