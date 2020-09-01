print("Hello! Welcome to the DPS calculator")

name = input("First, what is your name?")

print("Okay, " + name + ", I have some questions about the damage values of your gear.")

helm_dmg = float(input("What is the damage value on your helmet?")) 

chest_dmg = float(input("Thank you. Now what is the damage value on your chestpiece?"))

pants_dmg = float(input("Perfect, and how about the damage value on your pants?"))

weapon_dmg = float(input("And finally, what is your weapon's damage value?"))

total_gear_dmg = helm_dmg + chest_dmg + pants_dmg + weapon_dmg

boss_fight_duration = float(input("How many minutes will the next boss fight last?"))

