"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


from dataclasses import dataclass


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = open('data.csv', 'r').readlines()

    col2= [int(row[2])for row in data]
    sum_col2= sum(col2)       
    #print(sum_col2)    
    return sum_col2

pregunta_01()

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data=[linea.replace('\t',';')for linea in data]
    
    col1= [row[0] for row in data]
    contador = dict((k, col1.count(k)) for k in col1)
    lista_tuplas=list(zip(contador.keys(), contador.values()))
    lista_tuplas.sort()
    #print(lista_tuplas)
    return lista_tuplas

pregunta_02


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data=[linea.replace('\t',';')for linea in data]
    
    claves=[row[0] for row in data]
    
    valor=[int(row[2]) for row in data]
    list_clave=set(claves)
    lista_tupla2=[]
    for k in list_clave:
        c=0
        for indice, x in enumerate(claves):
            if k==x:
                c+=valor[indice]
        lista_tupla2.append((k, c))
        lista_tupla2.sort()
    #print(lista_tupla2)
    return lista_tupla2

pregunta_03

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', 'r') as file:
        data= file.readlines()
    
    data=[row.split('\t')[2] for row in data]
    data=[(row[5:7]) for row in data]
    contador = dict((k, data.count(k)) for k in data)
    contador=list(zip(contador.keys(), contador.values()))
    contador.sort()
    str(contador)
    #print(contador)
    return contador

pregunta_04


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data= file.readlines()
    
    data= [row.split('\t') for row in data]
    data= [(row[0], int(row[1])) for row in data]
    
    result={}
    for letra, valor in data:
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra]=[valor]
    result= [(key, max(valor), min(valor)) for key, valor in result.items()]
    result= sorted(result, key=itemgetter(2) ,reverse=True)
    result.sort()
    #print(result)
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data= file.readlines()

    data= [row.split('\t') for row in data]
    data=[(row[4].replace('\n','').split(',')) for row in data]
    lista2=[]
    for item in  data:
        lista2+=item
    #print(lista2)
    lista2=[tuple(str.split(':')) for str in lista2]
    #print(lista2)
    resultado={}
    for letras, valor in lista2:
        valor=int(valor)
        if letras in resultado.keys():
            resultado[letras].append(valor)
        else:
            resultado[letras]=[valor]
    #print(resultado)
    resultado= [(key, min(val), max(val))for key, val in resultado.items()]
    resultado=sorted(resultado, key=itemgetter(0), reverse=False)
    #print(resultado)
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data= file.readlines()
   
    data= [row.split('\t') for row in data]
    data= [row.replace('\n', '') for row in data]
    data= [(int(row[1]), row[0]) for row in data]
    resultado={}
    for valor, letras  in data:
        if valor in resultado.keys():
            resultado[valor].append(letras)
        else:
            resultado[valor]=[letras]
    resultado= [(key, letras) for key, letras in resultado.items()]
    resultado=sorted(resultado, key=itemgetter(0), reverse=False)
    #print(resultado)
    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data= file.readlines()
   
    data= [row.split('\t') for row in data]
    data= [row.replace('\n', '') for row in data]
    data= [(int(row[1]), row[0]) for row in data]
    #print(data)
    resultado={}
    for valor, letras  in data:
        if valor in resultado.keys():
            resultado[valor].append(letras)
        else:
            resultado[valor]=[letras]
    #print(resultado)
    resultado= [(key, list(set(letras)))for key, letras in resultado.items()]
    resultado=sorted(resultado, key=itemgetter(0))
    #print(resultado)
    return resultado
   

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv', 'r') as file:
        data= file.readlines()

    data= [row.split('\t') for row in data]
    data=[(row[4].replace('\n','').split(',')) for row in data]
    lista2=[]
    for item in  data:
        lista2+=item
    col5=[]
    for str in range(0, len(lista2)):
        col5.append(lista2[str][:3])
    col5.sort()
    contador = dict((k, col5.count(k)) for k in col5)
    #print(contador)
    return contador


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', 'r') as file:
        data= file.readlines()
   
    data= [row.split('\t') for row in data]
    data= [(row[0],(row[3].split(',')),(row[4].replace('\n','').split(','))) for row in data]
    claves=[row[0] for row in data]
    valor1=[len(row[1]) for row in data]
    valor2=[len(row[2]) for row in data]
    #print(valor2)
    lista_final=list(zip(claves, valor1, valor2))
    #print(lista_final)
    return lista_final


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data= file.readlines()

    data= [row.split('\t') for row in data]
    data= [(row[3].split(','),row[1]) for row in data]
    
    listacol5=[]
    for x in range(0, len(data)):
        for y in range(0, len(data[x][0])):
            listacol5.append(list(data[x][0][y]+data[x][1]))
    
    resultado={}
    for letras, valor in listacol5:
        valor=int(valor)
        if letras in resultado.keys():
            resultado[letras].append(valor)
        else:
            resultado[letras]=[valor]
    resultado=[(key, sum(val))for key, val in resultado.items()]
    resultado=dict(sorted(resultado, key=itemgetter(0), reverse=False))
    #print(resultado)
    return resultado


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data= file.readlines()
    data= [row.split('\t') for row in data]
    letras= sorted(set([x[0] for x in data]))
    my_dict={}
    for x in letras:
        for y in data:
            if x==y[0] and x not in my_dict.keys():
                my_dict[x]=sum([int(i[4:])for i in y[4].split(',')])
            elif x==y[0]:
                my_dict[x]+=sum([int(i[4:]) for i in y[4].split(',')])
    #print(my_dict)
    return my_dict
