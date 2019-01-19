#Creación de XML correspondiente al controlador ODL
import ipaddress
def ODL_cluster(ip_address, x):
    i = 1 #Pertmite crear varias interaciones para crear varios controladores ODL
    ip1 = ip_address
    while i <= x:
        i2 = 1 #Permite crear varias interacciones para enlazar las direcciones IP
        i += 1
        ip1 += 1
        ip2 = ip_address
        with open('escenario.xml', 'a') as file:
            cluster = ''
            while i2 <= x:
                ip2 += 1
                cluster = cluster + str(ip2) + ' '  # Enlazando todas las direcciones IP del clúster
                i2 += 1
            clusterfinal = str(i - 1) + '  '+ cluster
            file.write("\n")
            file.write('<vm name = "ODL' + str(i - 1) + '" type="lxc" exec_mode = "lxc-attach" arch = "x86_64">')
            file.write("\n")
            file.write('<filesystem type="cow">/usr/share/vnx/filesystems/vnx_rootfs_lxc_ubuntu64-16.04-v025</filesystem>')
            file.write("\n")
            file.write('<if id="1" net="Net0">')
            file.write("\n")
            file.write('<ipv4>'+str(ip1) + '/24</ipv4>')
            file.write("\n")
            file.write('</if>')
            file.write("\n")
            file.write('<exec seq="on_boot" type="verbatim"> /sdn/karaf-0.7.2/bin/configure_cluster.sh  ' + str(clusterfinal) + '</exec>')
            file.write("\n")
            file.write('</vm>')
            file.write("\n")
