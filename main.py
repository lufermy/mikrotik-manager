#Imports
import routeros_api #downloaded from pypi.org
import telebot #github.com/eternnoir
import time
#commands
from commands import commands_interface
from commands import commands_help
#---------------------------------------------------Functions
# 1
def menu_opc_2(login_username,login_password,login_ip,bot_token):
    print("")
    print("Saving...")
    f = open("data.txt", "w")
    f.write((login_username+"\n"))
    f.close()
    f = open("data.txt", "a")
    
    f.write((login_password+"\n"))
    f.write((login_ip+"\n"))
    f.write((bot_token+"\n"))
    f.close()
#3
def menu_opc_3():
    f = open("data.txt","r")
    data = f.read()
    return data
def menu_opc_4():
    f = open("data.txt","w")
    f.write("")
    print("All the data in data.txt removed succesfully!")
    f.close()
def menu_opc_5():
    print("Menu 5")

# Token prompt
def token_input():
    print("Please input the Telegram Bot token")
    token = input()
    return token
# Menu structure
def clear_screen():
    for x in range(1,50):
        print("\n")
def print_menu():
    clear_screen()
    print("-----------------------------------")
    print("---- Mikrotik telegram Manager ----")
    print("||        27/05/2021 Build       ||")
    print("||                               ||")
    print("||  1)Input the ip and token     ||")
    print("||  2)Save input to data.txt     ||")
    print("||  3)Load from data.txt         ||")
    print("||  4)Delete data.txt            ||")
    print("||  5)Run application            ||")
    print("||  6)Close application          ||")
    print("||  7)About                      ||")
    print("-----------------------------------")
    print("-----------------------------------")
def temporal():
    token=token_input()
    bot=telebot.TeleBot(token, parse_mode=None)
    connection = routeros_api.RouterOsApiPool('192.168.3.179', username='admin', password='', plaintext_login=True)
    mapi = connection.get_api()
    print("Bot activated")

#------------------------------------------------------Main function
loopstmnt=True
bot_token=""
login_username=""
login_password=""
login_ip=""
while loopstmnt == True:
    print_menu()
    menu_opc=input()
    if menu_opc == "1":
        bot_token=input("Paste the telegram bot token here: ")
        login_username=input("Type the username: ")
        login_password=input("Type the password: ")
        login_ip=input("Type the device's IP: ")
    if menu_opc == "2":
        menu_opc_2(login_username,login_password,login_ip,bot_token)
    if menu_opc == "3":
        data=menu_opc_3()
        login_username=data[0:data.index("\n")]
        data=data[(data.index("\n")+1):len(data)]
        login_password=data[0:data.index("\n")]
        data=data[data.index("\n")+1:len(data)]
        login_ip=data[0:data.index("\n")]
        data=data[data.index("\n")+1:len(data)]
        bot_token=data[0:data.index("\n")]
        print("Data loaded succesfully!")
    if menu_opc == "4":
        menu_opc_4()
    if menu_opc == "5":
#-----------------------------------------------------------BOT FUNCTIONS
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
            @bot.message_handler(commands=['help'])
            def write_firewall(message):
                bot.reply_to(message, commands_help.show())
            @bot.message_handler(commands=['interfaces'])
            def interfaces(message):
                reply="default reply"
                interface=mapi.get_resource('/interface')
                interface_list=interface.get()
                message_sliced = message.text[12:len(message.text)]
                if message_sliced == "":
                    reply = commands_interface.help()
                if message_sliced[0:4] == "show":
                    reply = commands_interface.show(message_sliced,interface_list)
                if message_sliced[0:7] == "restart":
                    reply = commands_interface.restart(message_sliced,mapi)
                if message_sliced[0:6] == "enable":
                    reply = "enable"
                if message_sliced[0:7] == "disable":
                    reply = "disable"
                bot.reply_to(message,reply)               
    
            @bot.message_handler(func=lambda message: True)
            def echo_all(message):
                bot.reply_to(message, message.text)
    
            bot.polling()
            connection.disconnect()
        except routeros_api.exceptions.RouterOsApiConnectionError:
            print("Timed out, try again")
            time.sleep(2)
        
        except:
            print("Something went wrong")
    
#-----------------------------------------------------------------------
    if menu_opc == "6":
        loopstmnt=False
        print("")
        print("Bye...")
        print("")
    if menu_opc == "7":
        for x in range(1,50):
            print("\n")
        print("This is where im supposed to write about, just, not yet")
        input("Press enter to be back")
        for x in range(1,50):
            print("\n")
    

