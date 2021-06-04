def help():
    return "/interfaces\nshow n - Shows the interface n\nshow r - Shows the interfaces that are running\nrestart n - Restarts the interface n\ndisable n - Disables the interface n\nenable n - Enables the interface n\n"
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
    

