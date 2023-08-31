import numpy as np

class Attributes(object):
    def __init__(self, height, strength, agility, expertise, resistance, hp):
        self.height = height
        self.strength = strength
        self.agility = agility
        self.expertise = expertise
        self.resistance = resistance
        self.hp = hp

    def get_height(self):
        return self.height

    def get_strength(self):
        return 100*np.tanh(0.01*self.strength)
        
    def get_agility(self):
        return np.tanh(0.01*self.agility)
        
    def get_expertise(self):
        return 0.6 * np.tanh(0.01*self.expertise)
        
    def get_resistance(self):
        return np.tanh(0.01*self.resistance)   
         
    def get_hp(self):
        return 100*np.tanh(0.01*self.hp)
    
    def get_atm(self):
        return 0.5 - np.power(3*self.height-5 ,4) + np.power(3*self.height-5 ,2) + self.height/2
        
    def get_dem(self):
        return 2 + np.power(3*self.height-5 ,4) - np.power(3*self.height-5 ,2) - self.height/2
        
    def get_attack(self):
        return (self.get_agility() + self.get_expertise()) * self.get_strength() * self.get_atm()

    def get_defense(self):
        return (self.get_resistance() + self.get_expertise()) * self.get_hp() * self.get_dem()



class Warrior(object):
    def __init__(self, attributes):
        self.attributes = attributes
    def get_performance(self):
        return 0.6 * self.attributes.get_attack() + 0.4 * self.attributes.get_defense()
    def get_attributes(self):
        return self.attributes
    

class Archer(object):
    def __init__(self,attributes):
        self.attributes = attributes
    def get_performance(self):
        return 0.9 * self.attributes.get_attack() + 0.1 * self.attributes.get_defense()
    def get_attributes(self):
        return self.attributes
    

class Defender(object):
    def __init__(self, attributes):
        self.attributes = attributes
    def get_performance(self):
        return 0.1 * self.attributes.get_attack() + 0.9 * self.attributes.get_defense()
    def get_attributes(self):
        return self.attributes


class Spy(object):
    def __init__(self, attributes):
        self.attributes = attributes
    def get_performance(self):
        return 0.8 * self.attributes.get_attack() + 0.3 * self.attributes.get_defense()
    def get_attributes(self):
        return self.attributes


    # def __eq__(self, other):
    #     if not isinstance(other, self.__class__):
    #         return False
    #     return (self.board == other.board).all()

    # def __hash__(self):
    #     return hash(str(self.board))
    