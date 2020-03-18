from tkinter import *
import os
import better_fileedit as fe
window = Tk()
window.title('custom_cmd')
window.geometry('647x343')
window.configure(background='black')
window.iconbitmap(r'command-line.ico')
window.resizable(0,0)
version = 'v2.0.0'
def outputtext(text):
    t.configure(state='normal')
    t.insert(INSERT,text + '\n')
    t.see('end')
    t.configure(state="disabled")

def command(*args):
    bad = False
    line = e.get()
    line = line.split(' ')
    commands = ['COMMANDS:','help','clear','info','exit','run','bin','hex','dec','+','-','*','/','new','del','open']
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
        t.delete(1.0,END)
        t.configure(state="disabled")

    # info command
    elif key == 'info':
        outputtext('--Custom Command Prompt ' + version + '-- ')

    # exit command
    elif key == 'exit':
        window.destroy()

    # run command
    elif key == 'run':
        if len(line) == 3:
            if line[1] == 'os':
                if line[2] == 'current':
                    window2 = Tk()
                elif line[2] == 'previous':
                    window3 = Tk()
                else:
                    bad = True
            elif line[1] == 'file':
                if line[2] == 'editor':
                    fe.fileedit()
                else:
                    bad = True
            else:
                bad = True
        else:
            bad = True

    #bin command
    elif key == 'bin': 
        if len(line) == 3:
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
        if len(line) == 3:
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
        if len(line) == 3:
            if line[1] == 'bin':
                outputtext(e.get() + '\n' + bin(int(line[2])).replace('0b',''))
            elif line[1] == 'hex':
                outputtext(e.get() + '\n' + hex(int(line[2])).replace('0x',''))
            else:
                bad = True
        else:
            bad = True

    # addition command
    elif key == '+':
        if len(line) > 1:
            total = float(line[1])
            for x in range(len(line)-1):
                total += float(line[x+1])
            outputtext(str(total))
        else:
            bad = True


    # subtraction command
    elif key == '-':
        if len(line) > 1:
            total = float(line[1])
            for x in range(len(line)-1):
                total -= float(line[x+1])
            outputtext(str(total))
        else:
            bad = True


    # multiplication command
    elif key == '*':
        if len(line) > 1:
            total = float(line[1])
            for x in range(len(line)-2):
                total *= float(line[x+2])
            outputtext(str(total))
        else:
            bad = True


    # division command
    elif key == '/':
        if len(line) > 1:
            total = float(line[1])
            for x in range(len(line)-2):
                if float(line[x+2]) == 0:
                    outputtext('Error: division by 0')
                    break
                else:
                    total /= float(line[x+2])
            outputtext(str(total))
        else:
            bad = True


    # new command
    elif key == 'new':
        if len(line) == 3:
            if line[1] == 'file':
                with open(line[2],'w') as f:
                    f.write('hello')
                outputtext('Created file: ' + line[2])
            else:
                bad = True
        else:
            bad = True


    # del command
    elif key == 'del':
        if len(line) == 3:
            if line[1] == 'file':
                if os.path.exists(line[2]):
                  os.remove(line[2])
                  outputtext('Deleted file: ' + line[2])
                else:
                  outputtext("The file does not exist")
            else:
                bad = True
        else:
            bad = True


    # open command
    elif key == 'open':
        if len(line) == 3:
            if line[1] == 'file':
                if os.path.exists(line[2]):
                    with open(line[2],'r') as f:
                        contents = f.read()
                        if contents == '':
                            outputtext('The file is empty')
                        else:
                            outputtext(contents)
                else:
                    outputtext('The file does not exist')
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
t = Text(window,bg='black',fg='white',state="disabled")
t.place(x=0,y=0,width=647,height=321)

# cmd input
e = Entry(window,bg='black',fg='white',insertbackground='white')
e.place(x=0,y=322,width=647,height=20)
e.bind('<Return>',command)
e.focus()

outputtext('--Custom Command Prompt ' + version + '-- ')

mainloop()
