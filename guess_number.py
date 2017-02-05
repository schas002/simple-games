import random

def init(state, mn="0", mx="1000", *args):
    state["number"] = random.randint(int(mn), int(mx))
    state["last"] = None
    state["room"].send_message("Guess the number! It's between %s and %s." % (mn, mx))
def game(state, msg, mgc):
    if msg.user.name == state["last"]:
        msg.message.reply("You already played your turn!")
        return
    try:
        a = int(mgc)
    except:
        msg.message.reply("Invalid format!")
        return
    if a == state["number"]:
        msg.message.reply("You win!")
        return
    elif a > state["number"]:
        msg.message.reply("Less.")
    elif a < state["number"]:
        msg.message.reply("More.")
    state["last"] = msg.user.name

HELP = "Turn-based guess the number game."
