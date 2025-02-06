import random
name = ""
hero_health = [100]
hero_armor = [0]
hero_weapons = ['Dagger', 'Silver Dart']
hero_damages = [20, 10]
hero_usages = [[10], [15]]
fafaro_incense = [5]
mask_health = [20]
vampire1_health = [100]
vampire1_armor = [10]
vampire1_weapons = ['Fang Spear', 'Blood Mace']  
vampire1_damages = [10, 30]

def reset():
    global name, hero_health, hero_armor, hero_weapons, hero_damages, hero_usages, fafaro_incense
    global mask_health, vampire1_health, vampire1_armor, vampire1_weapons, vampire1_damages
    name = ""
    hero_health = hero_health[:1]
    hero_armor = hero_armor[:1]
    hero_weapons = hero_weapons[:2]
    hero_damages = hero_damages[:2]
    hero_usages = [usage[:1] for usage in hero_usages]
    fafaro_incense = fafaro_incense[:1]
    mask_health = mask_health[:1]
    vampire1_health = vampire1_health[:1]
    vampire1_armor = vampire1_armor[:1]
    vampire1_weapons = vampire1_weapons[:2]
    vampire1_damages = vampire1_damages[:2]

def hero_status (health, armor):
    print (f"---------------------------------------\nYour health is {health}.\nYour armor is {armor}.\n---------------------------------------")
    input ("Press Enter to continue.")
    print("")

def vampire_status (health, armor):
    print (f"---------------------------------------\nThe vampire's health is {health}.\nThe vampire's armor is {armor}.\n---------------------------------------")
    input ("Press Enter to continue.")
    print("")

def attack (health, armor, damage):
    if armor - damage < 0:
        remaining = abs(armor - damage)
        health = health - remaining
        armor = 0
    else:
        armor = armor - damage
    if health <= 0:
        health = 0
    return health, armor

def choice ():
    while True:
        choice = input ("Type the name of the ATTACK you'd like to use: ")
        choice = choice.title()
        if choice == hero_weapons[0]:
            hero_usages[0].append(hero_usages[0][-1] - 1)
            print (f"\n{name} swings the {hero_weapons[0]} at the vampire.\nThe vampire took {hero_damages[0]} damage.")
            input ("\nPress Enter to continue.")
            return hero_weapons[0]
        elif choice == hero_weapons[1]:
            hero_usages[1].append(hero_usages[1][-1] - 1)
            print (f"\n{name} throws a {hero_weapons[1]} at the vampire.\nThe vampire took {hero_damages[1]} damage.")
            input ("\nPress Enter to continue.")
            return hero_weapons[1]

def stat_update(decision):
    if decision == hero_weapons[0]:
        health, armor = attack (vampire1_health[-1], vampire1_armor[-1], hero_damages[0])
        vampire1_health.append(health)
        vampire1_armor.append(armor)
        vampire_status(vampire1_health[-1], vampire1_armor[-1])
    elif decision == hero_weapons[1]:
        health, armor = attack (vampire1_health[-1], vampire1_armor[-1], hero_damages[1])
        vampire1_health.append(health)
        vampire1_armor.append(armor)
        vampire_status(vampire1_health[-1], vampire1_armor[-1])

def vampire_attack():
    rng = random.randint(1,2)
    if rng == 1:
        print (f"The vampire used {vampire1_weapons[0]}.\n{name} took {vampire1_damages[0]} damage.")
        input ("\nPress Enter to continue.")
        health, armor = attack (hero_health[-1], hero_armor[-1], vampire1_damages[0])
    elif rng == 2:
        print (f"The vampire used {vampire1_weapons[1]}.\n{name} took {vampire1_damages[1]} damage.")
        input ("\nPress Enter to continue.")
        health, armor = attack (hero_health[-1], hero_armor[-1], vampire1_damages[1])
    hero_health.append(health)
    hero_armor.append(armor)
    hero_status(hero_health[-1], hero_armor[-1])

def intro():
    global name
    print ("\n\n\n\n")
    print ("It's been 50 years since Zira has expanded his empire from the grand city Maruzia.\nThe vampires have taken over and it's up to the Silver Knights to stop them.")
    print ("Help Razir, a leader of the Silver Knights, defeat Zira and his vampire army.\n")
    name = input ("Please remind the Knight's Table of your name?: ")
    name = name.strip().title()
    print (f"\nCLAYMORE: That's right, {name}, I'm Claymore the blacksmith.")

def mission():
    print (f"Unfortunately, the vampires have taken our armory so I can only offer you this {hero_weapons[0]} and some {hero_weapons[1]}s. It'll have to do.")
    input ("Press Enter to receive the weapons.")
    print (f"\n---------------------------------------\nYou received a {hero_weapons[0]}\nDamage: {hero_damages[0]}\nUsage: {hero_usages[0][-1]}\n---------------------------------------")
    input ("Press Enter to continue.")
    print (f"\n---------------------------------------\nYou received a {hero_weapons[1]}\nDamage: {hero_damages[1]}\nUsage: {hero_usages[1][-1]}\n---------------------------------------")
    input ("Press Enter to continue.")
    print ("\nNow go and get our armory back from those wretched vampires!")
    while True:
        status_check = input("Type 'status' to check your health and armor: ").lower()
        if status_check == "status":
            print ("")
            hero_status (hero_health[-1], hero_armor[-1])
            break

