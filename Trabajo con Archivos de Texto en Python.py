# Escritura de Archivo de Texto con datos personales
with open("my_notes.txt", "w") as file:
    file.write("Esta es mi primera línea de notas.\n")
    file.write("Hoy he aprendido sobre la manipulación de archivos en Python.\n")
    file.write("Es importante recordar cerrar los archivos después de usarlos.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # Eliminar saltos de línea adicionales al imprimir