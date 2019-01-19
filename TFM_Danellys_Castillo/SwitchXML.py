#from netaddr import *
#import ipaddress
#Creación de XML correspondiente a los controladores
def create_switch(switch, ipcontrollers,x, TopologyType):
    i= 1
    icontrollers = 1
    controllers = ''
    while i <= switch:
        switchrange = list(range(i+1, switch+1))
        while icontrollers < x:
            ipcontrollers += 1
            controllers = controllers+'tcp:' + str(ipcontrollers) +':6653,'
            icontrollers += 1
        if icontrollers == x:
            ipcontrollers += 1
            controllers = controllers+'tcp:' + str(ipcontrollers) +':6653" '
            icontrollers +=1
        with open('escenario.xml', 'a') as file:
            file.write('<net name="Net'+str(i)+'" mode="openvswitch" controller="'+str(controllers)+ ' fail_mode='+"'secure' of_version="+'"OpenFlow13">')
            file.write("\n")
            if (TopologyType.get()=="Malla"):
                for connections in switchrange:
                    file.write("<connection name='link" +str(i)+str(connections)+"' net='Net" +str(connections)+ "' >")
                    file.write("\n")
                    file.write("</connection>")
                    file.write("\n")
                file.write("</net>")
                file.write("\n")
            if (TopologyType.get() == "Anillo"):
                if (i<switch):
                    file.write("<connection name='link" +str(i)+str(i+1)+"' net='Net" +str(i+1)+ "' >")
                    file.write("\n")
                    file.write("</connection>")
                    file.write("\n")
                    file.write("</net>")
                    file.write("\n")
                if (i==switch):
                    file.write("<connection name='link" +str(i)+"1' net='Net1' >")
                    file.write("\n")
                    file.write("</connection>")
                    file.write("\n")
                    file.write("</net>")
                    file.write("\n")
        i+= 1
    return controllers
