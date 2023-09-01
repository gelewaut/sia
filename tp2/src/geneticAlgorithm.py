import math

POINTS = 150

def normalize(strength, agility, expertise, resistance, hp):
    points =  strength + agility + expertise + resistance + hp
    points -= POINTS
    cant = 5
    while not math.isclose(points,0):
        delta = points/cant
        if strength - delta < 0:
            points -= strength
            strength = 0
            cant -= 1
        else:
            strength -= delta
            points -= delta

        if agility - delta < 0:
            points -= agility
            agility = 0
            cant -= 1
        else:
            agility -= delta
            points -= delta

        if expertise - delta < 0:
            points -= expertise
            expertise = 0
            cant -= 1
        else:
            expertise -= delta
            points -= delta

        if resistance - delta < 0:
            points -= resistance
            resistance = 0
            cant -= 1
        else:
            resistance -= delta
            points -= delta
    
        if hp - delta < 0:
            points -= hp
            hp = 0
            cant -= 1
        else:
            hp -= delta
            points -= delta
        
    return [strength, agility, expertise, resistance, hp]