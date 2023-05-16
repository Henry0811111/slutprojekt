from customtkinter import *

class käft(CTk):
    def __init__(self,*args,**kwargs):
        CTk.__init__(self,*args,**kwargs)
        self.geometry("500x500")
        a = CTkButton(self,width=100,height=50,text="Käft zebastian")
        a.place(relx=0.5,rely=0.5,anchor="center")


if __name__ == "__main__":
    app = käft()
    app.mainloop()