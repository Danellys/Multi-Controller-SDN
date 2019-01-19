#Prueba de agregar conmutador
import os
import datetime
from datetime import timedelta
import inspect
import GUI
import Errores
import time
def prueba(QuantityCtrl,ControllerType, IP_Address):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    ipgateway = Errores.check_ip(IP_Address)
    IP1=ipgateway+1
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm  -f OFEvents.txt")
    #Abriendo tshark para capturar paquetes
    with open('tshark.sh', 'w') as f:
        f.write("#!/bin/bash")
        f.write("\n")
        f.write("sudo tshark -i any  -Y 'ip.src==" + str(ipgateway) + " && tcp.flags.syn==1 && tcp.flags.ack==0' -e frame.time -Tfields  -l > OFEvents.txt")
        f.write("\n")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo bash ./tshark.sh")
    time.sleep(10)
    os.system("sudo ovs-vsctl add-br NetTest")
    os.system("sudo ovs-vsctl set bridge NetTest protocols=OpenFlow13")
    os.system("sudo ovs-vsctl set-controller NetTest tcp:" + str(IP1)+":6653")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm -f Topology.Events*")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm  -f Log*")
    x = int(QuantityCtrl.get())
    time.sleep(5)
    alldates = list()
    #Capturando los logs dependiendo del tipo de controlador
    if (ControllerType.get() == "ONOS"):
        i = 1
        while (i <= x):
            with open('scriptEvents' + str(i) + '.sh', "w") as f:
                f.write("#!/bin/bash")
                f.write("\n")
                f.write('sudo lxc-attach -n ONOS' + str(i) + ' -e sudo cat /opt/onos/apache-karaf-3.0.8/data/log/karaf.log >>Log' + str(i) + '.txt')
            os.system("gnome-terminal --working-directory=" + path + " -- bash ./scriptEvents" + str(i) + ".sh")
            os.system("gnome-terminal --working-directory=" + path + " -- cat TopologyEvents" + str(i) + ".txt")
            open('TopologyEvents' + str(i) + '.txt', 'w').writelines(
                [line for line in open('Log' + str(i) + '.txt') if 'TopologyManager' in line])

            with open('TopologyEvents' + str(i) + '.txt') as f:
                n = i - 1
                line = f.readlines()
                lastline = line[-1]
                lastdate = lastline.split('|')
                lastdate = lastdate[0]
                lastdate = lastdate.replace("-", ",")
                lastdate = lastdate.replace(":", ",")
                lastdate = lastdate.replace(" ", ",")
                lastdate = lastdate[:-1]
                lastdate = lastdate + '000'
                lastdate1 = datetime.datetime.strptime(lastdate, '%Y,%m,%d,%H,%M,%S,%f')
                alldates.append(lastdate1)
                alldates.sort()
                i = i + 1
    if (ControllerType.get() == "ODL"):
        i = 1
        while (i <= x):
            with open('scriptEvents' + str(i) + '.sh', "w") as f:
                f.write("#!/bin/bash")
                f.write("\n")
                f.write('sudo lxc-attach -n ODL' + str(i) + ' -e sudo cat /sdn/karaf-0.7.2/data/log/karaf.log >>Log' + str(i) + '.txt')
            os.system("gnome-terminal --working-directory=" + path + " -- bash ./scriptEvents" + str(i) + ".sh")
            os.system("gnome-terminal --working-directory=" + path + " -- cat TopologyEvents" + str(i) + ".txt")
            open('TopologyEvents' + str(i) + '.txt', 'w').writelines([line for line in open('Log' + str(i) + '.txt') if 'DeviceManagerImpl' in line])

            with open('TopologyEvents' + str(i) + '.txt') as f:
                if (os.stat('TopologyEvents' + str(i) + '.txt').st_size != 0):
                    n = i - 1
                    line = f.readlines()
                    lastline = line[-1]
                    lastdate = lastline.split('|')
                    lastdate = lastdate[0]
                    lastdate = lastdate.replace("-", ",")
                    lastdate = lastdate.replace(":", ",")
                    lastdate = lastdate.replace(" ", ",")
                    lastdate = lastdate[:-1]
                    lastdate = lastdate + '000'
                    lastdate1 = datetime.datetime.strptime(lastdate, '%Y,%m,%d,%H,%M,%S,%f') #Dandole formato a la fecha
                    alldates.append(lastdate1)
                    alldates.sort()
                i = i + 1
    #Obtenidendo los logs de las capturas de tshark
    with open('OFEvents.txt') as f:
        line = f.readlines()
        firstrequest = line[0]
        if (firstrequest[7]==""):
            firstrequest[7]=0
        firstrequest = firstrequest.replace(" ", ",")
        firstrequest= firstrequest.replace(".", ",")
        firstrequest= firstrequest.replace(":", ",")
        firstrequest = firstrequest[:6] + firstrequest[7:-8]
        firstrequestdate = datetime.datetime.strptime(firstrequest, '%b,%d,%Y,%H,%M,%S,%f') #Dandole  formato a la fecha
        delta = alldates[-1] - firstrequestdate + timedelta(hours=1) #bteniendo la latencia por medio de la diferencia de tiempo
        print("La latencia  al agregar conmutador es de " +  str(delta.total_seconds()) + " segundos")
