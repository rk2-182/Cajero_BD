from conexion import conectar
from time import sleep
import os
from datetime import datetime
import hashlib
import pyfiglet
titulo = pyfiglet.figlet_format(" BANCO CRIPTO ")

conexion = conectar()

bd = conexion[0]
cursor = conexion[1]

class Cliente:

    #Constructor
    def __init__(self):
        self.nombre = ""
        self.rut = ""
        self.monto_total = 0
        self.busqueda = 0
        self.fecha = datetime.today().strftime('%Y-%m-%d %H:%M')

    #====================Metodos===============================
    def registro_usuario(self):
        sql = "insert into usuarios_banco (monto_total,rut,nombre,clave)values (%s,%s,%s,%s);"
        print("\n********Registro Usuario**********")
        monto = self.monto_total
        rut = input('Ingrese su rut: ')
        nombre = input('Ingree su nombre: : ')
        clave =  input('Ingrese su clave: ')

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(clave.encode('utf-8'))

        values =(monto,rut,nombre,cifrado.hexdigest())

        try:
            
            cursor.execute(sql,values)
            bd.commit()
            if cursor.rowcount == 1:
                print("Registro ingresado exitosamente")
        except:
            print("Ocurrio un error a registrar, posiblemente el usuario ya existe.")

    def iniciar_sesion(self):
        print(titulo)

        sql = "select * from usuarios_banco where rut = %s and clave =%s" #consulta sql para buscar usuario

        usuario = input("Ingrese el rut para iniciar sesion de usuario: ")
        clave = input("Ingrese su clave  para iniciar sesion de usuario: ")

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(clave.encode('utf-8'))

        self.rut = usuario #tomar registro
        values=(usuario,cifrado.hexdigest())
        #resultado = usuario in self.usuarios

        cursor.execute(sql,values)
        registro = cursor.fetchone()

         #Validar si encuentra el registro
        if registro != None:
            print("\nUsuario encontrado:")
            #print(registro)
            busqueda = cursor.rowcount
            self.busqueda = busqueda
            #return busqueda
            #print(self.rut)
            return self.rut
            
        else:
            print(registro)
            print("No encontrado")
            busqueda = cursor.rowcount
            #return busqueda
    
    def ingresar_dinero(self):
        print("Fecha: {0}".format(self.fecha))
        print("********** Banco Cripto $$$ $$$ $$$ **********")
        print("")
        
        sql = "update usuarios_banco set monto_total = monto_total + %s where rut=%s;"

        rut = self.rut #asignar rut de la session 
        print(self.rut)
        dinero = float(input("Ingrese el monto: "))
        values = (dinero,rut)

        if dinero > 0:
            print("El usuario {0} a ingresado un monto de {1} con exito!".format(rut,dinero))
            sleep(1)
            self.monto_total = dinero + self.monto_total
            cursor.execute(sql,values)
            bd.commit()
            #Comprobar exito de la operacion
            if cursor.rowcount == 1:
                print("Registro ingresado exitosamente")
            else:
                print("Ocurrio un error al ingresar")
        else:
            print("No puede ingresar un monto igual a o menor a 0")

        return self.monto_total



#******************************************************************








