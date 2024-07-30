import random
from datetime import datetime

class Usuarios:
    def __init__(self, nombre, apellido, fecha_nacimiento, sexo, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.cedula = cedula

usuarios = {}

def calc_edad(fecha_nacimiento):
    hoy = datetime.now()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def crear_usuario():
    print('Escribe los datos para agregar el nuevo usuario')
    
    nombre_usuario = input('Nombre:\r\n')
    apellido_usuario = input('Apellido:\r\n')

    while True:
        fecha_nacimiento = input('Fecha de nacimiento (DD-MM-YYYY):\r\n')
        try:
            fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
            if calc_edad(fecha_nacimiento) >= 18:
                break
            else:
                print('El usuario debe ser mayor de 18 años.')
        except ValueError:
            print('Fecha de nacimiento inválida. Use el formato DD-MM-YYYY.')

    while True:
        sexo_usuario = input('Sexo (M/F):\r\n').upper()
        if sexo_usuario in ('M', 'F'):
            break
        else:
            print('Sexo inválido. Use M o F.')

    while True:
        cedula_usuario = input('Cédula:\r\n')
        if cedula_usuario.isdigit() and len(cedula_usuario) == 10:
            break
        else:
            print('La cédula debe tener 10 dígitos numéricos.')

    if cedula_usuario not in usuarios:
        usuario = Usuarios(nombre_usuario, apellido_usuario, fecha_nacimiento, sexo_usuario, cedula_usuario)
        usuarios[cedula_usuario] = usuario
        print('\r\n Usuario creado correctamente \r\n')
    else:
        print('Ese usuario ya existe.')

def mostrar_contactos():
    for cedula, usuario in usuarios.items():
        print(f'Nombre: {usuario.nombre}')
        print(f'Apellido: {usuario.apellido}')
        print(f'Fecha de nacimiento: {usuario.fecha_nacimiento}')
        print(f'Sexo: {usuario.sexo}')
        print(f'Cédula: {usuario.cedula}')
        print('\r\n')

def buscar_usuario():
    print('Escribe el número de cédula del usuario a buscar:')
    cedula = input('Cédula del usuario:\r\n')

    if cedula in usuarios:
        usuario = usuarios[cedula]
        print(f'Nombre: {usuario.nombre}')
        print(f'Apellido: {usuario.apellido}')
        print(f'Fecha de nacimiento: {usuario.fecha_nacimiento}')
        print(f'Sexo: {usuario.sexo}')
        print(f'Cédula: {usuario.cedula}')
        print('\r\n')
    else:
        print('Ese usuario no existe.')

def editar_usuario():
    print('Escribe el número de cédula del usuario a editar:')
    cedula_anterior = input('Cédula del usuario que desea editar:\r\n')

    if cedula_anterior in usuarios:
        nombre_usuario = input('Agrega nuevo nombre de usuario:\r\n')
        apellido_usuario = input('Agrega nuevo apellido:\r\n')

        while True:
            fecha_nacimiento = input('Agrega nueva fecha de nacimiento (DD-MM-YYYY):\r\n')
            try:
                fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
                if calc_edad(fecha_nacimiento) >= 18:
                    break
                else:
                    print('El usuario debe ser mayor de 18 años.')
            except ValueError:
                print('Fecha de nacimiento inválida. Use el formato DD-MM-YYYY.')

        while True:
            sexo_usuario = input('Cambio del sexo del usuario (M/F):\r\n').upper()
            if sexo_usuario in ('M', 'F'):
                break
            else:
                print('Sexo inválido. Use M o F.')

        while True:
            cedula_usuario = input('Agrega nuevo número de cédula del usuario:\r\n')
            if cedula_usuario.isdigit() and len(cedula_usuario) == 10:
                break
            else:
                print('La cédula debe tener 10 dígitos numéricos.')

        usuario = Usuarios(nombre_usuario, apellido_usuario, fecha_nacimiento, sexo_usuario, cedula_usuario)
        del usuarios[cedula_anterior]
        usuarios[cedula_usuario] = usuario
        print('\r\n Usuario editado correctamente \r\n')
    else:
        print('Ese usuario no existe.')

def eliminar_usuario():
    print('Escribe el número de cédula del usuario a eliminar:')
    cedula = input('Cédula del usuario:\r\n')

    if cedula in usuarios:
        del usuarios[cedula]
        print('\r\n Usuario eliminado correctamente \r\n')
    else:
        print('Ese usuario no existe.')

def unir_parejas():
    hombres = [usuario for usuario in usuarios.values() if usuario.sexo == 'M']
    mujeres = [usuario for usuario in usuarios.values() if usuario.sexo == 'F']

    random.shuffle(hombres)
    random.shuffle(mujeres)

    parejas = []
    while hombres and mujeres:
        pareja = (hombres.pop(), mujeres.pop())
        parejas.append(pareja)

    print('Parejas formadas:')
    for h, m in parejas:
        print(f'Hombre: {h.nombre}, Mujer: {m.nombre}')

    if hombres or mujeres:
        print('\nUsuarios sin pareja:')
        for h in hombres:
            print(f'Hombre: {h.nombre}')
        for m in mujeres:
            print(f'Mujer: {m.nombre}')

def app():
    while True:
        mostrar_menu()
        try:
            opcion = int(input('Seleccione una opción: \r\n'))
            if opcion == 1:
                crear_usuario()
            elif opcion == 2:
                editar_usuario()
            elif opcion == 3:
                buscar_usuario()
            elif opcion == 4:
                eliminar_usuario()
            elif opcion == 5:
                unir_parejas()
            elif opcion == 6:
                print('Salir')
                break
            else:
                print('Opción no válida, intente de nuevo')
        except ValueError:
            print('Por favor, ingrese un número válido.')

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer:')
    print('1) Agregar Nuevo Usuario')
    print('2) Editar Usuario')
    print('3) Buscar Usuario')
    print('4) Eliminar Usuario')
    print('5) Unir Parejas')
    print('6) Salir de la APP')

app()