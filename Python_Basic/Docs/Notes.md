- Siempre escribir una funcion que corra todo el codigo ejem:
    def run():
        palabra = input("Escribe una palabra: ")
    if __name__=="__main__":
        run()
        
- Transformar numero a:
    pesos = float(pesos) = convertir a Decimales
    dolares = round(dolares, 2) = especificar número de decimales
    pesos = str(pesos) = convertir a Caracteres
    pesos = int(pesos) = convertir a Entero

- Definir una funcion ejm:
    def imprimir_mensaje(): 
        print("mensaje especial: ")
        print("estoy aprendiendo a usar funciones")

- Cadenas de caracteres:
    nombre.upper() = Metodo para poner nombre en mayusculas
    nombre.capitalize() = Metodo para poner primera letra de nombre en mayusculas
    nombre.strip() = Metodo para eliminar espacios basura del inicio o final del nombre
    nombre.lower() = Metodo para poner nombre en minusculas
    nombre.replace("o", "a") = Metodo para remplazar caracteres
    nombre[0] = Devuelve el caracter que necesitamos
    len(nombre) = Devuelve el número de caracteres de nombre

- slices
    nombre[0:3] = Devuelve los caracter comprendidos en ese rango
    nombre[0:7:2] = Devuelve los caracter comprendidos en ese rango pero con pasos de 2 en 2
    
- Otros
    import random = Importa una libreria para crear cosas aleatorias
    LIMITE = 1000 = Colocando el nombre en mayuscula se crea una constante

- Listas
    numeros = [1, 3, 6, "hola", 5] = Para guardar varios datos
    numeros.append(9) = Para agregar un dato a la lista
    numeros.pop(1) = Para eliminar un elemento de la lista

    for elemento in numeros: #Para colocar la lista en columna
    print(elemnto)

- Tupla
    mi_tupla=(1, 5, 6) = crear una Tupla
        Nota. Estructura de datos más rapida, pero son inmutables osea que no se pueden modificar