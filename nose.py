# -*- coding: utf-8 -*-

# Autor: Brando Pérez Pacheco.
# Matrícula: 120300158.
# Instrucciones:
    # 1.- Examinar el siguiente elemento de la linea de entrada.
    # 2.- Extraer como salida si se trata de un operando.
    # 3.- Si es una apertura de parentesis se introduce a la pila.
    # 4.- Si es un operador entonces:
    #   4.1.- Si la cabecera de la pila contiene una apertura de parentesis, apilar el operador.
    #   4.2.- Si tiene una prioridad más alta que el de la cabecer de la pila, apilar el operador.
    #   4.3.- Si tiene una prioridad menor o igual, efectuar un pop de la fila a la salida y repetir el paso 4.
    # 5.- Si es un paréntesis de cierre, desapilar operadores acia la salida hasta que se encuentre un parentesis de apertura. Desapilar y descartar el paréntesis de de apertura.
    # 6.- Si hay mas entradas ir al paso 1.
    # 7.- Si no hay más elementos de entrada desapilar los restantes operadores.

ins = 'A+B*C+(D+E)*F'
pila = []
salida = ''
op = {'+': 0, '-': 0, '*': 1, '/': 1} # operadores y sus valores

print "Entrada: " + ins

for i in ins:
    # si es operando
    if i not in op.keys() and i != '(' and i != ')': salida += i
    # si es un paréntesis de apertura
    elif i == '(': pila.append(i)
    # si es un operador
    elif i in op.keys():
        while True:
            if '(' in pila: pila.append(i); break
            elif len(pila) == 0 or op[i] > op[pila[0]]: pila.append(i); break
            else: salida += pila.pop()
    # si es un paréntesis de cerradura
    elif i == ')':
        for i in pila:
            if i != '(': salida += pila.pop()
        pila.pop()

for i in range(len(pila)):
    salida += pila.pop()

print "Salida: " + salida
