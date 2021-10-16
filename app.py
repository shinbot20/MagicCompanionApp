import tkinter as tk


def createnew():
    new = tk.Toplevel(window)
    three_var = tk.Button(new, text='three cards', highlightbackground = '#c6e2e9', command = three)
    two_var = tk.Button(new, text='two cards', highlightbackground = '#c6e2e9', command = two)
    one_var = tk.Button(new, text='one card', highlightbackground = '#c6e2e9', command = one)
    three_var.grid(row=0, column=0)
    two_var.grid(row=1, column=0)
    one_var.grid(row=2, column=0)


def history():
    new = tk.Toplevel(window)
    new.title('History')
    turnhistory = tk.Text(new, font = ('Times New Roman', 20))
    turnhistory.pack()
    turnnum = int(historyentry.get())-1
    content = turnlist[turnnum]
    turnhistory.insert(tk.END, content)


def createnote():
    new = tk.Toplevel(window)
    new.title('Notes')
    label = tk.Label(new, text = 'Notes')
    label.pack()
    notes = tk.Text(new, font = ('Times New Roman', 20))
    notes.pack()
    

def one():
    def factorial(a):
        fact=1
        for i in range(1, int(a)+1):
            fact*=i
        return fact

    def combination(B, b):
	    return factorial(int(B))/(factorial(int(b))*factorial(int(B)-int(b)))

    def min(a,b):
	    if(int(a)<=int(b)):
		    return int(a)
	    else:
		    return int(b)

    def cumulativeprob():
        cumulative=0
        needed = int(card1num.get())
        numA = int(card1total.get())
        decksize = int(onedecksize.get())
        drawsize = int(onedrawn.get())
        for i in range (needed, min(numA, drawsize)+1):
            cumulative = cumulative+hypgeomdist(i, drawsize, numA, decksize)
        onepercentage.delete('0', tk.END)
        onepercentage.insert('0', cumulative)
    
    def hypgeomdist(needed, drawsize, numA, decksize): 
        total= (combination(numA,needed)*combination((decksize-numA),(drawsize-needed)))/combination(decksize,drawsize)
        return total    
    onevarwindow = tk.Toplevel(window)

    card1label = tk.Label(onevarwindow, text='Card 1: ')
    cardoneneededlabel = tk.Label(onevarwindow, text='Number needed: ')
    card1totallabel = tk.Label(onevarwindow, text='Number of cards in deck:')
    onedecksizelabel = tk.Label(onevarwindow, text='Size of deck:')
    onedrawnlabel = tk.Label(onevarwindow, text='Num cards drawn: ')

    card1num = tk.Entry(onevarwindow)
    onedecksize = tk.Entry(onevarwindow)
    card1total = tk.Entry(onevarwindow)    
    onedrawn = tk.Entry(onevarwindow)
    onebutton = tk.Button(onevarwindow, text='calculate', command = cumulativeprob)
    onepercentage = tk.Entry(onevarwindow)


    cardoneneededlabel.grid(row = 0, column=1)
    card1totallabel.grid(row = 0, column = 2)
    card1label.grid(row = 1, column = 0)
    card1num.grid(row = 1, column = 1)
    card1total.grid(row = 1, column = 2)
    onedecksizelabel.grid(row = 2, column = 0)
    onedecksize.grid(row = 2, column = 1)
    onedrawnlabel.grid(row = 3, column = 0)
    onedrawn.grid(row = 3, column = 1)
    onebutton.grid(row = 4, column=0)
    onepercentage.grid(row = 4, column=1)    


