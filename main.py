#Imports
import routeros_api #downloaded from pypi.org
import telebot #github.com/eternnoir
#Functions
# Saves data for faster login
def data_save(file_written):  
    file_to_write = open("data","w")
    file_to_write.write(file_written.read())
    return
# Token prompt
def token_input():
    print("Please input the Telegram Bot token")
    token = input()
    return token

token=token_input()
bot=telebot.TeleBot(token, parse_mode=None)
connection = routeros_api.RouterOsApiPool('192.168.3.179', username='admin', password='', plaintext_login=True)
mapi = connection.get_api()
print("Bot activated")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['write'])
def write_command(message):
    bot.reply_to(message, "Check the mikrotik firewall!")
    list_address =  mapi.get_resource('/ip/firewall/address-list')
    list_address.add(address="192.168.0.1",comment="P1",list="10M")
    list_address.get(comment="P1")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

connection.disconnect()
