import src.classes as classes

if __name__ == "__main__":
    attributes = classes.Attributes(1.3, 30, 30, 30, 30, 30)
    warrior = classes.Warrior(attributes)
    print("Performance: ", warrior.get_performance())