def init(state, game, args):
    state["game"] = False
    state["next"] = game
    state["args"] = args
    state["voters"] = []
    state["votes"] = 0
    thing = "start '" + game + "'" if game else "stop the current game"
    state["room"].send_message("Voting to " + thing + ". 2 votes needed. Reply to this message to register a vote.")
def game(state, msg, mgc):
    if msg.user.name in state["voters"]:
        msg.message.reply("You already voted!")
        return
    state["votes"] += 1
    state["voters"].append(msg.user.name)
    msg.message.reply("Vote registered.")
    if state["votes"] == 2:
        state["room"].send_message("Vote successful!")
        state["game"] = state["next"]
        if state["next"]:
            state["games"][state["game"]].init(state, *state["args"])
