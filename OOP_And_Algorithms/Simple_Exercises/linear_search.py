import random

def linear_search(lista, objetivo):
    match = False

    for item in lista: # O(n)
        if(item == objetivo):
            match = True
            break
    return match

if __name__=='__main__':
    tamanioLista = int(input('Tamaño de lista: '))
    objetivo = int(input('Que numero deseas buscar? '))
    lista = [random.randint(0,100) for i in range(tamanioLista)]
    lista.sort()
    print(lista)
    encontrado = linear_search(lista,objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    