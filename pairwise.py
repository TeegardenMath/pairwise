import tkinter as tk
from tkinter import ttk
from tkmacosx import Button


#create our initial window
window = tk.Tk()

#these variables will track which element we have selected on each side
elementLeft = tk.StringVar()
elementRight = tk.StringVar()

reactionLog = tk.StringVar()
reactionLog.set("Welcome to Pairwise!")
captionLog = tk.StringVar()
captionLog.set("to start, select and combine any two elements")

#the various frames for arranging our window
frameD = tk.Frame() #top half of the window -- ingredients
frameA = tk.Frame(relief=tk.SUNKEN,borderwidth=5, master=frameD) #categories (left)
frameB = tk.Frame(relief=tk.SUNKEN,borderwidth=5, master=frameD) #categories (right)
frameE = tk.Frame(relief=tk.SUNKEN,borderwidth=5, master=frameD,width=100) #radio buttons (left)
frameF = tk.Frame(relief=tk.SUNKEN,borderwidth=5, master=frameD,width=100) #radio buttons (right)
frameC = tk.Frame(relief=tk.SUNKEN,borderwidth=5) #bottom half of the window -- results
frameG = tk.Frame(master=frameC) #log
frameH = tk.Frame(relief=tk.SUNKEN,borderwidth=2,master=frameC,width=50) #bottom buttons

#scrolling apparatus
canvasE = tk.Canvas(frameE)
scrollbarE = ttk.Scrollbar(frameE, orient="vertical", command=canvasE.yview)
scrollableE = ttk.Frame(canvasE)

scrollableE.bind(
    "<Configure>",
    lambda e: canvasE.configure(
        scrollregion=canvasE.bbox("all")
    )
)

canvasE.create_window((0, 0), window=scrollableE, anchor="nw")
canvasE.configure(yscrollcommand=scrollbarE.set)

canvasF = tk.Canvas(frameF)
scrollbarF = ttk.Scrollbar(frameF, orient="vertical", command=canvasF.yview)
scrollableF = ttk.Frame(canvasF)

scrollableF.bind(
    "<Configure>",
    lambda e: canvasF.configure(
        scrollregion=canvasF.bbox("all")
    )
)

canvasF.create_window((0, 0), window=scrollableF, anchor="nw")
canvasF.configure(yscrollcommand=scrollbarF.set)

canvasG = tk.Canvas(frameG)
scrollbarG = ttk.Scrollbar(frameG, orient="vertical", command=canvasG.yview)
scrollableG = ttk.Frame(canvasG)

scrollableG.bind(
    "<Configure>",
    lambda e: canvasG.configure(
        scrollregion=canvasG.bbox("all")
    )
)

canvasG.create_window((0, 0), window=scrollableG, anchor="nw")
canvasG.configure(yscrollcommand=scrollbarG.set)

saveDisplay = tk.Text(scrollableG,wrap=tk.WORD)

#reaction log
logLabel = tk.Label(master=scrollableG, textvariable=reactionLog)
captionLabel = tk.Message(master=scrollableG, textvariable=captionLog,font=("TkDefaultFont",12,"italic"),width=1000)
logAppendix = ""

#names of the element categories
elementTypes = ["stuff","force","shape","?","object","weather","world","??","plant","animal","human","???","tool","product","invention","!!!!","vanity"]

#buttons shown
buttonsShown={
    'stuff':2,
    'force':2,
    'shape':2,
    '?':0,
    'object':0,
    'weather':0,
    'world':0,
    '??':0,
    'plant':0,
    'animal':0,
    'human':0,
    '???':0,
    'tool':0,
    'product':0,
    'invention':0,
    '!!!!':0,
    'vanity':0
}

