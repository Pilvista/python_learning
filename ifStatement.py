is_hungry = True
is_happy = False
is_unhappy = True
if is_hungry and is_happy:
    print("He needs food because of hunger or happiness")
elif is_hungry and is_unhappy:
    print("He needs to relax")
elif not(is_hungry) and is_unhappy:
    print("Care him with food")
