#Importando paquetes necesarios
import Errores
import SwitchXML
import HostXML
import Controller
import SubnetXML
import ComandosVNX
def editxml(ControllerType, QuantityCtrl, switch, host, ip_address,TopologyType):
    #Se crea una variable x que tendrá el valor de la cantidad de controladores definidas por el usuario
    x = int(QuantityCtrl.get())
    #Se verifica que las variables switch y host sean números enteros
    print(switch)
    print(host)
    # Se abre el archivo scriptescenario.xml y se agrega su contenido al archivo escenario.xml
    with open("scriptescenario.xml") as f:
        lines = f.readlines()
        with open("escenario.xml", "w") as f1:
            f1.writelines(lines)
    if (switch >0):
        controllers=SwitchXML.create_switch(switch, ip_address,x,TopologyType)
        if host > 0:
            HostXML.create_host(switch, host)
    Controller.create_cluster(ControllerType, ip_address, x)
    SubnetXML.create_subnet(ip_address)