#this dictionary will keep track of all elements and their types
typeDictionary={
    'algae':'plant',
    'amino acid':'object',
    'ball':'shape',
    'ball lightning':'weather',
    'balloon':'product',
    'beach':'world',
    'beach ball':'product',
    'seaglass':'vanity',
    'bird':'animal',
    'black hole':'world',
    'blimp':'product',
    'book':'object',
    'carbon dioxide':'stuff',
    'cloud':'weather',
    'coconut':'object',
    'comet':'world',
    'continent':'world',
    'crater':'world',
    'crystal ball':'tool',
    'death':'force',
    'desert':'world',
    'dinosaur':'animal',
    'dodo':'animal',
    'double rainbow':'weather',
    'dry ice':'stuff',
    'duck':'animal',
    'dune':'world',
    'eclipse':'weather',
    'egg':'object',
    'electricity':'force',
    'eruption':'weather',
    'fire':'force',
    'fireball':'vanity',
    'fish':'animal',
    'fog':'weather',
    'fried egg':'vanity',
    'geyser':'world',
    'glacier':'world',
    'glass':'stuff',
    'golf ball':'vanity',
    'grass':'plant',
    'gravity':'force',
    'gull':'animal',
    'happy gull':'vanity',
    'helium':'stuff',
    'horse':'animal',
    'hourglass':'product',
    'hydrogen':'stuff',
    'hydrothermal vent':'world',
    'ice':'stuff',
    'island':'world',
    'kink':'invention',
    'lake':'world',
    'lava':'stuff',
    'lava lamp':'vanity',
    'light':'force',
    'lightning':'weather',
    'lizard':'animal',
    'microbe':'animal',
    'moon':'world',
    'nitrogen':'stuff',
    'oasis':'world',
    'obsidian':'stuff',
    'ocean':'world',
    'oxygen':'stuff',
    'palm tree':'plant',
    'peacock':'animal',
    'penguin':'animal',
    'philosophy':'invention',
    'plain':'world',
    'planet':'world',
    'plankton':'plant',
    'plesiosaur':'animal',
    'primordial soup':'stuff',
    'rain':'weather',
    'rainbow':'weather',
    'rattlesnake':'animal',
    'reef':'world',
    'reincarnation':'invention',
    'religion':'invention',
    'river':'world',
    'riverbed':'world',
    'rock':'stuff',
    'rock star':'human',
    'salamander':'animal',
    'sand':'stuff',
    'short circuit':'vanity',
    'sky':'world',
    'sleet':'weather',
    'snow':'weather',
    'snowball':'object',
    'snowman':'product',
    'solar system':'world',
    'stained glass':'product',
    'star':'world',
    'starfish':'animal',
    'steam':'stuff',
    'stress ball':'object',
    'sun':'world',
    'testicles':'object',
    'tide':'weather',
    'tundra':'world',
    'turtle':'animal',
    'vanilla ice':'vanity',
    'volcano':'world',
    'water':'stuff',
    'water balloon':'vanity',
    'wave':'shape'
}

bucketDictionary={
    'algae':['@photosynthetic'],
    'bird':['@oviparous'],
    'black hole':['@celestial'],
    'comet':['@celestial'],
    'dodo':['@oviparous'],
    'duck':['@oviparous'],
    'dinosaur':['@oviparous'],
    'fire':['@hot'],
    'fish':['@oviparous'],
    'glacier':['@frozenwater'],
    'grass':['@photosynthetic'],
    'gull':['@oviparous'],
    'ice':['@frozenwater'],
    'lake':['@liquidwater'],
    'lava':['@hot'],
    'lizard':['@oviparous'],
    'moon':['@celestial'],
    'ocean':['@liquidwater'],
    'palm tree':['@photosynthetic'],
    'peacock':['@oviparous'],
    'penguin':['@oviparous'],
    'plesiosaur':['@oviparous'],
    'rain':['@liquidwater'],
    'rattlesnake':['@oviparous'],
    'river':['@liquidwater'],
    'salamander':['@oviparous'],
    'sleet':['@frozenwater'],
    'snow':['@frozenwater'],
    'snowball':['@frozenwater'],
    'snowman':['@frozenwater'],
    'solar system':['@celestial'],
    'star':['@celestial'],
    'sun':['@hot','@celestial'],
    'turtle':['@oviparous'],
    'volcano':['@hot'],
    'water':['@liquidwater']
}

