from os import system
import random
import csv
listadopedidos=[]
Ruta=["Concepcion", "Chiguayante", "Talcahuano", "Hualpen", "San Pedro"]
def Registrar_pedido():
    while True:
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        if nombre.isalpha() and len(nombre)>=3 and apellido.isalpha() and len(apellido)>=3:
            break
        else:
            print("Ingrese un nombre y apellido valido(mayores o igual a 3 y sin espacios)")
    
    while True: 
        print("Comunas Habilitadas.\nConcepcion, Chiguayante, Talcahuano, Hualpen, San Pedro.")
        
        comuna=input("Comuna: ")
        comuna=comuna.title()#Estoy funciona para cambiar el como se escribe una palabra ej: LOTA = Lota
        if comuna.isalpha and comuna in Ruta:
            break
        else:
            print("Ingrese bien los datos de la comuna e ingrese una comuna que tenga disponibilidad.")
    
    while True:
        direccion=input("Direccion: ")
        Numdireccion=input("Numero De Direccion: ")
        if direccion.isalpha() and Numdireccion.isnumeric():
            break
        else:
            print("Ingrese direccion y su numero por separado, sin espacios y validos.")
    
    while True:
        disp6=input("Disp.6: ")
        disp10=input("Disp.10: ")
        disp20=input("Disp.20: ")
        if disp6.isnumeric() and disp10.isnumeric() and disp20.isnumeric():
            disp6=int(disp6) 
            disp10=int(disp10)
            disp20=int(disp20)
            total=disp20+disp10+disp6
            if total!=0:
                break
            else:
                print("Ingrese los datos nuevamente, no puede ser 0")
                continue
        else:
            print("Ingrese valores numericos y la suma de los 3 no debe ser 0")

    Pedido={"ID": random.randint(1000,1900),
            "Cliente": nombre+ f" {apellido}",
            "Direccion": direccion+ f" {Numdireccion}",
            "Sector": comuna,
            "Disp.6lts": disp6,
            "Disp.10lts": disp10,
            "Disp.20lts": disp20,
            }      
    listadopedidos.append(Pedido)
    print("Pedido Registrado")
    input("Presione alguna tecla para continuar...")  

def Listar_pedidos():
    if not listadopedidos:
        print("No Hay lista existente..")
        input("Presione cualquier tecla para continuar...")
        return
    for pedidos in listadopedidos:
        print("ID\tCliente\t\t  Direccion\t\tSector\t\tDisp.6lts\t\tDisp.10lts\tDisp.20lts")
        print(f"{pedidos["ID"]}\t{pedidos["Cliente"]}\t{pedidos["Direccion"]}\t\t{pedidos["Sector"]}\t\t{pedidos["Disp.6lts"]}\t\t{pedidos["Disp.10lts"]}\t\t{pedidos["Disp.20lts"]}")
        print()
    input("Presione cualquier tecla para continuar...")    

def Imprimir_Ruta():
    if not listadopedidos:
        print("Imposible imprimir ya que la lista se encuentra vacia.")
        input("Presione cualquier tecla para continuar..")
        return
    while True:
        comuna=input("Ingrese comuna a imprimir: ")
        comuna=comuna.title()
        if comuna.isalpha() and comuna in Ruta:
            
            break
        else:
            print("Ingrese un valor valido y comuna habilitada(Concepcion, Chiguayante, Talcahuano, Hualpen, San Pedro")
    while comuna in Ruta:
        with open("Ruta.csv", mode="w", newline="")as archivo:
            escritura=csv.writer(archivo)
            escritura.writerow(["ID", "Cliente", "Direccion", "Sector", "Disp.6lts", "Disp.10lts", "Disp.20lts"])
            for pedido in listadopedidos:
                if pedido["Sector"]==comuna:
                    escritura.writerow([pedido["ID"], pedido["Cliente"], pedido["Direccion"], pedido["Sector"], pedido["Disp.6lts"], pedido["Disp.10lts"], pedido["Disp.20lts"]])
                    print("Hoja de ruta Imprimida")
                    print()       
                    input("Ingrese Cualquier tecla para continuar...")
                    return
    while comuna not in Ruta:
        print("Comuna no esta en nuestros registros de disponibilidad.")
        input("Ingrse cualquier tecla para continuar..")
        return


def Buscar_Pedido_ID():
    if not listadopedidos:
        print("Lista se Encuentra Vacias")
        input("Ingrese cualquier tecla para continuar")
        return
    while True:
        id=input("Ingresa ID para buscar el pedido==> ")
        if id.isnumeric():
            id=int(id)
            break
        else:
            print("Ingresa valores validos.")
    for pedido in listadopedidos:
        if pedido["ID"]==id:
            print(pedido)
            print()  
            
        else:
            print("Pedido no encontrado")
    input("Ingresa cualquiera tecla para continuar...")
        


def menu():
    while True:
        try:
            system("cls")
            print("Agua Purificada 'CleanWasser'")
            op=int(input("1.Registrar Pedidos\n2.Listar Pedidos\n3.Imprimir Hoja de Ruta\n4.Buscar Pedido Por ID\n5.Salir Del Programa\n"))
        except ValueError:
            print("Error en el ingreso, intentelo nuevamente.")
        if op==1:
            Registrar_pedido()
        elif op==2:
            Listar_pedidos()
        elif op==3:
            Imprimir_Ruta()
        elif op==4:
            Buscar_Pedido_ID()
        elif op==5:
            print("Saliendo del programa")
            break
        else:
            ("Intente nuevamente con digitos de 1 - 5")
menu()

