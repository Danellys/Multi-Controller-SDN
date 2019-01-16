import ipaddress
def create_subnet(ip_address):
    with open('escenario.xml', 'a') as file:
        file.write('<host>')
        file.write("\n")
        file.write('<hostif net="Net0">')
        file.write("\n")
        file.write("<ipv4>"+str(ip_address)+"/24 </ipv4>")
        file.write("\n")
        file.write(' </hostif>')
        file.write("\n")
        file.write(' </host>')
        file.write("\n")
        file.write('</vnx>')