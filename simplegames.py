import chatexchange6
import shlex
import time
import re

import vote
import nim
import guess_number

SMSG = "Hello! I am the game bot!"
HANDLING = True
BOTNAME = "Zalgo"

with open("D:/CREDENTIALS") as f: # Change the path to link your credential file looking like `<email> <password>`
    s = f.read().split()
email, password = s

class NoneGame:
    @staticmethod
    def game(_a, msg, _b):
        msg.message.reply("No game loaded!")

state = {
    "game": None,
}
games = {
    None: NoneGame,
    False: vote,

    "nim": nim,
    "guess_number": guess_number,
}

def getreply(msg, mgc):
    if "@%s" % BOTNAME in mgc:
        mgc = mgc[(len(BOTNAME) + 1):].strip()
        games[state["game"]].game(state, msg, mgc)
    else:
        mgc = mgc.split(" ")
        if len(mgc) < 1:
            return
        if mgc[0] == "!/start" and not state["game"] and len(mgc) > 1 and mgc[1] in games:
            vote.init(state, mgc[1], mgc[2:])
        elif mgc[0] == "!/stop" and state["game"]:
            vote.init(state, None, None)
        elif mgc[0] == "!/help" and len(mgc) > 1 and mgc[1] in games:
            msg.message.reply(games[mgc[1]].HELP)
        elif mgc[0] == "!/games":
            msg.message.reply(", ".join(list(filter(lambda x: x, games.keys()))))
        elif mgc[0] == "!/commands":
            room.send_message("!/start <game>: Start a game\n"
                            + "!/stop: Stop the current game\n"
                            + "!/help <game>: Get help for a game\n"
                            + "!/games: Get the list of all games\n"
                            + "!/commands: Print all supported commands")

def onevent(msg, client):
    if not HANDLING:
        return
    if isinstance(msg, chatexchange6.events.MessagePosted) and msg.user.name != "Zalgo":
        mgc = msg.content
        mgc = re.sub(r"^:(\d+)", lambda g: "@%s" % BOTNAME if client.get_message(int(g.group(1))).owner.name == BOTNAME else "", mgc)
        r = getreply(msg, mgc)
        if r: room.send_message(r)

def main(roomn):
    global client, me, room
    print("Starting...")
    client = chatexchange6.Client('stackexchange.com', email, password)
    me = client.get_me()
    room = client.get_room(roomn)
    state["room"] = room
    state["games"] = games
    room.join()
    room.watch(onevent)
    print("Started!")
    room.send_message(SMSG)
main(53072)

print("ZECL - Zalgo Embedded Command Line (Simple Games Version)")
while True:
    try:
        cmd, *args = shlex.split(input("> "))
        if cmd == "say":
            room.send_message(args[0])
        elif cmd == "py":
            exec(args[0])
        elif cmd == "quit":
            try:
                room.send_message("Goodbye")
            except: pass
            break
        elif cmd == "off":
            HANDLING = False
        elif cmd == "on":
            HANDLING = True
        else:
            print("Unknow command: %s" % cmd)
    except Exception as ex:
        print(ex)

time.sleep(6)
