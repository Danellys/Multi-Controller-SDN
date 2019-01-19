import os
import glob
import time
import inspect
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))


#Función para lanzar el escenario VNX  h abriendo las consolas de los controladores
def lanzar(ControllerType, QuantityCtrl, ip_address):
    print (path)
    x = int(QuantityCtrl.get())
    os.system("sudo vnx -f escenario.xml -v --create")
    i4 = 1
    # Se crean unos archivos bash que permiten dejar en ejecución los controladores
    while i4 <= x:
        if ControllerType.get() == "ODL":
            with open("scriptODL" + str(i4) + ".sh", "w") as f2:
                f2.write("#!/bin/bash")
                f2.write("\n")
                f2.write('sudo lxc-attach -n ODL' + str(i4) + ' -e  sudo ./sdn/karaf-0.7.2/bin/karaf')
                f2.write("\n")
            os.system("gnome-terminal working-directory="+ path + " -- bash ./scriptODL" + str(i4) + ".sh")
            time.sleep(20)
            i4 += 1
        if ControllerType.get() == "ONOS":
            cluster = ''
            i2 = 1
            ip2= ip_address
            while i2 <= x:
                ip2 += 1
                cluster = cluster + str(ip2) + ' '  # Enlazando todas las direcciones IP del clúster
                i2 += 1
            with open("scriptONOS" + str(i4) + ".sh", "w") as f2:
                f2.write("#!/bin/bash")
                f2.write("\n")
                f2.write('sudo lxc-attach -n ONOS' + str(i4) + ' -e sudo ./opt/onos/apache-karaf-3.0.8/bin/karaf clean')
            os.system("gnome-terminal working-directory="+ path + " -- bash ./scriptONOS" + str(i4) + ".sh")
            if x != 1:
                if i4 == x:
                    time.sleep(60)
                    os.system("sudo lxc-attach -n ONOS1 -e sudo /opt/onos/bin/onos-form-cluster " + str(cluster))
            i4 += 1
#Función para detener el escenario, eliminar el archivo escenario.xml y los script creados
def detener():
    os.system("sudo vnx -f escenario.xml -v --P")
    os.remove("escenario.xml")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm -f TopologyEvents*")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm  -f Log*")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm  -f OFEvents.txt")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm  -f scriptO*.sh")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm  -f scriptEve*.sh")

#Función para mostrar la topología creada
def topologia():
    os.system("sudo vnx -f escenario.xml -v --show-map")
