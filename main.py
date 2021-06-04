#
#   MIKROTIK MANAGER
#
#   CREATED BY LUFERMY (SO FAR) 
#
#   27/05/2021
#
#   Im sorry, everyone
#Imports
import routeros_api #downloaded from pypi.org
import telebot #github.com/eternnoir
import time
#commands
from commands import commands_interface
from commands import commands_help
from commands import commands_system
from commands import commands_tool
from commands import commands_ip
#Functions
# Saving data to text file
def menu_opc_2(login_username,login_password,login_ip,bot_token):
    print("")
    print("Saving...")
    time.sleep(0.25)
    f = open("data.txt", "w")
    f.write((login_username+"\n"))
    f.close()
    f = open("data.txt", "a")
    
    f.write((login_password+"\n"))
    f.write((login_ip+"\n"))
    f.write((bot_token+"\n"))
    f.close()
    input("Data saved. Press enter to continue")
# Read data and return it
def menu_opc_3():
    f = open("data.txt","r")
    data = f.read()
    return data
# Remove data
def menu_opc_4():
    f = open("data.txt","w")
    f.write("")
    print("All the data in data.txt removed succesfully!")
    f.close()
    input("Press enter to continue")

# Menu structure
def clear_screen():
    for x in range(1,50):
        print("\n")
def print_menu():
    clear_screen()
    print("----------------------------------------")
    print("------  Mikrotik telegram Manager ------")
    print("||            02/06/2021 Build        ||"+" ->  Username: "+ login_username)
    print("||                                    ||"+" ->  Password: "+ login_status)
    print("||       1)Input the ip and token     ||")
    print("||                                    ||")
    print("||       2)Save input to data.txt     ||")
    print("||                                    ||")
    print("||       3)Load from data.txt         ||")
    print("||                                    ||")
    print("||       4)Delete data.txt            ||")
    print("||                                    ||")
    print("||       5)Run application            ||")
    print("||                                    ||")
    print("||       6)Close application          ||")
    print("||                                    ||")
    print("||       7)About                      ||")
    print("----------------------------------------")
    print("----------------------------------------")
# Returns the password string hidden with *
def hide_password(password):
    hidden_password=""
    for x in range(0,len(password)):
        hidden_password=hidden_password+"*"
    return hidden_password
