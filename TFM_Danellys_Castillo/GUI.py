#Importando paquetes necesarios
from tkinter import *
from tkinter import font
import CreacionXML
import ComandosVNX
import ManejoEscenario
import Pruebas
from tkinter import messagebox
import ipaddress
import time
import os

def GUI():
    root = Tk() #Creando ventana para interfaz gráfica
    root.title("Escenarios SDN de Múltiples Controladores")
    root.geometry("960x930")
    root.resizable(width=False, height=False)
    #Creando la tipografia
    Fuente = font.Font(family='Helvetica', size=11)
    Fuente2 = font.Font(family='Helvetica', size=12, weight='bold')
    #Creando banner superior
    image1 = PhotoImage(file="banner.png")

    #Creacion de Etiquetas, cuadros de textos y menú desplegables
    frame = Frame(root)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    #Colocando una imagen superior a la aplicación
    Label1 = Label(root, image=image1)
    Label1.grid(columnspan=7)

    #Creando una etiqueta y un menú desplegable para seleccionar la cantidad de controladores
    Label01= Label(root, text="Despliegue de Escenario", font=Fuente2)
    Label01.grid(row=1, column=2, pady=(25,5))
    Label2 = Label(root, text="Controladores:", font=Fuente)
    Label2.grid(row=2, column=0, pady=(20,10), padx=(20,0), sticky=E)
    QuantityCtrl = StringVar(root)
    QuantityCtrl.set("3") # Seleccionando un valor por defecto
    w1 = OptionMenu(root, QuantityCtrl, "1", "3", "4", "5", "6", "7", "8", "9", "10")
    w1.grid(row=2, column=1, pady=(20,10), sticky=W)

    #Creando una eqtiqueta y un cuadro texto para ingresar la cantidad d switches en la topología
    Label4 = Label(root, text="Conmutadores:", font=Fuente)
    Label4.grid(row=3, column=0, pady=(10,30), sticky=E)
    QSwitch = Entry(root, font=Fuente, width=5)
    QSwitch.grid(row=3, column=1, pady=(10,30), sticky=W)

    #Creando etiqueta y cuadro de texto para indicar la cantidad de host por cada switch
    Label5 = Label(root, text="Host por Conmutador:", font=Fuente)
    Label5.grid(row=3, column=2, pady=(10,30), sticky=E)
    QHost = Entry(root, font=Fuente, width=5)
    QHost.grid(row=3, column=3, pady=(10,30), padx=(1,1),sticky=W)
    Label5 = Label(root, text="Topología", font=Fuente)
    Label5.grid(row=3, column=4, pady=(10, 30),padx=(5,5),sticky=E)
    TopologyType = StringVar(root)
    TopologyType.set("Anillo")  # Seleccionando un valor por defecto
    w2 = OptionMenu(root, TopologyType, "Anillo", "Malla")
    w2.grid(row=3, column=5, pady=(10,30), sticky=W)

    #Creando Boton para crear/eliminar switches
    button1 = Button(root, text="Agregar Conmutadores OVS", font=Fuente, command=lambda: ManejoEscenario.addswitch(QSwitch,IP_Address,QuantityCtrl, TopologyType))
    button1.grid(row=6, column=1, pady=(10, 30), padx=(5, 5), sticky=W + E)
    button1 = Button(root, text="Eliminar Conmutadores OVS", font=Fuente,command=lambda: ManejoEscenario.deleteswitch(QSwitch, TopologyType))
    button1.grid(row=6, column=2, pady=(10, 30), padx=(5, 5), sticky=W + E)

    # Creando etiqueta y cuadro de texto para indicar la direccion IP inicial
    Label6 = Label(root, text="Dirección IP:", font=Fuente)
    Label6.grid(row=4, column=1, pady=(10, 30), sticky=E)
    IP_Address = Entry(root, font=Fuente, width=5)
    IP_Address.grid(row=4, column=2, pady=(10, 30), padx=(1, 1), sticky=W+E)

    #Creando eqtiquetas y cuadros de textos para los parámetros de pruebas de prestaciones
    Label7 = Label(root, text="Pruebas de Entornos", font=Fuente2)
    Label7.grid(row=7, columnspan=6, pady=(10,10), sticky=W+E)
    Label8 = Label(root, text="Agregar y Eliminar Flujos (Interfaz Norte a Sur):", font=Fuente)
    Label8.grid(row=8, columnspan=2, pady=(5,1), padx=(5,0), sticky=E)
    Label9 = Label(root, text="Flujos:", font=Fuente)
    Label9.grid(row=9, column=4, pady=(5,10), sticky=E)
    QFlows = Entry(root, font=Fuente, width=7)
    QFlows.grid(row=9, column=5, pady=(5,10), sticky=W)
    Label10 = Label(root, text="Flujos por Solicitud:", font=Fuente)
    Label10.grid(row=9, column=2, pady=(5,10), padx=(1,10), sticky=E)
    QFpr = Entry(root, font=Fuente, width=7)
    QFpr.grid(row=9, column=3, pady=(5,10), sticky=W)
    Label6 = Label(root, text="Dirección IP:", font=Fuente)
    Label6.grid(row=9, column=0, pady=(5, 5), sticky=E)
    IP_Test = Entry(root, font=Fuente, width=20)
    IP_Test.grid(row=9, column=1, pady=(1, 1), padx=(1, 5), sticky=W)
    Label10 = Label(root, text=" ", font=Fuente)
    Label10.grid(row=9, column=7, pady=(5, 10), padx=(1, 10), sticky=E)
    Label13 = Label(root, text="Tiempo Descubrimiento de Topología:", font=Fuente)
    Label13.grid(row=12, columnspan=2, pady=(10, 10), padx=(5, 5), sticky=W+E)
    Label14 = Label(root, text="Latencia al Agregar y Eliminar un Conmutador", font=Fuente)
    Label14.grid(row=14, columnspan=2, pady=(15, 10), padx=(5, 5), sticky=W + E)
    #Creando un menú desplegable para seleccionar el tipo de controlador
    Label11 = Label(root, text="Tipo de Controlador:", font=Fuente)
    Label11.grid(row=2, column=2, pady=(30,10), sticky=E)
    ControllerType = StringVar(root)
    ControllerType.set("ODL") #Valor por Defecto
    w3 = OptionMenu(root, ControllerType, "ODL", "ONOS")
    w3.grid(row=2, column=3, pady=(30,10), padx=(0,20), sticky=W)

    #Creación de botones, cada uno asociado a una de las funciones definidas anteriormente
    button1 = Button(root, text="Lanzar Escenario VNX", font=Fuente, command=lambda: ManejoEscenario.create(ControllerType, QuantityCtrl,QSwitch, QHost, IP_Address,TopologyType))
    button1.grid(row=5, column=1, pady=(10,30), padx=(5,5), sticky=W+E)
    button2 = Button(root, text="Detener Escenario VNX", font=Fuente, command=ManejoEscenario.detener)
    button2.grid(row=5, column=3, pady=(10,30), padx=(5,5), sticky=W+E)
    button3 = Button(root, text="Mostrar Topologia VNX", font=Fuente, command=ManejoEscenario.topologia)
    button3.grid(row=5, column=2, pady=(10,30), padx=(5,5), sticky=W+E)
    button4 = Button(root, text="Ejecutar", font=Fuente, command=lambda: Pruebas.PruebaDeFlujos(QFlows, QFpr,IP_Test, ControllerType))
    button4.grid(row=10, columnspan=6, pady=(1,5))
    button6 = Button(root, text="Capturar Paquetes", font=Fuente, command=lambda: Pruebas.CapturarPaquetes(IP_Address))
    button6.grid(row=13, column=1, pady=(1, 5), padx=(5,5))
    button5 = Button(root, text="Calcular Latencia (segundos):", font=Fuente, command=lambda: Pruebas.CalcularLatencia(QuantityCtrl, QSwitch, ControllerType))
    button5.grid(row=13, column=2, pady=(1, 5))
    button7 = Button(root, text="Agregar Conmutador", font=Fuente, command=lambda: Pruebas.PruebaDeAgregarConmutador(QuantityCtrl,ControllerType, IP_Address))
    button7.grid(row=15, column=1, pady=(1, 40))
    button8 = Button(root, text="Eliminar Conmutador", font=Fuente, command=lambda: Pruebas.PruebaDeEliminarConmutador(QuantityCtrl,ControllerType))
    button8.grid(row=15, column=2, pady=(1, 40))

    root.mainloop()