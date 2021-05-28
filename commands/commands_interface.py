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
            contr = 0
            for x in data:
                s = str(data[cont])
                cont = cont+1
                try:
                    if s.replace(" ","").index("running:true") > 0:
                        contr=contr+1
                        print("one running")
                except:
                    text="text"
            s =(contr, " interfaces running")
        else:
            s = str(data[int(message_sliced)-1])
            s = s.replace("{"," ")
            s = s.replace("}"," ")
            s = s.replace(",","\n")
            s = s.replace("'"," ")
        return s
    except IndexError:
        return "ERROR: The interface does not exist"

