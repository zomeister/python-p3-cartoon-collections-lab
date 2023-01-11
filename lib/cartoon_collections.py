def roll_call_dwarves(dwarves):
    for index in range(len(dwarves)):
        print(f"{index + 1}. {dwarves[index]}")

def summon_captain_planet(planeteer_calls):
    return [f"{planeteer_calls[index].capitalize()}!" for index in range(len(planeteer_calls))]

def long_planeteer_calls(calls):
    for index in range(len(calls)):
        if(len(calls[index]) > 4):
            return True

    return False

def find_the_cheese(words):
    for index in range(len(words)):
        if words[index] == 'cheddar' or words[index] == 'gouda' or words[index] == 'camembert':
            return words[index]

    return None