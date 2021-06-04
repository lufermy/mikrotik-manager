def help():
    return "/system\nhelp - Prompts this screen\nhealth - Shows the voltage & temp\nidentity - shows the identity\n     print - prints the device's name\n     set 'name' - sets the identity to 'name'"
def health(api):
    liste = api.get_resource('/system/health')
    data = liste.get()
    s = str(data)
    s=s.replace("[","")
    s=s.replace("{","")
    s=s.replace("'","")
    s=s.replace(",","\n")
    s=s.replace("}","")
    s=s.replace("]","")
    return s
def identity(message,api):
    if message == "" or message == "print":
        liste = api.get_resource('/system/identity')
        data = liste.get()
        s = str(data)
        s=s.replace("[","")
        s=s.replace("{","")
        s=s.replace("'","")
        s=s.replace(",","\n")
        s=s.replace("}","")
        s=s.replace("]","")
        return s
    elif message[0:3] == "set":
        liste = api.get_resource('/system/identity')
        liste.set(name=message[4:len(message)])
        return "Name changed succesfully"
    print(message[0:3])
