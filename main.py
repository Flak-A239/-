#imports VvVv
import time
import array
import os

#functions
def dead() :
	time.sleep(1.2)
	print("D")
	time.sleep(1)
	print("E")
	time.sleep(1)
	print("A")
	time.sleep(1)
	print("D")

#arrays vVvV
inCar = ["flare", "screwdriver", "beef jerky", "slim jim", "heavy coat", "pen"]
search = ["check", "sitrep", "search", "søk", "look"]
affirm = ["yes", "Yes", "yeah", "Yeah", "yup", "Yup", "ja", "Ja", "j", "J", "y", "Y", "Yee", "yee", "Yuh", "yuh"]
negate = ["no", "No", "nei", "Nei", "nah", "Nah", "Nope", "nope", "n", "N", "Nah", "nah"]
idle = ["nothing", "stay", "sit", "idle", "bore", "ingenting", "bo", "ingen"]
engage = ["chase", "scream", "yell", "scare", "scare away", "pursue", "kill", "attack", "dreypa", "angrep", "drepe", "engage", "engasjere", "fight"]
inventory = ["broken cell phone", "wet shirt", "wet pants", "wet socks", "boots", "laces", "keys", "tire iron", "fleeting sense of integrity"]
traverse = ["crawl", "go", "move", "gjøre", "gjør", "far", "fara", "run"]

#story VvVv
print("\nBuild 0.1\n")

#name = input("Input Name: ")

os.system("clear")
time.sleep(1)

print("Upper case commands won't be necessary during your time in Сибирь\n")
time.sleep(2)
print("inv - List items in your inventory\nlook - Survey your surroundings\nquit - Exit game")
#time.sleep(4.5)

os.system("clear")
print("Welcome to Сибирь\n")

time.sleep(1)
print("On the way to surprise your aunt and uncle in Siberia, in February, in the rain. Your tire runs flat.\nThe car has been jacked up and the lug nuts have been taken off and set beside you on the ground.\n")

time.sleep(1.4)
print("A quiet sound resonates with you from the red dirt behind you. Upon turning around a see a raccoon staring back at you in the night...")

look = "\nMiles of flat dirtland surround you in all directions.\nVisibility is very poor.\nThe temperature is currently 12.2153C"

flareUse = False

def core() :

	global look
	global do
	global flareUse

	while do == "inv" :
		print(" ")
		print(inventory)
		do = input("\n> ")
		core()

	if (do == "quit") :
		exit()

	while do in search :
		print(look)
		do = input("\n> ")
		core()

	while do == "use" :
		print("What do you want to use?\n")
		item = input("> ")

		if flareUse == True :
			print("\nYou've already used this item\n")

		if flareUse == False :
		
			for item in "flare" :
				print("\nYou take the cap off of the flare and it ignites, illuminating your immediate surroundings\n")

				look = "\nThe flare shines for what seems like forever\nA wall of shadow marks the end of the eye can see\nThe temperature is currently 8.2433C"

				flareUse = True

				break

		do = input("> ")
		core()

time.sleep(1)
do = input("\nWhat do you want to do?\n\n> ")
core()

while do == "suicide" :
	print("\nAre you sure about that?")
	do = input("> ")

	if do in affirm :
		dead()

	if do in negate :
		print("\nGood decision bud")
	
	do = input("\n> ")
	core()

if (do in engage):
	time.sleep(0.9)
	print("\nYou run toward the raccoon, slip and break your ankle. It's profusely bleeding.\n\nThe raccoon has escaped into the night.")
	do = input("\n> ")
	core()

	while (do in traverse) :
		print("\nWhere do you wish to go?")
		do = input ("\n> ")

		if (do in ["car", "back", "safety", "up", "tilbakke"]) :
			time.sleep(1.2)
			print("\nYou crawl back towards the car.")
			do = input("\n> ")
			core()

			if (do in idle) :
				time.sleep(1.2)
				print("\nYou lay inside of the car listening to the rain hit the top of the car...")
				time.sleep(4.2)
				os.system("clear")
				time.sleep(4)
				print("You jump out of the back seat and hit your head on the roof of the vehicle.\n")
				time.sleep(1.2)
				print("\nYou notice the car is almost completely flooded with rain water.\n")
				time.sleep(0.9)
				print("Amidst the adrenaline, you've exauhsted yourself flailing around in the rain-water flooded car-cup of death.\n")
				time.sleep(0.8)
				print("But the car being in a ditch; was quickly submersed")

	while (do in engage) :
		print("\nAre you sure about that?\n")
		do = input("> ")

		if (do in affirm) :
			print("\nYou crawl into the darkness, drops of water assault your clothes and quaking flesh.")
			time.sleep(1.1)
			print("\nYour arms start to tremble and give out on you...")
			time.sleep(0.9)
			os.system("clear")
			time.sleep(1)
			print("You're now surrounded by darkness and hard dirt and dust.")
			time.sleep(1.2)
			print("\nOut of the corner of your vision you see something move...")
			time.sleep(0.8)
			print("\nThe raccoon from earlier has come to examine you.\n")
			time.sleep(1.8)
			print("You got the Travis Raccoon Rage ending XD\n")
			time.sleep(0.7)
			dead()
			break
			exit()

		if (do in negate) :
			print("\nGood idea\n")
			do = input("> ")
			core()

	while (do in ["heal", "treat self", "treat", "fix"]) :
		time.sleep(1)
		print("\nYou try to touch your ankle, your vision becomes dark and blurry...")
		time.sleep(1)
		print("\nContinue?")
		do = input("\n> ")
	
		if (do in negate) :
			print("\nA throbbing pressure you didn't even notice before is released.")
			do = input("\n> ")
			core()

		if (do in affirm) :
			time.sleep(0.9)
			print("\nYou can feel a heartbeat in your lower calf. Your hands are chilled to the bone but are drowning in hot liquid.\nYou can feel your fingertips swelling...\n")
			time.sleep(2.4)
			print("Your vision fades into darkness and your head starts floati-...\n")
			dead()

while (do in idle) :

	time.sleep(0.8)
	print("\nYou stand in the rain...")
	time.sleep(2.2)
	print("\nStaring at a raccoon...")
	time.sleep(2.1)
	print("\nHope you're satisfied with your life choices bud.")
	time.sleep(2)
	do = input("\n> ")
	core()

while do in traverse :
	print("Where do you want to go?")
	do = input("\n> ")
	core()
