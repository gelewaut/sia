import src.classes as classes
import src.geneticAlgorithm as gen
import random

def create_child(parent, attributes):
    if isinstance(parent, classes.Archer):
        return classes.Archer(attributes)
    if isinstance(parent, classes.Defender):
        return classes.Defender(attributes)
    if isinstance(parent, classes.Spy):
        return classes.Spy(attributes)
    if isinstance(parent, classes.Warrior):
        return classes.Warrior(attributes)
    
def get_attributes(l):
    s, a, e, r, h = gen.normalize(l[1], l[2], l[3], l[4], l[5])
    return classes.Attributes(l[0], s, a, e, r, h)

def one_point_cross(parents):
    dim = len(parents)
    children = []
    if dim % 2 != 0:
        dim -= 1
        att = parents[dim].get_attributes().get_all()
        new_att = get_attributes(att)
        children.append(create_child(parents[dim], new_att))
    
    for i in range(int(dim/2)):
        p = random.randint(0,5)
        p1 = parents[i]
        p1_att = p1.get_attributes().get_all()
        p2 = parents[dim-1-i]
        p2_att = p2.get_attributes().get_all()
        child_1 = []
        child_2 = []

        for j in range(p):
            child_1.append(p1_att[j])
            child_2.append(p2_att[j])
        for j in range(p, 6):
            child_1.append(p2_att[j])
            child_2.append(p1_att[j])
        
        children.append(create_child(p1, get_attributes(child_1)))
        children.append(create_child(p2, get_attributes(child_2)))
    
    return children

    
