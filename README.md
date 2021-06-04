# mikrotik-manager
A mikrotik status manager that works throught a telegram bot

The code both the mikrotik API and the telegram API are NOT mine.
The telegram bot API is from eternnoir
The mikrotik API is fro Pypi

All the code is written and tested in a clean Ubuntu Server 21.04 installation

How to install

$ git clone https://github.com/lufermy/mikrotik-manager.git
$ cd pyTelegramBotAPI
$ python3 setup.py install

Once its installed, just run main.py

$ python3 main.py

The code is very intolerant with errors for now, i'll change that

Functions (so far as 28/05/2021)
	Menu:
		1.- Input the ip and token
			Here's where you put your Bot token, mikrotik device's user and password, also the IP
		2.- Save input to data.txt
			Here you save your (already inputed) login credentials to a text file, so you can use them later for faster logins!
		3.- Load from data.txt
			Loads the file data.txt, so it loads the login credentials. ATTENTION: data.txt must be been created before running it!
		4.- Delete data.txt
			It clears the data.txt file, in case you dont want anyone to find your password.
		5.- Run application
			Runs the bot and activates the telegram api. Might give errors, sent them to luisfernandezmartinezz@gmail.com or contact me on twitter @lufermy
		6.- Close application
			Stops the application
		7.- About
			I dont know what will i put here

	Application functions as of 1.0.1 (send them to your telegram bot) 
		/help - prompts the help menu. Might not be updated yet
		/interfaces - manages your interfaces on your mikrotik
			Options
				show
					r - Shows all running interfaces
					n - Shows interface n
				restart
					n - Restarts interface n
				disable
					n - Disables interface n
				enable
					n - Enables interface n
		
					-- NOTE THAT N MUST BE A NUMBER
		/ip - manages the ip on your mikrotik
			Options
				address
					print - Prints all the ips
					
					add - Adds an ip
						Syntax-> add ip/masq comment(no_white_spaces) interface_name
						Example: /ip address add 192.168.0.10/24 "My_Pc" ether1
					remove - Removes an ip based on the id. To know the ip id, print them by using /ip addresses print
						Syntax-> remove ip_id
						Example: /ip address remove *2
					enable - Enables an ip based on the id. To know the ip id, print them by using /ip addresses print
						Syntax-> enable ip_id
						Example: /ip address enable *4
					disable - Disables an ip based on the id. To know the ip id, print them by using /ip addresses print
						Syntax-> disable ip_id
						Example: /ip address disable *4
				pool
					print - Prints all the pools
					add - Adds a pool
						Syntax-> add ipmin-ipmax comment(with no blank spaces) pool_name
						Example: /ip pool add 192.168.1.50-192.168.1.100 local_devices pool2
					remove - Removes a pool
						Syntax-> remove id
						Example: /ip pool remove *1
						
Note that this is my first project so im kinda new, please feel fre to give me any advice. Thanks
