#Imports
import routeros_api #downloaded from pypi.org
import telebot #github.com/eternnoir
#commands
from commands import commands_interface
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
def print_menu():
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
        print(len(data))
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
        
        bot = telebot.TeleBot(bot_token)
        connection = routeros_api.RouterOsApiPool(login_ip, username=login_username, password=login_password, plaintext_login=True)
        mapi = connection.get_api()
        print("Connected succesfully!")
        print("The bot is listening")
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
	        bot.reply_to(message, "Howdy, how are you doing?")
        
        @bot.message_handler(commands=['write'])
        def write_firewall(message):
            bot.reply_to(message, "Check the mikrotik firewall!")
            list_address =  mapi.get_resource('/ip/firewall/address-list')
            list_address.add(address="192.168.0.1",comment="P1",list="10M")
            print(list_address.get(comment="P1"))
        @bot.message_handler(commands=['show_interfaces'])
        def show_interfaces(message):
            interfaces=mapi.get_resource('/interface')
            interfaces_list=interfaces.get()
            message_sliced = message.text[16:len(message.text)]
            reply = commands_interface.show(message_sliced,interfaces_list)
            bot.reply_to(message,reply)


        @bot.message_handler(func=lambda message: True)
        def echo_all(message):
            bot.reply_to(message, message.text)

        bot.polling()
        connection.disconnect()
#-----------------------------------------------------------------------
    if menu_opc == "6":
        loopstmnt=False
        print("")
        print("Bye...")
        print("")
