import random

def display_nim(rows):
    padlength = len(str(len(rows) + 1))
    lines = []
    for i, row in enumerate(rows):
        a = str(i + 1)
        a = " " * (padlength - len(a)) + a
        lines.append("    " + a + " " + "." * row)
    return "\n".join(lines)
def init(state, rows="3", stones="7", *args):
    state["rows"] = []
    for i in range(int(rows)):
        state["rows"].append(random.randint(1, int(stones) + 1))
    state["last"] = None
    state["room"].send_message(display_nim(state["rows"]))
def game(state, msg, mgc):
    if msg.user.name == state["last"]:
        msg.message.reply("You already played your turn!")
        return
    try:
        a, b = map(int, mgc.split())
    except:
        msg.message.reply("Invalid format!")
        return
    if a < 1 or a > len(state["rows"]) or b < 1 or b > state["rows"][a - 1]:
        msg.message.reply("Invalid move!")
        return
    state["rows"][a - 1] -= b
    if not any(state["rows"]):
        msg.message.reply("You lose!")
        state["game"] = None
        return
    state["last"] = msg.user.name
    state["room"].send_message(display_nim(state["rows"]))

HELP = "Game of [Nim](https://en.wikipedia.org/wiki/Nim). Format is `<row> <number of stones to remove>`."