def two():
    def factorial(a):
	    fact=1
	    for i in range(1, int(a)+1):
		    fact*=i
	    return fact

    def combination(B, b):
	    return factorial(int(B))/(factorial(int(b))*factorial(int(B)-int(b)))

    def min(a,b):
	    if(int(a)<=int(b)):
		    return int(a)
	    else:
		    return int(b)
    def twocardslarger(numA,numB,needA,needB, decksize,drawn):
        prob=0
        for i in range(needA,drawn-1+1):
            for j in range(needA, min(numB, drawn-i)+1):
                prob+=combination(numA,i)*combination(numB, j)*combination(decksize-numA-numB, drawn-i-j)/combination(decksize, drawn)
        ans.delete('0', tk.END)
        ans.insert(prob, tk.END)

    def twocardssmaller(numA,numB,needA,needB,decksize,drawn):
        prob=0
        for i in range(needA,numA+1):
            for j in range(needA, min(numB,decksize-i)+1):
                prob+=combination(numA,i)*combination(numB, j)*combination(decksize-numA-numB, drawn-i-j)/combination(decksize, drawn)
        ans.delete('0', tk.END)
        ans.insert('0', prob)


    def twocards():
        numA = int(card1total.get())
        numB = int(card2total.get())
        needA = int(card1.get())
        needB = int(card2.get())
        decksize =int(twonumcards.get())
        drawn = int(numdrawn.get())
        if(numA>drawn or numB>drawn):
            return twocardslarger(numA,numB,needA,needB,decksize,drawn)
        else:
            return twocardssmaller(numA,numB,needA,needB,decksize,drawn)


    twowindow = tk.Toplevel(window)


    name1 = tk.Label(twowindow, text='Card 1:')
    name2 = tk.Label(twowindow, text='Card 2:')
    needlabel = tk.Label(twowindow, text='Number needed: ')
    inlabel = tk.Label(twowindow, text='Number of cards in deck:')
    twodecksize_label = tk.Label(twowindow, text='Size of deck:')
    drawnlabel = tk.Label(twowindow, text='Cards drawn: ')


    card1 = tk.Entry(twowindow)
    card2 = tk.Entry(twowindow)
    twonumcards = tk.Entry(twowindow)
    card1total = tk.Entry(twowindow)
    card2total = tk.Entry(twowindow)
    numdrawn = tk.Entry(twowindow)
    button = tk.Button(twowindow, text='calculate', command = twocards)
    ans = tk.Entry(twowindow)
    
    name1.grid(row=1, column=0)
    name2.grid(row=2,column=0)
    twodecksize_label.grid(row=3, column=0)
    needlabel.grid(row=0, column=1)
    inlabel.grid(row=0,column=2)
    card1.grid(row=1, column=1)
    card2.grid(row=2, column=1)
    card1total.grid(row=1, column=2)
    card2total.grid(row=2, column=2)
    twonumcards.grid(row=3, column=1)
    drawnlabel.grid(row=4, column=0)
    numdrawn.grid(row=4, column=1)
    button.grid(row=5, column=0)
    ans.grid(row=5, column=1)


