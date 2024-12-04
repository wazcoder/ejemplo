def verificar_ceros_consecutivos(*args):
    # Recorremos los argumentos y verificamos si hay dos ceros consecutivos
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

# Pedimos al usuario que ingrese los números
entrada = input("Ingresa los números separados por comas: ")

# Convertimos la entrada en una lista de números
numeros = tuple(map(int, entrada.split(',')))

# Llamamos a la función y mostramos el resultado
resultado = verificar_ceros_consecutivos(*numeros)
print("¿Hay ceros consecutivos?", resultado)
























































'''Entrada del usuario: Usamos input() para que el usuario introduzca los números separados por comas.
Conversión a una tupla: Usamos split(',') para dividir la cadena en una lista y map(int, ...) para convertir cada elemento a entero. Finalmente, se convierte a una tupla con tuple().
Llamada a la función: Pasamos los números como argumentos utilizando el operador *.
Resultado: Imprimimos si hay ceros consecutivos en los números ingresados.'''