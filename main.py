from cliente import Cliente

#Crear obejto
cliente = Cliente()

#cliente.registro_usuario()
cliente.iniciar_sesion()

print("Por favor seleccione una opcion...")
print("1 - INGRESAR DINERO")
print("2 - RETIRAR DINERO")
print("3 - MOSTRAR DINERO")
opcion = int(input(""))

if opcion == 1:
    cliente.ingresar_dinero()
elif opcion == 2:
    pass
elif opcion == 3:
    pass
else:
    print("Opcion incorrecta")
