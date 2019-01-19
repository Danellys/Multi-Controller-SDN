import os
import datetime
from datetime import timedelta
import inspect
import GUI
import Errores
def CalcularLatencia(QuantityCtrl, QSwitch, ControllerType):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    x = int(QuantityCtrl.get())
    qswicth = Errores.switcherror(QSwitch)
    alldates = list()
    #Obtenidendo los logs de los controladores
    if (ControllerType.get()=="ONOS"):
        i=1
        while (i<=x):
            with open('scriptEvents'+str(i)+'.sh', "w") as f:
                f.write("#!/bin/bash")
                f.write("\n")
                f.write('sudo lxc-attach -n ONOS'+str(i)+' -e sudo cat /opt/onos/apache-karaf-3.0.8/data/log/karaf.log >>Log'+str(i)+'.txt')
            os.system("gnome-terminal --working-directory=" +path+ " -- bash ./scriptEvents"+str(i)+".sh")
            os.system("gnome-terminal --working-directory=" + path + " -- cat TopologyEvents"+str(i)+".txt")
            open('TopologyEvents'+str(i)+'.txt','w').writelines([line for line in open('Log'+str(i)+'.txt') if 'TopologyManager' in line])

            with open('TopologyEvents'+str(i)+'.txt') as f:
                n =i-1
                line = f.readlines()
                lastline = line[-1]
                lastdate = lastline.split('|')
                lastdate=lastdate[0]
                lastdate=lastdate.replace("-", ",")
                lastdate=lastdate.replace(":", ",")
                lastdate = lastdate.replace(" ", ",")
                lastdate=lastdate[:-1]
                lastdate=lastdate+'000'
                lastdate1=datetime.datetime.strptime(lastdate, '%Y,%m,%d,%H,%M,%S,%f')
                alldates.append(lastdate1)
                alldates.sort()
                i = i + 1
        print(alldates[-x])
    if (ControllerType.get()=="ODL"):
        i = 1
        while (i<=x):
            with open('scriptEvents'+str(i)+'.sh', "w") as f:
                f.write("#!/bin/bash")
                f.write("\n")
                f.write('sudo lxc-attach -n ODL'+str(i)+' -e sudo cat /sdn/karaf-0.7.2/data/log/karaf.log >>Log'+str(i)+'.txt')
            os.system("gnome-terminal --working-directory=" +path+ " -- bash ./scriptEvents"+str(i)+".sh")
            os.system("gnome-terminal --working-directory=" + path + " -- cat TopologyEvents"+str(i)+".txt")
            open('TopologyEvents'+str(i)+'.txt','w').writelines([line for line in open('Log'+str(i)+'.txt') if ' DeviceFlowRegistryImpl' in line])

            with open('TopologyEvents'+str(i)+'.txt') as f:
                if (os.stat('TopologyEvents'+str(i)+'.txt').st_size != 0):
                    n =i-1
                    line = f.readlines()
                    lastline = line[-1]
                    lastdate = lastline.split('|')
                    lastdate=lastdate[0]
                    lastdate=lastdate.replace("-", ",")
                    lastdate=lastdate.replace(":", ",")
                    lastdate = lastdate.replace(" ", ",")
                    lastdate=lastdate[:-1]
                    lastdate=lastdate+'000'
                    lastdate1=datetime.datetime.strptime(lastdate, '%Y,%m,%d,%H,%M,%S,%f') #Dandole formato a la fecha
                    alldates.append(lastdate1)
                    alldates.sort()
                i = i + 1
    with open('OFEvents.txt') as f:
        line = f.readlines()
        lastrequest = line[0]
        if (lastrequest[7] == ""):
            lastrequest[7] = 0
        lastrequest = lastrequest.replace(" ", ",")
        lastrequest = lastrequest.replace(".", ",")
        lastrequest = lastrequest.replace(":", ",")
        lastrequest = lastrequest[:6] + lastrequest[7:-8]
        lastrequestdate = datetime.datetime.strptime(lastrequest, '%b,%d,%Y,%H,%M,%S,%f') #Dandole formato a la fecha
        delta = alldates[-1] - lastrequestdate + timedelta(hours=1) #Calculando la latencia por medio de la diferencia de timepos
        print("La latencia al descubrir la topología es de: " + str(delta.total_seconds()) + "segundos")
        GUI.latencia = delta.total_seconds
#Obteniendo los logs de tshark
def CapturarPaquetes(IP_Address):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    ipgateway = Errores.check_ip(IP_Address)
    with open('tshark.sh', 'w') as f:
        f.write("#!/bin/bash")
        f.write("\n")
        f.write("sudo tshark -i any  -Y 'ip.src=="+str(ipgateway)+" && tcp.flags.syn==1 && tcp.flags.ack==0' -e frame.time -Tfields  -l > OFEvents.txt")
        f.write("\n")
    os.system("gnome-terminal --working-directory=" + path + " -- sudo bash ./tshark.sh")