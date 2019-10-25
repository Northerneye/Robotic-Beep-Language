import winsound
import time
import math

ourfrequency = 400
length = 0
pitch = 0
between = 0
doubsky = 0
trill = 0

def Beep(frequency, duration):
    winsound.Beep(frequency, duration)

def sort(userchar):
    global length
    global pitch
    global between
    global doubsky
    global trill
    if(userchar == "a"):
        length = 1
        pitch = 1
        between = 1
        doubsky = 1
        trill = 0
        
    if(userchar == "b"):
        length = 1
        pitch = 1
        between = 1
        doubsky = 1
        trill = 1

    if(userchar == "c"):
        length = 1
        pitch = 1
        between = 1
        doubsky = 0
        trill = 0
    
    if(userchar == "d"):
        length = 1
        pitch = 1
        between = 1
        doubsky = 0
        trill = 1
    
    if(userchar == "e"):
        length = 1
        pitch = 1
        between = 0
        doubsky = 1
        trill = 0
    
    if(userchar == "f"):
        length = 1
        pitch = 1
        between = 0
        doubsky = 1
        trill = 1

    if(userchar == "g"):
        length = 1
        pitch = 1
        between = 0
        doubsky = 0
        trill = 0

    if(userchar == "h"):
        length = 1
        pitch = 1
        between = 0
        doubsky = 0
        trill = 1

    if(userchar == "i"):
        length = 1
        pitch = 0
        between = 1
        doubsky = 1
        trill = 0

    if(userchar == "j"):
        length = 1
        pitch = 0
        between = 1
        doubsky = 1
        trill = 1

    if(userchar == "k"):
        length = 1
        pitch = 0
        between = 1
        doubsky = 0
        trill = 0

    if(userchar == "l"):
        length = 1
        pitch = 0
        between = 1
        doubsky = 0
        trill = 1

    if(userchar == "m"):
        length = 1
        pitch = 0
        between = 0
        doubsky = 1
        trill = 0
    
    if(userchar == "n"):
        length = 1
        pitch = 0
        between = 0
        doubsky = 1
        trill = 1

    if(userchar == "o"):
        length = 1
        pitch = 0
        between = 0
        doubsky = 0
        trill = 0

    if(userchar == "p"):
        length = 1
        pitch = 0
        between = 0
        doubsky = 0
        trill = 1
    
    if(userchar == "q"):
        length = 0
        pitch = 1
        between = 1
        doubsky = 1
        trill = 0

    if(userchar == "r"):
        length = 0
        pitch = 1
        between = 1
        doubsky = 1
        trill = 1

    if(userchar == "s"):
        length = 0
        pitch = 1
        between = 1
        doubsky = 0
        trill = 0
    
    if(userchar == "t"):
        length = 0
        pitch = 1
        between = 1
        doubsky = 0
        trill = 1

    if(userchar == "u"):
        length = 0
        pitch = 1
        between = 0
        doubsky = 1
        trill = 0
    
    if(userchar == "v"):
        length = 0
        pitch = 1
        between = 0
        doubsky = 1
        trill = 1
    
    if(userchar == "w"):
        length = 0
        pitch = 1
        between = 0
        doubsky = 0
        trill = 0

    if(userchar == "x"):
        length = 0
        pitch = 1
        between = 0
        doubsky = 0
        trill = 1

    if(userchar == "y"):
        length = 0
        pitch = 0
        between = 1
        doubsky = 1
        trill = 0

    if(userchar == "z"):
        length = 0
        pitch = 0
        between = 1
        doubsky = 1
        trill = 1

    if(userchar == ","):
        length = 0
        pitch = 0
        between = 1
        doubsky = 0
        trill = 0

    if(userchar == "."):
        length = 0
        pitch = 0
        between = 1
        doubsky = 0
        trill = 1

    if(userchar == " "):
        time.sleep(.5)
    
def say():
    global ourfrequency
    global length
    global pitch
    global between
    global doubsky
    global trill
    if(length == 0):
        beeptime = 250
    if(length == 1):
        beeptime = 750

    if(pitch == 0):
        newfrequency = ourfrequency - 50
    if(pitch == 1):
        newfrequency = ourfrequency + 50

    if(between == 0):
        time.sleep(math.floor(beeptime/4000))
    if(between == 1):
        Beep(math.floor((newfrequency+ourfrequency)/2)+1,math.floor(beeptime/4))
    
    if(doubsky == 0):
        if(trill == 0):
            Beep(math.floor(newfrequency)+1, math.floor(beeptime))
        if(trill == 1):
            Beep(math.floor(ourfrequency)+1, math.floor(beeptime/4))
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/4))
            Beep(math.floor(ourfrequency)+1, math.floor(beeptime/4))
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/4))
    if(doubsky == 1):
        if(trill == 0):
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/2))
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/2))
        if(trill == 1):
            Beep(math.floor(ourfrequency)+1, math.floor(beeptime/8))
            Beep(math.floor(ourfrequency)+1, math.floor(beeptime/8))
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/8))
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/8))
            Beep(math.floor(ourfrequency)+1, math.floor(beeptime/8))
            Beep(math.floor(ourfrequency)+1, math.floor(beeptime/8))
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/8))
            Beep(math.floor(newfrequency)+1, math.floor(beeptime/8))
    Beep(ourfrequency, 500)
    time.sleep(.5)

while(True):
    ourfrequency = 400
    userstr = input("Translate:")
    userstr = list(userstr)
    Beep(math.floor(ourfrequency)+1, 250)
    Beep(math.floor(ourfrequency)+26, 250)
    Beep(math.floor(ourfrequency)+51, 250)
    Beep(math.floor(ourfrequency)+1, 250)
    time.sleep(1)
    for x in range(len(userstr)):
        sort(userstr[x])
        say()
