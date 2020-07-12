from tkinter import *
import file_editor as fe
import os
window = Tk()
window.title('custom_cmd')
window.geometry('647x343')
window.configure(background='black')
window.iconbitmap(r'command-line.ico')
window.resizable(0,0)
text = ''
version = 'v2.0.0'
def getcommand():
    global text
    text2 = t.get('1.0','end-1c')
    commandlength = len(text2) - len(text)
    command = text2[len(text):len(text2)]
    return command

def newline():
    t.insert(END,'\n')
    
def outputtext(text):
    t.insert(END,'\n' + text + '\n')
    t.see('end')

def command(event):
    global text
    '''text2 = t.get('1.0','end-1c')
    commandlength = len(text2) - len(text)
    command = text2[len(text):len(text2)]'''
    command = getcommand()
    line = command.split(' ')
    key = line[0]
    bad = False
    commands = ['COMMANDS:','help','clear','info','exit','run','bin','hex','dec','+','-','*','/','new','del','open']
    
    # help command
    if key == 'help':
        if len(line) < 2:
            outputtext('\n'.join(commands))
        else:
            bad = True
        newline()

    # clear command
    elif key == 'clear':
        t.delete(1.0,END)

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
        newline()

    #bin command
    elif key == 'bin': 
        if len(line) == 3:
            if line[1] == 'hex':
                outputtext(getcommand() + ':\n' + hex(int(line[2],2)).replace('0x',''))
            elif line[1] == 'dec':
                outputtext(getcommand() + ':\n' + str(int(line[2],2)))
            else:
                bad = True
        else:
            bad = True

    # hex command
    elif key == 'hex':
        if len(line) == 3:
            if line[1] == 'bin':
                outputtext(getcommand() + ':\n' + bin(int(line[2],16)).replace('0b',''))
            elif line[1] == 'dec':
                outputtext(getcommand() + ':\n' + str(int(line[2],16)))
            else:
                bad = True
        else:
            bad = True

    # dec command
    elif key == 'dec':
        if len(line) == 3:
            if line[1] == 'bin':
                outputtext(getcommand() + ':\n' + bin(int(line[2])).replace('0b',''))
            elif line[1] == 'hex':
                outputtext(getcommand() + ':\n' + hex(int(line[2])).replace('0x',''))
            else:
                bad = True
        else:
            bad = True

    # addition command
    elif key == '+':
        if len(line) > 1:
            total = float(0)
            for x in range(len(line)-1):
                total += float(line[x+1])
            outputtext(str(total))
        else:
            bad = True


    # subtraction command
    elif key == '-':
        if len(line) > 1:
            total = float(0)
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
                    badoutput = True
                    break
                else:
                    total /= float(line[x+2])
            if not badoutput:
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

    if command == '':
        bad = False

    # unknown commands
    if bad == True:
        badcommand = getcommand()
        outputtext("'" + badcommand + "' not recognised")
        bad = False

    if t.get('1.0','end-1c') == '':
        t.insert('end','C:\\')
    else:
        t.insert('end','\nC:\\')
    text = t.get('1.0','end-1c')
    return "break"

def preventbackspace(event):
    global text
    pos = t.index(INSERT)
    pos.split('.')
    print(pos)
    if int(pos[2]) == len(text):
        return "break"

t = Text(window,bg='black',fg='white',insertbackground='white')
t.place(x=0,y=0,width=677,height=343)
t.insert('end','C:\\')
t.bind("<Return>",command)
t.bind("<BackSpace>",preventbackspace)
text = t.get('1.0','end-1c')
t.focus()
window.mainloop()
