'''

Code for Curse of Strahd Adventure 
By Ethan Penney

'''

#Brings the clear the screen thing
import os
os.system('clear')

#I am 90% sure the game functions perfectly. 

def start_game(): 
#creates variables 
	global hole
	global name
	global has_holy
	global has_sword
	global doll_house
	global bolt
	global has_kit
	global w_ismark
	global gold
	global p1
	global has_cross
	global hated
	global key
	global armor 
	global wolf
	wolf = True
	hole = False
	doll_house = False
	armor = True
	hated = False
	has_holy = False
	has_sword = False
	bolt = 0
	has_kit = False
	w_ismark = False
	has_cross = False
	key = False
	gold = False
#Starts game 
	os.system('clear')
	name = str(input('''
	What is your name? '''))
	os.system('clear')
	print('''
	 _____                              __   _____ _             _         _ 
	/  __ \                            / _| /  ___| |           | |       | |
	| /  \/_   _ _ __ ___  ___    ___ | |_  \ `--.| |_ _ __ __ _| |__   __| |
	| |   | | | | '__/ __|/ _ \  / _ \|  _|  `--. \ __| '__/ _` | '_ \ / _` |
	| \__/\ |_| | |  \__ \  __/ | (_) | |   /\__/ / |_| | | (_| | | | | (_| |
	 \____/\__,_|_|  |___/\___|  \___/|_|   \____/ \__|_|  \__,_|_| |_|\__,_|
																			 
				  
		
	------------------------------------------------------
	
	Welcome to Curse of Strahd, ''' + (name) + '''!
	When reading the story, note that your options will be (m)arked 
	with brackets.
	If you'd like to quit at any time, just enter an incorrect response,
	then selct quit.
	Good luck defeating the devil Strahd!
	
	------------------------------------------------------
	
	You are sitting at a noisy, foul smelling tavern when
	a man dressed in colorful clothing slams the tavern door open. 
	He drops a letter on the table that you're sitting at.
	He exclaims with an accent to no one person: 
	'Take the west road from here some five hours march down through 
	the Svalich Woods. There you will find my master in Barovia' 
	He hurries out, and rides away on a horse, not waiting for a response.
	
	------------------------------------------------------
	
	''')
	leave_the_tavern()
def game_over():
	global name
	global p1 
	print ('''
	
	------------------------------------------------------
	
	You have succumbed to the lands of Barovia. That's unfortunate!
	
	------------------------------------------------------
	
	''')
	p1 = str(input('''
	Would you like to play again? (y)es or (n)o  '''))
	os.system('clear')
	if p1 == "y":
		os.system('clear') 
		start_game()
	elif p1 == "n":
		print(''' 
		
	------------------------------------------------------
		
	Thank you for playing, ''' + (name) + '''!
		
	------------------------------------------------------
		
		''')
		quit()
	else:
		os.system('clear')
		print ('''
				
	------------------------------------------------------
		
	Invalid response
				
	------------------------------------------------------
		
		''')
		game_over()
def leave_the_tavern():
	global p1
	p1 = str(input('''
	Would you like to (i)gnore the letter or (r)ead it? '''))
	os.system('clear') 
	if p1 == "i":
		print('''
	
	------------------------------------------------------
	
	You toss the letter away, where it is hurridly swept up by a worker. 
	As you finish your food and head to your room, all is normal. The 
	night is warm, and you sleep well. How boring, Game over!
	
	------------------------------------------------------
	
		''')
		game_over()
	elif p1 == "r":
		print('''
	
	------------------------------------------------------
	
	You read the old, rain warped parchment that details the Burgomaster
	of a town called Barovia asking for help. The letter claims that the 
	love of his life has fallen to illness and despair. The information 
	matches what the strange man said. You leave the tavern and follow the
	directions given by the man. A thick fog hangs over the night, and you 
	soon lose your way in a forest with dark wooded trees with a canopy of 
	leaves that almost entirely block out the moonlight. Out of the fog emerges
	a large black iron gate, with two haunting gargoyles flanking it. It's at 
	this moment that you realize you forgot your bag.
	
	------------------------------------------------------
	
		''')
		turn_back()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				leave_the_tavern()
			elif p1 == "q":
				quit()	
def turn_back():
	p1 = str(input('''
	Do you turn (b)ack, or stay on (p)ath? '''))
	os.system('clear')
	if p1 == "b":
		print ('''
		
	------------------------------------------------------
	
	You decide to go back for your bag. The fog surrounds you, and limits 
	your visibility, to the point where you can't see your own hand. You're 
	unable to follow the path, and panic starts to creep up on you when you 
	slowly realize you're lost. The air becomes thin, and your breathing becomes 
	labored as the fog chokes you, and you begin to become weary. Your eyes 
	droop and you start to see black spots. You collapse to the ground. 
	You are dead. 
	Game over!
	
	------------------------------------------------------
	
	''')
		game_over()
	elif p1 == "p":
		print ('''
	
	------------------------------------------------------
	
	You decide that you've gone too far now, and head towards the gates. As 
	you approach, the gates open on their own, letting out a ghastly screech, 
	as if in pain. The fog swirls into the opening as you walk through. After 
	walking for a couple hours, you spot a village emitting warm light into 
	the fog that swirls and claws at the stone walls surrounding it. As you enter
	the town, you see several things. One path leads to a building with a sign reading
	'Bildraths Mercantile', clearly a shop. Another path leads to a three story 
	house with peeling paint and cracked windows. Outside the house there are two 
	children, one is crying. Near the entrance to the town is an inn from which 
	you hear laughter and music. Finaly, there is a path straight through town, 
	into the woods. 
	
	------------------------------------------------------
	
		''')
		town_square()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				turn_back()
			elif p1 == "q":
				quit()
def town_square(): 
	p1 = str(input('''
	Would you like to go to the (s)hop, the (i)nn, the (h)ouse, or (l)eave town?
	 '''))
	if p1 == "s":
		shop()
	elif p1 == "i":
		inn()
	elif p1 == "h":
		death_house()
	elif p1 == "l":
		leave_town()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit		
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				town_square()
			elif p1 == "q":
				quit()
