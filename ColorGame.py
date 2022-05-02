#Color game using Tkinter in Python
#from https://www.geeksforgeeks.org/color-game-python/
#new/changed: line 48,49,61,84,85
#new:timesup function
#changed: nextColor function score
# import the modules
import tkinter
import random

# list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'Purple', 'Brown']
correct = 0
wrong = -1

# the game time left, initially 30 seconds.
timeleft = 30


# function that will start the game.
def startGame(event):
    if timeleft == 30:
        # start the countdown timer.
        countdown()
    # run the function to
    # choose the next colour.
    nextColour()


# Function to choose and
# display the next colour.
#changed: correct score  to count how many time is correct and wrong
def nextColour():
    # use the globally declared 'score'
    # and 'play' variables above.
    global correct
    global wrong
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
            correct += 1
        else:
            wrong += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        scoreLabel.config(text="Correct: " + str(correct) + " Wrong: " + str(wrong))


# Countdown timer function
def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: "
                              + str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)
    else:
        timesup()

#New function: show times up after 30s
#Times up
def timesup():
    label.config(text="Times up!!", fg="black")


# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set the size
root.geometry("375x200")

# add an instructions label
instructions = tkinter.Label(root, text="Type in the color "
                                        "of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