#this dictionary will keep track of the possible reactions
reactionDictionary={
    '@hot@liquidwater':[['steam'],"reason and justice tell me there's more love for humanity in electricity and steam than in chastity and vegetarianism - anton chekhov"],
    'ballrock':[['planet']],
    'rockwater':[['sand'],"I don't like sand. It's coarse and rough and irritating — and it gets everywhere. - anakin skywalker"],
    'electricitywater':[['oxygen','hydrogen']],
    'ballhydrogen':[['star'],'the sun is a mass of incandescent gas, a great big nuclear furnace - they might be giants'],
    'firesand':[['glass'],"elastic, hard, and brittle: glass presents properties that do not always seem compatible and yield unpleasant surprises - etienne guyon"],
    'firerock':[['lava'],"now I am alive with the ore of words pouring from my lips like molten lava glittering with joy - rumi"],
    'lava@liquidwater':[['steam','obsidian']],
    'lavarock':[['volcano']],
    'sandwater':[['ocean']],
    'gravityplanet':[['moon']],
    'moonocean':[['tide'],'the moon to the tide, i can feel you inside - amber benson'],
    'glasswater':[['ice']],
    'fireice':[['comet'],"some say the world will end in fire, some say in ice - robert frost"],
    'cometplanet':[['crater','nitrogen','amino acid']],
    'nitrogenoxygen':[['sky']],
    'craterwater':[['lake']],
    'skysteam':[['cloud']],
    'cloudwater':[['rain']],
    'skywater':[['rain']],
    'cloudice':[['snow']],
    'oceansand':[['beach']],
    'beachtide':[['starfish']],
    'oceanstar':[['starfish']],
    'skystarfish':[['star']],
    'cloudelectricity':[['lightning']],
    'gravitystar':[['solar system']],
    'ballgravity':[['black hole']],
    'solar systemstar':[['sun']],
    'cometstar':[['steam']],
    'cometsun':[['steam']],
    'lakevolcano':[['geyser']],
    'icerain':[['sleet'],"the four horsemen whose appearance foreshadows any public holiday are Storm, Gales, Sleet, and Contra-flow - terry pratchett"],
    'lightningsand':[['glass'],"they have a sign at the beach, 'no glass bottles'. i think that's so the other sand particles don't feel like underachievers - emo philips"],
    'oceanvolcano':[['island']],
    'geyserocean':[['hydrothermal vent']],
    'lavaocean':[['hydrothermal vent']],
    'firehydrogen':[['fire','fire','fire']],
    'beachglass':[['seaglass']],
    'glassocean':[['seaglass']],
    'carbon dioxideice':[['dry ice']],
    '@frozenwater@hot':[['water']],
    'sandsun':[['desert']],
    'amino acidhydrothermal vent':[['primordial soup']],
    'craterrain':[['lake']],
    'oceansun':[['cloud']],
    'rainsun':[['rainbow']],
    'cloudsun':[['sky']],
    'moonsun':[['eclipse'],"nations, like stars, are entitled to eclipse - victor hugo"],
    'hydrogenoxygen':[['fire','water']],
    'balllightning':[['ball lightning']],
    'hydrogenhydrogen':[['helium'],"hydrogen is built into helium at a temperature of millions of degrees - they might be giants"],
    'ballhelium':[['balloon']],
    'ballbeach':[['beach ball'],"beach balls at festivals are the work of the devil - gerard way"],
    'ballglass':[['crystal ball'],"he who lives by the crystal ball will learn to eat ground glass - anon"],
    'crystal ballsun':[['fire'],"when i bought my giant crystal ball the lady looked me in the eye and said 'whatever you do, never EVER leave it uncovered when youre not home' and i said 'oh wow because of spirits?' and she said 'what? no bc if the sun hits it weird it'll burn down your house'. important lesson - a tweet"],
    'glassrainbow':[['stained glass'],"if the body is a temple, then tattoos are its stained glass windows - sylvia plath"],
    'desertsnow':[['tundra']],
    'desertice':[['tundra']],
    'desertrain':[['plain']],
    'balloonhydrogen':[['blimp'],"it is a lot like inflating a blimp with a bicycle pump. anybody can do it. all it takes is time - kurt vonnegut"],
    'hydrothermal ventprimordial soup':[['microbe']],
    'oceanprimordial soup':[['plankton']],
    'fishstar':[['starfish']],
    'beachfish':[['dinosaur']],
    'microbeocean':[['plankton']],
    'desertlake':[['oasis']],
    'balloonwater':[['water balloon']],
    'microbeocean':[['fish']],
    'carbon dioxide@photosynthetic':[['oxygen']],
    'plainrain':[['grass'],'the rain in spain falls mainly on the plain - my fair lady'],
    'firelizard':[['salamander'],"the good fairy of my equilibrium, who banished the salamanders of my doubts and strengthened the lions of certainties - salvador dali"],
    'dinosaurdinosaur':[['lizard']],
    'dinosaursky':[['bird']],
    'birdtundra':[['penguin']],
    'eggtundra':[['penguin']],
    'birdrainbow':[['peacock']],
    'birdwater':[['duck']],
    'beachbird':[['gull']],
    'ball@oviparous':[['egg']],
    '@oviparous@oviparous':[['egg']],
    'beachegg':[['turtle']],
    'eggocean':[['fish']],
    'birdisland':[['dodo'],"but alas, we forget the dodo - aldous huxley"],
    'planetturtle':[['philosophy'],"it's turtles all the way down - anon"],
    'desertgrass':[['palm tree']],
    'rockrock':[['fire']],
    'starwater':[['starfish']],
    'planetwater':[['ocean']],
    'ballpalm tree':[['coconut'],"my friend thinks he's smart. he said onions are the only food that make you cry. so i threw a coconut at his face"],
    'rockstar':[['rock star']],
    'gravityocean':[['tide']],
    'oceansteam':[['hydrothermal vent']],
    'glasssteam':[['fog']],
    'islandisland':[['continent']],
    'islandrock':[['reef']],
    'islandvolcano':[['continent']],
    'planktonsun':[['plankton','plankton']],
    'lakeplankton':[['algae']],
    'dinosaurocean':[['plesiosaur']],
    'cometdinosaur':[['crater','death']],
    'sandsand':[['desert']],
    'beachsand':[['desert']],
    'fishgull':[['happy gull']],
    'birdocean':[['gull']],
    'glasslava':[['lava lamp'],"that's a big lava lamp. congratulations. - mitt romney"],
    'ballfire':[['fireball']],
    'ballball':[['testicles']],
    'ballsky':[['balloon']],
    'ballsnow':[['snowball']],
    'snowballsnowball':[['snowman'],"do you want to build a snowman? - anna"],
    'balloonsand':[['stress ball']],
    'eggfire':[['fried egg']],
    'eggisland':[['dodo']],
    'desertegg':[['rattlesnake'],"i do not think i have any uncharitable prejudice against the rattlesnake, still, i should not like to be one - herman melville"],
    'egglake':[['duck']],
    'oceantide':[['wave']],
    'tidewater':[['wave']],
    'sandwave':[['beach']],
    'desertwave':[['dune']],
    'skywave':[['cloud']],
    'icewave':[['glacier']],
    'lavawave':[['eruption']],
    'volcanowave':[['eruption']],
    'amino acidocean':[['plankton']],
    'amino acidamino acid':[['microbe']],
    'ballcrater':[['golf ball']],
    'gravityhydrogen':[['star']],
    'gravitynitrogen':[['sky']],
    'glasssand':[['hourglass']],
    'gravitysand':[['hourglass']],
    'gravityrock':[['planet']],
    'electricitysky':[['lightning']],
    'electricityball':[['ball lightning']],
    'electricityfire':[['short circuit']],
    'firesky':[['sun']],
    'fireoxygen':[['fire','fire']],
    'icesteam':[['water','water']],
    'lavasand':[['glass']],
    'iceice':[['vanilla ice']],
    'beachbeach':[['riverbed']],
    'waterwater':[['lake']],
    'lakelava':[['obsidian']],
    'philosophystained glass':[['religion']],
    'stress balltesticles':[['kink'],"ow"],
    'rainbowrainbow':[['double rainbow']],
    'oceansteam':[['fog']],
    '@celestial@celestial':[['gravity'],"i suppose i'll have to add the force of gravity to my list of enemies - lemony snicket"],
    'rainriverbed':[['river']],
    'riverbedwater':[['river']],
    'eggphilosophy':[['reincarnation']],
    'gravityrainbow':[['book']],
    'sunwave':[['light']],
    'coconutcoconut':[['horse'],"you've got two empty 'alves of coconuts and you're bangin' 'em together! - a castle guard"]
}