def end_fight():
    if vampire1_health[-1] != 0:
            vampire_attack()
    else:
        print("The vampire was killed.\n")
    if hero_health[-1] == 0:
        print(f"{name} was killed. Perhaps Claymore may find you again in another light.")
        input("Press Enter to enter a new light.")
        reset()
        main()

def fight_one():
    print (f"Now {name} walks onto a dark path towards the armory.\nYou notice a vampire blocking the entrance.")
    input (f"Press Enter to view your stats and the vampires.")
    print ("")
    hero_status (hero_health[-1], hero_armor[-1])
    vampire_status (vampire1_health[-1], vampire1_armor[-1])
    input ("Press Enter to equip your weapons and select an attack.")
    while vampire1_health[-1] > 0 and hero_health[-1] > 0:
        print (f"ATTACK: {hero_weapons[0]}      | DAMAGE: {hero_damages[0]} | USAGE: {hero_usages[0][-1]}/{hero_usages[0][0]}")
        print (f"ATTACK: {hero_weapons[1]} | DAMAGE: {hero_damages[1]} | USAGE: {hero_usages[1][-1]}/{hero_usages[1][0]}")
        decision = choice()
        stat_update(decision)
        end_fight()

def heal():
    while fafaro_incense[0] > 0:
        print(f"\nYou have {fafaro_incense[0]} Fafaro Incense")
        print(f"You have {hero_health[-1]} health.\nYou have {hero_armor[-1]}.")
        while True:
            choice = input("Would you like to use a Fafaro Incense? It heals 20 health. Type 'yes' or 'no': ").lower()
            if choice == "yes":
                if hero_health[-1] == 100:
                    print("You have max health, let's not waste a Fafaro Incense!\n")
                    return
                fafaro_incense[0] -= 1
                if hero_health[-1] + mask_health[-1] <= 100:
                    new_health = mask_health[-1] + hero_health[-1]
                    hero_health.append(new_health)
                    print(f"{name} used a Fafaro Incense.\nTotal Fafaro Incense: {fafaro_incense[0]}\nUpdated health to: {hero_health[-1]}")
                    break
                else:
                    hero_health.append(100)
                    print(f"{name} used a Fafaro Incense.\nTotal Fafaro Incense: {fafaro_incense[0]}\nUpdated health to: {hero_health[-1]}")
                    break
            elif choice == "no":
                print("")
                return
   
def story1():
    print(f"CLAYMORE: {name}, I heard a racket out here! I know I sent you out here but I didn't think a spawn would be this close to the road.")
    print("Looks like you took care of it just nicely though. Not without some bruises...\n")
    input("Press Enter to continue.")
    print("\nHere take these, I was able to craft them while you were scuffling.\n")
    input("Press Enter to accept Claymore's gift.")
    print("\nYou received a Mask SP131 and 5 Fafaro Incense.\n")
    input("Press Enter to continue.")
    print("\nCLAYMORE: That mask right there is the device that every Silver Knight needs to have.")
    print("The Fafaro Incense comes from the Fafaro flower. A flower from the coast that contains healing properties that'll save your life.")
    print("You'll receive 20 health but won't exceed your 100 health.")
    print("I got to craft more for the Knights. Continue to the armory, the Knights depend on it!\n")
    input("Press Enter to continue.")
    print("\nOh one last thing I almost forgot. Crafted this with scrap metal but it'll have to do.\n")
    input("Press Enter to accept Claymore's gift.")
    print("\nYou received a Scrap Helmet. ARMOR: 10\n")
    hero_armor.append(10)
    input("Press Enter to continue.")
    print(f"\nClaymore turns around while {name} moves forward and reaches the armory.")
    heal()

def fight_two():
    print(f"{name} continues down the road until reaching the front gates of the armory.\nThere is a loose lock binding the gates.")
    print("You also notice a hidden trail behind bushes that may lead into the armory. You ponder on breaking the lock or pursuing the trail.")
    print(f"Use your {hero_weapons[0]} to break the lock? Your {hero_weapons[0]}'s USAGE will decrease by 1.\n")
    print(f"USAGE: {hero_usages[0][-1]}/{hero_usages[0][0]}")
    while True:
        choice = input("Type 'yes' or 'no': ")
        if choice == "yes":
            hero_usages[0].append(hero_usages[0][-1] - 1)
            print(f"{name} hit the lock with the {hero_weapons[0]}. USAGE: {hero_usages[0][-1]}")


def main():
    intro()
    mission()
    fight_one()
    story1()
    fight_two()

main()