def shop():
	os.system('clear')
	global bolt
	global has_holy
	global has_kit
	global has_sword
	global gold
	if gold == True:
		print ('''
	
	------------------------------------------------------
	
	You enter an incredibly... humble shop. Inside, a large man sits 
	behind a counter. In a drab, almost sad voice he presents you with
	the contents of his shop. There are only four items in stock, each 
	for ten gold pieces. Checking your pockets, you realise you only have 
	twenty gold pieces. That means two items max! In the shop you can find:
	
	- climbers (k)it
	- (h)oly Water
	- (s)ilvered Sword
	- (c)rossbow Bolt
	
	------------------------------------------------------
	
		''')
		p1 = input('''
	What's the first item you would like to buy? 
	
	------------------------------------------------------
	
	''')
	
		if p1 == "h":
			has_holy = True
		elif p1 == "s":
			has_sword = True
		elif p1 == "c":
			bolt = bolt + 1
		elif p1 == "k":
			has_kit = True
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
				if p1 == "t":
					shop()
				elif p1 == "q":
					quit()
		p1 = input('''
	
	------------------------------------------------------
		
	What's the second item you would like to buy?

	------------------------------------------------------
	
	''')
		if p1 == "h" and has_holy != True:
			has_holy = True
		elif p1 == "s" and has_sword != True:
			has_sword = True
		elif p1 == "c":
			bolt = bolt + 1
		elif p1 == "k" and has_kit != True:
			has_kit = True
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
				if p1 == "t":
					shop()
				elif p1 == "q":
					quit()
		gold = False
		os.system('clear')
		town_square()
	elif gold == False:
		print ('''
		
	------------------------------------------------------
	
	You haven't got any money to spend! Such is life. 
		
	------------------------------------------------------
		''')
		town_square()
def inn():
	os.system('clear')
	if w_ismark == False and hated == False:
		print ('''
	
	------------------------------------------------------
	
	You aproach an inviting inn that spills warm light into the grey world. 
	As you get closer you hear the singing of drunkards and the crackle of a fire. 
	Inside the inn, there's several groups of people sitting together. One man sits 
	alone, but calls you over as you enter. He introduces himself as Ismark the Lesser,
	son of the Burgomaster. His father ruled the village, just three days ago. An ill 
	fate has befallen him though. Their village has been assailed by monsters of the night, 
	and he seeks help from an adventurer. Ismark invites you to join him in his late fathers 
	mansion, where he can give you more details. 
	
	------------------------------------------------------
		''')
		p1 = input('''
	Do you (f)ollow Ismark, (a)ttack him or (l)eave him in the Tavern to figure it out himself? ''')
		if p1 == "l":
			os.system('clear')
			town_square()
		elif p1 == "f":
			os.system('clear')
			mansion()
		elif p1 == "a":
			os.system('clear')
			print ('''
		
	------------------------------------------------------
	
	You grab a nearby knife and plunge it into Ismark the Lessers neck. 
	Blood gushes around you, and the inn goes silent, but only for a 
	moment. All patrons, bellow in rage and mob you with knives and torches. 
	You don't stand to chance, as you're outnumberd ten to one. They drag you 
	to the town square and hang you by the neck, Ismarks blood still wet 
	on your clothes, you monster. 
	You're dead.
	
	------------------------------------------------------
	
	''')
			game_over()
		else:
			os.system('clear')
			p1 = "a"
			while p1 != "t" and p1 != "q":
				p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
				if p1 == "t":
					inn()
				elif p1 == "q":
					quit()	
	elif w_ismark == True:
		print (''' 
		
	------------------------------------------------------

		You enter a tavern with men sitting at tables and a fire blazing.
		There's no time to waste in the Tavern though, there's more important 
		things to do.
		
	------------------------------------------------------
	
		''')
		town_square()
	elif hated == True:
		print ('''
		
	------------------------------------------------------

	You enter the tavern, but it's empty. Glasses left on the table and fire
	still blazing. Everyones left. Nothing left to do here. 
	
	------------------------------------------------------

	''')
		town_square()
def mansion():
	global p1
	global bolt
	global has_cross
	print ('''
	
	------------------------------------------------------
	
	Ismark leads you to a mansion with boarded up windows and dead shrubs 
	all around. This home has clearly been under seige for weeks by unnatural
	forces, made clear by the damaged walls. Inside, Ismark 
	introduces you to his Sister, Ireena. On the floor of the house is a man 
	in his thirties, lying dead. Their father. 
	The two explain that Ireena is sought after by a powerful vampire named Strahd. 
	He sent his minions to attack the house nightly, up until her father died. 
	Strahd has entered the home and bitten Ireena twice before. They seek help 
	in bringing Ireena to a distant village named Vallaki that is safer.
	First, Ireena insists that you help them give their father a proper 
	burial at the church. All the other villagers fear Ireena because of 
	Strahds obsession, so they won't help.   
	
	------------------------------------------------------
	
		''')
	p1 = input('''
	Would you like to (h)elp bring their father to the church, (a)ttack Ireena out of fear, or
	(l)eave the two of them be?
		''')
	if p1 == "h":
		os.system('clear')
		church()
	elif p1 == "a":
		os.system('clear')
		if has_cross and bolt > 0:
			print ('''

	------------------------------------------------------
	
	"The girl's been bitten, she must be a vampire!" You exclaim.  
	You fire a crossbow bolt into Ireena's chest. She falls instantly. 
	Ismark draws his blade and attacks you, roaring with rage at the loss
	of his sister. Just barely, you block his attack with the wood on the 
	crossbow. You fire three shots to bring him down. The two of them fall 
	to the ground, reuinited with their father, in some sort of twisted 
	poetic fate. As you exit the house, rain begins to fall, washing some of 
	the blood off of you. The rain quickly becomes a downpour, followed by lightning. 
	Lots of lightning.
	Storm clouds swell and thunder begins to boom constantly. Close behind you, lightning 
	strikes a rooftop. This isn't natural. suddenly, bats swarm around you, biting 
	and screeching. You're overwhelmed, helpless. With a crash of lighting, they scatter. 
	Crouching on a rooftop adjacent to you, you see a human figure, outlined by the moon. 
	The only feature you can discern are eyes literally glowing red with rage. Before you
	can think, Strahd van Varkovoch leaps towards you, biting down on your neck as quick 
	you've ever seen. Life leaves your body swiftly. You are dead. 
	
	------------------------------------------------------
	
			''')
			game_over()
		elif has_cross == False or bolt < 1:
			print ('''
	
	------------------------------------------------------
	
	You attempt to attack the girl, sure that she's a vampire. Ismark cuts you down 
	with his sword with ease. He was prepared for the actions of this strange 
	man he brought into his house it would seem. You are dead. 
	
	------------------------------------------------------
	
	''')
			game_over()
	elif p1 == "l":
		os.system('clear')
		print ('''
	
	------------------------------------------------------
	
	You decide that this has all gotten a bit too strange. It's time to leave. 
	You exit the home as the two siblings look to the ground, having lost all 
	hope. There's a lingering feeling of guilt, but keep your chin up, champ!
	If you change your mind, he's probably still at the inn. 
	
	------------------------------------------------------
	
	''')
		town_square()
		w_ismark = False
	else:
		os.system('clear')
		p1 = "a"
		while p1 != "t" and p1 != "q":
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				mansion()
			elif p1 == "q":
				quit()