#Main function
loopstmnt=True
bot_token=""
login_username=""
login_password=""
login_ip=""
login_status=""
while loopstmnt == True:
    print_menu()
    menu_opc=input()
    if menu_opc == "1":
        # Input data
        bot_token=input("Paste the telegram bot token here: ")
        login_username=input("Type the username: ")
        login_password=input("Type the password: ")
        login_ip=input("Type the device's IP: ")
        login_status="Loaded"
        print("Data recieved")
        input("Press enter to continue")
    if menu_opc == "2":
        # Save
        menu_opc_2(login_username,login_password,login_ip,bot_token)
    if menu_opc == "3":
        # Load data
        data=menu_opc_3()
        login_username=data[0:data.index("\n")]
        data=data[(data.index("\n")+1):len(data)]
        login_password=data[0:data.index("\n")]
        data=data[data.index("\n")+1:len(data)]
        login_ip=data[0:data.index("\n")]
        data=data[data.index("\n")+1:len(data)]
        bot_token=data[0:data.index("\n")]
        login_status=hide_password(login_password)
        print("Data loaded succesfully!")
        time.sleep(1)

    if menu_opc == "4":
        # Delete data
        menu_opc_4()
    if menu_opc == "5":
        # Run bot
        try:
            try:
                bot = telebot.TeleBot(bot_token)
            except:
                clear_screen()
                print("Something went wrong with the telegram bot. Make sure that the token is correct")
                time.sleep(1)
                print("Restart the bot")
                time.sleep(1)
                input()
            try:
                connection = routeros_api.RouterOsApiPool(login_ip, username=login_username, password=login_password, plaintext_login=True)
                mapi = connection.get_api()
            except:
                clear_screen()
                print("Something went wrong with the routerOS API. Make sure that both user and password are correct. Also make sure that the host's ip address is correct and that has the api service active with the default port")
                time.sleep(1)
                print("Restart the bot")
                time.sleep(1)
                input()
            print("Connected succesfully!")
            print("The bot is listening")        
            # Commands
            #       Help -> Prompts all available commands
            @bot.message_handler(commands=['help'])
            def show_help(message):
                bot.reply_to(message, commands_help.show())
            #       Interfaces -> Lets u manage interfaces
            #                   Show
            #                   Restart
            #                   Enable
            #                   Disable
            @bot.message_handler(commands=['interfaces'])
            def interfaces(message):
                reply="interfaces default reply"
                interface=mapi.get_resource('/interface')
                interface_list=interface.get()
                message_sliced = message.text[12:len(message.text)]
                if message_sliced == "":
                    reply = commands_interface.help()
                if message_sliced[0:4] == "show":
                    reply = commands_interface.show(message_sliced,interface_list)
                if message_sliced[0:7] == "restart":
                    reply = commands_interface.restart(message_sliced,interface)
                if message_sliced[0:6] == "enable":
                    reply = commands_interface.enable(message_sliced,interface)
                if message_sliced[0:7] == "disable":
                    reply = commands_interface.disable(message_sliced,interface)
                bot.reply_to(message,reply)               
            #       Tools -> Prompts tools
            #       NOT WORKING YET
            @bot.message_handler(commands=['tools'])
            def tools(message):
                reply="tools default reply"
                #tools=mapi.get_resource('/tool')
                #tools_list=tools.get()
                message_sliced = message.text[6:len(message.text)]
                if message_sliced == "":
                    reply = commands_tool.help() 
                if message_sliced == "help":
                    reply = commands_tool.help()
                bot.reply_to(message,reply)
            #       System -> Modifies the /system
            #       NOT WORKING YET
            @bot.message_handler(commands=['system'])
            def system(message):
                reply = "system default reply"
                message_sliced = message.text[8:len(message.text)]
                #system=mapi.get_resource("/system")
                #system_list=system.get()
                if message_sliced == "":
                    reply = commands_system.help()
                if message_sliced == "help":
                    reply = commands_system.help()
                if message_sliced == "health":
                    reply = commands_system.health(mapi)
                if message_sliced == "identity":
                    reply = commands_system.health(message_sliced[9:len(messaege_sliced)],mapi)                    
                bot.reply_to(message,reply)
            #       IP -> Modifies the IP interfaces
            #           Help -> Prompts help
            #           Address -> Prompts help
            #               -> Add
            #               -> Remove
            #               -> Print
            #               -> Enable
            #               -> Disable
            #~              ->
            @bot.message_handler(commands=['ip'])
            def ip(message):
                reply ="ip default reply"
                message_sliced = message.text[4:len(message.text)]
                if message_sliced =="":
                    reply = commands_ip.help()
                if message_sliced[0:4] =="help":
                    reply = commands_ip.help()
                if message_sliced[0:7] =="address":
                    reply = commands_ip.address(mapi,message_sliced[8:len(message_sliced)])
                bot.reply_to(message,reply)
            @bot.message_handler(func=lambda message: True)
            def echo_all(message):
                bot.reply_to(message, message.text)
    
            bot.polling()
            connection.disconnect()
        except routeros_api.exceptions.RouterOsApiConnectionError:
            print("Timed out, try again")
            time.sleep(2)
        
        except Exception as e:
            print("Something went wrong")
            print("Error code: ", e)
    if menu_opc == "6":
        #Exit
        loopstmnt=False
        print("")
        print("Bye...")
        print("")
    if menu_opc == "7":
        #About?
        for x in range(1,50):
            print("\n")
        print("Special thanks")
        time.sleep(0.25)
        about="This are the credits of my video game.\n Director: Hideo Kojima\n Storyboard: Hideo Kojima \n Everything else,@lufermy\n\n Seriously now, thanks to everyone who has collaborated in this tool, and has\n showed his support. I really appreciate it since this was my first project so far. Yet it looks\n so unpolished... Well, for now i dont have anyone else to give special thanks to...\n\n\nWhatever."
        for x in range(0,len(about)):
            print(about[x],sep='',end='',flush=True)
            time.sleep(0.06)
        input("\nPress enter to go back")
        for x in range(1,50):
            print("\n")
    

