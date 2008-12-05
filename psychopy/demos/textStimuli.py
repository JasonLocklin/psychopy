#! /usr/local/bin/python2.5
from psychopy import *
"""
Text rendering has changed a lot (for the better) under pyglet. This
script shows you the new way to specify fonts.
"""
#create a window to draw in
myWin = visual.Window((800.0,800.0),allowGUI=False,winType='pyglet',
				monitor='testMonitor', units ='cm', screen=0)

#choose some fonts. If a list is provided, the first font found will be used.
fancy = ['Monotype Corsiva', 'Palace Script MT', 'Edwardian Script ITC']
sans = ['Gill Sans MT', 'Arial','Helvetica','Verdana'] #use the first font found on this list
serif = ['Times','Times New Roman'] #use the first font found on this list
comic = 'Comic Sans MS' #note the full name of the font - the short name won't work

#INITIALISE SOME STIMULI
fpsText = visual.TextStim(myWin, 
                        units='norm',height = 0.1,
                        pos=(-0.98, -0.98), text='starting...',
                        font=sans, 
                        alignHoriz = 'left',alignVert='bottom',
                        rgb=[+1,-1,-1])
rotating = visual.TextStim(myWin,text="Fonts \nrotate!",pos=(0, 0),#and can have line breaks
                        rgb=[-1.0,-1,1],
                        ori=0, height = 0.5,
                        font=comic)
unicodeStuff = visual.TextStim(myWin,
                        text = u"unicode (eg \u03A8 \u040A \u03A3)",#you can find the unicode character value from MS Word 'insert symbol'
                        rgb=-1,  font=serif,pos=(0,3),
                        height = 1)
psychopyTxt = visual.TextStim(myWin, 
                        text = u"PsychoPy \u00A9Jon Peirce",
                        units='norm', height=0.1,
                        pos=[0.95, 0.95], alignHoriz='right',alignVert='top',
                        font=fancy, italic=True) 
longSentence = visual.TextStim(myWin, 
                        text = u"Very long sentences can wrap", wrapWidth=0.2,
                        units='norm', height=0.05,
                        pos=[0.95, -0.95], alignHoriz='center',alignVert='bottom') 
trialClock = core.Clock()
t=lastFPSupdate=0;
while t<20:#quits after 20 secs
    t=trialClock.getTime()
    
    rotating.setOri(1,"+")
    rotating.draw()
    
    unicodeStuff.draw()
    longSentence.draw()
    
    if t-lastFPSupdate>1:#update the fps every second
        fpsText.setText("%i fps" %myWin.fps())
        lastFPSupdate+=1
    fpsText.draw()
    psychopyTxt.draw()
    
    myWin.flip()