def church():
	global p1 
	global w_ismark
	print ('''
	
	------------------------------------------------------
	
	You assist in carrying a makeshift coffin to the towns church, just
	out of town. The church is decrepid and empty, all except for one man 
	kneeling by the altar. As you enter, you start to notice all the pews
	have been smashed and thrown about. The church is silent except for 
	the mans prayers until a gut wrenching scream from the basement breaks 
	the silence. 
	"FATHER FEED ME"
	
	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you go to the (b)asement, or (i)gnore the screams and get on with the 
	funeral?
	''')
	os.system('clear')
	if p1 == "b":
		basement()
	elif p1 == "i":
		print ('''
			
	------------------------------------------------------
	
	The preist helps you bury their father properly, and says nothing about the 
	screams. As soon as the funeral is done, you all leave, clearly unnerved by 
	the location. Ismark agrees to travel with you from now on, while Ireena waits
	by the town gate for you all to depart. 
	You have friends!
		
	------------------------------------------------------
	
	''')
		w_ismark = True 
		town_square()
	else:
		os.system('clear')
		p1 = "a"
		while p1 != "t" and p1 != "q":
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				church()
			elif p1 == "q":
				quit()
def basement():
	global p1
	global bolt
	global has_cross
	global w_ismark
	global hated
	if has_cross == True and bolt > 0:
		print (''' 
			
	------------------------------------------------------
	
	You enter a cold damp basement through a trapdoor. The basement is 
	dimly lit by a single torch, but you see a young man in rags kneeling 
	in the corner. He says nothing, but looks up at you, revealing blood 
	shot eyes and glistening fangs.
	
	------------------------------------------------------
	
	''')
		p1 = input('''
	Do you (a)ttack the boy with your crossbow, or try to (g)o closer?  
	
	''')
		if p1 == "a":
			os.system('clear')
			print ('''
				
	------------------------------------------------------
	
	You shoot the boy, and he collapses to the ground. The torch flickers and 
	the prayers of the man upstairs stop. Soon after he furiously storms down 
	forces you to leave the church, locking the door behind you. Ireena and 
	Ismark leave you alone in the town square, as you've ruined their chances
	of a proper burial. It seems you've lost some potential friends, and you're 
	down a crossbow bolt. 
	
	------------------------------------------------------
	
	''')
			bolts = bolt - 1
			w_ismark = False
			hated = True
			town_square()
		elif p1 == "g":
			os.system('clear')
			print ('''
	
	------------------------------------------------------
	
	You gently step closer to the boy, lowering your crossbow. He looks up at you 
	and recoils slightly, still not saying anything. You pause, then take another 
	step towards him. As you step, a rock is kicked accidentally, rolling across the 
	floor, echoing. The young man lunges and bites at you, clamping down on your 
	neck. You are dead.
	
	------------------------------------------------------
	
	''')
			os.system('clear')
			game_over
		else:
			os.system('clear')
			p1 == "a"
			while p1 != "t" and p1 != "q":
				p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
				if p1 == "t":
					basement()
				elif p1 == "q":
					quit()
	elif bolt < 1 or has_cross == False:
		os.system('clear')
		print (''' 
			
	------------------------------------------------------
	
	You enter a cold damp basement through a trapdoor. The basement is 
	dimly lit by a single torch, but you see a young man in rags kneeling 
	in the corner. He says nothing, but looks up at you, revealing blood 
	shot eyes and glistening fangs.
	
	------------------------------------------------------
	
	''')
		p1 = input('''
	Do you (a)ttack the boy with your fists, or try to (g)o closer?  
	
	''')
		if p1 == "a" or p1 == "g":
			os.system('clear')
			print ('''
				
	------------------------------------------------------
	
	You gently step closer to the boy, lowering your crossbow. He looks up at you 
	and recoils slightly, still not saying anything. You pause, then take another 
	step towards him. As you step, a rock is kicked accidentally, rolling across the 
	floor, echoing. The young man lunges and bites at you, clamping down on your 
	neck. You are dead.
		
	------------------------------------------------------
				
	''')
			game_over()
		else:
			os.system('clear')
			p1 = "a"
		while p1 != "t" and p1 != "q":
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				basement()
			elif p1 == "q":
				quit()
def death_house():
	global p1 
	os.system('clear')
	print ('''
		
	------------------------------------------------------
	
	You decide to help the two children by the house. As you approach,
	one sushes the other and yells at you "Theres a monster in our house!"
		
	------------------------------------------------------
	
	''')
	
	p1 = input('''
	Do you (e)nter the house, or (l)eave the children?
	
	''')
	if p1 == "e":
		os.system('clear')
		lobby()
	elif p1 == "l":
		os.system('clear')
		town_square()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				death_house()
			elif p1 == "q":
				quit()
def lobby():
	os.system('clear')
	global p1 
	print ('''
			
	------------------------------------------------------
	
	You enter the decrepid house's well cared for lobby. 
	There's three options as you start to explore. There's a spiral 
	staircase with a red carpet, leading to the next floor, an open 
	door leading to a den with hunting trophies, and a curtain hanging 
	over a doorway. 
		
	------------------------------------------------------
	
		''')
	p1 = input('''
	Do you go (u)pstairs, to the (d)en, through the (c)urtain?, or (l)eave? 
	''')
	if p1 == "u":
		floor_2()
	elif p1 == "d":
		den()
	elif p1 == "c":
		kitchen()
	elif p1 == "l":
		os.system('clear')
		town_square()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				lobby()
			elif p1 == "q":
				quit()
def den():
	global p1 
	global has_cross
	global bolt
	os.system('clear')
	if has_cross == False:
		print ('''
	
	------------------------------------------------------
	
	You enter the den, and are met with the snarling face of a grizzly 
	bear! The stuffed bear looms in the corner of the den. The room has 
	red chairs and a stone cold fireplace filled with ashes. Against the 
	wall of the room is a cabinet, with the door hanging open. Inside you 
	see a crossbow with one bolt! 
	
	------------------------------------------------------
	
	''')
		p1 = input('''
	Do you (t)ake the crossbow or (l)eave the room? 
	''')
		if p1 == "t": 
			has_cross = True
			bolt = bolt + 1
			lobby()
		elif p1 == "l": 
			os.system('clear')
			lobby()
		else:
			p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				den()
			elif p1 == "q":
				quit()
	elif has_cross == True:
		print ('''
		
	------------------------------------------------------

	You enter the den. You've been here before, and nothing has 
	changed. Very cool.
	
	------------------------------------------------------

	''')
		p1 = input('''
	Do you (l)eave the room?
	''')
		if p1 == "l":
			lobby()
		else:
				p1 = "a"
				while p1 != "t" and p1 != "q":
					os.system('clear')
					p1 = (input('''
						
	------------------------------------------------------
				
	Invalid response
	(t)ry again or (q)uit 			
			
	------------------------------------------------------

			'''))
					if p1 == "t":
						den()
					elif p1 == "q":
						quit()
def kitchen():
	global p1 
	os.system('clear')
	print ('''
	
	------------------------------------------------------

	You enter the kitchen, with rotted food and tarnished cooking 
	tools. Against the wall is a dumb waiter, with a small bell 
	attatched to a string. Seems like someobdy could fit in it if 
	they squeezed...
	
	------------------------------------------------------

	''')
	p1 = input('''
	Do you want to try to climb into the (d)umbwaiter, or (l)eave? 
	''')
	if p1 == "d":
		dumbwaiter()
	elif p1 == "l":
		lobby()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				kitchen()
			elif p1 == "q":
				quit()
