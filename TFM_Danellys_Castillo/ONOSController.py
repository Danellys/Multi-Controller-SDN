#Creación de XML correspondiente a controlador ONOS
import ipaddress
def ONOS_cluster(ip_address, x):
    i = 1
    ip1 = ipaddress.IPv4Address('0.0.0.0')
    ip1 = ip_address
    while i <= x:
        i2 = 1
        i += 1
        ip1 += 1
        with open('escenario.xml', 'a') as file:
            ip2 = ip_address
            cluster = ''
            while i2 <= x:
                cluster = cluster + str(ip2) + ' '  # Enlazando todas las direcciones IP del clúster
                i2 += 1
                ip2 += 1
            file.write("\n")
            file.write('<vm name = "ONOS' + str(i - 1) + '" type="lxc" exec_mode = "lxc-attach" arch = "x86_64">')
            file.write("\n")
            file.write('<filesystem type="cow">/usr/share/vnx/filesystems/vnx_rootfs_lxc_ubuntu64-16.04-v025</filesystem>')
            file.write("\n")
            file.write('<if id="1" net="Net0">')
            file.write("\n")
            file.write('<ipv4>' + str(ip1) + '/24</ipv4>')
            file.write("\n")
            file.write('</if>')
            file.write("\n")
            file.write('</vm>')