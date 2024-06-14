# tupple can not change the values list can
def make_pizza(*topping):
    print(topping)
    for topin in topping:
        print(topin)


pramod = make_pizza("tomato")
bharkave = make_pizza("Olives", "mashroom", "paneer")
achman = make_pizza("mshroom", "pinaple", "paneer", "banana")