#this dictionary will keep track of the elements available in each category
elementDictionary = {}

#establish some starting elements
elementDictionary['force'] = ['fire','electricity']
elementDictionary['stuff'] = ['rock','water']
elementDictionary['shape'] = ['ball']
elementDictionary['?'] = []
elementDictionary['world'] = []
elementDictionary['weather'] = []
elementDictionary['object'] = []
elementDictionary['??'] = []
elementDictionary['animal'] = []
elementDictionary['plant'] = []
elementDictionary['human'] = []
elementDictionary['???'] = []
elementDictionary['tool'] = []
elementDictionary['product'] = []
elementDictionary['invention'] = []
elementDictionary['!!!'] = []
elementDictionary['vanity']=[]

         
#for clearing the widgets in frames

def clearE():
    # destroy all widgets from frame
    for widget in scrollableE.winfo_children():
       widget.destroy()
    canvasE.yview_moveto('0')


def clearF():
    # destroy all widgets from frame
    for widget in scrollableF.winfo_children():
       widget.destroy()

def clearA():
    # destroy all widgets from frame
    for widget in frameA.winfo_children():
       widget.destroy()

def clearB():
    # destroy all widgets from frame
    for widget in frameB.winfo_children():
       widget.destroy()

def clearG():
    # destroy all widgets from frame
    for widget in scrollableG.winfo_children():
       widget.pack_forget()

