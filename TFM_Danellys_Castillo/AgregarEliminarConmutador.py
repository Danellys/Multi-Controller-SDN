#Pruebas de Agregar y eliminar conmutadores
import os

#Funcion para eliminar conmutadores
def Eliminar(QSwitch, TopologyType):
    for bridge in range(1,QSwitch+1):
        os.system("sudo ovs-vsctl del-br Net" + str(bridge))
    if (TopologyType.get()=="Anillo"):
        for bridge in range(1, QSwitch + 1):
            if (bridge != QSwitch):
                os.system("ip link delete Link" + str(bridge) + "-" + str(bridge + 1) + "-1")
            if (bridge == QSwitch):
                os.system("ip link delete Link" + str(bridge) + "-1-1")
    if (TopologyType.get()=="Malla"):
        for bridge in range(1,QSwitch):
            if (bridge!=QSwitch):
                for peer in range(bridge+1,QSwitch+1,1):
                    os.system("ip link delete dev Link" + str(bridge) + "-" + str(peer) + "-1")

#Función para  agregar conmutadores
def Agregar(QSwitch, controllers, TopologyType):
    #Creando los conmutadores e indicando que utilizan OpenFlow1.3
    if (TopologyType.get()=="Anillo"):
        for bridge in range(1,QSwitch+1):
            os.system("sudo ovs-vsctl add-br Net" + str(bridge))
            os.system("sudo ovs-vsctl set bridge Net"+ str(bridge)+" protocols=OpenFlow13")
        for bridge in range(1,QSwitch+1):
        #Creando los enlaces entre conmutadores
            if (bridge!=QSwitch):
                os.system("ip link add dev Link"+str(bridge)+"-"+str(bridge+1)+"-1 type veth peer name Link"+str(bridge)+"-"+str(bridge+1)+"-2")
                os.system("sudo ip link set Link"+ str(bridge) + "-"+ str(bridge + 1) + "-1 up")
                os.system("sudo ip link set Link"+ str(bridge) + "-"+ str(bridge + 1) + "-2 up")
            if (bridge == QSwitch):
                os.system("ip link add dev Link"+str(bridge)+"-1-1 type veth peer name Link"+str(bridge)+"-1-2")
                os.system("sudo ip link set Link"+ str(bridge) + "-1-1 up")
                os.system("sudo ip link set Link"+ str(bridge) + "-1-2 up")
        for bridge in range(1,QSwitch+1):
            if (bridge== 1):
                os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(bridge) +"-"+ str(bridge + 1) + "-1")
                os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(QSwitch) +"-"+ str(bridge) + "-2")
            if (bridge!=QSwitch and bridge!=1):
                os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(bridge) + "-"+str(bridge + 1)+"-1")
                os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(bridge-1) + "-"+str(bridge) + "-2")
            if (bridge==QSwitch):
                os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(bridge) +  "-1-1")
                os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(bridge - 1) + "-"+str(bridge) +"-2")
    if (TopologyType.get()=="Malla"):
        for bridge in range(1,QSwitch+1):
            os.system("sudo ovs-vsctl add-br Net" + str(bridge))
            os.system("sudo ovs-vsctl set bridge Net"+ str(bridge)+" protocols=OpenFlow13")
        for bridge in range(1,QSwitch):
        #Creando los enlaces entre conmutadores
            if (bridge!=QSwitch):
                for peer in range(bridge+1,QSwitch+1,1):
                    os.system("ip link add dev Link" + str(bridge) + "-" + str(peer) + "-1 type veth peer name Link" + str(bridge) + "-" + str(peer) + "-2")
                    os.system("sudo ip link set Link" + str(bridge) + "-" + str(peer) + "-1 up")
                    os.system("sudo ip link set Link" + str(bridge) + "-" + str(peer) + "-2 up")
        for bridge in range(1, QSwitch+1):
            if (bridge!=QSwitch):
                for peer in range(bridge+1,QSwitch+1):
                    os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(bridge) + "-"+str(peer)+"-1")
            if (bridge!=1):
                for peer in range(bridge-1,0,-1):
                    os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(peer) + "-"+str(bridge) + "-2")
            if (bridge==QSwitch):
                for peer in range(bridge - 1, 0, -1):
                    os.system("sudo ovs-vsctl add-port Net" + str(bridge) + " Link" + str(peer) + "-" + str(bridge) + "-2")

    for bridge in range(1, QSwitch + 1):
        os.system("sudo ovs-vsctl set-controller Net" + str(bridge)+" "+str(controllers))
   