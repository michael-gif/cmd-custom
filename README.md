# cmd-custom
- this is a custom cmd that has limited functionality, but lots of room for expansion

### Getting started
1. To get started, download the py file, and run it.
2. Then type one of the commands below:
   
### Commands
  
Command|Syntax|Function
-------|------|--------
`help`|`help`|displays all possible commands
`clear`|`clear`|clears the cmd output
`info`|`info`|displays the available information about the cmd
`exit`|`exit`|exits the program
`run`|`run os <verison>`<br>`run file editor`|can run an os version<br>launches the file editor
`bin`|`bin hex <binary>`  or  `bin dec <binary>`|converts binary to hexadecimal or decimal
`hex`|`hex bin <hexadecimal>` or `hex dec <hexadecimal>`|converts hexadecimal to binary or decimal
`dec`|`dec bin <decimal>`  or  `dec hex <decimal>`|converts decimal to binary or hexadecimal
`+`|`+ <number> <number>`|adds all the numbers after it together
`-`|`- <number> <number>`|subtracts all the numbers after it
`*`|`* <number> <number>`|multiplies all the numbers after it together
`/`|`/ <number> <number>`|divides all the numbers after it
`new`|`new file <file name>`|creates a file
`del`|`del file <file name>`|deletes a file
`open`|`open file <file name>`|opens a file

### Command examples
- `bin hex 10100110` outputs a6 (10100110 was converted to a6)
- `bin dec 0011` outputs 3 (0011 was converted to 3)
- `hex bin ff` outputs 11111111 (ff was converted to 11111111)
- `hex dec f8` outputs 248 (f8 was converted to 248)
- `dec bin 295` outputs 100100111 (295 was converted to 100100111)
- `dec hex 179` outputs b3 (179 was converted to b3)
- `run os current` opens a new tkinter window
- `run os previous` opens a new tkinter window
- `run file editor` launches the file editor
- `+ 1 3` outputs 4 (3 was added to 1)
- `- 5 4` outputs 1 (4 was subtracted from 5)
- `* 3 8` outputs 24 (8 was multiplied by 3)
- `/ 6 3` outputs 2 (6 was divided by 3)
- `/ 8 4 2` outputs 1 (8 was divided by 4, then the answer was divided by 2)
- `new file bob.txt` creates a text file called bob
- `del file bob.txt` deletes the file `bob.txt`
- `open file bob.txt` opens the file `bob.txt` and displays it's contents
