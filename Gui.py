from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

class myWin:
    def __init__(self, win):
        self.root = win
        
        x_size = 800
        y_size = 800
        
        margin = 20
        
        x_divison = x_size/2
        y_divison = y_size/2
        
        # TOP LEFT ------ ADD INTERACTION
        
        x_min_NW = margin
        y_min_NW = margin
        
        self.lbl1 = Label(win, text='Target pokemon name:')
        self.lbl2 = Label(win, text='Type of move used:')
        self.lbl3 = Label(win, text='Result:')
        
        self.message = StringVar()
        self.lbl4 = Label(win, textvariable = self.message)
        
        self.t1 = Entry()
        self.t2 = Entry()
        
        self.lbl1.place(x = x_min_NW, y = y_min_NW)
        self.t1.place(x = x_min_NW + 150, y = y_min_NW)
        
        self.lbl2.place(x = x_min_NW, y = y_min_NW + 50)
        self.t2.place(x = x_min_NW + 150, y = y_min_NW + 50)
        
        
        self.result = StringVar(value = '1')
        C1 = Radiobutton(win, text = "Immune", variable = self.result, value = '0')
        C2 = Radiobutton(win, text = "Not very effective...", variable = self.result, value = '-')
        C3 = Radiobutton(win, text = "Normal", variable = self.result, value = '1')
        C4 = Radiobutton(win, text = "Super effective!", variable = self.result, value = '+')
        
        self.lbl3.place(x = x_min_NW, y = y_min_NW + 130)
        C1.place(x = x_min_NW + 150, y = y_min_NW + 100)
        C2.place(x = x_min_NW + 150, y = y_min_NW + 120)
        C3.place(x = x_min_NW + 150, y = y_min_NW + 140)
        C4.place(x = x_min_NW + 150, y = y_min_NW + 160)
        
        self.b1 = Button(win, text='Add to Pokedex', command = self.addEntry)
        self.b1.place(relx = 0.25, anchor = CENTER, y = y_min_NW + 210)
        
        self.lbl4.place(x = x_min_NW, y = y_min_NW + 260)
        
        # ------------------
        
        
        # TOP RIGHT ----- SHOW THE CHART
        
        self.plot(margin)
        
        # ------------------
        
        
        # BOTTOM LEFT ------ ADD POKEMON
        
        x_min_SW = margin
        y_min_SW = y_divison + margin
        
        self.newName = Label(win, text='New pokemons name:')
        self.type1 = Label(win, text='1st Type:')
        self.type2 = Label(win, text='2nd Type:')
        
        self.message2 = StringVar()
        #self. = Label(win, textvariable = self.message2)
        
        self.newName_entry = Entry()
        self.type1_entry = Entry()
        self.type2_entry = Entry()
        
        self.newName.place(x = x_min_SW, y = y_min_SW)
        self.newName_entry.place(x = x_min_SW + 150, y = y_min_SW)
        
        self.type1.place(x = x_min_SW, y = y_min_SW + 50)
        self.type1_entry.place(x = x_min_SW + 150, y = y_min_SW + 50)
        
        self.type2.place(x = x_min_SW, y = y_min_SW + 100)
        self.type2_entry.place(x = x_min_SW + 150, y = y_min_SW + 100)
        
        self.addPokemon = Button(win, text='Add to Pokedex', command = self.addPokemon)
        self.addPokemon.place(relx = 0.25, anchor = CENTER, y = y_min_SW + 150)
        
        self.messagePokemon = StringVar()
        self.labelPokemon = Label(win, textvariable = self.messagePokemon)
        self.labelPokemon.place(x = x_min_SW + 50, y = y_min_SW + 200)
        
        # ------------------
        
        # BOTTOM RIGHT ----- GET POKEMON DATA
        
        x_min_NE = x_divison + margin
        y_min_NE = y_divison + margin
        
        self.whichPokemon = Label(win, text='Which Pokemon?')
        self.whichPokemon_entry = Entry()
        
        self.whichPokemon.place(x = x_min_NE, y = y_min_NE)
        self.whichPokemon_entry.place(x = x_min_NE + 150, y = y_min_NE)
        
        self.whatData = Label(win, text='Show Pokemons:')
        
        self.what = IntVar(value = 0)
        C_move = Radiobutton(win, text = "moves", variable = self.what, value = 0)
        C_type = Radiobutton(win, text = "type", variable = self.what, value = 1)
        
        self.whatData.place(x = x_min_NE, y = y_min_NE + 50)
        C_move.place(x = x_min_NE + 150, y = y_min_NE + 50)
        C_type.place(x = x_min_NE + 250, y = y_min_NE + 50)
        
        
        
        
        
        
    def plot(self, margin):
         # the figure that will contain the plot
        fig = Figure(figsize = (5, 5),
                     dpi = 100)

        # list of squares
        y = [i**2 for i in range(101)]

        # adding the subplot
        plot1 = fig.add_subplot(111)

        # plotting the graph
        plot1.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, self.root)  
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack(anchor = NE, expand = False, padx = margin, pady = margin)
        
    def addEntry(self):
        res = self.result.get() + self.t2.get() + self.t1.get()
        self.t2.delete(0, 'end')
        self.message.set(res)
        
    def addPokemon(self):
        res = self.newName_entry.get() + self.type1_entry.get() + self.type2_entry.get() 
        self.messagePokemon.set(res)

window = Tk()
mywin = myWin(window)
window.title('Pokedex')
window.geometry("800x800+10+10")
window.mainloop()