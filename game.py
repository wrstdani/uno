import random
import time


def chupate(a, b):
    if a.__contains__('CambioDeColor'):
        return False
    elif a.__contains__('+4'):
        return True
    numb, colb = map(str, b.strip().split())
    numa, cola = map(str, a.strip().split())
    if numb == '+4':
        if cola == colb and numa == '+2':
            return True
        else:
            return False
    elif numb == numa:
        return True
    else:
        return False


def sacar_carta(a):
    x = random.randint(0, len(a) - 1)
    b = a[x]
    return b


def chupar_cartas(a, b, c):
    for i in range(c):
        carta = sacar_carta(a)
        b.append(carta)
        a.remove(carta)
    return a, b


def repartir_cartas(a, b):
    for i in range(7):
        carta = sacar_carta(a)
        b.append(carta)
        a.remove(carta)
    return a, b


def juego(a, b, c, d, e, f, g, h, j):
    if g == 1:
        x = 1
        input('Turno del Jugador 1:')
        print(b)
        if h != 0:
            cartas_posibles = []
            print('Te han echado un chúpate devuelveselo si tienes otro:')
            for i in range(len(b)):
                if chupate(b[i], f):
                    print(str(x) + '.', b[i])
                    cartas_posibles.append(b[i])
                    x += 1
            if len(cartas_posibles) == 0:
                print('No tienes cartas para devolver el chupate. :(')
                a, b = chupar_cartas(a, b, h)
                h = 0
                time.sleep(3.5)
                return a, b, c, d, e, f, g, h, j
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                b.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('+4'):
                    h += 4
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                elif f.__contains__('+2'):
                    h += 2
                g += 1 * j
                return a, b, c, d, e, f, g, h, j
        print('Opciones:')
        print('1: Usar carta.')
        print('2: Robar y pasar turno.')
        eleccion = int(input().strip())
        while eleccion < 1 or eleccion > 2:
            eleccion = int(input('Número inválido, seleccione otro: ').strip())
        if eleccion == 1:
            cartas_posibles = []
            for i in range(len(b)):
                if comprobar_cartas(f, b[i]):
                    print(str(x) + '.', b[i])
                    cartas_posibles.append(b[i])
                    x += 1
            if len(cartas_posibles) < 1:
                eleccion = 2
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                b.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('🔄'):
                    j *= -1
                    if numero_de_jugadores == 2:
                        g += 2 * j
                    else:
                        g += 1 * j
                elif f.__contains__('🚫'):
                    g += 2 * j
                elif f.__contains__('CambioDeColor') or f.__contains__('+4'):
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                    g += 1 * j
                    if f.__contains__('+4'):
                        h += 4
                elif f.__contains__('+2'):
                    h += 2
                    g += 1 * j
                else:
                    g += 1 * j
                return a, b, c, d, e, f, g, h, j
        if eleccion == 2:
            carta_robada = sacar_carta(a)
            b.append(carta_robada)
            a.remove(carta_robada)
            g += 1 * j
            print('Nueva carta:' + carta_robada)
            time.sleep(2)
            return a, b, c, d, e, f, g, h, j
    elif g == 2:
        x = 1
        input('Turno del Jugador 2:')
        print(c)
        if h != 0:
            cartas_posibles = []
            print('Te han echado un chúpate devuelveselo si tienes otro:')
            for i in range(len(c)):
                if chupate(c[i], f):
                    print(str(x) + '.', c[i])
                    cartas_posibles.append(c[i])
                    x += 1
            if len(cartas_posibles) == 0:
                print('No tienes cartas para devolver el chupate. :(')
                a, c = chupar_cartas(a, c, h)
                h = 0
                time.sleep(3.5)
                return a, b, c, d, e, f, g, h, j
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                c.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('+4'):
                    h += 4
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                elif f.__contains__('+2'):
                    h += 2
                g += 1 * j
                return a, b, c, d, e, f, g, h, j
        print('Opciones:')
        print('1: Usar carta.')
        print('2: Robar y pasar turno.')
        eleccion = int(input().strip())
        while eleccion < 1 or eleccion > 2:
            eleccion = int(input('Número inválido, seleccione otro: ').strip())
        if eleccion == 1:
            cartas_posibles = []
            for i in range(len(c)):
                if comprobar_cartas(f, c[i]):
                    print(str(x) + '.', c[i])
                    cartas_posibles.append(c[i])
                    x += 1
            if len(cartas_posibles) < 1:
                eleccion = 2
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                c.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('🔄'):
                    j *= -1
                    if numero_de_jugadores == 2:
                        g += 2 * j
                    else:
                        g += 1 * j
                elif f.__contains__('🚫'):
                    g += 2 * j
                elif f.__contains__('CambioDeColor') or f.__contains__('+4'):
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                    g += 1 * j
                    if f.__contains__('+4'):
                        h += 4
                elif f.__contains__('+2'):
                    h += 2
                    g += 1 * j
                else:
                    g += 1 * j
                return a, b, c, d, e, f, g, h, j
        if eleccion == 2:
            carta_robada = sacar_carta(a)
            c.append(carta_robada)
            a.remove(carta_robada)
            g += 1 * j
            print('Nueva carta:' + carta_robada)
            time.sleep(2)
            return a, b, c, d, e, f, g, h, j
    elif g == 3:
        x = 1
        input('Turno del Jugador 3:')
        print(d)
        if h != 0:
            cartas_posibles = []
            print('Te han echado un chúpate devuelveselo si tienes otro:')
            for i in range(len(d)):
                if chupate(d[i], f):
                    print(str(x) + '.', d[i])
                    cartas_posibles.append(d[i])
                    x += 1
            if len(cartas_posibles) == 0:
                print('No tienes cartas para devolver el chupate. :(')
                a, d = chupar_cartas(a, d, h)
                h = 0
                time.sleep(3.5)
                return a, b, c, d, e, f, g, h, j
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                d.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('+4'):
                    h += 4
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                elif f.__contains__('+2'):
                    h += 2
                g += 1 * j
                return a, b, c, d, e, f, g, h, j
        print('Opciones:')
        print('1: Usar carta.')
        print('2: Robar y pasar turno.')
        eleccion = int(input().strip())
        while eleccion < 1 or eleccion > 2:
            eleccion = int(input('Número inválido, seleccione otro: ').strip())
        if eleccion == 1:
            cartas_posibles = []
            for i in range(len(d)):
                if comprobar_cartas(f, d[i]):
                    print(str(x) + '.', d[i])
                    cartas_posibles.append(d[i])
                    x += 1
            if len(cartas_posibles) < 1:
                eleccion = 2
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                d.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('🔄'):
                    j *= -1
                    g += 1 * j
                elif f.__contains__('🚫'):
                    g += 2 * j
                elif f.__contains__('CambioDeColor') or f.__contains__('+4'):
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                    g += 1 * j
                    if f.__contains__('+4'):
                        h += 4
                elif f.__contains__('+2'):
                    h += 2
                    g += 1 * j
                else:
                    g += 1 * j
                return a, b, c, d, e, f, g, h, j
        if eleccion == 2:
            carta_robada = sacar_carta(a)
            d.append(carta_robada)
            a.remove(carta_robada)
            g += 1 * j
            print('Nueva carta:' + carta_robada)
            time.sleep(2)
            return a, b, c, d, e, f, g, h, j
    elif g == 4:
        x = 1
        input('Turno del Jugador 4:')
        print(e)
        if h != 0:
            cartas_posibles = []
            print('Te han echado un chúpate devuelveselo si tienes otro:')
            for i in range(len(e)):
                if chupate(e[i], f):
                    print(str(x) + '.', e[i])
                    cartas_posibles.append(e[i])
                    x += 1
            if len(cartas_posibles) == 0:
                print('No tienes cartas para devolver el chupate. :(')
                a, e = chupar_cartas(a, e, h)
                h = 0
                time.sleep(3.5)
                return a, b, c, d, e, f, g, h, j
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                e.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('+4'):
                    h += 4
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                elif f.__contains__('+2'):
                    h += 2
                g += 1 * j
                return a, b, c, d, e, f, g, h, j
        print('Opciones:')
        print('1: Usar carta.')
        print('2: Robar y pasar turno.')
        eleccion = int(input().strip())
        while eleccion < 1 or eleccion > 2:
            eleccion = int(input('Número inválido, seleccione otro: ').strip())
        if eleccion == 1:
            cartas_posibles = []
            for i in range(len(e)):
                if comprobar_cartas(f, e[i]):
                    print(str(x) + '.', e[i])
                    cartas_posibles.append(e[i])
                    x += 1
            if len(cartas_posibles) < 1:
                eleccion = 2
            else:
                carta_elegida = int(input().strip())
                while carta_elegida < 1 or carta_elegida > len(cartas_posibles):
                    carta_elegida = int(input('Número inválido, seleccione otro: ').strip())
                f = cartas_posibles[carta_elegida - 1]
                a.append((cartas_posibles[carta_elegida - 1]))
                e.remove(cartas_posibles[carta_elegida - 1])
                if f.__contains__('🔄'):
                    j *= -1
                    g += 1 * j
                elif f.__contains__('🚫'):
                    g += 2 * j
                elif f.__contains__('CambioDeColor') or f.__contains__('+4'):
                    print('1: 🔵')
                    print('2: 🔴')
                    print('3: 🟢')
                    print('4: 🟡')
                    color = int(input('Elige el color al que desea cambiar:'))
                    while color < 1 or color > 4:
                        color = int(input('Número inválido, seleccione otro: ').strip())
                    if color == 1:
                        f = f + ' 🔵'
                    elif color == 2:
                        f = f + ' 🔴'
                    elif color == 3:
                        f = f + ' 🟢'
                    elif color == 4:
                        f = f + ' 🟡'
                    g += 1 * j
                    if f.__contains__('+4'):
                        h += 4
                elif f.__contains__('+2'):
                    h += 2
                    g += 1 * j
                else:
                    g += 1 * j
                return a, b, c, d, e, f, g, h, j
        if eleccion == 2:
            carta_robada = sacar_carta(a)
            e.append(carta_robada)
            a.remove(carta_robada)
            g += 1 * j
            print('Nueva carta:' + carta_robada)
            time.sleep(2)
            return a, b, c, d, e, f, g, h, j