def dumbwaiter():
	os.system('clear')
	print ('''
	
	------------------------------------------------------

	You enter the dumbwaiter, with very little space to move.
	You pull the rope, lifting the box through the house.
	
	------------------------------------------------------

	''')
	p1 = input(''' 
	Do you get out at the (f)irst, (s)econd, or (t)hird floor?
	''')
	if p1 == "s":
		quarters()
	elif p1 == "t":
		bedroom()
	if p1 == "f":
		kitchen()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				dumbwaiter()
			elif p1 == "q":
				quit()
def floor_2():
	os.system('clear')
	print ('''
	
	------------------------------------------------------

	You walk into the second floor, and are met by a long hallway with two doors,
	perpendicular to a large spiral staircase. One door leads to a library, 
	the other leads to a large room with many beds, clearly a servants quarters. 
	
	------------------------------------------------------

	''')
	p1 = input('''
	Would you like to go to the (l)ibrary the (s)ervents quarters, go 
	(d)ownstairs, or do you continue (u)pstairs?
	''')
	if p1 == "l":
		os.system('clear')
		library()
	elif p1 == "s":
		os.system('clear')
		quarters()
	elif p1 == "u":
		os.system('clear')
		floor_3()
	elif p1 == "d":
		os.system('clear')
		lobby()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				floor_2()
			elif p1 == "q":
				quit()
def quarters():
	os.system('clear')
	global p1
	print ('''
	
	------------------------------------------------------

	You enter a room lined with cheap straw stuffed beds. Each
	bed has a footlocker with a folded servants uniform. The room 
	contains a dumbwaiter opposite the door. 
	
	------------------------------------------------------

	''')
	p1 = input(''' 
	Do you (l)eave the room, or enter the (d)umbwaiter? 
	''')
	if p1 == "l":
		floor_2()
	elif p1 == "d":
		dumbwaiter()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				quarters()
			elif p1 == "q":
				quit()	
def library():
	global p1 
	global key 
	os.system('clear')
	print ('''
	
	------------------------------------------------------
	
	You enter a well furnished library with stacks of books everywhere. 
	There's two large shelves lined with books, and a comfortable reading 
	chair sitting next to a wooden desk.
	
	------------------------------------------------------

	''')
	p1 = input('''
	Do you (r)ead a book, investigate the (d)esk or (l)eave the room?
	''')
	if p1 == "r":
		os.system('clear')
		secret_room()
	elif p1 == "d":
		os.system('clear')
		if key == False:
			print ('''
			
	------------------------------------------------------
		
	You search the desk drawers, finding several useless writing tools,
	and a silver key tucked under some papers. Good job, you got a key!
		
	------------------------------------------------------

			''')
			key = True 
			p1 = input('''
	Do you (l)eave the library or (k)eep investigating? 
		''')
			if p1 == "l":
				floor_2()
			elif p1 == "k":
				library()
			else:
				p1 = "a"
				while p1 != "t" and p1 != "q":
					os.system('clear')
					p1 = (input('''
						
	------------------------------------------------------
				
	Invalid response
	(t)ry again or (q)uit 			
			
	------------------------------------------------------

			'''))
					if p1 == "t":
						library()
					elif p1 == "q":
						quit()
		elif key == True:
			print ('''
			
	------------------------------------------------------
		
	You search the desk drawers, finding several useless writing tools.
		
	------------------------------------------------------

			''')
			p1 = input('''
	Do you (l)eave the library or (k)eep investigating? 
		''')
			if p1 == "l":
				floor_2()
			elif p1 == "k":
				library()
			else:
				p1 = "a"
				while p1 != "t" and p1 != "q":
					os.system('clear')
					p1 = (input('''
						
	------------------------------------------------------
				
	Invalid response
	(t)ry again or (q)uit 			
			
	------------------------------------------------------

			'''))
					if p1 == "t":
						library()
					elif p1 == "q":
						quit()
			library()
	elif p1 == "l":
		os.system('clear')
		floor_2()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				library()
			elif p1 == "q":
				quit()
