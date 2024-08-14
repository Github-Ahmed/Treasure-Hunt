print("Welcome to Treasure island, Your mission is to find the treasure!")
print(r"""

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
            """)

left_right = input("Do you want to proceed to left or right?: ").lower()

if left_right == "left":
    swim = input("Do you want to swim or wait?: ").lower()
    if swim == "wait":
        door = input("Choose a door from Red, Yellow, Blue: ").lower()
        if door == "yellow":
            print("\nYou found the tressure. Congrats!")
        elif door == "red":
            print("\nYou were burned by the fire. Game over.")
        elif door == "blue":
            print("\nYou were eaten by a lion. Game over.")
        else:
            print("\nGame over.")
    else:
        print("\nYou were attacked by a trout. Game over.")
else:
    print("\nYou fell into a hole. Game over.")
