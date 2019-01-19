import os
import datetime
from datetime import timedelta
import inspect
import GUI
import Errores
import time
def prueba(QuantityCtrl,ControllerType):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    os.system("gnome-terminal --working-directory=" + path + " -- sudo ovs-vsctl del-br NetTest")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm -f Topology.Events*")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo rm  -f Log*")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo  bash OVS.sh")
    x = int(QuantityCtrl.get())
    alldates = list()
    time.sleep(5)
    #Obteniendo los logs de los controladores
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
                f.write(
                    'sudo lxc-attach -n ODL' + str(i) + ' -e sudo cat /sdn/karaf-0.7.2/data/log/karaf.log >>Log' + str(i) + '.txt')
            os.system("gnome-terminal --working-directory=" + path + " -- bash ./scriptEvents" + str(i) + ".sh")
            os.system("gnome-terminal --working-directory=" + path + " -- cat TopologyEvents" + str(i) + ".txt")
            open('TopologyEvents' + str(i) + '.txt', 'w').writelines([line for line in open('Log' + str(i) + '.txt') if'Removing device from operational DS openflow' in line])

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
                    lastdate1 = datetime.datetime.strptime(lastdate, '%Y,%m,%d,%H,%M,%S,%f') #Dando formato a la fecha
                    alldates.append(lastdate1)
                    alldates.sort()
                i = i + 1
    # #Obtenidendo los logs de las capturas de tshark
    with open('OVSEvents.txt') as f:
        line = f.readlines()
        lastlog = line[-1]
        lastlog=lastlog.split(" ")
        logtime=lastlog[3]
        lastrequest=lastlog[2]+"," +logtime[:12]+str("000")
        if (lastrequest[5] == ""):
            lastrequest[5] = 0
        lastrequest = lastrequest.replace(".", ",")
        lastrequest = lastrequest.replace(":", ",")
        lastrequest = lastrequest.replace("-", ",")
        lastrequestdate = datetime.datetime.strptime(lastrequest, '%Y,%m,%d,%H,%M,%S,%f')#Dando formato a la fecha
        delta = alldates[-1] - lastrequestdate
        print("La latencia al eliminar el conmutador es de "+str(delta.total_seconds())+" segundos") #bteniendo la latencia por medio de la diferencia de tiempo
        GUI.latencia = delta.total_seconds