def secret_room():
	global gold
	os.system('clear')
	if gold == True:
		print ('''
		
	------------------------------------------------------
	
	The secret room offers no more treasure, which makes it considerably 
	less interesting than before. 
	
	------------------------------------------------------

		''')
	elif gold == False:
		print ('''
				
	------------------------------------------------------
			
	You pull a red leather book off the shelf, triggering a 
	mechanism that slides the bookshelf to the side, revealing 
	a dusty hidden room. In the room is a small lockbox containing 
	twenty shiny gold pieces, with a nobleman's face stamped on them. 
		
	------------------------------------------------------
		
				''')
		gold = True 
	p1 = input('''
	Do you (s)tay in the room, or go back to the (l)ibrary?
	''')
	if p1 == "s":
		os.system('clear')
		secret_room()
	elif p1 == "l":
		os.system('clear')
		library()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
						
	------------------------------------------------------
				
	Invalid response
	(t)ry again or (q)uit 			
			
	------------------------------------------------------

			'''))
			if p1 == "t":
				secret_room()
			elif p1 == "q":
				quit()
def floor_3():
	global bolt
	global has_cross
	global has_sword
	global w_ismark
	global armor 
	global p1
	if armor == True:
		print ('''
			
	------------------------------------------------------
		
	You walk onto the third floor lobby. Parrallell the stairs 
	stands a suit of armor. This floor has doors leading to a 
	small nursery, the master bedroom, and the staircase leading 
	down. Suddenly, before you can choose a path, the armor comes to 
	life and attacks you!
			
	------------------------------------------------------
		
		''')
		p1 = input('''
	Do you (a)ttack it, or (r)un away?
		''')
		os.system('clear')
		if p1 == "a":
			if has_cross == True and bolt > 0:
				print ('''
					
	------------------------------------------------------
		
	You shoot your crossbow into the center piece of the 
	armor. It's unnatural jerky movements stop, and it clatters 
	to the ground. 
		
	------------------------------------------------------
		
		''')
				armor = False
				bolt = bolt - 1
				floor_3()
			elif has_sword == True:
				print ('''
					
	------------------------------------------------------
		
	You swing your mighty silvered sword at the armor, cutting
	it down and sending pieces of metal everywhere! Unfortunately 
	the weapon was very fragile, and shatters on impact.
		
	------------------------------------------------------
		
		''')
				has_sword = False
				armor = False
				floor_3()
			elif w_ismark == True:
				print ('''
				
	------------------------------------------------------
	
	You ready your weapon, but before you can attack, Ismark comes
	in and cuts the monster down with a longsword. He gives you a 
	smirk and continues on. 
	
	------------------------------------------------------
	
	''')
				armor = False
				floor_3()
			else: 
				print ('''
				
	------------------------------------------------------
	
	The armor stumbles towards you, and you punch it right in the 
	center piece. The bones in your hand break as they meet metal, 
	and you're cut down by the magically sentient armor. You rot away 
	in this forsaken house forever. You are dead!
	
	------------------------------------------------------
	
	''')
				game_over()
		elif p1 == "r":
			floor_2()
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				os.system('clear')
				p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
				if p1 == "t":
					floor_3()
				elif p1 == "q":
					quit()
		
	elif armor == False:
		p1 = input('''
	Would you like to go to the (n)ursery, the (b)edroom, or back
	(d)ownstairs? 
	''')
		if p1 == "n":
			os.system('clear')
			nursery()
		elif p1 == "b":
			os.system('clear')
			bedroom()
		elif p1 == "d":
			os.system('clear')
			floor_2()
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				os.system('clear')
				p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
				if p1 == "t":
					floor_3()
				elif p1 == "q":
					quit()
def nursery():
	os.system('clear')
	print ('''
				
	------------------------------------------------------
	
	You enter the nursery, and see a swaddled bundle of blankets;
	a baby lying alone in the crib. Also on the wall, there is the 
	outline of a secret door that's wallpaper hiding place has 
	rotted away.
	
	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you (l)eave the room, (h)elp the baby, or go through the 
	(s)ecret door?
	''')
	if p1 == "l":
		os.system('clear')
		floor_3()
	elif p1 == "h":
		print ('''
	------------------------------------------------------
	
	You pick up the baby, only to have the cloth collapse in 
	your hand. Behind you, a chilly wind picks up. You turn to 
	see a floating woman with sunken eyes and a broken jaw. She
	extends her hand, and your lifeforce is drained, reducing you 
	to a shriveled, dryed out husk. You are dead!
	
	------------------------------------------------------
	
	''')
		game_over()
	elif p1 == "s":
		os.system('clear')
		attic()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				nursery()
			elif p1 == "q":
				quit()
def bedroom():
	os.system('clear')
	print ('''
	
	------------------------------------------------------
	
	This poorly mantained master suite has faded red cloth lining the 
	windows and four poster bed. Against the wall opposite the door 
	is a dumbwaiter. 
	
	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you enter the (d)umbwaiter or (l)eave the room? 
	''')
	if p1 == "d":
		os.system('clear')
		dumbwaiter()
	elif p1 == "l":
		os.system('clear')
		floor_3()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				bedroom()
			elif p1 == "q":
				quit()
def attic():
	print ('''
	
	------------------------------------------------------
	
	you enter a dust choked hallway with two doors. One has a 
	silver lock on the door. The other leads to a storage room. 
	
	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you want to go to the (l)ocked room, the (s)torage room, 
	or back (d)ownstairs?
	''')
	os.system('clear')
	if p1 == "l":
		if key == True:
			os.system('clear')
			kids_room()
		elif key == False:
			print ('''
			
	------------------------------------------------------
	
	You try the door, but the lock holds tight. Maybe there's
	a key somewhere in the house...
	
	''')
			attic()
	elif p1 == "s":
	    storage()
	elif p1 == "d":
		os.system('clear')
		nursery()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				attic()
			elif p1 == "q":
				quit()
def kids_room():
	global doll_house
	print ('''
			
	------------------------------------------------------
	
	Inside the room, you see two children sized beds and toys everywhere. 
	There's a childs doll house in the likeness of the house you're currently 
	exploring. Most notibly though, is the two floating ghosts in the 
	center of the room that look identical to the kids who were 
	outside the house earlier. 

	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you investigate the (d)oll house, talk to the (g)hosts, or (l)eave?
	''')
	os.system('clear')
	if p1 == "d":
		os.system('clear')
		print ('''
				
	------------------------------------------------------
	
	You investigate the doll house for ten minutes, under the watchful 
	eyes of the silent ghosts. Eventually you see a doorway you hadn't 
	noticed before in the storage room.
	
	------------------------------------------------------
	
	''')
		doll_house = True
		kids_room()
	elif p1 == "g":
		print ('''
		
	------------------------------------------------------
	
	You try to strike up a conversation with the previously chatty children. 
	All you get in return is two sets of somber, hollow eyes staring back
	at you.
	
	------------------------------------------------------
	
	''')
		kids_room()
	elif p1 == "l":
		os.system('clear')
		attic()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				kids_room()
			elif p1 == "q":
				quit()
def storage():
	global doll_house
	if doll_house == False:
		print ('''
	   
	------------------------------------------------------
	
	You enter a dusty storage room packed with boxes and barrels. 
	There's furniture covered in white sheets. Suddenly, a cool wind
	blows, whipping the sheets. A pale nursemaid ghost appears, and 
	attacks you with sharp claws. You try to fight back, but your 
	weapons pass straight through the specter. You are slowly killed 
	by deep claw wounds. You are dead!
	
	------------------------------------------------------
	
	''')
		game_over()
	elif doll_house == True:
		print ('''
	
	------------------------------------------------------
	
	You enter the storage room, and notice the outline of a secret door
	on the wall. Inside the secret door is a wooden spiral staircase leading 
	down the full height of the house. 
	
	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you (e)nter the secret door, or (l)eave the room?
	''')
	if p1 == "e":
		os.system('clear')
		dungeon()
	elif p1 == "l":
		os.system('clear')
		attic()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				storage()
			elif p1 == "q":
				quit()
def dungeon():
	print ('''
			
	------------------------------------------------------
	
	As you reach the bottom of the staircase, you begin to hear chanting. 
	The words are difficult to distinguish, and sound as if they're coming 
	from deep in the cavern. You begin to wander through an elaborate maze 
	under the house. Clay floors show imprints of ancient footprints. 
	Through the halls you see living quarters with strange clothes and books 
	belonging to a cult. You pass through crypts with family names. Eventually you 
	come to a dining room, with two paths; left and right. 
	Footprints lead down the left path. None lead to the right.
			
	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you go (l)eft , (r)ight, or (b)ack?
	''')
	if p1 == "l":
		fork()
	elif p1 == "r":
		print ('''
			
	------------------------------------------------------
	
	You're walking through the clay hallway when suddenly the floor gives
	away below you. You fall thirty feet onto sharpened wooden spears. 
	You live, but slowly bleed out while attempting to scale the wall, with
	no real company except the distant chanting.
	You are dead!
			
	------------------------------------------------------
	
	''')
		game_over()
	elif p1 == "b":
		os.system('clear')
		storage()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
				
	------------------------------------------------------
		
	Invalid response
	(t)ry again or (q)uit 			
	
	------------------------------------------------------

	'''))
			if p1 == "t":
				dungeon()
			elif p1 == "q":
				quit()
