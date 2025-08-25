import random
import time as t

def action(choice):
    h_sum = b_sum = 0
    print("Start playing the game now!")
    t.sleep(1)
    humanNames = ['Michael', 'Emma', 'Daniel', 'Sophia', 'Lucas', 'Olivia']
    randomHumanName = random.choice(humanNames)

    botNames = ['EVA', 'NEXA', 'LUMI', 'KORA', 'GLADoS', 'AIDA']
    randomBotName = random.choice(botNames)

    for dice in range(choice):
        person = random.randint(1,6)
        t.sleep(1)
        print(randomHumanName + " got:", person)
        h_sum += person

    t.sleep(1)
    print("\nTotal sum of " + randomHumanName  + " is:", h_sum)
    t.sleep(1)
    print("\nNow it's the turn for the " + randomBotName)
    t.sleep(1)

    for dice in range(choice):
        bot = random.randint(1,6)
        t.sleep(1)
        print(randomBotName + " got:", bot)
        b_sum += bot

    t.sleep(1)
    print("\nTotal sum of " + randomBotName + " is:", b_sum)
    t.sleep(2)

    if h_sum > b_sum:
        print("\n" + randomHumanName + "won")
    elif h_sum < b_sum:
        print("\n" + randomBotName + " won")
    else:
        print("\nIt's a tie between " + randomHumanName + " and " + randomBotName)


def play():
    while True:
        try:
            choice = int(input("How many times should the dice be rolled? (1-5): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= choice <= 5:
            action(choice)
        else:
            print("Please enter the correct choice (1-5).")
            continue

        rolling = input("Do you want to continue the game? (yes/no): ").strip().lower()
        if rolling != "yes":
            print("It was wonderful playing with a bot!")
            break


if __name__ == "__main__":
    play()
