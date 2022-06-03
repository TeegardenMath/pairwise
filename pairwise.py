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
    'algae':['plant',0],
    'amino acid':['object',0],
    'ball':['shape',1],
    'ball lightning':['weather',0],
    'balloon':['product',0],
    'beach':['world',0],
    'beach ball':['product',0],
    'seaglass':['vanity',0],
    'bird':['animal',0],
    'black hole':['world',0],
    'blimp':['product',0],
    'book':['object',0],
    'carbon dioxide':['stuff',0],
    'cloud':['weather',0],
    'coconut':['object',0],
    'comet':['world',0],
    'continent':['world',0],
    'crater':['world',0],
    'crystal ball':['tool',0],
    'death':['force',0],
    'desert':['world',0],
    'dinosaur':['animal',0],
    'dodo':['animal',0],
    'double rainbow':['weather',0],
    'dry ice':['stuff',0],
    'duck':['animal',0],
    'dune':['world',0],
    'eclipse':['weather',0],
    'egg':['object',0],
    'electricity':['force',1],
    'eruption':['weather',0],
    'fire':['force',1],
    'fireball':['vanity',0],
    'fish':['animal',0],
    'fog':['weather',0],
    'fried egg':['vanity',0],
    'geyser':['world',0],
    'glacier':['world',0],
    'glass':['stuff',0],
    'golf ball':['vanity',0],
    'grass':['plant',0],
    'gravity':['force',0],
    'gull':['animal',0],
    'happy gull':['vanity',0],
    'helium':['stuff',0],
    'horse':['animal',0],
    'hourglass':['product',0],
    'hydrogen':['stuff',0],
    'hydrothermal vent':['world',0],
    'ice':['stuff',0],
    'island':['world',0],
    'kink':['invention',0],
    'lake':['world',0],
    'lava':['stuff',0],
    'lava lamp':['vanity',0],
    'light':['force',0],
    'lightning':['weather',0],
    'lizard':['animal',0],
    'microbe':['animal',0],
    'moon':['world',0],
    'nitrogen':['stuff',0],
    'oasis':['world',0],
    'obsidian':['stuff',0],
    'ocean':['world',0],
    'oxygen':['stuff',0],
    'palm tree':['plant',0],
    'peacock':['animal',0],
    'penguin':['animal',0],
    'philosophy':['invention',0],
    'plain':['world',0],
    'planet':['world',0],
    'plankton':['plant',0],
    'plesiosaur':['animal',0],
    'primordial soup':['stuff',0],
    'rain':['weather',0],
    'rainbow':['weather',0],
    'rattlesnake':['animal',0],
    'reef':['world',0],
    'reincarnation':['invention',0],
    'religion':['invention',0],
    'river':['world',0],
    'riverbed':['world',0],
    'rock':['stuff',1],
    'rock star':['human',0],
    'salamander':['animal',0],
    'sand':['stuff',0],
    'short circuit':['vanity',0],
    'sky':['world',0],
    'sleet':['weather',0],
    'snow':['weather',0],
    'snowball':['object',0],
    'snowman':['product',0],
    'solar system':['world',0],
    'stained glass':['product',0],
    'star':['world',0],
    'starfish':['animal',0],
    'steam':['stuff',0],
    'stress ball':['object',0],
    'sun':['world',0],
    'testicles':['object',0],
    'tide':['weather',0],
    'tundra':['world',0],
    'turtle':['animal',0],
    'vanilla ice':['vanity',0],
    'volcano':['world',0],
    'water':['stuff',1],
    'water balloon':['vanity',0],
    'wave':['shape',0],
    'wolf':['animal',0]
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

bucketList=[
    "@celestial",
    "@frozenwater"
    "@hot",
    "@liquidwater",
    "@oviparous",
    "@photosynthetic"
]