def fork():
	p1 = input('''
			
	------------------------------------------------------
	
	You come through the passageway to find another fork. One leads 
	down a set of stairs, the other to a fine bedroom. The chanting that 
	echos through the clay halls is clearly coming from beneath 
	the staircase. 
	
	------------------------------------------------------
	
	Do you go (d)ownstairs, into the (b)edroom, or do you (r)etrace your steps?
	
	''')
	if p1 == "d":
		os.system('clear')
		trophy_room()
	elif p1 == "b":
		os.system('clear')
		leaders_room()
	elif p1 == "r":
		os.system('clear')
		dungeon()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
					
	------------------------------------------------------
			
	Invalid response
	(t)ry again or (q)uit 			
		
	------------------------------------------------------

		'''))
			if p1 == "t":
				fork()
			elif p1 == "q":
				quit()
def leaders_room():
	os.system('clear')
	print ('''
	
	------------------------------------------------------
	
	You enter the clay room, and see intricate furniture and 
	a large king size bed. The walls have a vast mural depicting 
	a great evil taking over the land. At the foot of the bed 
	is a chest, with no lock.
		
	------------------------------------------------------
	
	''')
	p1 = input('''
	Do you (o)pen the chest, or go (b)ack?
	''')
	if p1 == "o":
		print ('''
		
	------------------------------------------------------
	
	You open the chest to find an assortment of magical goods 
	and potions. Unfortunately, as you do this, two large ghouls 
	burst from the wall, and with the element of surprise, take you 
	down rather quickly. They are unnaturally strong, and you 
	are ripped apart. You are dead!
		
	------------------------------------------------------
	
	''')
		game_over()
	elif p1 == "b":
		os.system('clear')
		fork()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
					
	------------------------------------------------------
			
	Invalid response
	(t)ry again or (q)uit 			
		
	------------------------------------------------------

		'''))
			if p1 == "t":
				leaders_room()
			elif p1 == "q":
				quit()
def trophy_room():
	os.system('clear')
	print ('''
	
	------------------------------------------------------

	This room has well over twenty niches in the wall containing 
	various objects used in cultish rituals. These range from daggers 
	carved from bone to monkeys heads shrunken in a jar. From this room,
	you can hear the chanting clearly. Over a dozen voices chant 
	"He is ancient, He is the land" 
	Two halls lead from this room. One leads to a flooded chamber with chains 
	hanging from the ceiling, where the chanting is loudest. 
	The other hall leads to a chamber with several prison chambers. 
		
	------------------------------------------------------

	''')
	p1 = input('''
	Do you go to the flooded (c)hamber the (p)rison area, or (b)ack? 
	''') 
	if p1 == "c":
		os.system('clear')
		sacrifice_room()
	elif p1 == "p":
		os.system('clear')
		prison()
	elif p1 == "b":
		os.system('clear')
		fork()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
					
	------------------------------------------------------
			
	Invalid response
	(t)ry again or (q)uit 			
		
	------------------------------------------------------

		'''))
			if p1 == "t":
				trophy_room()
			elif p1 == "q":
				quit()
def prison():
	global hole
	print ('''
		
	------------------------------------------------------

	You enter a small prison area lined with cages and shackles. 
	Several skeletons hang in tattered robes in manacles against 
	the walls. One cage has a hole in it, covered by rotten wooden
	planks. 
	
	------------------------------------------------------

	''')
	p1 = input ('''
	Do you break through the boards, into the (h)ole, or (l)eave the room?
	''')
	if p1 == "h":
		os.system('clear')
		hole = True
		sacrifice_room()
	elif p1 == "l":
		os.system('clear')
		trophy_room()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
					
	------------------------------------------------------
			
	Invalid response
	(t)ry again or (q)uit 			
		
	------------------------------------------------------

		'''))
			if p1 == "t":
				prison()
			elif p1 == "q":
				quit()
def sacrifice_room():
	global w_ismark
	os.system('clear')
	print ('''
		
	------------------------------------------------------

	You step into the chamber with water two feet high, and the chanting 
	stops. For the first time since you entered the dungeon, there is silence. 
	This room is large, with pillars of marble forming a hexagon. In the center 
	is a stone table stained with blood, elevated on a platform. Over the table 
	hangs chains with hooks and spikes. As you step through the water, up onto 
	the platform with the table, thirteen hooded figures appear around you. 
	They slowly float in a circle around you, and begin to chant:
	"One must die! One must die! One must die!"
	They begin to pick up speed, and it's now that you notice a dagger on the table.
		
	------------------------------------------------------
	
	''')
	if w_ismark == True:
		p1 = input('''
	Do you sacrifice (i)smark, sacrifice (y)ourself, or (s)tep off the platform?
	''')
		os.system('clear')
		if p1 == "i":
			print ('''
		
	------------------------------------------------------
	
	Ismark stands, mouth agape in shock at what's happening. Unfortunately
	for him, he wasn't looking at the real danger. You grab him, slamming 
	him onto the table and plunge the dagger into his heart. He's shocked.
	As his blood spills into the water below, the hooded figures fade, and 
	the chant "He is ancient, He is the land" resumes. You escape the house
	with no trouble, as if the very building has decided not to harm you.
		
	------------------------------------------------------
	
	When you return to the village, Ireena is gone. Stolen away into the 
	night, never to be seen again. You leave town, only to be consumed by 
	the fog once more. Eventually, you find yourself back where you started,
	at the doorstep to a tavern by the woods. Congradulations! You've survived 
	the Curse of Strahd, and lived to tell the tale. To be fair, you did 
	some messed up stuff, but hey, nobody's still alive to hold you 
	accountable! Good job, you monster. 
		
	------------------------------------------------------
	
	''')
			p1 = input('''
	Would you like to play again? (y)es or (n)o
	''')	
			if p1 == "y":
				os.system('clear')
				start_game()
			elif p1 == "n":
				quit()
			else:
				quit()
		elif p1 == "y":
			print ('''
		
	------------------------------------------------------
	
	You grab the dagger and plunge it into your own chest. 
	Nobody really expected that one...
	You're dead!
		
	------------------------------------------------------
	
	''')
			game_over()
		elif p1 == "s":
			os.system('clear')
			fight()
		else:
			p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
					
	------------------------------------------------------
			
	Invalid response
	(t)ry again or (q)uit 			
		
	------------------------------------------------------

		'''))
			if p1 == "t":
				sacrifice_room()
			elif p1 == "q":
				quit()
	elif w_ismark == False:
		p1 = input('''
	Do you sacrifice (y)ourself or (s)tep off the platform?
	''')
		os.system('clear')
		if p1 == "y":
			print ('''
		
	------------------------------------------------------
	
	You grab the dagger and plunge it into your own chest. 
	Nobody really expected that one...
	You're dead!
		
	------------------------------------------------------
	
	''')
			game_over()
		elif p1 == "s":
			print ('''
		
	------------------------------------------------------
	
	You step off the platform, defying the cult their blood. 
	The chanting stops.
	There's a moment of silence, but then the chanting begins once more;
	"Lorgoth the Decayer, we awaken thee!"
	From the corner of the room, rises a massive mound of rotting plants
	and food. It takes a nearly human form, but is three times bigger than
	anyone you've ever seen. It slowly shambles through the murky water,
	making it's way towards you. The chant changes once again;
	"The end comes! Death be praised!"
	The end certainly seems within sight. 
		
	------------------------------------------------------
	
	''')
			fight()
		else:
			p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
					
	------------------------------------------------------
			
	Invalid response
	(t)ry again or (q)uit 			
		
	------------------------------------------------------

		'''))
			if p1 == "t":
				trophy_room()
			elif p1 == "q":
				quit()
