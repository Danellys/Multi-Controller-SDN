#Función para  ejecutar pruebas de flujos
import inspect
import os
def prueba(flows,fpr, IP_test, ControllerType):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    if (ControllerType.get()=="ONOS"):
        os.system("gnome-terminal --working-directory=" + path +" -- python clustering-performance-test/onos_tester.py --host=" + str(IP_test) + " --flows "+ str(flows) +" --fpr=" +str(fpr) + " --bulk-delete")
    if (ControllerType.get()=="ODL"):
        os.system("gnome-terminal --working-directory=" + path +" -- python clustering-performance-test/odl_tester.py --host="+str(IP_test)+" --flows "+ str(flows)+ " --fpr=" +str(fpr)+" --bulk-delete")