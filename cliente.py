from conexion import conectar
from time import sleep
import os
from datetime import datetime


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

    def iniciar_sesion(self):
        print("\n********** Banco Cripto $$$ $$$ $$$ **********")
        sql = "select * from usuarios_banco where rut = %s"
        usuario = input("Ingrese el rut para iniciar sesion de usuario: ")
        self.rut = usuario
        values=(usuario,)
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
            print(self.rut)
            return self.rut
            
        else:
            print("No encontrado")
            busqueda = cursor.rowcount
            #return busqueda
    
    def ingresar_dinero(self):
        print("Fecha: {0}".format(self.fecha))
        print("********** Banco Cripto $$$ $$$ $$$ **********")
        print("")
        if self.busqueda == 1:
            print("Usuario encontrado:")
            dinero = float(input("Ingrese el monto: $"))

            if dinero >0:
                print("El usuario {0} a ingresado un monto de {1} con exito!".format(self.usuario_session,dinero))
                sleep(1)
                self.monto_total = dinero + self.monto_total
        else:
            print("Usuario no encontrado!")


        return self.monto_total


"""
#************** Insertar registros ***************
def insertar():
    sql = "insert into Usuario (email,username,edad) values (%s,%s,%s)"

    print("\n********Registro Usuario**********")
    email = input('Ingrese su email: ')
    username = input('Ingree su username: ')
    age =  int(input('Ingrese su edad: '))
    values =(email,username,age)

    cursor.execute(sql,values)

    database.commit()
    #print(cursor.rowcount)
    if cursor.rowcount == 1:
        print("Registro ingresado exitosamente")
    else:
        print("Ocurrio un error al ingresar")
"""


#******************************************************************

#Crear obejto
cliente = Cliente()

cliente.iniciar_sesion()

cliente.ingresar_dinero()







