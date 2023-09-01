import numpy as np

class Attributes(object):
    def __init__(self, height, strength, agility, expertise, resistance, hp):
        self.height = height
        self.strength = strength
        self.agility = agility
        self.expertise = expertise
        self.resistance = resistance
        self.hp = hp

    def get_strength(self):
        return self.strength
        
    def get_agility(self):
        return self.agility
        
    def get_expertise(self):
        return self.expertise
        
    def get_resistance(self):
        return self.resistance 
         
    def get_hp(self):
        return self.hp

    def set_strength(self, strength):
        self.strength = strength
        
    def set_agility(self, agility):
        self.agility = agility
        
    def set_expertise(self, expertise):
        self.expertise = expertise
        
    def set_resistance(self, resistance):
        self.resistance = resistance
         
    def set_hp(self, hp):
        self.hp = hp


class Character(object):
    def __init__(self, attributes):
        self.attributes = attributes

    def get_attributes(self):
        return self.attributes
        
    def get_strength(self):
        return 100*np.tanh(0.01*self.attributes.strength)
        
    def get_agility(self):
        return np.tanh(0.01*self.attributes.agility)
        
    def get_expertise(self):
        return 0.6 * np.tanh(0.01*self.attributes.expertise)
        
    def get_resistance(self):
        return np.tanh(0.01*self.attributes.resistance)   
         
    def get_hp(self):
        return 100*np.tanh(0.01*self.attributes.hp)
    
    def get_atm(self):
        return 0.5 - np.power(3*self.attributes.height-5 ,4) + np.power(3*self.attributes.height-5 ,2) + self.attributes.height/2
        
    def get_dem(self):
        return 2 + np.power(3*self.attributes.height-5 ,4) - np.power(3*self.attributes.height-5 ,2) - self.attributes.height/2
        
    def get_attack(self):
        return (self.get_agility() + self.get_expertise()) * self.get_strength() * self.get_atm()

    def get_defense(self):
        return (self.get_resistance() + self.get_expertise()) * self.get_hp() * self.get_dem()
    
    def get_fitness(self):
        pass


class Warrior(Character):
    def get_fitness(self):
        return 0.6 * self.get_attack() + 0.4 * self.get_defense()
    

class Archer(Character):
    def get_fitness(self):
        return 0.9 * self.get_attack() + 0.1 * self.get_defense()
    

class Defender(Character):
    def get_fitness(self):
        return 0.1 * self.get_attack() + 0.9 * self.get_defense()


class Spy(Character):
    def get_fitness(self):
        return 0.8 * self.get_attack() + 0.3 * self.get_defense()


    # def __eq__(self, other):
    #     if not isinstance(other, self.__class__):
    #         return False
    #     return (self.board == other.board).all()

    # def __hash__(self):
    #     return hash(str(self.board))
    