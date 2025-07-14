import random
import time as t

def action():
    h_sum = b_sum = 0
    print("Start playing the game now!")
    t.sleep(1)
    for dice in range(0, choice):
        person = random.randint(1,6)
        t.sleep(1)
        print("Human got: ", person)
        h_sum += person
t.sleep(1)
print("\n Total sum of Human is: ", h_sum)
t.sleep(1)
print("\n Now it's the turn for the bot")
t.sleep(1)

for dice in range(0, choice):
    bot = random.randint(1,6)
    t.sleep(1)
    print("Bot got: ", bot)
    b_sum += bot
t.sleep(1)
print("\n Total sum of Bot is: ", b_sum)
t.sleep(2)