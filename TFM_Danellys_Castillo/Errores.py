#Verificación de Datos de Entrada
from tkinter import messagebox
import ipaddress
def switcherror(QSwitch):
    #Se crea una variable switch que contiene la cantidad de switches definidos por el usuario
    answer_switch = QSwitch.get()
    #Se verifica previamente que sea un entero, de lo contrario, enviará un mensaje de error
    try:
        switch = int(answer_switch)
    except ValueError:
        messagebox.showerror("Error", "La cantidad de Switch debe ser un número entero")
    return switch

def hosterror(QHost) :
    # Se crea una variable switch que contiene la cantidad de host definidos por el usuario
    # Se verifica previamente que sea un entero, de lo contrario,enviará un mensaje de error
    answer_host = QHost.get()
    try:
        host = int(answer_host)
    except ValueError:
        messagebox.showerror("Error", "La cantidad de Host debe ser un número entero")
    return host
def check_ip(IPAddress):
    answer_ip=IPAddress.get()
    try:
        ip_address = ipaddress.ip_address(answer_ip)
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar una dirección IPv4")
    return ip_address