#Creando el clúster de controladores dependiendo del tipo seleccionado
import ODLController
import ONOSController
def create_cluster(ControllerType, ip_address,x):
    if ControllerType.get() == "ODL":
        ODLController.ODL_cluster(ip_address,x)
    if ControllerType.get() == "ONOS":
        ONOSController.ONOS_cluster(ip_address,x)