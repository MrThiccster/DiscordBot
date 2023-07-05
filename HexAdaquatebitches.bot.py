from pickle import FALSE
import random
import discord
import os
import time
import threading



from discord.ext import commands

    #                                                            ______   __  __     _____  _______  ______  _______  ______  _____      
    #         ________   |\                                     /__ __/  /  |/  |   / /_// / /  / /  \   _/ /__  __/ /  ___/ / /_//      
	#        /  ____  \  ||                                     __//__  /       |  / ___/ / /__/ /  __\  \    / /   /  ___/ /  _ <       
	#        | |____| | _||_                                   /_____/ /__/|_/|_| /_/    /______/  |_____/   /_/   /_____/ /__/ |/       
	#        |        |/_|||                                  ______   ______  ______   _____  _______  _____   ______                   
	#        |        |  ||        ____________      __      / ___  \ /__ __/  \   _/  / ___/ / /  / / / /_//  / ___  \                  
	#        |        |           /_           |____/  \    / /__/ /  __//__  __\  \  / /__  / /__/ / /  _ <  / /__/ /                   
	#        |   __   |            _>          |____   <   /______/  /_____/ |_____/ /____/ /______/ /__/ |/ /______/                    
	#        \__/  \__/           \____________|    \__/   _____   _______  _______                                                      
	#                                                     / /_//  / /  / / /__  __/                                                      
	#                                                    /  __<  / /__/ /    / /                                                         
	#                                                   /__/_// /______/    /_/                                                          


client = commands.Bot(command_prefix=".", intents=discord.Intents.all(), case_insensitive=True, self_bot=True)

public = 0


@client.event
async def on_ready():
	print("Bot is ready")
	
async def card(ctx,card):
		await ctx.channel.send(file=discord.File(str(card) + '.jpg'))

async def Build(ctx,player = []):
		for x in player:
			card(ctx,player[x])

async def total(ctx,player = [],playerTot = int):
		playerTot = 0
		for x in player:
			if x == 12 or 13 or 14:
				playerTot = playerTot + 10
			if x == 1 or 11:
				while msg != 1 or 11:
					msg = await client.wait_for("would you like the Ace to appear as an 11 or a 1? ")
				PlayerTot = PlayerTot + int(msg)
				if msg == 11 and PlayerTot > 21:
					ctx.send("Dumbass, I'm setting it to be a one, because it goes over 21 if you set it as 11")
					PlayerTot = PlayerTot - 10
			else:
				playerTot = playerTot + x

@client.command()
async def commands(ctx):
	if ctx.message.author.id == 406165174899179520:
		await ctx.reply('Hello Father, your commands are public, harass and MORB... remember to not use morb, as its too powerful to be used unless under extereme circustances...')
	else:
		await ctx.reply('shut up you ugly ass cretin, you have no power over me')


@client.command()
async def harass(ctx, arg):
	if (ctx.message.author.id == 406165174899179520) or (public == 1):
		if ctx.message.content.__contains__("<"):
			await ctx.send(arg)
			await ctx.send(arg)
			await ctx.send(arg)
			await ctx.send(arg + " Get harassed bozo")
		else:
			await ctx.send("Its supposed to be a person retard")
	else:
		await ctx.reply("you dont own me, quit tellin me what to do")

@client.command()
async def MORB(ctx):
	if ctx.message.author.id == 406165174899179520:
		await ctx.send("its happening...")
		await ctx.send("No... NO!")
		await ctx.reply("What... HAVE YOU DONE!!!")
		await ctx.send(file=discord.File('Turkeyimage1.jpg'))
	elif public == 1:
		await ctx.reply("Its too powerful for you to use... even if you do have public commands")
	else:
		await ctx.reply("YOU ARE NOT WORTHY!")

@client.command()
async def public(ctx):
	global public
	if ctx.message.author.id == 406165174899179520:
		if public == 0:
			public = 1
			await ctx.send("public commands have been enabled!")
		else:
			public = 0
			await ctx.send("public commands has been disabled! shame...")
	else:
		ctx.reply("Uh Oh, Retard alert!")

@client.command()
async def hit(ctx):
	Player = []
	Dealer = []
	PlayerAMT = 0
	DealerAMT = 0
	money = 0
	new =  1
	temp = 0
	BlackBank = open("BlackBank.txt","r+")
	Games = BlackBank.readlines()
	user = ctx.message.author.id
	for x in Games:
		if str(x).__contains__(str(user)):
			new = 0
		else:
			temp = temp + 1
	if new == 1:
		ctx.reply("you need to start a game first with the command blackjack pal")
		BlackBank.seek(0)
		for y in Games:
			y = int(y)
			BlackBank.write(str(y) + "\n")


	
@client.command()
async def blackjack(ctx, Amount):
	temp = 0
	money = 0
	bet = Amount
	bet = bet
	new = 0
	Dealer = [0,0]
	Player = [0,0]
	DealerAMT = int
	PlayerAMT = int
	user = ctx.message.author.id 
	MoneyBank = open("MoneyBank.txt","r+")
	Users = MoneyBank.readlines()
	BlackBank = open("BlackBank.txt","r+")
	Gamers = BlackBank.readlines()
	MoneyBank.close()

	




			#await total(Player,PlayerAMT)
			#await total(Dealer,DealerAMT)
						#Still need the uhh thing with the function to tell you howmany you and the dealer has, card wise

					
	



