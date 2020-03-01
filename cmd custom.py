import tkinter as tk
window = tk.Tk()
window.title('custom_cmd')
window.geometry('647x343')
window.configure(background='grey25')
window.resizable(0,0)

def outputtext(text):
    t.configure(state='normal')
    t.insert(tk.INSERT,text + '\n')
    t.see('end')
    t.configure(state="disabled")

def command(*args):
    bad = False
    line = e.get()
    line = line.split(' ')
    commands = ['COMMANDS:','help','clear','info','exit','run','bin','hex','dec']
    key = line[0]

    # help command
    if key == 'help':
        if len(line) < 2:
            outputtext('\n'.join(commands) + '\n')
        else:
            bad = True

    # clear command
    elif key == 'clear':
        t.configure(state='normal')
        t.delete(1.0,tk.END)
        t.configure(state="disabled")

    # info command
    elif key == 'info':
        outputtext('--Custom Command Prompt--')

    # exit command
    elif key == 'exit':
        root.destroy()

    # run command
    elif key == 'run':
        if len(line) == 3:
            if line[1] == 'os':
                if line[2] == 'current':
                    window2 = tk.Tk()
                elif line[2] == 'previous':
                    window3 = tk.Tk()
                else:
                    bad = True
            else:
                bad = True
        else:
            bad = True

    #bin command
    elif key == 'bin': 
        if len(line) > 2:
            if line[1] == 'hex':
                outputtext(e.get() + '\n' + hex(int(line[2],2)).replace('0x',''))
            elif line[1] == 'dec':
                outputtext(e.get() + '\n' + str(int(line[2],2)))
            else:
                bad = True
        else:
            bad = True

    # hex command
    elif key == 'hex':
        if len(line) > 2:
            if line[1] == 'bin':
                outputtext(e.get() + '\n' + bin(int(line[2],16)).replace('0b',''))
            elif line[1] == 'dec':
                outputtext(e.get() + '\n' + str(int(line[2],16)))
            else:
                bad = True
        else:
            bad = True

    # dec command
    elif key == 'dec':
        if len(line) > 2:
            if line[1] == 'bin':
                outputtext(e.get() + '\n' + bin(int(line[2])).replace('0b',''))
            elif line[1] == 'hex':
                outputtext(e.get() + '\n' + hex(int(line[2])).replace('0x',''))
            else:
                bad = True
        else:
            bad = True


    else:
        bad = True

    # unknown commands
    if bad == True:
        outputtext("'" + e.get() + "' not recognised")
        bad = False

# cmd output
t = tk.Text(window,bg='black',fg='white',state="disabled")
t.place(x=0,y=0,width=647,height=321)

# cmd input
e = tk.Entry(window,bg='black',fg='white',insertbackground='white')
e.place(x=0,y=322,width=647,height=20)
e.bind('<Return>',command)
e.focus()

outputtext('--Custom Command Prompt--')

tk.mainloop()