def three():
    def factorial(a):
	    fact=1
	    for i in range(1, int(a)+1):
		    fact*=i
	    return fact

    def combination(B, b):
	    return factorial(int(B))/(factorial(int(b))*factorial(int(B)-int(b)))

    def min(a,b):
	    if(int(a)<=int(b)):
		    return int(a)
	    else:
		    return int(b)
    def threecardssmaller(numA, numB,numC,needA,needB,needC,decksize,drawn):
        prob=0
        for i in range(needA,numA+1):
            for j in range(needB, numB+1):
                for k in range(1, min(numC, drawn-i-j)+1):
                    prob+=combination(numA, i)*combination(numB, j)*combination(4,k)*combination(decksize-numA-numB-numC,drawn-i-j-k)/combination(decksize,drawn)
        return prob

    def threecardslarger(numA,numB,numC,needA,needB,needC, decksize,drawn):
        prob=0
        for i in range(needA, drawn-2+1):
            for j in range(needB, drawn-1-i+1):
                for k in range(needC, drawn-i-j+1):
                    prob+=combination(numA,i)*combination(numB,j)*combination(numC, k)*combination(decksize-numA-numB-numC, drawn-i-j-k)/combination(decksize, drawn)
        return prob
    def three():
        numA = int(threetotalcard1neededentry.get())
        numB = int(threetotalcard2neededentry.get())
        numC = int(threetotalcard3neededentry.get())
        needA = int(threecard1neededentry.get())
        needB = int(threecard2neededentry.get())
        needC = int(threecard3neededentry.get())
        decksize = int(threenumcards.get())
        drawn = int(threedrawnentry.get())
        if((numA+numB)>drawn or (numA)>drawn or numB>drawn):
            threepercentage.delete('0', tk.END)
            
            threepercentage.insert('0',round(threecardslarger(numA,numB, numC, needA,needB, needC, decksize, drawn), 4))
            
        else:
            threepercentage.delete('0', tk.END)
            threepercentage.insert('0',round(threecardssmaller(numA,numB, numC,needA,needB,needC, decksize, drawn), 4))
    
    threewindow = tk.Toplevel(window)
    threecard1_label = tk.Label(threewindow, text='Card 1: ')
    threecard2_label = tk.Label(threewindow, text='Card 2: ')
    threecard3_label = tk.Label(threewindow, text='Card 3: ')
    threecardsneeded = tk.Label(threewindow, text='Number needed: ')
    threecardtotal = tk.Label(threewindow, text='Number of cards in deck:')
    threedecksize_label = tk.Label(threewindow, text='Size of deck:')
    threecard1neededentry = tk.Entry(threewindow)
    threecard2neededentry = tk.Entry(threewindow)
    threecard3neededentry = tk.Entry(threewindow)
    threenumcards = tk.Entry(threewindow)
    threetotalcard1neededentry = tk.Entry(threewindow)
    threetotalcard2neededentry = tk.Entry(threewindow)
    threetotalcard3neededentry = tk.Entry(threewindow)
    threedrawncards = tk.Label(threewindow, text='Cards drawn: ')
    threedrawnentry = tk.Entry(threewindow)
    threecalculate_button = tk.Button(threewindow, text='calculate', command = three)
    threelabel = tk.Label(threewindow, text = "The probability of getting the combination is:")
    threepercentage = tk.Entry(threewindow)

    threecard1_label.grid(row=1, column=0)
    threecard2_label.grid(row=2,column=0)
    threecard3_label.grid(row=3,column=0)
    threedecksize_label.grid(row=4, column=0)
    threecardsneeded.grid(row=0, column=1)
    threecardtotal.grid(row=0,column=2)
    threecard1neededentry.grid(row=1, column=1)
    threecard2neededentry.grid(row=2, column=1)
    threecard3neededentry.grid(row=3, column=1)
    threetotalcard1neededentry.grid(row=1, column=2)
    threetotalcard2neededentry.grid(row=2, column=2)
    threetotalcard3neededentry.grid(row=3, column=2)
    threenumcards.grid(row=4, column=1)
    threedrawncards.grid(row=5, column=0)
    threedrawnentry.grid(row=5, column=1)
    threecalculate_button.grid(row=6, column=0)
    threelabel.grid(row = 6, column = 1)
    threepercentage.grid(row=6, column=2)  

#changing life
def increasevalue():
    value = int(life["text"])
    life["text"] = f"{value + 1}"


def decreasevalue():
    value = int(life["text"])
    life["text"] = f"{value - 1}"

#changing turn
def incrementturn():
    value = int(turncount["text"])
    turncount["text"] = f"{value + 1}"
    tuple = ('turn:', value, 'play:', playlist, 'grave:', gravelist, 'exile:', exilelist)
    turnlist.append(tuple)
    print(tuple)

#functions to help move between lists
def movedeckinplay(name):
    pos1=0
    pos2=0
    length1 = len(decklist)
    for i in range(0,length1):
        if(decklist[i][1]==name):
            num = int(decklist[i][0])-1
            decklist[i] = (num, name)
    playlist.append((1,name))
    for j in range(0, length1):
        if(decklist[j][0]==0):
            pos2=j
    decklist.pop(pos2)
    reflectplay()
    reflectdeck()

def movedeckgrave(name):
    pos1=0
    pos2=0
    length1 = len(decklist)
    for i in range(0,length1):
        if(decklist[i][1]==name):
            num = int(decklist[i][0])-1
            decklist[i] = (num, name)
    gravelist.append((1,name))
    for j in range(0, length1):
        if(decklist[j][0]==0):
            pos2=j
    decklist.pop(pos2)
    reflectgrave()
    reflectdeck()  