def clearH():
    # destroy all widgets from frame
    for widget in frameH.winfo_children():
       widget.destroy()

def drawH():
    clearH()
    mixButton = Button(master=frameH, text="Mix!", command=elGet)
    debugButton = Button(master=frameH, text="Debug", command=debugMode)
    if buttonsShown['vanity'] == 1:
        vanityButton = Button(master=frameH, text='Vanity', command=displayElementsVanity)
    elif buttonsShown['vanity'] > 1:
        vanityButton = Button(master=frameH, text='Vanity', bg = 'yellow', command=displayElementsVanity)
    saveButton = Button(master=frameH, text='Save', command=saveGame)
    loadButton = Button(master=frameH, text='Load', command=loadGame)
    mixButton.pack(padx=2,pady=2)
    saveButton.pack(padx=2,pady=2)
    loadButton.pack(padx=2,pady=2)
    if buttonsShown['vanity'] > 0:
        vanityButton.pack(padx=2,pady=2)
    debugButton.pack(padx=2,pady=2)

def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s ) 

def saveGame():
    clearG()
    saveFile = ""
    for type in elementDictionary:
        elementsKnown = elementDictionary[type]
        for el in elementsKnown:
            saveFile = saveFile+el+"6"
        saveFile=saveFile+"8"
    reactionLog.set("Game saved.")
    captionLog.set("")
    saveDisplay.delete("1.0","end")
    saveFile=rot13(saveFile)
    saveDisplay.insert(tk.INSERT, saveFile)
    saveDisplay.pack()

def loadSave():
    saveFile=saveDisplay.get('1.0','end')
    saveFile=rot13(saveFile)
    splitOne = saveFile.split('8')
    splitOne.pop()
    typeNum=0
    for type in elementDictionary:
        splitTwo=splitOne[typeNum].split('6')
        splitTwo.pop()
        elementDictionary[type]=splitTwo
        if len(splitTwo) > 0:
            buttonsShown[type]=1
        typeNum=typeNum+1
    drawA()
    drawB()
    clearE()
    clearF()
    clearG()
    reactionLog.set("Game loaded from savefile.")
    captionLog.set("")
    logLabel.pack()
    captionLabel.pack()