def comprobar_cartas(a, b):
    if b.__contains__('+4') or b.__contains__('CambioDeColor'):
        return True
    else:
        numb, colb = map(str, b.strip().split(' '))
        numa, cola = map(str, a.strip().split(' '))
        if numa == numb or cola == colb:
            return True
        else:
            return False


def comprobar_turno(a, b):
    if a > b:
        a -= b
    elif a < 1:
        a += b
    return a, b


mazo_de_cartas = ['0 🔵', '1 🔵', '2 🔵', '3 🔵', '4 🔵', '5 🔵', '6 🔵', '7 🔵', '8 🔵', '9 🔵', '🔄 🔵', '🚫 🔵',
                  '+2 🔵', '1 🔵', '2 🔵', '3 🔵', '4 🔵', '5 🔵', '6 🔵', '7 🔵', '8 🔵', '9 🔵', '🔄 🔵', '🚫 🔵',
                  '+2 🔵',
                  '0 🔴', '1 🔴', '2 🔴', '3 🔴', '4 🔴', '5 🔴', '6 🔴', '7 🔴', '8 🔴', '9 🔴', '🔄 🔴', '🚫 🔴',
                  '+2 🔴', '1 🔴', '2 🔴', '3 🔴', '4 🔴', '5 🔴', '6 🔴', '7 🔴', '8 🔴', '9 🔴', '🔄 🔴', '🚫 🔴',
                  '+2 🔴',
                  '0 🟢', '1 🟢', '2 🟢', '3 🟢', '4 🟢', '5 🟢', '6 🟢', '7 🟢', '8 🟢', '9 🟢', '🔄 🟢', '🚫 🟢',
                  '+2 🟢', '1 🟢', '2 🟢', '3 🟢', '4 🟢', '5 🟢', '6 🟢', '7 🟢', '8 🟢', '9 🟢', '🔄 🟢', '🚫 🟢',
                  '+2 🟢',
                  '0 🟡', '1 🟡', '2 🟡', '3 🟡', '4 🟡', '5 🟡', '6 🟡', '7 🟡', '8 🟡', '9 🟡', '🔄 🟡', '🚫 🟡',
                  '+2 🟡', '1 🟡', '2 🟡', '3 🟡', '4 🟡', '5 🟡', '6 🟡', '7 🟡', '8 🟡', '9 🟡', '🔄 🟡', '🚫 🟡',
                  '+2 🟡',
                  'CambioDeColor', 'CambioDeColor', 'CambioDeColor', 'CambioDeColor', '+4', '+4', '+4', '+4']