def movedeckexile(name):
    pos1=0
    pos2=0
    length1 = len(decklist)
    for i in range(0,length1):
        if(decklist[i][1]==name):
            num = int(decklist[i][0])-1
            decklist[i] = (num, name)
    exilelist.append((1,name))
    for j in range(0, length1):
        if(decklist[j][0]==0):
            pos2=j
    decklist.pop(pos2)
    reflectexile()
    reflectdeck()



def moveplaydeck(name):
    pos1=0
    pos2=0
    length1 = len(playlist)
    for i in range(0,length1):
        if(playlist[i][1]==name):
            num = int(playlist[i][0])-1
            playlist[i] = (num, name)
    decklist.append((1,name))
    for j in range(0, length1):
        if(playlist[j][0]==0):
            pos2=j
    playlist.pop(pos2)
    reflectplay()
    reflectdeck()

def moveplaygrave(name):
    pos1=0
    pos2=0
    length1 = len(playlist)
    for i in range(0,length1):
        if(playlist[i][1]==name):
            num = int(playlist[i][0])-1
            playlist[i] = (num, name)
    gravelist.append((1,name))
    for j in range(0, length1):
        if(playlist[j][0]==0):
            pos2=j
    playlist.pop(pos2)
    reflectplay()
    reflectgrave() 

def moveplayexile(name):
    pos1=0
    pos2=0
    length1 = len(playlist)
    for i in range(0,length1):
        if(playlist[i][1]==name):
            num = int(playlist[i][0])-1
            playlist[i] = (num, name)
    exilelist.append((1,name))
    for j in range(0, length1):
        if(playlist[j][0]==0):
            pos2=j
    playlist.pop(pos2)
    reflectplay()
    reflectexile()

def moveexileplay(name):
    pos1=0
    pos2=0
    length1 = len(exilelist)
    for i in range(0,length1):
        if(exilelist[i][1]==name):
            num = int(exilelist[i][0])-1
            exilelist[i] = (num, name)
    playlist.append((1,name))
    for j in range(0, length1):
        if(exilelist[j][0]==0):
            pos2=j
    exilelist.pop(pos2)
    reflectplay()
    reflectexile()

def moveexiledeck(name):
    pos1=0
    pos2=0
    length1 = len(exilelist)
    for i in range(0,length1):
        if(exilelist[i][1]==name):
            num = int(exilelist[i][0])-1
            exilelist[i] = (num, name)
    decklist.append((1,name))
    for j in range(0, length1):
        if(exilelist[j][0]==0):
            pos2=j
    exilelist.pop(pos2)
    reflectdeck()
    reflectexile()

def moveexilegrave(name):
    pos1=0
    pos2=0
    length1 = len(exilelist)
    for i in range(0,length1):
        if(exilelist[i][1]==name):
            num = int(exilelist[i][0])-1
            exilelist[i] = (num, name)
    gravelist.append((1,name))
    for j in range(0, length1):
        if(exilelist[j][0]==0):
            pos2=j
    exilelist.pop(pos2)
    reflectgrave()
    reflectexile()

def movegraveexile(name):
    pos1=0
    pos2=0
    length1 = len(gravelist)
    for i in range(0,length1):
        if(gravelist[i][1]==name):
            num = int(gravelist[i][0])-1
            gravelist[i] = (num, name)
    exilelist.append((1,name))
    for j in range(0, length1):
        if(gravelist[j][0]==0):
            pos2=j
    gravelist.pop(pos2)
    reflectgrave()
    reflectexile()

def movegravedeck(name):
    gravelength = len(gravelist)
    print(gravelength)
    print(gravelist)
    print(gravelength-1)
    print(gravelist[0][1])
    print(int(gravelist[0][0])-1)
    tuple = (int(gravelist[0][0])-1, name)
    print(tuple)
    for i in range(0,gravelength):
        if(gravelist[i][1]==name):
            num = int(gravelist[i][0])-1
            gravelist[i] = (num, name)
    decklist.append((1,name))
    for j in range(0, gravelength):
        if(gravelist[j][0]==0):
            pos2=j
    gravelist.pop(pos2)
    reflectgrave()
    reflectdeck()

