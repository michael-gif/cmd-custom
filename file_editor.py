def fileedit():
    import tkinter as tk
    from tkinter import filedialog
    window2 = tk.Tk()
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
            t.insert(tk.INSERT,lines)
    def savefile():
        global name
        with open(name,'w') as f:
            text = t.get('1.0','end-1c')
            f.write(text)
    t = tk.Text(window2,bg='black',fg='white',insertbackground='white',state="normal")
    t.place(x=0,y=0,width=647,height=320)
    b = tk.Button(window2,bg='grey25',fg='white',text='Open',command=openfile)
    b.place(x=0,y=318,width=323)
    b2 = tk.Button(window2,bg='grey25',fg='white',text='Save',command=savefile)
    b2.place(x=324,y=318,width=323)
    tk.mainloop()

if __name__ == "__main__":
    fileedit()