mazo_de_cartas_copia = mazo_de_cartas
carta_principal = sacar_carta(mazo_de_cartas)
while carta_principal.__contains__('🔄') or carta_principal.__contains__('🚫') or \
        carta_principal.__contains__('CambioDeColor') or carta_principal.__contains__('+4') \
        or carta_principal.__contains__('+2'):
    mazo_de_cartas.append(carta_principal)
    carta_principal = sacar_carta(mazo_de_cartas)
cartas_j1 = []
cartas_j2 = []
cartas_j3 = []
cartas_j4 = []
repartir_cartas(mazo_de_cartas, cartas_j1)
repartir_cartas(mazo_de_cartas, cartas_j2)
repartir_cartas(mazo_de_cartas, cartas_j3)
repartir_cartas(mazo_de_cartas, cartas_j4)
turno = 1
ataque = 0
sentido = 1
numero_de_jugadores = int(input('Introduzca el número de jugadores (2-4): '))
while numero_de_jugadores < 2 or numero_de_jugadores > 4:
    numero_de_jugadores = int(input('Número de jugadores inválido, introduzca el número de jugadores (2-4): '))
print('\n' * 19)
while len(cartas_j1) != 0 and len(cartas_j2) != 0 and len(cartas_j3) != 0 and len(cartas_j4) != 0:
    print(carta_principal)
    if len(mazo_de_cartas) < 32:
        mazo_de_cartas = mazo_de_cartas_copia
    turno, numero_de_jugadores = comprobar_turno(turno, numero_de_jugadores)
    mazo_de_cartas, cartas_j1, cartas_j2, cartas_j3, cartas_j4, carta_principal, turno, ataque, sentido = \
        juego(mazo_de_cartas, cartas_j1, cartas_j2, cartas_j3, cartas_j4, carta_principal, turno, ataque, sentido)
    print('\n' * 50)
if len(cartas_j1) == 0:
    print('Felicidades Jugador 1.')
elif len(cartas_j2) == 0:
    print('Felicidades Jugador 2.')
elif len(cartas_j3) == 0:
    print('Felicidades Jugador 3.')
elif len(cartas_j4) == 0:
    print('Felicidades Jugador 4.')
