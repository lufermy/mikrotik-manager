def help():
    return "/interfaces\nshow n - Shows the interface n\nshow r - Shows the interfaces that are running\nrestart n - Restarts the interface n\ndisable n - Disables the interface n\nenable n - Enables the interface n\n"
def show(message,data):
    try:
        message_sliced = message[5:len(message)]
        if message_sliced.replace(" ","") == "":
            cont = 0
            for x in data:
                cont=cont+1
            s="Select an interface please"
        elif message_sliced.replace(" ","") == "r":
            cont = 0
            running = ""
            for x in data:
                s = data[cont]
                cont = cont+1
                try:
                    if s['running'] == "true":
                        running=running+s['name']+"\n"
                except Exception as e:
                    print(e)
            return running
        else:
            s = str(data[int(message_sliced)-1])
            s = s.replace("{"," ")
            s = s.replace("}"," ")
            s = s.replace(",","\n")
            s = s.replace("'"," ")
        return s
    except IndexError:
        return "ERROR: The interface does not exist"
def restart(message,api):
    message_sliced=message[8:len(message)]
    if message_sliced.replace(" ","") != "":
        print (message_sliced)
        api.set(id=message_sliced, disabled = "yes")
        api.set(id=message_sliced, disabled = "no")
        return "Interface restarted succesfully"
        
    else:
        print(message_sliced)
    return "Wrong interface..."
def disable(message,api):
    message_sliced=message[7:len(message)]
    if message_sliced.replace(" ","") != "":
        message_sliced=str(int(message_sliced)-1)
        api.set(id=message_sliced, disabled = "yes")
        return "Interface disabled succesfully"

    else:
        print(message_sliced)
    return "Wrong interface..."
def enable(message,api):
    message_sliced=message[6:len(message)]
    if message_sliced.replace(" ","") != "":
        message_sliced=str(int(message_sliced)-1)
        print(message_sliced)
        api.set(id=message_sliced, disabled = "no")
        return "Interface enabled succesfully"

    else:
        print("Wrong interface")
        print(message_sliced)

    return "Wrong interface..."