reactDict={
    'amino acid':{
        'hydrothermal vent':[0,['primordial soup'],""],
        'ocean':[0,['plankton'],""],
        'amino acid':[0,['microbe'],""]
    },
    'ball':{
        'ball':[0,['testicles'],""],
        'beach':[0,['beach ball'],"beach balls at festivals are the work of the devil - gerard way"],
        'crater':[0,['golf ball'],""],
        'fire':[0,['fireball'],""],
        'glass':[0,['crystal ball'],"he who lives by the crystal ball will learn to eat ground glass - anon"],
        'gravity':[0,['black hole'],""],
        'helium':[0,['balloon'],""],
        'hydrogen':[0,['star'],'the sun is a mass of incandescent gas, a great big nuclear furnace - they might be giants'],
        'lightning':[0,['ball lightning'],""],
        'palm tree':[0,['coconut'],"my friend thinks he's smart. he said onions are the only food that make you cry. so i threw a coconut at his face"],
        'rock':[0,['planet'],""],
        'sky':[0,['balloon'],""],
        'snow':[0,['snowball'],""],
        '@oviparous':[0,['egg'],""]     
    },
    'balloon':{
        'hydrogen':[0,['blimp'],"it is a lot like inflating a blimp with a bicycle pump. anybody can do it. all it takes is time - kurt vonnegut"],
        'sand':[0,['stress ball'],""],
        'water':[0,['water balloon'],""]
    },
    'beach':{
        'beach':[0,['riverbed'],""],
        'bird':[0,['gull'],""],
        'egg':[0,['turtle'],""],
        'fish':[0,['dinosaur'],""],
        'glass':[0,['seaglass'],""],
        'sand':[0,['desert'],""],
        'tide':[0,['starfish'],""]
    },
    'bird':{
        'island':[0,['dodo'],"but alas, we forget the dodo - aldous huxley"],
        'ocean':[0,['gull'],""],
        'rainbow':[0,['peacock'],""],
        'tundra':[0,['penguin'],""],
        'water':[0,['duck'],""]
    },
    'carbon dioxide':{
        'ice':[0,['dry ice'],""],
        '@photosynthetic':[0,['oxygen'],""]
    },
    'cloud':{
        'electricity':[0,['lightning'],""],
        'ice':[0,['snow'],""],
        'sun':[0,['sky'],""],
        'water':[0,['rain'],""]
    },
    'coconut':{
        'coconut':[0,['horse'],"you've got two empty 'alves of coconuts and you're bangin' 'em together! - a castle guard"]
    },
    'comet':{
        'dinosaur':[0,['crater','death'],""],
        'planet':[0,['crater','nitrogen','amino acid'],""],
        'star':[0,['steam'],""],
        'sun':[0,['steam'],""]
    },
    'crater':{
        'rain':[0,['lake'],""],
        'water':[0,['lake'],""]
    },
    'crystal ball':{
        'sun':[0,['fire'],"when i bought my giant crystal ball the lady looked me in the eye and said 'whatever you do, never EVER leave it uncovered when youre not home' and i said 'oh wow because of spirits?' and she said 'what? no bc if the sun hits it weird it'll burn down your house'. important lesson - a tweet"]
    },
    'desert':{
        'egg':[0,['rattlesnake'],"i do not think i have any uncharitable prejudice against the rattlesnake, still, i should not like to be one - herman melville"],
        'ice':[0,['tundra'],""],
        'grass':[0,['palm tree'],""],
        'lake':[0,['oasis'],""],
        'rain':[0,['plain'],""],
        'snow':[0,['tundra'],""],
        'wave':[0,['dune'],""]
    },
    'dinosaur':{
        'dinosaur':[0,['lizard'],""],
        'ocean':[0,['plesiosaur'],""],
        'sky':[0,['bird'],""]
    },
    'egg':{
        'fire':[0,['fried egg'],""],
        'island':[0,['dodo'],""],
        'lake':[0,['duck'],""],
        'ocean':[0,['fish'],""],
        'philosophy':[0,['reincarnation'],""],
        'tundra':[0,['penguin'],""]
    },
    'electricity':{
        'ball':[0,['ball lightning'],""],
        'fire':[0,['short circuit'],""],
        'sky':[0,['lightning'],""],
        'water':[0,['oxygen','hydrogen'],""]
    },
    'fire':{
        'hydrogen':[0,['fire','fire','fire'],""],
        'ice':[0,['comet'],"some say the world will end in fire, some say in ice - robert frost"],
        'lizard':[0,['salamander'],"the good fairy of my equilibrium, who banished the salamanders of my doubts and strengthened the lions of certainties - salvador dali"],
        'oxygen':[0,['fire','fire'],""],
        'rock':[0,['lava'],"now I am alive with the ore of words pouring from my lips like molten lava glittering with joy - rumi"],
        'sand':[0,['glass'],"elastic, hard, and brittle: glass presents properties that do not always seem compatible and yield unpleasant surprises - etienne guyon"],
        'sky':[0,['sun'],""]
    },
    'fish':{
        'gull':[0,['happy gull'],""],
        'star':[0,['starfish'],""]
    },
    'geyser':{
        'ocean':[0,['hydrothermal vent'],""]
    },
    'glass':{
        'lava':[0,['lava lamp'],"that's a big lava lamp. congratulations. - mitt romney"],
        'ocean':[0,['seaglass'],""],
        'rainbow':[0,['stained glass'],"if the body is a temple, then tattoos are its stained glass windows - sylvia plath"],
        'sand':[0,['hourglass'],""],
        'steam':[0,['fog'],""],
        'water':[0,['ice'],""]
    },
    'gravity':{
        'hydrogen':[0,['star'],""],
        'nitrogen':[0,['sky'],""],
        'ocean':[0,['tide'],""],
        'planet':[0,['moon'],""],
        'rainbow':[0,['book'],""],
        'rock':[0,['planet'],""],
        'sand':[0,['hourglass'],""],
        'star':[0,['solar system'],""]
    },
    'hydrogen':{
        'hydrogen':[0,['helium'],"hydrogen is built into helium at a temperature of millions of degrees - they might be giants"],
        'oxygen':[0,['fire','water'],""]
    },
    'hydrothermal vent':{
        'primordial soup':[0,['microbe'],""]
    },
    'ice':{
        'ice':[0,['vanilla ice'],""],
        'rain':[0,['sleet'],"the four horsemen whose appearance foreshadows any public holiday are Storm, Gales, Sleet, and Contra-flow - terry pratchett"],
        'steam':[0,['water','water'],""],
        'wave':[0,['glacier'],""]
    },
    'island':{
        'island':[0,['continent'],""],
        'rock':[0,['reef'],""],
        'volcano':[0,['continent'],""]
    },
    'lake':{
        'plankton':[0,['algae'],""],
        'volcano':[0,['geyser'],""]
    },
    'lava':{
        'ocean':[0,['hydrothermal vent'],""],
        'rock':[0,['volcano'],""],
        'sand':[0,['glass'],""],
        'wave':[0,['eruption'],""],
        '@liquidwater':[0,['steam','obsidian'],""]
    },
    'lightning':{
        'sand':[0,['glass'],"they have a sign at the beach, 'no glass bottles'. i think that's so the other sand particles don't feel like underachievers - emo philips"]
    },
    'microbe':{
        'ocean':[0,['fish'],""]
    },
    'moon':{
        'moon':[0,['wolf'],"oh shit who brought fucking moon moon along? - anon"],
        'ocean':[0,['tide'],"the moon to the tide, i can feel you inside - amber benson"],
        'sun':[0,['eclipse'],"nations, like stars, are entitled to eclipse - victor hugo"]
    },
    'nitrogen':{
        'oxygen':[0,['sky'],""]
    },
    'ocean':{
        'primordial soup':[0,['plankton'],""],
        'sand':[0,['beach'],""],
        'star':[0,['starfish'],""],
        'steam':[0,['hydrothermal vent'],""],
        'sun':[0,['cloud'],""],
        'tide':[0,['wave'],""],
        'volcano':[0,['island'],""]
    },
    'philosophy':{
        'stained glass':[0,['religion'],""]
    },
    'plain':{
        'rain':[0,['grass'],"the rain in spain falls mainly on the plain - my fair lady"]
    },
    'planet':{
        'turtle':[0,['philosophy'],"it's turtles all the way down - anon"],
        'water':[0,['ocean'],""]
    },
    'plankton':{
        'sun':[0,['plankton','plankton'],""]
    },
    'rain':{
        'riverbed':[0,['river'],""],
        'sun':[0,['rainbow'],""],
        'water':[0,['river'],""]
    },
    'rainbow':{
        'rainbow':[0,['double rainbow'],""]
    },
    'rock':{
        'rock':[0,['fire'],""],
        'star':[0,['rock star'],""],
        'water':[0,['sand'],"I don't like sand. It's coarse and rough and irritating — and it gets everywhere. - anakin skywalker"]
    },
    'sand':{
        'sand':[0,['desert'],""],
        'sun':[0,['desert'],""],
        'water':[0,['ocean'],""],
        'wave':[0,['dune'],""]
    },
    'sky':{
        'starfish':[0,['star'],""],
        'steam':[0,['cloud'],""],
        'water':[0,['rain'],""]
    },
    'snowball':{
        'snowball':[0,['snowman'],"do you want to build a snowman? - anna"]
    },
    'solar system':{
        'star':[0,['sun'],""]
    },
    'star':{
        'water':[0,['starfish'],""]
    },
    'stress ball':{
        'testicles':[0,['kink'],"ow."]
    },
    'sun':{
        'wave':[0,['light'],""]
    },
    'tide':{
        'water':[0,['wave'],""]
    },
    'volcano':{
        'wave':[0,['eruption'],""]
    },
    'water':{
        'water':[0,['lake'],""]
    },
    '@celestial':{
        '@celestial':[0,['gravity'],"i suppose i'll have to add the force of gravity to my list of enemies - lemony snicket"]
    },
    '@frozenwater':{
        '@hot':[0,['water'],""]
    },
    '@hot':{
        '@liquidwater':[0,['steam'],"reason and justice tell me there's more love for humanity in electricity and steam than in chastity and vegetarianism - anton chekhov"]
    },
    '@oviparous':{
        '@oviparous':[0,['egg'],""]
    }
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


#let's make sure all reactions work both ways

def reverseReacts():
    #first let's make sure every element is in the dictionary
    for el in typeDictionary:
        if el not in reactDict:
            reactDict[el]={}
    for bucket in bucketList:
        if bucket not in reactDict:
            reactDict[bucket]={}
    for elA in reactDict:
        for elB in reactDict[elA]:
            #we're looking at each existing reaction
            output = reactDict[elA][elB][1]
            quote = reactDict [elA][elB][2]
            tempDict={elA:[0,output,quote]}
            reactDict[elB].update(tempDict)
            
         
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
        if typeDictionary[element][1]==1:
            r = ttk.Radiobutton(
                master=scrollableE,
                text=element,
                value=element,
                variable=elementLeft
            )
            r.pack(fill='x', padx=5, pady=5)
    for element in elementList:
        if typeDictionary[element][1]==0:
            r=tk.Label(master=scrollableE,text=element)
            r.pack(fill='x',padx=5,pady=5)
    #frameE.config(width=100)

def displayElementsRight(type):
    clearF()
    if buttonsShown[type] > 1:
        buttonsShown[type]=1
        drawA()
        drawB()
    elementList = elementDictionary[type]
    for element in elementList:
        if typeDictionary[element][1]==1:
            r = ttk.Radiobutton(
                master=scrollableE,
                text=element,
                value=element,
                variable=elementLeft
            )
            r.pack(fill='x', padx=5, pady=5)
    for element in elementList:
        if typeDictionary[element][1]==0:
            r=tk.Label(master=scrollableE,text=element)
            r.pack(fill='x',padx=5,pady=5)

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
        clearE()
        clearF()
    else:
        print(elA, " and ", elB, " did not react")


def hasMatches(el):
    if el not in reactDict:
        return False
    for elB in reactDict[el]:
        if reactDict[el][elB][0] == 0:
            return True
    return False
    
def checkMatches(el):
    if hasMatches(el):
        typeDictionary[el][1]=1
    else:
        typeDictionary[el][1]=0
        

def doReact(elA,elB):
    canReact = 0
    isCaption = 0
    if elA in reactDict:
        if elB in reactDict[elA]:
            canReact = 1
    global logAppendix
    if canReact == 1:
        output = reactDict[elA][elB][1]
        reactDict[elA][elB][0]=1
        checkMatches(elA)
        checkMatches(elB)
        conjunctioncounter = 0
        logAppendix = ""
        for element in output:
            addEl(element)
            if conjunctioncounter > 0:
                logAppendix=logAppendix+" and "
            logAppendix=logAppendix+element
            conjunctioncounter=conjunctioncounter+1
        if len(reactDict[elA][elB]) > 2:
            isCaption=1
            captionLog.set(reactDict[elA][elB][2])
    clearG()
    #reaction log
    logLabel = tk.Label(master=scrollableG, textvariable=reactionLog)
    logLabel.pack()
    if isCaption > 0:
        captionLabel = tk.Message(master=scrollableG, textvariable=captionLog,font=("TkDefaultFont",12,"italic"))
        captionLabel.pack()
    if canReact==1:
        return 1
    else:
        return 0

#add an element if it doesn't already exist
def addEl(element):
    elType = typeDictionary[element][0]
    if element not in (elementDictionary[elType]):
        checkMatches(element)
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
    if typeDictionary[element][0] == 'vanity':
        vanitymax = vanitymax+1

#set up our reaction dictionary
reverseReacts()

#and now actually run
window.mainloop()