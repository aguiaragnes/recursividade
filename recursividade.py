# exemplo 1
def imprimir_num_recursivo(num):
    if num < 5:
        print(num)
        imprimir_num_recursivo(num + 1)

imprimir_num_recursivo(0)


# exemplo 1.1
def imprimir_num_recursivo(num):
    if num < 5:
        imprimir_num_recursivo(num + 1)
        print(num)
       
imprimir_num_recursivo(0)