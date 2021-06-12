
from tkinter import * 

def icalc(source,side):
    storeobj = Frame(source,borderwidth=4,bd=4,bg="dark grey")
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj

def button(source, side, text, command= NONE):
    storeobj = Button(source, text=text, command=command)
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand = YES, fill=BOTH)
        self.master.title('Calculator')
        display= StringVar()
        Entry(self,relief=RIDGE,textvariable=display,justify='right',bd=30,bg="grey").pack(side='top',expand='YES',fill='both')
        for clearButton in (["C"]):
            erase= icalc(self, TOP)
            for ichar in clearButton:
                button(erase,LEFT,ichar,lambda storeobj=display,q=ichar:storeobj.set(''))
        for numButton in ("789/","456*","123-","0.+"):
            FunctionNum = icalc(self,TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeobj=display,q=iEquals: storeobj.set(storeobj.get()+q))
        EqualButton= icalc(self, TOP)
        for iEquals in "=":
            if iEquals == "=":
                btniEquals= button(EqualButton,LEFT,iEquals)
                btniEquals.bind('<ButtonRelease-1>',lambda e, s=self, storeobj=display:s.calc(storeobj),'+')
            else:
                btniEquals=button(EqualButton,LEFT,iEquals,lambda storeobj = display,s='%s'% iEquals: storeobj.set(storeobj.get()+s))
    def calc(self,display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
                
if __name__=='__main__':
    app().mainloop()