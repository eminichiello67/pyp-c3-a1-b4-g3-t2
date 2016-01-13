import random
import time


class GameCharacterTrait():
    """
    Creates the score variable for when the fight method is called
    also creates the power variables for both you and other
    contains methods that are called at the result of the fight method
    """

    def __init__(self, power1, power2):
        self.power1 = power1
        self.power2 = power2
        self.score = 0
        
    def lose(self):
        print self.opponent.name + " Beat You! Game Over!"

    def win(self):
        print "You have defeated " + self.opponent.name

    def tie(self):
        print "You and " + self.opponent.name + " have tied!"

class FlyingTrait(GameCharacterTrait):
    #Inherited by the Characters, activated during fight method
    
    def fly1(self):
        if self.opponent.power1 == "Flying":
            pass
        if self.opponent.power1 == "Superspeed":
            self.score -= 1
        if self.opponent.power1 == "Superstrength":
            self.score += 1

    def fly2(self):
        if self.opponent.power2 == "Flying":
            pass
        if self.opponent.power2 == "Superspeed":
            self.score -= 1
        if self.opponent.power2 == "Superstrength":
            self.score += 1        
	
class SuperSpeedTrait(GameCharacterTrait):
    #Inherited by the Characters, activated during fight method
    
    def superspeed1(self):
        if self.opponent.power1 == "Superspeed":
            pass
        if self.opponent.power1 == "Flying":
            self.score += 1
        if self.opponent.power1 == "Superstrength":
            self.score -= 1
            
    def superspeed2(self):
        if self.opponent.power2 == "Superspeed":
            pass
        if self.opponent.power2 == "Flying":
            self.score += 1
        if self.opponent.power2 == "Superstrength":
            self.score -= 1
            
class SuperStrengthTrait(GameCharacterTrait):
    #Inherited by the Characters, activated during fight method
    
    def superstrength1(self):
        if self.opponent.power1 == "Superstrength":
            pass
        if self.opponent.power1 == "Superspeed":
            self.score += 1
        if self.opponent.power1 == "Flying":
            self.score -= 1

    def superstrength2(self):
        if self.opponent.power2 == "Superstrength":
            pass
        if self.opponent.power2 == "Superspeed":
            self.score += 1
        if self.opponent.power2 == "Flying":
            self.score -= 1
            
class Character(FlyingTrait, SuperSpeedTrait, SuperStrengthTrait):
    #Inherits the logic from the trait classes, has the fight method
    
    def fight1(self, opponent):
        
        self.opponent = opponent
        
        if self.power1 == "Flying":
            self.fly1()
        if self.power1 == "Superspeed":
            self.superspeed1()
        if self.power1 == "Superstrength":
            self.superstrength1()

    def fight2(self, opponent):

        self.opponent = opponent
        
        if self.power2 == "Flying":
            self.fly2()
        if self.power2 == "Superspeed":
            self.superspeed2()
        if self.power2 == "Superstrength":
            self.superstrength2()


def main():
    #Game Start

    looper = True
    
    #List of powers to choose from
    powerlist = ["Flying", "Superspeed", "Superstrength"]
    #Randomized for Other (opponent Character)
    random.shuffle(powerlist)
    
    #List of letters available for opponent Chracter name
    namelist = ["a","b","c","d","e","1","2","3"]
    #Randomizes the name for the opponent
    random.shuffle(namelist)

    print "Welcome to.....!"
    
    time.sleep(1)

    print "SUPERHERO SHOWDOWN!!!"
    print "____________________"

    time.sleep(1)

    print "Before we begin, we'd like to know some information about your superhero"

    time.sleep(2)
    
    name = raw_input("What is your superhero's name? ")

    print "\nWelcome to the showdown " + name + " its time to choose your powers!\n"
    print "Your powers can be 2 of the following: Flying, Superspeed, and Superstrength"

    time.sleep(2)
    
    pow1 = raw_input("What is " + name + "'s first power? ").title()

    while looper:
        if pow1 not in powerlist:
            print "Try again, that's not a valid power"
            pow1 = raw_input("What is " + name + "'s first power? ").title()
        else:
            looper = False

    pow2 = raw_input("What is " + name + "'s second power? ").title()

    while looper:
        if pow2 not in powerlist:
            print "Try again, that's not a valid power"
            pow2 = raw_input("What is " + name + "'s second power? ").title()
        else:
            looper = False
            
    you = Character(pow1, pow2)
    you.name = name
    
    other = Character(powerlist[0], powerlist[1])
    other.name = "".join(namelist[:3])
    
    print "Now, the moment we've all been waiting for! The fight between:\n"
    print you.name + " and " + other.name
    
    time.sleep(1)
    
    print "3"
    
    time.sleep(1)
    
    print "2"
    
    time.sleep(1)
    
    print "1"
    
    time.sleep(1)
    
    print "FIGHT!"

    time.sleep(2)
    
    you.fight1(other)
    
    time.sleep(1)
    
    you.fight2(other)

    if you.score == 0:
        you.tie()
        
    if you.score < 0:
        you.lose()
        
    if you.score > 0:
        you.win()


if __name__ == '__main__':
    main()