def loadGame():
    clearG()
    loadSaveButton = Button(master=scrollableG, text='Load Save', command=loadSave)   
    loadSaveButton.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    saveDisplay.delete("1.0","end")
    saveDisplay.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
    saveFile = "fire6electricity68rock6water6sand6glass68ball68888888888crystal ball688888"


def drawA():
    clearA()
    #create the left-side category buttons
    buttonsA = []
    for i in range(4):
        frameA.columnconfigure(i, weight=1)
        frameA.rowconfigure(i, weight=1)

        for j in range(4):
            elementNum=4*i+j
            z=elementTypes[elementNum]
            frame = tk.Frame(
                master=frameA,
                relief=tk.RAISED,
                borderwidth=1
            )
            if buttonsShown[z] > 0:
                frame.grid(row=i, column=j, padx=5, pady=5)
                if buttonsShown[z] > 1:
                    buttonsA.append(Button(master=frame, width=75, height=75, bg='yellow', text=z, command= lambda ztemp=z : displayElementsLeft(ztemp)))
                else:
                    buttonsA.append(Button(master=frame, width=75, height=75, text=z, command= lambda ztemp=z : displayElementsLeft(ztemp)))
                buttonsA[elementNum].pack(padx=2,pady=2)
            else:
                buttonsA.append(0)


def drawB():
    clearB()
    #create the right-side category buttons
    buttonsB = []

    for i in range(4):
        frameB.columnconfigure(i, weight=1)
        frameB.rowconfigure(i, weight=1)

        for j in range(4):
            elementNum=4*i+j
            z=elementTypes[elementNum]
            frame = tk.Frame(
                master=frameB,
                relief=tk.RAISED,
                borderwidth=1
            )
            if buttonsShown[z] > 0:
                frame.grid(row=i, column=j, padx=5, pady=5)
                if buttonsShown[z] > 1:
                    buttonsB.append(Button(master=frame, width=75, height=75, bg='yellow', text=z, command= lambda ztemp=z : displayElementsRight(ztemp)))
                else:
                    buttonsB.append(Button(master=frame, width=75, height=75, text=z, command= lambda ztemp=z : displayElementsRight(ztemp)))
                buttonsB[elementNum].pack(padx=2,pady=2)
            else:
                buttonsB.append(0)


#display the radio buttons as requested

def displayElementsLeft(type):
    clearE()
    if buttonsShown[type] > 1:
        buttonsShown[type]=1
        drawA()
        drawB()
    elementList = elementDictionary[type]
    for element in elementList:
        r = ttk.Radiobutton(
            master=scrollableE,
            text=element,
            value=element,
            variable=elementLeft
        )
        r.pack(fill='x', padx=5, pady=5)
    #frameE.config(width=100)

def displayElementsRight(type):
    clearF()
    if buttonsShown[type] > 1:
        buttonsShown[type]=1
        drawA()
        drawB()
    elementList = elementDictionary[type]
    for element in elementList:
        r = ttk.Radiobutton(
            master=scrollableF,
            text=element,
            value=element,
            variable=elementRight
        )
        r.pack(fill='x', padx=5, pady=5)

def displayElementsVanity():
    clearG()
    if buttonsShown['vanity'] > 1:
        buttonsShown['vanity']=1
        drawH()
    vanityLabel = tk.Label(master=scrollableG, text='Vanity elements unlocked: '+ str(len(elementDictionary['vanity'])) +'/'+str(vanitymax))
    vanityLabel.pack(fill='x', padx=5, pady=10)
    elementList = elementDictionary['vanity']
    for element in elementList:
        vanityLabel = tk.Label(master=scrollableG, text=element)
        vanityLabel.pack(fill='x', padx=5, pady=5)


#perform the reaction between two selected elements


def elGet():
    elA = elementLeft.get()
    elB = elementRight.get()
    elReact(elA,elB)

