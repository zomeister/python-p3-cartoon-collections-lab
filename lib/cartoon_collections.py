MY_CHEESES = ["cheddar", "gouda", "camembert"]
def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves):
        print("{}. {}".format(i+1, dwarf))
    # pass
def summon_captain_planet(planeteer_calls):
    return [call.title() + '!' for call in planeteer_calls]
    # pass
def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
    # pass
def find_the_cheese(foods):
    for cheese in MY_CHEESES:
        if cheese in foods:
            return cheese
    return None
    pass
