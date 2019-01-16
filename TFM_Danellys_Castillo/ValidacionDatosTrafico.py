
from tkinter import messagebox
import ipaddress

def flowerror (QFlows):
    answer_flows = QFlows.get()
    try:
        flows = int(answer_flows)
        if flows ==0:
            messagebox.showerror("Error", "La cantidad de flujos debe ser diferente de cero")
    except ValueError:
        messagebox.showerror("Error", "La cantidad de flujos debe ser un número entero")
    return answer_flows


def fprerror (QFpr):
    answer_fpr = QFpr.get()
    try:
        fpr = int(answer_fpr)
        if fpr==0:
            messagebox.showerror("Error", "La cantidad de flujos por solicitud  debe ser mayor a cero")
    except ValueError:
        messagebox.showerror("Error", "La cantidad de flujos por solicitud  debe ser un número entero")
    return answer_fpr

def check_iptest(IP_Test):
    answer_ip=IP_Test.get()
    try:
        IP_Test = ipaddress.ip_address(answer_ip)
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar una dirección IPv4")
    return IP_Test