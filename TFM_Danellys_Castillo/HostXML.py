#Crreación de la parte del XML correspondiente a los hosts
def create_host(switch, host):
    iswitch = 1
    ihost = 1
    while iswitch <= switch:
        ihost = 1
        while ihost <= host:
            with open('escenario.xml', 'a') as file:
                file.write('<vm name = "PC'+str(iswitch)+'_'+str(ihost)+'" type="lxc" exec_mode = "lxc-attach" arch = "x86_64">')
                file.write("\n")
                file.write('<filesystem type="cow">/usr/share/vnx/filesystems/vnx_rootfs_lxc_ubuntu64-16.04-v025</filesystem>')
                file.write("\n")
                file.write('<if id="1" net="Net'+str(iswitch)+'">')
                file.write("\n")
                file.write('<ipv4>192.168.'+str(iswitch)+'.'+str(ihost+1)+'/24</ipv4>')
                file.write("\n")
                file.write('</if> ')
                file.write("\n")
                file.write('<route type="ipv4" gw="192.168.'+str(iswitch)+'.'+str(ihost+1)+'">default</route>')
                file.write("\n")
                file.write('</vm>')
            ihost += 1
        iswitch += 1
