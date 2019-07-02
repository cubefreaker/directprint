from tkinter import *
from tkinter import messagebox
import json
import win32print
import sqlite3

window = Tk()
window.title("Autoprint Settings")
window.geometry("300x300")

branchLabel = Label(window, text="Branch")
branchLabel.grid(column=0, row=0, sticky=W)

conn = sqlite3.connect('data.db')
c = conn.cursor()


c.execute('SELECT isChecked FROM settings where branchCode="013"')
val1 = c.fetchone()[0]
checkState1 = IntVar()
checkState1.set(val1)
checkBranch1 = Checkbutton(window, text='CCC Surabaya', variable=checkState1)
checkBranch1.grid(column=0, row=1, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="015"')
val2 = c.fetchone()[0]
checkState2 = IntVar()
checkState2.set(val2)
checkBranch2 = Checkbutton(window, text='CCC Balikpapan', variable=checkState2)
checkBranch2.grid(column=0, row=2, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="051"')
val3 = c.fetchone()[0]
checkState3 = IntVar()
checkState3.set(val3)
checkBranch3 = Checkbutton(window, text='CC', variable=checkState3)
checkBranch3.grid(column=0, row=3, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="052"')
val4 = c.fetchone()[0]
checkState4 = IntVar()
checkState4.set(val4)
checkBranch4 = Checkbutton(window, text='CCC 2', variable=checkState4)
checkBranch4.grid(column=0, row=4, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="054"')
val5 = c.fetchone()[0]
checkState5 = IntVar()
checkState5.set(val5)
checkBranch5 = Checkbutton(window, text='CCC 1', variable=checkState5)
checkBranch5.grid(column=0, row=5, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="055"')
val6 = c.fetchone()[0]
checkState6 = IntVar()
checkState6.set(val6)
checkBranch6 = Checkbutton(window, text='Global Corporate', variable=checkState6)
checkBranch6.grid(column=0, row=6, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="057"')
val7 = c.fetchone()[0]
checkState7 = IntVar()
checkState7.set(val7)
checkBranch7 = Checkbutton(window, text='CCC Makassar', variable=checkState7)
checkBranch7.grid(column=0, row=7, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="300"')
val8 = c.fetchone()[0]
checkState8 = IntVar()
checkState8.set(val8)
checkBranch8 = Checkbutton(window, text='Implant', variable=checkState8)
checkBranch8.grid(column=0, row=8, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="016"')
val9 = c.fetchone()[0]
checkState9 = IntVar()
checkState9.set(val9)
checkBranch9 = Checkbutton(window, text='Vaya Papua', variable=checkState9)
checkBranch9.grid(column=0, row=9, sticky=W)

c.execute('SELECT isChecked FROM settings where branchCode="001"')
val10 = c.fetchone()[0]
checkState10 = IntVar()
checkState10.set(val10)
checkBranch10 = Checkbutton(window, text='Vaya HO', variable=checkState10)
checkBranch10.grid(column=0, row=10, sticky=W)

timeLabel = Label(window, text="Time Schedule (in minutes)")
timeLabel.grid(column=1, row=0, sticky=W)


c.execute('SELECT timeSet FROM time where id=1')
tVal = c.fetchone()[0]

textVal = StringVar()
text = Entry(window, width=10, textvariable=textVal)
text.grid(column=1, row=1, sticky=W)
textVal.set(tVal)


def save():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    #1
    if checkState1.get() == 1:
        query1 = 'update settings set isChecked="1" where branchCode="013"'
        c.execute(query1)
        conn.commit()
    else:
        query1 = 'update settings set isChecked="0" where branchCode="013"'
        c.execute(query1)
        conn.commit()

    #2
    if checkState2.get() == 1:
        query2 = 'update settings set isChecked="1" where branchCode="015"'
        c.execute(query2)
        conn.commit()
    else:
        query2 = 'update settings set isChecked="0" where branchCode="015"'
        c.execute(query2)
        conn.commit()

    #3
    if checkState3.get() == 1:
        query3 = 'update settings set isChecked="1" where branchCode="051"'
        c.execute(query3)
        conn.commit()
    else:
        query3 = 'update settings set isChecked="0" where branchCode="051"'
        c.execute(query3)
        conn.commit()

    #4
    if checkState4.get() == 1:
        query4 = 'update settings set isChecked="1" where branchCode="052"'
        c.execute(query4)
        conn.commit()
    else:
        query4 = 'update settings set isChecked="0" where branchCode="052"'
        c.execute(query4)
        conn.commit()

    #5
    if checkState5.get() == 1:
        query5 = 'update settings set isChecked="1" where branchCode="054"'
        c.execute(query5)
        conn.commit()
    else:
        query5 = 'update settings set isChecked="0" where branchCode="054"'
        c.execute(query5)
        conn.commit()

    #6
    if checkState6.get() == 1:
        query6 = 'update settings set isChecked="1" where branchCode="055"'
        c.execute(query6)
        conn.commit()
    else:
        query6 = 'update settings set isChecked="0" where branchCode="055"'
        c.execute(query6)
        conn.commit()

    #7
    if checkState7.get() == 1:
        query7 = 'update settings set isChecked="1" where branchCode="057"'
        c.execute(query7)
        conn.commit()
    else:
        query7 = 'update settings set isChecked="0" where branchCode="057"'
        c.execute(query7)
        conn.commit()

    #8
    if checkState8.get() == 1:
        query8 = 'update settings set isChecked="1" where branchCode="300"'
        c.execute(query8)
        conn.commit()
    else:
        query8 = 'update settings set isChecked="0" where branchCode="300"'
        c.execute(query8)
        conn.commit()

    #9
    if checkState9.get() == 1:
        query9 = 'update settings set isChecked="1" where branchCode="016"'
        c.execute(query9)
        conn.commit()
    else:
        query9 = 'update settings set isChecked="0" where branchCode="016"'
        c.execute(query9)
        conn.commit()

    #10
    if checkState10.get() == 1:
        query10 = 'update settings set isChecked="1" where branchCode="001"'
        c.execute(query10)
        conn.commit()
    else:
        query10 = 'update settings set isChecked="0" where branchCode="001"'
        c.execute(query10)
        conn.commit()

    #save printer
    printerUsed = variablePrint.get()
    queryPrinter = 'UPDATE printerUsed SET name="%s" WHERE id=1'%(printerUsed)
    c.execute(queryPrinter)
    conn.commit()

    t = text.get()
    query9 = 'update time set timeSet=%s'%(t)
    c.execute(query9)
    conn.commit()

    conn.close()
    messagebox.showinfo('Info', 'Save Success!')


printLabel = Label(window, text="Select Printer")
printLabel.grid(column=1, row=2, sticky=W)


listPrinter = []

for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1):
    listPrinter.append(printer[2])

c.execute('SELECT name FROM printerUsed where id = 1')
printVal = c.fetchone()[0]
variablePrint = StringVar()
variablePrint.set(printVal)
printerSelect = OptionMenu(window, variablePrint, *listPrinter)
printerSelect.grid(column=1, row=3, sticky=W)

button = Button(window, text="Save", command=save)
button.grid(column=1, row=5, sticky=W)

window.mainloop()