def elReact(elA,elB):
    success = doReact(elA,elB)
    if success == 0:
        if elA in bucketDictionary:
            bucketsA=bucketDictionary[elA]
            bucketsA.append(elA)
        else:
            bucketsA=[elA]
        if elB in bucketDictionary:
            bucketsB=bucketDictionary[elB]
            bucketsB.append(elB)
        else:
            bucketsB=[elB]

        for newElA in bucketsA:
            for newElB in bucketsB:
                if not ((newElA == elA and newElB==elB) or success>0):
                    trial = doReact(newElA,newElB)
                    success = success+trial
    if success > 0:
        global logAppendix
        logText=elA + " and " + elB + " reacted to create "+logAppendix
        reactionLog.set(logText)
    else:
        print(elA, " and ", elB, " did not react")


        
        

def doReact(elA,elB):
    reaction = elA+elB
    isCaption = 0
    success = 0
    global logAppendix
    if reaction in reactionDictionary:
        output = reactionDictionary[reaction][0]
        success=1
        conjunctioncounter = 0
        logAppendix = ""
        for element in output:
            addEl(element)
            if conjunctioncounter > 0:
                logAppendix=logAppendix+" and "
            logAppendix=logAppendix+element
            conjunctioncounter=conjunctioncounter+1
        if len(reactionDictionary[reaction]) > 1:
            isCaption=1
            captionLog.set(reactionDictionary[reaction][1])
    elif elB+elA in reactionDictionary:
        reaction=elB+elA
        output = reactionDictionary[reaction][0]
        success=1
        conjunctioncounter = 0
        logAppendix = ""
        for element in output:
            addEl(element)
            if conjunctioncounter > 0:
                logAppendix=logAppendix+" and "
            logAppendix=logAppendix+element
            conjunctioncounter=conjunctioncounter+1
        if len(reactionDictionary[reaction]) > 1:
            isCaption=1
            captionLog.set(reactionDictionary[reaction][1])
    clearG()
    #reaction log
    logLabel = tk.Label(master=scrollableG, textvariable=reactionLog)
    logLabel.pack()
    if isCaption > 0:
        captionLabel = tk.Message(master=scrollableG, textvariable=captionLog,font=("TkDefaultFont",12,"italic"))
        captionLabel.pack()
    if success==1:
        return 1
    else:
        return 0

#add an element if it doesn't already exist
def addEl(element):
    elType = typeDictionary[element]
    if element not in (elementDictionary[elType]):
        elementDictionary[elType].append(element)
        buttonsShown[elType]=2
        drawA()
        drawB()
        drawH()
        clearE()
        clearF()

def debugMode():
    for element in typeDictionary:
        addEl(element)


drawA()
drawB()

#put our frames into the window (top half)

frameA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frameE.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frameB.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
frameF.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

#add scrolling parts
canvasE.pack(side="left", fill="both", expand=True)
scrollbarE.pack(side="right", fill="y")
canvasF.pack(side="left", fill="both", expand=True)
scrollbarF.pack(side="right", fill="y")
canvasG.pack(side="left", fill="both", expand=True)
scrollbarG.pack(side="right", fill="y")

#lower buttons
mixButton = Button(master=frameH, text="Mix!", command=elGet)
debugButton = Button(master=frameH, text="Debug", command=debugMode)
vanityButton = Button(master=frameH, text='Vanity', command=displayElementsVanity)
saveButton = Button(master=frameH, text='Save', command=saveGame)
loadButton = Button(master=frameH, text='Load', command=loadGame)

#fill in frame C
frameH.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
frameG.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
mixButton.pack(padx=2,pady=2)
saveButton.pack(padx=2,pady=2)
loadButton.pack(padx=2,pady=2)
debugButton.pack(padx=2,pady=2)
logLabel.pack()
captionLabel.pack()

#put our top and bottom frames into the window
frameD.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
frameC.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

#count total number of vanity elements
vanitymax = 0
for element in typeDictionary:
    if typeDictionary[element] == 'vanity':
        vanitymax = vanitymax+1

#and now actually run
window.mainloop()