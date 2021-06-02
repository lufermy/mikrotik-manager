def help():
    linea = "/ip -- Parameters\naddress - Addresses\nneighbors - Neighbor config\nfirewall - Firewall config\nroute - Routes config\ndhcp - DHCP Config\npool - Pools config\nservices - Services config"
    return linea
def address(api,message):
    linea="default address response"
    if message == "" or message == "help":
        return "/ip address - Parameters\nprint - shows all ips\nadd - adds an ip\ncomment - shows or edit a comment\ndisable - disables an ip\nedit - edits an ip\nenable - enables an ip\nremove - removes an ip"
    address = api.get_resource('/ip/address')
    address_list = address.get()
    if message == "print":
        linea="IPs\n--------------\n"
        for x in address_list:
            y=str(x)
            y=y.replace("{","")
            y=y.replace(",","\n")
            y=y.replace("'","")
            y=y.replace("}","")
            linea=linea+y+"\n"+"--------------\n"
    if message[0:3] == "add":
        message_sliced=message[4:len(message)]
        if message_sliced == "":
            return 'Parameter ordrer - examples\naddress - 192.168.1.15/24 \ncomment - "to_my_pc" (no spaces) \ninterface - ether1'
        ipinputed=False
        commentinputed=False
        ip=""
        commentairo=''
        interfaces=""
        for x in range(0,len(message_sliced)):
                if ipinputed == False:
                    if message_sliced[x] == " ":
                        ipinputed =True
                    else:
                        ip = ip+message_sliced[x]
                elif commentinputed == False:
                    if message_sliced[x] == " ":
                        commentinputed = True
                    else:
                        commentairo = commentairo+message_sliced[x]
                else:
                    interfaces=interfaces+message_sliced[x]
        address.add(address=ip,comment=commentairo,interface=interfaces)
        return "Address added succesfully"
    if message[0:6] == "remove":
        amessage_sliced=message[7:len(message)]
        if amessage_sliced == "" or amessage_sliced == "help":
            return "Remove an IP based on the IP's ID. Example:\n /ip address remove *1 - removes the ip with the id *1"
        address.remove(id=amessage_sliced)
        return "Address removed succesfully"
    if message[0:6] == "enable":
        message_sliced = message[7:len(message)]
        if message_sliced == "" or message_sliced == "help":
            return "Enables an IP based on the IP's ID. Example:\n/ip address enable *1 - Enables the ip with id *1"
        else:
            address.set(id=message_sliced,disabled="no")
            return "Address enabled succesfully"
    if message[0:7] == "disable":
        message_sliced = message[8:len(message)]
        if message_sliced == "" or message_sliced == "help":
            return "Disables an IP based on the IP's ID. Example:\n/ip address disable *1 - Disables the ip with id *1"
        else:
            address.set(id=message_sliced,disabled="yes")
            return "Address disabled succesfully"

    

    return linea
    
