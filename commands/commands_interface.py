def show(message,data):
    try:
        if message == "":
            cont = 0
            for x in data:
                linea = str(data[cont])
                linea = linea.replace("{"," ")
                linea = linea.replace("}"," ")
                linea = linea.replace(",","\n")
                linea = linea.replace("'"," ")
                cont=cont+1
        else:
            linea = str(data[int(message)-1])
            linea = linea.replace("{"," ")
            linea = linea.replace("}"," ")
            linea = linea.replace(",","\n")
            linea = linea.replace("'"," ")
        return linea
    except IndexError:
        return "ERROR: The interface does not exist"