def movegraveplay(name):
    pos1=0
    pos2=0
    length1 = len(gravelist)
    for i in range(0,length1):
        if(gravelist[i][1]==name):
            num = int(gravelist[i][0])-1
            gravelist[i] = (num, name)
    playlist.append((1,name))
    for j in range(0, length1):
        if(gravelist[j][0]==0):
            pos2=j
    gravelist.pop(pos2)
    reflectgrave()
    reflectplay()

def cleardeck():
    decktext.delete('1.0', tk.END)

def cleargrave():
    gravetext.delete('1.0', tk.END)

def clearexile():
    exiletext.delete('1.0', tk.END)

def clearplay():
    playtext.delete('1.0', tk.END)

def reflectdeck():
    cleardeck()
    decklength = len(decklist)
    temp = []
    for k in range(0, decklength):
        temp.append(str(decklist[k][0]))
        temp.append(decklist[k][1])
    tstring = ', '.join(temp)
    decktext.insert(tk.END, tstring)
    
    

def reflectplay():
    clearplay()
    playlength =len(playlist)
    temp=[]
    for k in range(0, playlength):
        temp.append(str(playlist[k][0]))
        temp.append(playlist[k][1])
    tstring = ', '.join(temp)
    playtext.insert(tk.END, tstring)
    

def reflectgrave():
    cleargrave()
    gravelength = len(gravelist)
    temp = []
    for k in range(0, gravelength):
        temp.append(str(gravelist[k][0]))
        temp.append(gravelist[k][1])
    tstring = ', '.join(temp)
    gravetext.insert(tk.END, tstring)
    

def reflectexile():
    clearexile()
    exilelength =len(exilelist)
    temp=[]
    for k in range(0, exilelength):
        temp.append(str(exilelist[k][0]))
        temp.append(exilelist[k][1])
    tstring = ', '.join(temp)
    exiletext.insert(tk.END, tstring)
    
    
def process():
    cleardeck()
    decklist.clear()
    list = deck_entry.get().split(';')
    length = len(list)
    for i in range(0, length-1):
        cleardeck()
        pos=list[i].find('x')
        end = len(list[i])
        decklist.append((list[i][0:pos], str(list[i][pos+2:end])))
    reflectdeck()



def callmove():
    name = movename.get()
    if(entrylist1.get() == 'grave'):
        if(entrylist2.get()=='exile'):
            movegraveexile(name)
            print('done')
        elif(entrylist2.get()=='play'):
            movegraveplay(name)
            print('done')
        else:
            movegravedeck(name)
            print('done')
    if(entrylist1.get() == 'deck'):
        if(entrylist2.get()=='exile'):
            movedeckexile(name)
            print('done')
        elif(entrylist2.get()=='play'):
            movedeckinplay(name)
            print('done')
        else:
            movedeckgrave(name)
            print('done')
    
    if(entrylist1.get() == 'play'):
        if(entrylist2.get()=='exile'):
            moveplayexile(name)
            print('done')
        elif(entrylist2.get()=='grave'):
            moveplaygrave(name)
            print('done')
        else:
            moveplaydeck(name)
            print('done')
    if(entrylist1.get() == 'exile'):
        if(entrylist2.get()=='play'):
            moveexileplay(name)
            print('done')
        elif(entrylist2.get()=='grave'):
            moveexilegrave(name)
            print('done')
        else:
            moveexiledeck(name)
            print('done')

def yerr():
    print(decklist)

    





window = tk.Tk()

window.title('Draft 2')

decklist=[(1,'a'),(2,'b')]
playlist=[]
gravelist=[]
exilelist=[]

turnlist = []

top = tk.Frame(window, bg='#a7bed3', width=450, height=50, pady=3)
bottom = tk.Frame(window, bg='#a7bed3', width=50, height=40, padx=3, pady=3)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
top.grid(row=0, sticky="nsew")
bottom.grid(row=1, sticky="nsew")


#top labels
life_label = tk.Label(top, text='Life:', bg='#a7bed3',highlightbackground = '#a7bed3')
life_label.grid(row=0, column=0)

turn_label = tk.Label(top, text='Turn:')
turn_label.configure(background='#a7bed3')
turn_label.grid(row=1, column=0)

