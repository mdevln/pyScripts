from Tkinter import *
from random import randint
from datetime import datetime
# from ScrolledText import ScrolledText


def convert(x):
    # Convert hand into a string.
    hand = ""
    if x == 1:
        hand = "Rock"
    elif x == 2:
        hand = "Paper"
    elif x == 3:
        hand = "Scissors"
    return hand


def play(hand):
    global games, comp_wins, player_wins, gameBox
    # Play RPS.
    timestamp = datetime.now().strftime('%H:%M:%S')
    comp = randint(1, 3)
    if comp == hand:
        # Compare computer's choice to player's and select a winner.
        games.set(games.get() + 1)
        outcome = "%s - Its a tie, you both chose %s.\n" % (timestamp, convert(comp))
    elif (hand == 3 and comp == 1) or (hand == 1 and comp == 2) \
            or (hand == 2 and comp == 3):
        comp_wins.set(comp_wins.get() + 1)
        games.set(games.get() + 1)
        outcome = "%s - You lose %s beats %s.\n" % (timestamp, convert(comp), convert(hand))
    else:
        player_wins.set(player_wins.get() + 1)
        games.set(games.get() + 1)
        outcome = "%s - You win! %s beats %s.\n" % (timestamp, convert(hand), convert(comp))
    # Update textbox with new result
    score = 'Player: %d/Computer: %d - Total games: %d' % (player_wins.get(), comp_wins.get(), games.get())
    scoreStr.set(score)
    gameBox.configure(state=NORMAL)
    gameBox.delete('2.0', '3.0')
    gameBox.insert('1.0', outcome + '\n')
    gameBox.configure(state=DISABLED)


def Exitgame():
    # Exit game
    exit()


def Clear():
    games.set(0)
    comp_wins.set(0)
    player_wins.set(0)
    scoreStr.set("")
    gameBox.configure(state=NORMAL)
    gameBox.delete(1.0, END)
    gameBox.configure(state=DISABLED)


# GUI loop begin
rps = Tk()
rps.geometry('+300+300')

# Create textbox frame/scrollbar
txtFrame = Frame(rps, width=46, height=20, relief=SUNKEN)
scrBar = Scrollbar(txtFrame)
gameBox = Text(txtFrame, width=46, height=20, yscrollcommand=scrBar.set, state=DISABLED, relief=SUNKEN)
scrBar.config(command=gameBox.yview)
scrBar.pack(side='right', fill='y')
gameBox.pack(side='left', fill='both', expand=True)

# Setup variables
games = IntVar()
comp_wins = IntVar()
player_wins = IntVar()
games.set(0)
comp_wins.set(0)
player_wins.set(0)
scoreStr = StringVar()
scoreStr.set(None)

# Configure GUI grid
rps.columnconfigure(0, pad=3)
rps.columnconfigure(1, pad=3)
rps.columnconfigure(2, pad=3)
rps.columnconfigure(3, pad=3)
rps.rowconfigure(0, pad=3)
rps.rowconfigure(1, pad=3)
rps.rowconfigure(2, pad=3)
rps.rowconfigure(3, pad=3)

# Create/configure buttons, labels and text area.
scoreStr = StringVar()
scoreLabel = Label(rps, textvariable=scoreStr)
scoreLabel.grid(row=3, column=0, columnspan=4, sticky=E)

txtFrame.grid(row=2, column=0, columnspan=3, sticky=W,)

button1 = Button(rps, text='Rock', command=lambda: play(1)).grid(row=1, column=0)
button2 = Button(rps, text='Paper', command=lambda: play(2)).grid(row=1, column=1)
button3 = Button(rps, text='Scissors', command=lambda: play(3)).grid(row=1, column=2)
button4 = Button(rps, text='Exit', command=lambda: Exitgame()).grid(row=4, column=2, stick=E)
button5 = Button(rps, text='Clear', command=lambda: Clear()).grid(row=4, column=3, sticky=W)
label1 = Label(rps, text='Choose a hand!').grid(row=0, column=0, columnspan=2)


rps.mainloop()