def fight():
	global bolt
	global has_cross
	global w_ismark
	global has_sword
	global hole
	if has_cross == True and has_sword == True:
		p1 = input('''
		
	------------------------------------------------------

	The giant shambling mound of vegetation lurches forward 
	swinging large fist like limbs, as a metal gate slams shut 
	over the main entrance behind you. 
		
	------------------------------------------------------

	Do you attack with your (s)word or your (c)rossow?
	''')
	
		if p1 == "c" and bolt > 0 and w_ismark and hole == False:
			print ('''
			
	------------------------------------------------------

	You fire a bolt into the beast as Ismark the Lesser comes 
	in while it recoils, cutting off a limb with his longsword. 
	The beast cries in pain, and falls forward into the murky water. 
	The chanting fades. You go to leave, but find the exit blocked. 
	Uh oh. 
	The metal gate won't budge, and you're trapped. Eventually, 
	both you and Ismark starve. You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "c" and bolt < 1 and w_ismark:
			print ('''
			
	------------------------------------------------------

	You watch as Ismark attacks the beast with his sword, and 
	you raise your crossbow to assist him. You aim for the core 
	of the beast, and pull the trigger. 
	Nothing. 
	You watch as Ismark is pounded into the water by a large 
	plant-like fist, and as the monster turns towards you.
	It would seem that you're out of bolts.
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "c" and bolt > 0 and w_ismark == False:
			print ('''
			
	------------------------------------------------------

	You fire a bolt into the beasts center, causing it to flinch 
	backwards. This opening would have been perfect if there 
	was someone to finish the beast. Unfortunately, that's not 
	how this goes. The beast lumbers forwards, and engulfs you 
	in putrid smelling compost. 
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "c" and bolt < 1 and w_ismark == False:
			print ('''
			
	------------------------------------------------------

	You know the old saying; 
	"Count your bolts before you attack the monster alone"
	You are smashed into the water while you try to shoot 
	an empty crossbow.
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "c" and bolt > 0 and w_ismark and hole:
			print ('''
			
	------------------------------------------------------

	You fire a bolt into the beast as Ismark the Lesser comes 
	in while it recoils, cutting off a limb with his longsword. 
	The beast cries in pain, and falls forward into the murky water. 
	The chanting fades. You go to leave, exiting into the prison. 
	You make your way through the house with little trouble. You 
	go on to help Ireena and Ismark to Vallaki, where they live 
	happily forever. Great job! You've beaten the Curse of Strahd!
	
	------------------------------------------------------

	''')
			p1 = input('''
	Would you like to play again? (y)es or (n)o
	''')
			if p1 == "y":
				start_game()
			else:
				quit()
		elif p1 == "s":
			print ('''
			
	------------------------------------------------------

	You swipe at the beast with your sword, but it was expecting 
	that. The silvered shortsword refuses to come out of the beast, 
	and you are engulfed by the mound of rotting plants. 
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
	elif has_cross:
		p1 = input('''
		
	------------------------------------------------------

	The giant shambling mound of vegetation lurches forward 
	swinging large fist like limbs, as a metal gate slams shut 
	over the main entrance behind you. 
		
	------------------------------------------------------

	Do you attack with your (f)ists or your (c)rossow?
	''')
	
		if p1 == "c" and bolt > 0 and w_ismark and hole == False:
			print ('''
			
	------------------------------------------------------

	You fire a bolt into the beast as Ismark the Lesser comes 
	in while it recoils, cutting off a limb with his longsword. 
	The beast cries in pain, and falls forward into the murky water. 
	The chanting fades. You go to leave, but find the exit blocked. 
	Uh oh. 
	The metal gate won't budge, and you're trapped. Eventually, 
	both you and Ismark starve. You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "c" and bolt > 0 and w_ismark and hole:
			print ('''
			
	------------------------------------------------------

	You fire a bolt into the beast as Ismark the Lesser comes 
	in while it recoils, cutting off a limb with his longsword. 
	The beast cries in pain, and falls forward into the murky water. 
	The chanting fades. You go to leave, exiting into the prison. 
	You make your way through the house with little trouble. You 
	go on to help Ireena and Ismark to Vallaki, where they live 
	happily forever. Great job! You've beaten the Curse of Strahd!
	
	------------------------------------------------------

	''')
			p1 = input('''
	play again? (y)es or (n)o
	''')
			if p1 == "y": 
				start_game()
			else:
				quit()
		elif p1 == "c" and bolt < 1 and w_ismark:
			print ('''
			
	------------------------------------------------------

	You watch as Ismark attacks the beast with his sword, and 
	you raise your crossbow to assist him. You aim for the core 
	of the beast, and pull the trigger. 
	Nothing. 
	You watch as Ismark is pounded into the water by a large 
	plant-like fist, and as the monster turns towards you.
	It would seem that you're out of bolts.
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "c" and bolt > 0 and w_ismark == False:
			print ('''
			
	------------------------------------------------------

	You fire a bolt into the beasts center, causing it to flinch 
	backwards. This opening would have been perfect if there 
	was someone to finish the beast. Unfortunately, that's not 
	how this goes. The beast lumbers forwards, and engulfs you 
	in putrid smelling compost. 
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "c" and bolt < 1 and w_ismark == False:
			print ('''
			
	------------------------------------------------------

	You know the old saying; 
	"Count your bolts before you attack the monster alone"
	You are smashed into the water while you try to shoot 
	an empty crossbow.
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		elif p1 == "f": 
			print ('''
			
	------------------------------------------------------

	That was dumb. 
	You are dead!
	
	------------------------------------------------------

	''')
			game_over()
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				os.system('clear')
				p1 = (input('''
							
			------------------------------------------------------
					
			Invalid response
			(t)ry again or (q)uit 			
				
			------------------------------------------------------

				'''))
				if p1 == "t":
					fight()
				elif p1 == "q":
					quit()
def leave_town():
	os.system('clear')
	p1 = input('''
	
	------------------------------------------------------
	
	You walk through the foggy forest untill eventually you come to a 
	fork in the road, with two opetions. One leads up, the other winds 
	down into a valley. The fog blocks visibility for both paths.
		
	------------------------------------------------------
	
	Do you go (u)p, (d)own or back to (t)own?
	''')
	os.system('clear')
	if p1 == "d":
		camp()
	elif p1 == "u":
		trail()
	elif p1 == "t":
		os.system('clear')
		town_square()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
					
	------------------------------------------------------
			
	Invalid response
	(t)ry again or (q)uit 			
		
	------------------------------------------------------

		'''))
			if p1 == "t":
				leave_town()
			elif p1 == "q":
				quit()
def camp():
	os.system('clear')
	p1 = input('''
		
	------------------------------------------------------

	You walk downward onto a dirt path, with trees hugging it 
	tightly. Eventually you find a large camp filled with gypsies 
	singing and drinking. Further down the path is a steep cliff 
	heading thousands of feet both up and down. mist coats the  
	rock walls, making it slick with moisture. Far overhead is a 
	stone bridge. 
	
	------------------------------------------------------
	
	Do you (c)limb the cliff, or (t)urn back?
	''')
	if p1 == "c" and has_kit:
		os.system('clear')
		bridge()
	elif p1 == "c" and has_kit == False:
		os.system('clear')
		print ('''
	
	------------------------------------------------------
	
	You attempt to climb the slippery rock, and make it a good 
	ten feet up. Here, you lose your grip and fall the thousands 
	of feet into the river, where you drown. You are dead!
	
	------------------------------------------------------
	
	''')
		game_over()
	elif p1 == "t":
		os.system('clear')
		leave_town()	
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
						
		------------------------------------------------------
				
		Invalid response
		(t)ry again or (q)uit 			
			
		------------------------------------------------------

			'''))
			if p1 == "t":
				camp()
			elif p1 == "q":
				quit()
def bridge():
	os.system('clear')
	if wolf == True:
		print ('''
	
	------------------------------------------------------
	
	You use your climbers kit to scale the cliff. The pins and 
	ropes make the climb much easier. It may not have been possible 
	without the kit. You climb onto the bridge, which leads to a 
	clearing, or back to the town.
	
	------------------------------------------------------
	
	''')
	elif wolf == False:
		print ('''
	
	------------------------------------------------------
	
	You step onto the bridge and see two options. Forwards towards 
	a clearing, or back towards town. 
	
	------------------------------------------------------
	
	''')
	
	p1 = input('''
	Do you go (f)orward, or (b)ack towards town?
	''')
	if p1 == "f":
		strahd()
	elif p1 == "b":
		trail()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
						
		------------------------------------------------------
				
		Invalid response
		(t)ry again or (q)uit 			
			
		------------------------------------------------------

			'''))
			if p1 == "t":
				bridge()
			elif p1 == "q":
				quit()
def trail():
	global wolf 
	if wolf == True:
		p1 = input('''
		
	------------------------------------------------------
		
	As you walk along the forest path, a man walks out from 
	the woods. He looks you in the eyes, and snarls, revealing
	fangs. His form convulses into the form of a wearwolf!
		
	------------------------------------------------------
		
	Do you (a)ttack the wearwolf, or (r)un away?
		''')
		os.system('clear')
		if p1 == "a" and has_sword:
			os.system('clear')
			print ('''
		
	------------------------------------------------------
		
	You use your silvered sword to cut down the wearwolf. The 
	expensive steel mixed with silver cuts through the wolf as 
	if heated in a forge. The creature howls in pain, then falls 
	to the ground. 
		
	------------------------------------------------------
		
		''')
			wolf = False
			trail()
		elif p1 == "r":
			leave_town()
		elif p1 == "a":
			print ('''
		
	------------------------------------------------------
		
	Your weapons do no damage to the magical beast, and you're 
	eaten alive. Aw shucks. You are dead!
	
	------------------------------------------------------
		
	''')
			game_over()
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				os.system('clear')
				p1 = (input('''
						
	------------------------------------------------------
				
	Invalid response
	(t)ry again or (q)uit 			
			
	------------------------------------------------------

			'''))
				if p1 == "t":
					trail()
				elif p1 == "q":
					quit()
	elif wolf == False:
		p1 = input('''
	Do you head (f)orward towards the bridge, or (b)ack towards town?
	''')
		if p1 == "f":
			bridge()
		elif p1 == "b":
			leave_town()
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				os.system('clear')
				p1 = (input('''
						
		------------------------------------------------------
				
		Invalid response
		(t)ry again or (q)uit 			
			
		------------------------------------------------------

			'''))
				if p1 == "t":
					trail()
				elif p1 == "q":
					quit()
def strahd():
	global has_cross
	global bolt
	global has_holy
	global w_ismark
	global has_sword
	os.system('clear')
	p1 = input('''
	
	------------------------------------------------------
	
	You walk down the forest path, when for the first time, the 
	clouds overhead clear. They part to reveal a large, pale moon. 
	Silhouetted by the moon, is a single bat. The bat flys closer, 
	and turns into a man. 
	"It's a shame on my family name to not introduce myself to visitors. 
	Welcome to Barovia travellor, my name is Strahd van Zarokovich. "
	The strange man smiles, revealing blood stained fangs. 
	
	------------------------------------------------------
	
	Do you (a)ttack the vampire or (r)un away?
	''')
	if p1 == "a" and has_sword and has_holy and has_cross and bolt > 0 and w_ismark:
		print ('''
	
	------------------------------------------------------
	
	You attack the vampire, firing a crossbow bolt at him. The bolt 
	sinks into his chest, sprouting out the other side. You watch as 
	his skin contorts and pushes the bolt out, healing the wound over. 
	The monster lurches forward with unimaginable speed, but not fast 
	enough. As he lunges forward, you smash the bottle of holy water 
	onto his face, burning it like acid. This time it doesn't heal. 
	With this opening, Ismark lunges and slashes the vampire with his 
	longsword, leaving a deep gouge. There's an opening for you, created 
	by Ismarks attack. With a mighty cut, you behead the monster with 
	your sword. The body turns to mist, and floats off into the night. 
	Something in your gut tells you that he's not dead. That you just 
	got lucky. 
	
	------------------------------------------------------
	
	''')
		
		p1 = input('''
	Do you (l)eave the clearing?
	''')
		if p1 == "l":
			has_holy = False
			bolt = bolt - 1 
			bridge()
		else:
			p1 = "a"
			while p1 != "t" and p1 != "q":
				os.system('clear')
				p1 = (input('''
							
	------------------------------------------------------
					
	Invalid response
	(t)ry again or (q)uit 			
				
	------------------------------------------------------

				'''))
				if p1 == "t":
					strahd()
				elif p1 == "q":
					quit()
	elif p1 == "a":
		print ('''
	
	------------------------------------------------------
	
	You attempt to fight the vampire, but his speed is unmatched. 
	He strikes you with his fists, with more power than a gorilla 
	stored in his thin frame. You're sent flying. As you lay on 
	the ground, he approaches, and bites your neck. You are dead 
	for hours, until you rise as a vampire slave the next morning.
	
	------------------------------------------------------
	
	''')
		game_over()
	elif p1 == "r":
		os.system('clear')
		bridge()
	else:
		p1 = "a"
		while p1 != "t" and p1 != "q":
			os.system('clear')
			p1 = (input('''
						
		------------------------------------------------------
				
		Invalid response
		(t)ry again or (q)uit 			
			
		------------------------------------------------------

			'''))
			if p1 == "t":
				strahd()
			elif p1 == "q":
				quit()
	
start_game()