life = tk.Label(master=top, text="20")
life.configure(background='#a7bed3')
life.grid(row=0, column=3)

turncount = tk.Label(master=top, text="1" ,highlightbackground = '#a7bed3')
turncount.configure(background='#a7bed3')
turncount.grid(row=1, column=4)

one_label = tk.Label(top, text="From: ")
one_label.configure(background='#a7bed3')
one_label.grid(row=0, column=7)

two_label = tk.Label(top, text="To: ")
two_label.configure(background='#a7bed3')
two_label.grid(row=1, column=7)

name_label = tk.Label(top, text="Name: ")
name_label.configure(background='#a7bed3')
name_label.grid(row=1, column=9)


#top buttons
cal_button = tk.Button(top, text='Distribution calculator', highlightbackground = '#a7bed3', command=createnew)
cal_button.grid(row=0, column=5)

btn_decrease = tk.Button(master=top, text="-",highlightbackground = '#a7bed3', command=decreasevalue)
btn_decrease.grid(row=0, column=2)

btn_increase = tk.Button(top, text="+", highlightbackground = '#a7bed3',command=increasevalue)
btn_increase.grid(row=0, column=4)

turnup = tk.Button(master=top, text="+",highlightbackground = '#a7bed3', command=incrementturn)
turnup.grid(row=1, column=5)

transfer_button = tk.Button(top, text='Move', highlightbackground='#a7bed3', command=callmove)
transfer_button.grid(row=1, column=11)

notebutton = tk.Button(top, text = 'Notes', highlightbackground = '#a7bed3', command = createnote)
notebutton.grid(row = 0, column = 10)

historybutton = tk.Button(top, text = 'Turn:', highlightbackground = '#a7bed3', command = history)
historybutton.grid(row = 0, column = 11)



#top entries
entrylist1 = tk.Entry(top)
entrylist1.grid(row=0, column=8)

entrylist2 = tk.Entry(top)
entrylist2.grid(row=1, column=8)

movename = tk.Entry(top)
movename.grid(row=1, column=10)

historyentry = tk.Entry(top)
historyentry.grid(row = 0, column = 12)


#bottom widget frame creation
left = tk.Frame(bottom, bg='#c6e2e9', width=100, height=90)
left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

mid = tk.Frame(bottom, bg='#c6e2e9', width=100, height=90, padx=3, pady=3)
mid.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

right = tk.Frame(bottom, bg='#c6e2e9', width=100, height=90, padx=3, pady=3)
right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


#left bottom
gravelabel = tk.Label(left, text = "Graveyard", fg='white', bg='#c6e2e9')
gravelabel.pack(fill=tk.X)

gravetext = tk.Text(left, width=50, height=20, fg='white', bg='#c6e2e9')
gravetext.pack(fill=tk.X)

exilelabel = tk.Label(left, text = "Exile", fg='white', bg='#c6e2e9')
exilelabel.pack(fill=tk.X)

exiletext = tk.Text(left, width = 50, height=20, fg='white', bg='#c6e2e9')
exiletext.pack(fill=tk.X)

#other bottom

inplaylabel = tk.Label(mid, text = "In-play", fg='white', bg='#c6e2e9')
inplaylabel.pack(fill=tk.X)

deck_entry_label = tk.Label(right, text='Please enter decklist ------>', fg='white', bg='#c6e2e9')
deck_entry_label.grid(row=0, column=0, sticky = 'nsew')

playtext = tk.Text(mid, width = 50, height = 20, fg='white', bg='#c6e2e9')
playtext.pack(fill=tk.X)

#deck stuff
decktext = tk.Text(right, width=50, height=20, fg='white', bg='#c6e2e9')
decktext.grid(row=1,column=0, sticky = 'nsew')

deck_entry = tk.Entry(right, fg='white', bg='#c6e2e9')
deck_entry.grid(row=0, column=1, sticky = 'nsew')

deck_entry_button = tk.Button(right, text = 'Process', fg='blue', highlightbackground='#c6e2e9', command = process)
deck_entry_button.grid(row=0,column=2, sticky = 'nsew')

window.mainloop()
