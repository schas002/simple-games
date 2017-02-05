import random

def init(state, *args):
    state["last"] = None

def game(state, msg, msc):
    if msg.user.name == state["last"]:
        msg.message.reply("You already played your turn!")
        return
    try:
        isodd = {"odd":True,"even":False}[msc.casefold()]
    except KeyError:
        msg.message.reply("I don't understand!")
        return
    if random.rand_int(0, 1):
        msg.message.reply("You win!")
    else:
        msg.message.reply("You lose.")
    state["last"] = msg.user.name
HELP = "Enter 'odd' or 'even'."
