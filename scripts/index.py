import tkinter
import os

class testapphome(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.minsize(width=800, height=800)
        self.resizable(False,False)
        self.geometry(self.geometry())
        self.initialize()

    def initialize(self):
        self.grid()

        # TEXT INPUT FRAME
        containerentry = tkinter.Frame(self, borderwidth=1, relief="sunken", width=475, height=100)
        containerentry.place(x=25, y=675)
        containerentry.grid_propagate(False)
        containerentry.grid_columnconfigure(0,weight=1)

        # TEXT INPUT BAR
        self.textinVariable = tkinter.StringVar()
        self.textinp = tkinter.Text(containerentry, bd = 6, height = 4)
        self.textinp.grid(column=0,row=1,sticky='EW')
        self.textinp.bind("<Return>", self.OnPressEnter)
        #self.textVariable.set(u"Enter text here.")

        # TEXT OUTPUT FRAME
        containeroutpt = tkinter.Frame(self, borderwidth=1, relief="sunken", width=550, height=650)
        containeroutpt.place(x=25, y=25)
        containeroutpt.grid_propagate(False)
        containeroutpt.grid_columnconfigure(0,weight=1)

        # TEXT OUTPUT BAR
        self.textoutVariable = tkinter.StringVar()
        self.textout = tkinter.Text(containeroutpt, bd = 1, height = 32, bg = "light blue")
        self.textout.grid(column=0,row=1,sticky='EW')
        #self.textout.bind("<Return>", self.OnPressEnter)
        #self.textVariable.set(u"Enter text here.")

        # SEND BUTTON FRAME
        containersend = tkinter.Frame(self, borderwidth=1, relief="sunken", width=75, height=100)
        containersend.place(x=500, y=675)
        containersend.grid_propagate(False)
        containersend.grid_columnconfigure(0,weight=1)

        # SEND BUTTON
        sendbutton = tkinter.Button(containersend,text="SEND", height=4, bg="light slate gray")
        sendbutton.grid(column=0,row=0, sticky="EW")

        # INFO BUTTON FRAME
        containerinfo = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containerinfo.place(x=625, y=100)
        containerinfo.grid_propagate(False)
        containerinfo.grid_columnconfigure(0,weight=1)

        # INFO BUTTON
        infobutton = tkinter.Button(containerinfo,text="About App", command=self.OnAboutClick, height=3)
        infobutton.grid(column=0,row=0, sticky="EW")

        # QUIT BUTTON FRAME
        containerquit = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containerquit.place(x=625, y=200)
        containerquit.grid_propagate(False)
        containerquit.grid_columnconfigure(0,weight=1)

        # QUIT BUTTON
        quitButton = tkinter.Button(containerquit, text="Quit",command=self.quit, height=3)
        quitButton.grid(row=0, column=0, sticky="EW")


    def OnAboutClick(self):
        #print("check")
        os.system('about.py')

    def OnPressEnter(self,event):
        #self.labelVariable.set(self.entryVariable.get()+" (You pressed ENTER)")
        return


if __name__ == "__main__":
    app = testapphome(None)
    app.title('V1_APP')
    app.mainloop()