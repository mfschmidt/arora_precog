from psychopy import visual, core, event, data
import numpy, time
visual.useFBO=True

# Here define paths to image intpus and the path to store the output files
imgdir='C:\\Path\\to\\Iaps\\Images\\IAPS2008\\'
logdir='C:\\Path\\to\\log\\directory\\'
#imgdir='C:\\Users\\Science\\Dropbox\\Sarika2\\IAPS2008\\'
#logdir='C:\\Users\\Science\\Dropbox\\Sarika2\\task\\'

# create a window to draw in
win = visual.Window([], monitor="testMonitor", fullscr=True, allowGUI=False)

# here import the stimulis conditions
stimList=data.importConditions(logdir + 'Conditions.xlsx')

#organise them with the trial handler
# Collect the participants name
message=visual.TextStim(win, text='Please type in participants initials and year of birth (i.e. NP86)', pos=(0,0.5))
input=visual.TextStim(win, text='',pos=(0,-0.6))
k=['']
name=[]
message.draw()
win.flip()
while k[0] not in ['return']:
    message.draw()
    k = event.waitKeys()
    if k[0] != 'backspace' and k[0] != 'return':
        name.append(k[0])
    elif k[0] == 'backspace':
        name.pop()
    input.setText("".join(name))
    input.draw()
    win.flip()

name="".join(name)
print name

trials = data.TrialHandler(stimList,1,extraInfo= {'participant':name,'session':1})
trials.data.addDataType('choice')#this will help store things with the stimuli
trials.data.addDataType('RT')#add as many types as you like
trials.data.addDataType('Hit_Miss')
trials.data.addDataType('MaskedStim')

# Here write out and present the instructions and also administer Anxiety
# Scales, collect demographic info etc?

button_des=visual.TextStim(win, text='"Z" (left image)           "/" (right image)', height=0.05, pos=(0,-0.8))
blankScreen = visual.TextStim(win, text='+')

# Here present the instructions.
message.draw()
win.flip()
# Here wait for person to input button to flip
message.setText('Instruction set #2')

# Here present all 36 trials
#create a clock to get reaction time data
clock=core.Clock()
nDone=0
for thisTrial in trials: #handler can act like a for loop

    # Here initialize stimuli
    #neu_pic = visual.ImageStim(win, image=imgdir + str(thisTrial["neutral"]) + ".jpg", pos=(-200,0), units='pix',size=(256,192))
    neu_pic = visual.ImageStim(win, image=imgdir + str(thisTrial["neutral"]) + ".jpg", pos=(-250,0), units='pix',size=(384,288))
    neu_pic_M = visual.ImageStim(win, image=imgdir + str(thisTrial["neutral"]) + "_m.jpg", pos=(250,0), units='pix',size=(384,288))
    neu_pic_mask = visual.ImageStim(win, image=imgdir + str(thisTrial["neutral"]) + ".jpg", pos=(0,0), units='pix',size=(512,384))
    neu_pic_M_mask = visual.ImageStim(win, image=imgdir + str(thisTrial["neutral"]) + "_m.jpg", pos=(0,0), units='pix',size=(512,384))
    #neu_pic = visual.ImageStim(win, image=imgdir + str(thisTrial["neutral"]) + ".jpg", pos=(0,0), units='pix',size=(512,384))
    pos_pic = visual.ImageStim(win, image=imgdir + str(thisTrial["positive"]) + ".jpg", pos=(0,0), units='pix',size=(512,384))
    neg_pic = visual.ImageStim(win, image=imgdir + str(thisTrial["negative"]) + ".jpg", pos=(0,0), units='pix',size=(512,384))

    # Here present the question stimulus and collect response
    k=['']
    choice=''
    while choice not in ['z', 'slash']:
        button_des.draw()
        neu_pic.draw()
        neu_pic_M.draw()

        clock.reset() #to get reaction time relative to the reset
        win.flip()
        k = event.waitKeys(timeStamped=clock)
        thisReactionTime=k[0][1]
        choice=k[0][0]

        # log the subjects key press
        trials.data.add('choice', choice)
        trials.data.add('RT', thisReactionTime) #add the data to our set

        # Here to break out of loop and start over if need be
        if choice=='escape':
            core.quit()
            event.clearEvents()

        # Here randomly select the target after the subject
        # already picks a preferred stimulus
        target=numpy.random.choice(['z','slash'])

        # If the subject's choice matches the target, play the positive stimuli
        # else play the negative stimuli
        if choice==target:
            masked_pic=pos_pic;
            # Log this has a hit
            trials.data.add('Hit_Miss','Hit')
        else:
            masked_pic=neg_pic;
            # Log this has a miss
            trials.data.add('Hit_Miss','Miss')

        # Here record which image was subliminally presented
        #event.clearEvents()
        trials.data.add('MaskedStim',masked_pic.image)

    # Here present the masked stimulus
    for i in range(3):
        for frameN in range(42):  #for exactly 42 frames
            if 0 <= frameN < 30:
                blankScreen.draw()
                win.flip()
            if 30 <= frameN < 32:  # present fixation for just 2 frames
                masked_pic.draw()
                win.flip()
            if 32 <= frameN < 42:  # present stim for a different subset
                if choice=='z':
                    neu_pic_mask.draw()
                    win.flip()
                else:
                    neu_pic_M_mask.draw()
                    win.flip()
            #win.flip()

    blankScreen.draw()
    win.flip()
    core.wait(3) # here wait 3 seconds

#after the experiment
print('\n')
trials.printAsText(stimOut=['neutral'], #write summary data to screen
                  dataOut=['choice_raw','Hit_Miss_raw','RT_raw','MaskedStim_raw'])

trials.saveAsText(fileName=name + '-' + time.strftime("%m-%d-%Y-%H-%M"), stimOut=['neutral'], #write summary data to text file
                  dataOut=['choice_raw','Hit_Miss_raw','RT_raw','MaskedStim_raw'])
#trials.saveAsText(fileName='testData', # also write summary data to a text file
#                  stimOut=['sf','ori'],
#                  dataOut=['RT_mean','RT_std', 'choice_raw'])
#trials.saveAsExcel(fileName='testData', # ...or an xlsx file (which supports sheets)
#                  sheetName = 'rawData',
#                  stimOut=['sf','ori'],
#                  dataOut=['RT_mean','RT_std', 'choice_raw'])
#trials.saveAsPickle(fileName = 'testData')#this saves a copy of the whole object
#df = trials.saveAsWideText("testDataWide.txt") #wide is useful for analysis with R or SPSS. Also returns dataframe df
