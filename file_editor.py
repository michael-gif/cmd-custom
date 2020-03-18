from tkinter import *
def fileedit():
    from tkinter import filedialog
    window2 = Tk()
    window2.title('custom_cmd:file-editor')
    window2.geometry('647x343')
    window2.configure(bg='black')
    window2.iconbitmap(r'command-line.ico')
    name = ''
    def openfile():
        global name
        name = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(name,'r') as f:
            lines = f.read()
            t.insert(INSERT,lines)
    def savefile():
        global name
        with open(name,'w') as f:
            text = t.get('1.0','end-1c')
            f.write(text)
    t = Text(window2,bg='black',fg='white',insertbackground='white',state="normal")
    t.place(x=0,y=0,width=647,height=320)
    b =Button(window2,bg='grey25',fg='white',text='Open',command=openfile)
    b.place(x=0,y=318,width=323)
    b2 = Button(window2,bg='grey25',fg='white',text='Save',command=savefile)
    b2.place(x=324,y=318,width=323)
    mainloop()

if __name__ == "__main__":
    fileedit()
