import Errores
import VNX
import ComandosVNX
import AgregarEliminarConmutador
import os
def create (ControllerType, QuantityCtrl,QSwitch, QHost, IP_Address, TopologyType):
    #Verificación de errores
    switch = Errores.switcherror(QSwitch)
    host = Errores.hosterror(QHost)
    ip_address = Errores.check_ip(IP_Address)
    controllers=VNX.editxml(ControllerType, QuantityCtrl, switch, host, ip_address,TopologyType)
    ComandosVNX.lanzar(ControllerType, QuantityCtrl, ip_address)
def AgregarConmutador(QSwitch,IP_Address,QuantityCtrl, TopologyType):
    x = int(QuantityCtrl.get())
    switch = Errores.switcherror(QSwitch)
    ipcontrollers= Errores.check_ip(IP_Address)
    i = 1
    icontrollers = 1
    controllers = ''
    while i <= switch:
        switchrange = list(range(1, switch + 1))
        switchrange.remove(i)
        while icontrollers < x:
            ipcontrollers += 1
            controllers = controllers + 'tcp:' + str(ipcontrollers) + ':6653 '
            icontrollers += 1
        if icontrollers == x:
            ipcontrollers += 1
            controllers = controllers + 'tcp:' + str(ipcontrollers) + ':6653'
            icontrollers += 1
        i += 1
    AgregarEliminarConmutador.Agregar(switch, controllers, TopologyType)

def EliminarConmutador(QSwitch, TopologyType):
    switch = Errores.switcherror(QSwitch)
    AgregarEliminarConmutador.Eliminar(switch,TopologyType)
def topologia():
    ComandosVNX.topologia()
def detener():
    ComandosVNX.detener()
