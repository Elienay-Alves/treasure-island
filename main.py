from treasure_trunk import treasure_trunk

print(treasure_trunk)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


CROSS_ROADS_OPTIONS = input(
    'You are at a cross road. Where do you want to go? Type "left" or "right":\n'
).lower()


def game_options():
    result = ""

    if CROSS_ROADS_OPTIONS == "left":
        wait_or_not = input(
            'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
        ).lower()
        if wait_or_not == "wait":
            what_door = input(
                "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
            ).lower()
            if what_door == "yellow":
                result = "You found the trasure! You win!"
            elif what_door == "red":
                result = "It's a room full of fire. Game Over!"
            elif what_door == "blue":
                result = "You enter a room of beasts. Game Over!"
            else:
                result = "You choose a door that doesn't exist. Game Over!"
        else:
            result = "You get attacked by an angry trout.Game over!"
    else:
        result = "You fell into a hole. Game over!"

    return result


print(game_options())
