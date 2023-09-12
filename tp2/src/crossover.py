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

def two_point_cross(parents):
    parents_dim = len(parents)
    children = []
    index = 0
    if parents_dim % 2 == 1 :
        odd_parent = parents[index]
        children.append(create_child(odd_parent, get_attributes(odd_parent.get_attributes().get_all())))
        index += 1
    while parents_dim != 0:
        parents_dim -= 2
        parent1 = parents[index]
        index += 1
        parent2 = parents[index]
        index += 1
        parent1_attributes = parent1.get_attributes().get_all()
        parent2_attributes = parent2.get_attributes().get_all()
        p1 = -1      
        p2 = -2     
        while p1 > p2:
            p1 = random.randint(0, 5)
            p2 = random.randint(0, 5)
        if (p1 + p2) <= 6:
            mid = 6 - (p1 + p2)
        else:
            mid = p2 - p1
        child1_attributes = []
        child2_attributes = []
        i = 0
        while i < p1:
            child1_attributes.append(parent1_attributes[i])
            child2_attributes.append(parent2_attributes[i])
            i += 1
        while (i - p1) < mid:
            child1_attributes.append(parent2_attributes[i])
            child2_attributes.append(parent1_attributes[i])
            i += 1    
        while i < 6:
            child1_attributes.append(parent1_attributes[i])
            child2_attributes.append(parent2_attributes[i])
            i += 1
        children.append(create_child(parent1, get_attributes(child1_attributes)))
        children.append(create_child(parent2, get_attributes(child2_attributes)))
    return children

def ring_cross(parents):
    parents_dim = len(parents)
    index = 0
    children = []
    if parents_dim % 2 == 1 :
        odd_parent = parents[index]
        index += 1
        children.append(create_child(odd_parent, get_attributes(odd_parent)))
    while parents_dim != 0:
        parents_dim -= 2
        parent1 = parents[index]
        index += 1
        parent2 = parents[index]
        index += 1
        parent1_attributes = parent1.get_attributes().get_all()
        parent2_attributes = parent2.get_attributes().get_all()
        attributes_dim = len(parent1_attributes)
        ring_start_pos = random.randint(0, 5)
        ring_dim = random.randint(0, 3)
        child1_attributes = []
        child2_attributes = []
        children_attributes_filled = False
        i = 0
        while i < ring_start_pos:
            child1_attributes.append(parent1_attributes[i])
            child2_attributes.append(parent2_attributes[i])
            i += 1
        while ring_dim != 0:
            child1_attributes.append(parent2_attributes[i])
            child2_attributes.append(parent1_attributes[i])
            i += 1
            ring_dim -= 1
            if i == attributes_dim:
                i = 0
                children_attributes_filled = True
                ring_dim = 0     
                child1_attributes[i] = parent2_attributes[i]
                child2_attributes[i] = parent1_attributes[i]   
        if children_attributes_filled == False:
            while i < attributes_dim:
                child1_attributes.append(parent1_attributes[i])
                child2_attributes.append(parent2_attributes[i])
                i += 1
        children.append(create_child(parent1, get_attributes(child1_attributes)))
        children.append(create_child(parent2, get_attributes(child2_attributes)))
    return children    

def uniform_cross(parents):
    parents_dim = len(parents)
    children = []
    index = 0
    if parents_dim % 2 == 1 :
        odd_parent = parents[index]
        index += 1
        children.append(create_child(odd_parent, get_attributes(odd_parent)))
    while parents_dim != 0:
        parents_dim -= 2
        parent1 = parents[index]
        index += 1
        parent2 = parents[index]
        index += 1
        parent1_attributes = parent1.get_attributes().get_all()
        parent2_attributes = parent2.get_attributes().get_all()
        attributes_dim = len(parent1_attributes)
        child1_attributes = []
        child2_attributes = []
        cross_probability = 0.5
        for i in range(attributes_dim):
            probability = random.uniform(0.0, 1.0)
            if probability <= cross_probability:
                child1_attributes.append(parent2_attributes[i])
                child2_attributes.append(parent1_attributes[i])
            else:
                child1_attributes.append(parent1_attributes[i])
                child2_attributes.append(parent2_attributes[i])
        children.append(create_child(parent1, get_attributes(child1_attributes)))
        children.append(create_child(parent2, get_attributes(child2_attributes)))
    return children