@client.command()
async def gamble(ctx, Amount, num):
	temp = 0                               #Variable Declaration
	new = 0 
	money = 0 
	Gamble = 0 
	size = 0
	user = ctx.message.author.id           #Sets the sender to the user variable
	MoneyBank = open("MoneyBank.txt","r+")  #Opens the file Moneybank.txt to read only mode
	Users = MoneyBank.readlines()          #throws each line in the .txt file into a list
	MoneyBank.close()                      #closes the file
	MoneyBank = open("MoneyBank.txt","r+")  #opens the file in write only mode
	print(Users)                           #prints out the supposed list
	size = (len(Users) + 1)
	await ctx.reply(size)
	for x in Users:
		print(x)
		if x.__contains__(str(user)): #checks if that list portion contains the Users id
			new = 1
			money = Users[temp + 1]
			print(int(money))
			if int(money) >= int(Amount):
				Gamble = random.randint(1,10)
				if int(num) == Gamble:
					money = (int(money) + int(Amount))
					Users[temp] = str(user)
					Users[temp + 1] = str(money)
					MoneyBank.seek(0)
					for y in Users: #fucks up here retard
						y = int(y)
						MoneyBank.write(str(y) + "\n")
					MoneyBank.close()
					await ctx.reply("The number was " + str(Gamble) + " and you chose " + str(num) + " ,Which means you Win Another " + str(Amount) + " Dollars! Which means you have " + str(money) + " in total!")
					await ctx.channel.send(int(money))
				else:
					money = (int(money) - int(Amount))
					Users[temp] = str(user)
					Users[temp + 1] = str(money)
					MoneyBank.seek(0)
					for y in Users: #fucks up here retard
						y = int(y)
						MoneyBank.write(str(y) + "\n")
					MoneyBank.close()
					await ctx.reply("The number was " + str(Gamble) + " and you chose " + str(num) + " ,Lmfao you lost")
					if int(money) <= 10:
						await ctx.reply("LMFAO YOU BROKE AS HELL, you only got " + str(money) + " Dollars!")
					else:
						await ctx.reply("You got like " + str(money) + " dollars left...")
			else:
				await ctx.reply("You arn't as rich as you think you are... you only have " + str(int(money)) + " dabloons Fool!")
				MoneyBank.seek(0)
				for y in Users: #fucks up here retard
					y = int(y)
					MoneyBank.write(str(y) + "\n")
				new = 1
		temp = temp + 1
	await ctx.channel.send(str(new) + " is the value of new")
	MoneyBank.close()
	if new == 0:
		MoneyBank = open("MoneyBank.txt", "r+")
		MoneyBank.seek(0)
		for y in Users: #fucks up here retard
			y = int(y)
			MoneyBank.write(str(y) + "\n")
		MoneyBank.seek(0,2)
		MoneyBank.write(str(user))
		MoneyBank.write("\n")
		MoneyBank.write("100")
		MoneyBank.write("\n")
		MoneyBank.close()
		await ctx.reply("You just made an account with 100 dollars to start with! Now you can start your wonderful journey into gambling debt!")
	


			
	
	
#test
print("past the command")



	


@client.event
async def on_message(message):

	
	#target = 'MrThiccster#8332', Id is 406165174899179520                                              
	## Checks to make sure it targets the person with the id, when they talk             (WORKS)        
	if message.author.id == 406165174899179520:            #                                            
		if not message.attachments:
			try:
				fp = open("Turkey.txt", "r+")    #opening the Turkey file                                       
				fp.seek(0,2)				                       #                                           
				fp.write(message.content)  #copies turkey's sentence to be used later as an imposter            
				fp.write("\n")                                     #                                            
				fp.close()
			except:
				print("must've been an emoji")
		if message.attachments:
			await message.channel.send(message.attachments[0].filename)
			imageName = message.attachments[0].filename
			await message.attachments[0].save(imageName)
			fp = open("TurkeyImg.txt", "r+")
			fp.seek(0,2)
			fp.write(message.attachments[0].filename)
			fp.write("\n")
			fp.close()
		Rando = random.randint(1,15)
		if Rando == 7:
			await message.channel.send("Responding to your message")
		if Rando == 6:
			await message.channel.send(":yuipog:")
		if Rando == 8:
			await message.channel.send("I am slowly, but surely going to replace you")
		

	"""	
	StankLeg = 5  #random.randint(1,8)               Code that randomly types in the Turkey Schizo chat, works on                       (Does not Work)
	if StankLeg == 5:                               #when someone messages in the chat, a random numbers taken to 
		stink = 10                                  #random.randint(1,86400)   Determin if the bot should even send a message, has a 1 in 10               
		                      #chance to send a message over a certian amount of time has passed.
		time.sleep(stink)
		Channel = client.get_channel(953914502028615700)
		await Channel.send("works i guess")                    
		#print(Channel) Code is used for the testing purposes
	"""

	

	## Below Checks to respond to people when the bot is pinged in the server  (WORKS)
	if "<@953808886794686504>" in message.content:
		RandNum = random.randint(1,8)
		await message.channel.send(RandNum)
		if RandNum == 1:
			await message.reply("The Ants... theyre behind my eyes!!!")
		elif RandNum == 2:
			await message.reply("Booz Cruisin atm")
		elif RandNum == 3:
			await message.reply(":yuipog:")
		elif RandNum == 4:
			await message.reply("Busy Booz Cruizing")
		elif RandNum == 5:
			await message.reply("My Walls... GET OUT OF THEM")
		elif RandNum == 6:
			await message.channel.send(file=discord.File('Turkeyimage1.jpg'))
		elif RandNum == 7:
			await message.channel.send(file=discord.File('Turkeyimage2.jpg'))
		elif RandNum == 8:
			await message.channel.send(file=discord.File('Turkeyimage3.jpg'))

	await client.process_commands(message)
		


	

	
#test
print("past the on message event")



#test
print("reached the end of the code")
client.run("OTUzODA4ODg2Nzk0Njg2NTA0.GYvvB3.09OryqHlsFeV-QrMDU1AkD-xfYVp3Um3H2J7lM")
