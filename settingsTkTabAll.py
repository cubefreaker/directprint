from tkinter import *
from tkinter import messagebox, filedialog, ttk
import json, os
import win32print
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

window = Tk()

c.execute('select windowTitle from title')
title = c.fetchone()[0]

window.title(title)
window.geometry("550x400")

tabControl = ttk.Notebook(window)

tabBranch = ttk.Frame(tabControl)
tabSetting = ttk.Frame(tabControl)
tabAppRun = ttk.Frame(tabControl)

tabControl.add(tabAppRun, text="Application")
tabControl.add(tabSetting, text="Settings")
tabControl.add(tabBranch, text="Branch")

tabControl.pack()

branchLabel = Label(tabBranch, text="Branch")
branchLabel.grid(column=0, row=0, sticky=W)

implantLabel = Label(tabBranch, text="Implant")
implantLabel.grid(column=1, row=0, sticky=W)

#CCC SURABAYA
c.execute('SELECT * FROM settings where branchCode="013"')
val1 = c.fetchone()
checkState1 = IntVar()
checkState1.set(val1[3])
checkBranch1 = Checkbutton(tabBranch, text=val1[1], variable=checkState1)
checkBranch1.grid(column=0, row=1, sticky=W)

#CCC BALIKPAPAN
c.execute('SELECT * FROM settings where branchCode="015"')
val2 = c.fetchone()
checkState2 = IntVar()
checkState2.set(val2[3])
checkBranch2 = Checkbutton(tabBranch, text=val2[1], variable=checkState2)
checkBranch2.grid(column=0, row=2, sticky=W)

#CC
c.execute('SELECT * FROM settings where branchCode="051"')
val3 = c.fetchone()
checkState3 = IntVar()
checkState3.set(val3[3])
checkBranch3 = Checkbutton(tabBranch, text=val3[1], variable=checkState3)
checkBranch3.grid(column=0, row=3, sticky=W)

#CCC 2
c.execute('SELECT * FROM settings where branchCode="052"')
val4 = c.fetchone()
checkState4 = IntVar()
checkState4.set(val4[3])
checkBranch4 = Checkbutton(tabBranch, text=val4[1], variable=checkState4)
checkBranch4.grid(column=0, row=4, sticky=W)

#CCC 1
c.execute('SELECT * FROM settings where branchCode="054"')
val5 = c.fetchone()
checkState5 = IntVar()
checkState5.set(val5[3])
checkBranch5 = Checkbutton(tabBranch, text=val5[1], variable=checkState5)
checkBranch5.grid(column=0, row=5, sticky=W)

#GLOBAL CORPORATE
c.execute('SELECT * FROM settings where branchCode="055"')
val6 = c.fetchone()
checkState6 = IntVar()
checkState6.set(val6[3])
checkBranch6 = Checkbutton(tabBranch, text=val6[1], variable=checkState6)
checkBranch6.grid(column=0, row=6, sticky=W)

#CCC MAKASSAR
c.execute('SELECT * FROM settings where branchCode="057"')
val7 = c.fetchone()
checkState7 = IntVar()
checkState7.set(val7[3])
checkBranch7 = Checkbutton(tabBranch, text=val7[1], variable=checkState7)
checkBranch7.grid(column=0, row=7, sticky=W)

#IMPLANT
c.execute('SELECT * FROM settings where branchCode="300"')
val8 = c.fetchone()
checkState8 = IntVar()
checkState8.set(val8[3])
checkBranch8 = Checkbutton(tabBranch, text=val8[1], variable=checkState8)
checkBranch8.grid(column=0, row=8, sticky=W)

#VAYA PAPUA
c.execute('SELECT * FROM settings where branchCode="016"')
val9 = c.fetchone()
checkState9 = IntVar()
checkState9.set(val9[3])
checkBranch9 = Checkbutton(tabBranch, text=val9[1], variable=checkState9, state=DISABLED)
checkBranch9.grid(column=0, row=9, sticky=W)

#VAYA HO
c.execute('SELECT * FROM settings where branchCode="001"')
val10 = c.fetchone()
checkState10 = IntVar()
checkState10.set(val10[3])
checkBranch10 = Checkbutton(tabBranch, text=val10[1], variable=checkState10, state=DISABLED)
checkBranch10.grid(column=0, row=10, sticky=W)

#IMPLANT ASIH EKA ABADI
c.execute('SELECT * FROM settings where branchCode="300.100"')
val11 = c.fetchone()
checkState11 = IntVar()
checkState11.set(val11[3])
checkBranch11 = Checkbutton(tabBranch, text=val11[1], variable=checkState11)
checkBranch11.grid(column=1, row=1, sticky=W )

#IMPLANT BI
c.execute('SELECT * FROM settings where branchCode="300.101"')
val12 = c.fetchone()
checkState12 = IntVar()
checkState12.set(val12[3])
checkBranch12 = Checkbutton(tabBranch, text=val12[1], variable=checkState12)
checkBranch12.grid(column=1, row=2, sticky=W )

#IMPLANT GA FOOD
c.execute('SELECT * FROM settings where branchCode="300.102"')
val13 = c.fetchone()
checkState13 = IntVar()
checkState13.set(val13[3])
checkBranch13 = Checkbutton(tabBranch, text=val13[1], variable=checkState13)
checkBranch13.grid(column=1, row=3, sticky=W )

#IMPLANT KALBE
c.execute('SELECT * FROM settings where branchCode="300.103"')
val14 = c.fetchone()
checkState14 = IntVar()
checkState14.set(val14[3])
checkBranch14 = Checkbutton(tabBranch, text=val14[1], variable=checkState14)
checkBranch14.grid(column=1, row=4, sticky=W )

#IMPLANT KPPU
c.execute('SELECT * FROM settings where branchCode="300.104"')
val15 = c.fetchone()
checkState15 = IntVar()
checkState15.set(val15[3])
checkBranch15 = Checkbutton(tabBranch, text=val15[1], variable=checkState15)
checkBranch15.grid(column=1, row=5, sticky=W )

#IMPLANT THIESS
c.execute('SELECT * FROM settings where branchCode="300.107"')
val16 = c.fetchone()
checkState16 = IntVar()
checkState16.set(val16[3])
checkBranch16 = Checkbutton(tabBranch, text=val16[1], variable=checkState16)
checkBranch16.grid(column=1, row=6, sticky=W )

#IMPLANT UT
c.execute('SELECT * FROM settings where branchCode="300.108"')
val17 = c.fetchone()
checkState17 = IntVar()
checkState17.set(val17[3])
checkBranch17 = Checkbutton(tabBranch, text=val17[1], variable=checkState17)
checkBranch17.grid(column=1, row=7, sticky=W )

#IMPLANT TRANS RETAIL
c.execute('SELECT * FROM settings where branchCode="300.114"')
val18 = c.fetchone()
checkState18 = IntVar()
checkState18.set(val18[3])
checkBranch18 = Checkbutton(tabBranch, text=val18[1], variable=checkState18)
checkBranch18.grid(column=1, row=8, sticky=W )

#IMPLANT TRAKINDO
c.execute('SELECT * FROM settings where branchCode="300.117"')
val19 = c.fetchone()
checkState19 = IntVar()
checkState19.set(val19[3])
checkBranch19 = Checkbutton(tabBranch, text=val19[1], variable=checkState19)
checkBranch19.grid(column=1, row=9, sticky=W )

#IMPLANT TRANS TV
c.execute('SELECT * FROM settings where branchCode="300.123"')
val20 = c.fetchone()
checkState20 = IntVar()
checkState20.set(val20[3])
checkBranch20 = Checkbutton(tabBranch, text=val20[1], variable=checkState20)
checkBranch20.grid(column=1, row=10, sticky=W )

#UNILEVER GROUP
c.execute('SELECT * FROM settings where branchCode="300.127"')
val21 = c.fetchone()
checkState21 = IntVar()
checkState21.set(val21[3])
checkBranch21 = Checkbutton(tabBranch, text=val21[1], variable=checkState21)
checkBranch21.grid(column=2, row=1, sticky=W )

#IMPLANT INDOFOOD
c.execute('SELECT * FROM settings where branchCode="300.133"')
val22 = c.fetchone()
checkState22 = IntVar()
checkState22.set(val22[3])
checkBranch22 = Checkbutton(tabBranch, text=val22[1], variable=checkState22)
checkBranch22.grid(column=2, row=2, sticky=W )

#IMPLANT KOMATSU
c.execute('SELECT * FROM settings where branchCode="300.140"')
val23 = c.fetchone()
checkState23 = IntVar()
checkState23.set(val23[3])
checkBranch23 = Checkbutton(tabBranch, text=val23[1], variable=checkState23)
checkBranch23.grid(column=2, row=3, sticky=W )

#ABB SAKTI INDUSTRI
c.execute('SELECT * FROM settings where branchCode="300.142"')
val24 = c.fetchone()
checkState24 = IntVar()
checkState24.set(val24[3])
checkBranch24 = Checkbutton(tabBranch, text=val24[1], variable=checkState24)
checkBranch24.grid(column=2, row=4, sticky=W )

#IMPLANT TRIPATRA
c.execute('SELECT * FROM settings where branchCode="300.146"')
val25 = c.fetchone()
checkState25 = IntVar()
checkState25.set(val25[3])
checkBranch25 = Checkbutton(tabBranch, text=val25[1], variable=checkState25)
checkBranch25.grid(column=2, row=5, sticky=W )

#IMPLANT US EMBASSY
c.execute('SELECT * FROM settings where branchCode="300.162"')
val26 = c.fetchone()
checkState26 = IntVar()
checkState26.set(val26[3])
checkBranch26 = Checkbutton(tabBranch, text=val26[1], variable=checkState26)
checkBranch26.grid(column=2, row=6, sticky=W )

#IMPLANT ASTRA HONDA MOTOR
c.execute('SELECT * FROM settings where branchCode="300.163"')
val27 = c.fetchone()
checkState27 = IntVar()
checkState27.set(val27[3])
checkBranch27 = Checkbutton(tabBranch, text=val27[1], variable=checkState27)
checkBranch27.grid(column=2, row=7, sticky=W )

#TETRA PAK INDONESIA
c.execute('SELECT * FROM settings where branchCode="300.165"')
val28 = c.fetchone()
checkState28 = IntVar()
checkState28.set(val28[3])
checkBranch28 = Checkbutton(tabBranch, text=val28[1], variable=checkState28)
checkBranch28.grid(column=2, row=8, sticky=W )

#IMPLANT BANK MANDIRI
c.execute('SELECT * FROM settings where branchCode="300.166"')
val29 = c.fetchone()
checkState29 = IntVar()
checkState29.set(val29[3])
checkBranch29 = Checkbutton(tabBranch, text=val29[1], variable=checkState29)
checkBranch29.grid(column=2, row=9, sticky=W )

#IMPLANT OJK
c.execute('SELECT * FROM settings where branchCode="300.167"')
val30 = c.fetchone()
checkState30 = IntVar()
checkState30.set(val30[3])
checkBranch30 = Checkbutton(tabBranch, text=val30[1], variable=checkState30)
checkBranch30.grid(column=2, row=10, sticky=W )

#IMPLANT ANTAM
c.execute('SELECT * FROM settings where branchCode="300.125"')
val31 = c.fetchone()
checkState31 = IntVar()
checkState31.set(val31[3])
checkBranch31 = Checkbutton(tabBranch, text=val31[1], variable=checkState31)
checkBranch31.grid(column=2, row=11, sticky=W )

def saveBranch():

    #CCC SURABAYA
    if checkState1.get() == 1:
        query1 = 'update settings set isChecked="1" where branchCode="013"'
        c.execute(query1)
        conn.commit()
    else:
        query1 = 'update settings set isChecked="0" where branchCode="013"'
        c.execute(query1)
        conn.commit()

    #CCC BALIKPAPAN
    if checkState2.get() == 1:
        query2 = 'update settings set isChecked="1" where branchCode="015"'
        c.execute(query2)
        conn.commit()
    else:
        query2 = 'update settings set isChecked="0" where branchCode="015"'
        c.execute(query2)
        conn.commit()

    #CC
    if checkState3.get() == 1:
        query3 = 'update settings set isChecked="1" where branchCode="051"'
        c.execute(query3)
        conn.commit()
    else:
        query3 = 'update settings set isChecked="0" where branchCode="051"'
        c.execute(query3)
        conn.commit()

    #CCC 2
    if checkState4.get() == 1:
        query4 = 'update settings set isChecked="1" where branchCode="052"'
        c.execute(query4)
        conn.commit()
    else:
        query4 = 'update settings set isChecked="0" where branchCode="052"'
        c.execute(query4)
        conn.commit()

    #CCC 1
    if checkState5.get() == 1:
        query5 = 'update settings set isChecked="1" where branchCode="054"'
        c.execute(query5)
        conn.commit()
    else:
        query5 = 'update settings set isChecked="0" where branchCode="054"'
        c.execute(query5)
        conn.commit()

    #GLOBAL CORPORATE
    if checkState6.get() == 1:
        query6 = 'update settings set isChecked="1" where branchCode="055"'
        c.execute(query6)
        conn.commit()
    else:
        query6 = 'update settings set isChecked="0" where branchCode="055"'
        c.execute(query6)
        conn.commit()

    #CCC MAKASSAR
    if checkState7.get() == 1:
        query7 = 'update settings set isChecked="1" where branchCode="057"'
        c.execute(query7)
        conn.commit()
    else:
        query7 = 'update settings set isChecked="0" where branchCode="057"'
        c.execute(query7)
        conn.commit()

    #IMPLANT
    if checkState8.get() == 1:
        query8 = 'update settings set isChecked="1" where branchCode="300"'
        c.execute(query8)
        conn.commit()
    else:
        query8 = 'update settings set isChecked="0" where branchCode="300"'
        c.execute(query8)
        conn.commit()

    #VAYA PAPUA
    if checkState9.get() == 1:
        query9 = 'update settings set isChecked="1" where branchCode="016"'
        c.execute(query9)
        conn.commit()
    else:
        query9 = 'update settings set isChecked="0" where branchCode="016"'
        c.execute(query9)
        conn.commit()

    #VAYA HO
    if checkState10.get() == 1:
        query10 = 'update settings set isChecked="1" where branchCode="001"'
        c.execute(query10)
        conn.commit()
    else:
        query10 = 'update settings set isChecked="0" where branchCode="001"'
        c.execute(query10)
        conn.commit()
        
    #IMPLANT ASIH EKA ABADI
    if checkState11.get() == 1:
        query11 = 'update settings set isChecked="1" where branchCode="300.100"'
        c.execute(query11)
        conn.commit()
    else:
        query11 = 'update settings set isChecked="0" where branchCode="300.100"'
        c.execute(query11)
        conn.commit()
        
    #IMPLANT BI
    if checkState12.get() == 1:
        query12 = 'update settings set isChecked="1" where branchCode="300.101"'
        c.execute(query12)
        conn.commit()
    else:
        query12 = 'update settings set isChecked="0" where branchCode="300.101"'
        c.execute(query12)
        conn.commit()
        
    #IMPLANT GA FOOD
    if checkState13.get() == 1:
        query13 = 'update settings set isChecked="1" where branchCode="300.102"'
        c.execute(query13)
        conn.commit()
    else:
        query13 = 'update settings set isChecked="0" where branchCode="300.102"'
        c.execute(query13)
        conn.commit()
        
    #IMPLANT KALBE
    if checkState14.get() == 1:
        query14 = 'update settings set isChecked="1" where branchCode="300.103"'
        c.execute(query14)
        conn.commit()
    else:
        query14 = 'update settings set isChecked="0" where branchCode="300.103"'
        c.execute(query14)
        conn.commit()
    
    #IMPLANT KPPU
    if checkState15.get() == 1:
        query15 = 'update settings set isChecked="1" where branchCode="300.104"'
        c.execute(query15)
        conn.commit()
    else:
        query15 = 'update settings set isChecked="0" where branchCode="300.104"'
        c.execute(query15)
        conn.commit()
        
    #IMPLANT THIESS
    if checkState16.get() == 1:
        query16 = 'update settings set isChecked="1" where branchCode="300.107"'
        c.execute(query16)
        conn.commit()
    else:
        query16 = 'update settings set isChecked="0" where branchCode="300.107"'
        c.execute(query16)
        conn.commit()
        
    #IMPLANT UT
    if checkState17.get() == 1:
        query17 = 'update settings set isChecked="1" where branchCode="300.108"'
        c.execute(query17)
        conn.commit()
    else:
        query17 = 'update settings set isChecked="0" where branchCode="300.108"'
        c.execute(query17)
        conn.commit()
    
    #IMPLANT TRANS RETAIL
    if checkState18.get() == 1:
        query18 = 'update settings set isChecked="1" where branchCode="300.114"'
        c.execute(query18)
        conn.commit()
    else:
        query18 = 'update settings set isChecked="0" where branchCode="300.114"'
        c.execute(query18)
        conn.commit()
        
    #IMPLANT TRAKINDO
    if checkState19.get() == 1:
        query19 = 'update settings set isChecked="1" where branchCode="300.117"'
        c.execute(query19)
        conn.commit()
    else:
        query19 = 'update settings set isChecked="0" where branchCode="300.117"'
        c.execute(query19)
        conn.commit()
        
    #IMPLANT TRANS TV
    if checkState20.get() == 1:
        query20 = 'update settings set isChecked="1" where branchCode="300.123"'
        c.execute(query20)
        conn.commit()
    else:
        query20 = 'update settings set isChecked="0" where branchCode="300.123"'
        c.execute(query20)
        conn.commit()
        
    #UNILEVER GROUP
    if checkState21.get() == 1:
        query21 = 'update settings set isChecked="1" where branchCode="300.127"'
        c.execute(query21)
        conn.commit()
    else:
        query21 = 'update settings set isChecked="0" where branchCode="300.127"'
        c.execute(query21)
        conn.commit()
        
    #IMPLANT INDOFOOD
    if checkState22.get() == 1:
        query22 = 'update settings set isChecked="1" where branchCode="300.133"'
        c.execute(query22)
        conn.commit()
    else:
        query22 = 'update settings set isChecked="0" where branchCode="300.133"'
        c.execute(query22)
        conn.commit()
        
    #IMPLANT KOMATSU
    if checkState23.get() == 1:
        query23 = 'update settings set isChecked="1" where branchCode="300.140"'
        c.execute(query23)
        conn.commit()
    else:
        query23 = 'update settings set isChecked="0" where branchCode="300.140"'
        c.execute(query23)
        conn.commit()
        
    #ABB SAKTI INDUSTRI
    if checkState24.get() == 1:
        query24 = 'update settings set isChecked="1" where branchCode="300.142"'
        c.execute(query24)
        conn.commit()
    else:
        query24 = 'update settings set isChecked="0" where branchCode="300.142"'
        c.execute(query24)
        conn.commit()
        
    #IMPLANT TRIPATRA
    if checkState25.get() == 1:
        query25 = 'update settings set isChecked="1" where branchCode="300.146"'
        c.execute(query25)
        conn.commit()
    else:
        query25 = 'update settings set isChecked="0" where branchCode="300.146"'
        c.execute(query25)
        conn.commit()
        
    #IMPLANT US EMBASSY
    if checkState26.get() == 1:
        query26 = 'update settings set isChecked="1" where branchCode="300.162"'
        c.execute(query26)
        conn.commit()
    else:
        query26 = 'update settings set isChecked="0" where branchCode="300.162"'
        c.execute(query26)
        conn.commit()
        
    #IMPLANT ASTRA HONDA MOTOR
    if checkState27.get() == 1:
        query27 = 'update settings set isChecked="1" where branchCode="300.163"'
        c.execute(query27)
        conn.commit()
    else:
        query27 = 'update settings set isChecked="0" where branchCode="300.163"'
        c.execute(query27)
        conn.commit()
        
    #TETRA PAK INDONESIA
    if checkState28.get() == 1:
        query28 = 'update settings set isChecked="1" where branchCode="300.165"'
        c.execute(query28)
        conn.commit()
    else:
        query28 = 'update settings set isChecked="0" where branchCode="300.165"'
        c.execute(query28)
        conn.commit()
        
    #IMPLANT BANK MANDIRI
    if checkState29.get() == 1:
        query29 = 'update settings set isChecked="1" where branchCode="300.166"'
        c.execute(query29)
        conn.commit()
    else:
        query29 = 'update settings set isChecked="0" where branchCode="300.166"'
        c.execute(query29)
        conn.commit()
        
    #IMPLANT OJK
    if checkState30.get() == 1:
        query30 = 'update settings set isChecked="1" where branchCode="300.167"'
        c.execute(query30)
        conn.commit()
    else:
        query30 = 'update settings set isChecked="0" where branchCode="300.167"'
        c.execute(query30)
        conn.commit()
        
    #IMPLANT ANTAM
    if checkState31.get() == 1:
        query31 = 'update settings set isChecked="1" where branchCode="300.125"'
        c.execute(query31)
        conn.commit()
    else:
        query31 = 'update settings set isChecked="0" where branchCode="300.125"'
        c.execute(query31)
        conn.commit()
    
    messagebox.showinfo('Info', 'Save Success!')

#Settings Tab
timeLabel = Label(tabSetting, text="Time Schedule (in minutes)")
timeLabel.grid(column=0, row=0, pady=5, padx=5, sticky=W)

c.execute('SELECT timeSet FROM time where id=1')
tVal = c.fetchone()[0]

textVal = StringVar()
textEntry = Entry(tabSetting, width=10, textvariable=textVal)
textEntry.grid(column=1, row=0, sticky=W)
textVal.set(tVal)

def saveSettings():
    
    #save printer
    printerUsed = variablePrint.get()
    queryPrinter = 'UPDATE printerUsed SET name="%s" WHERE id=1'%(printerUsed)
    c.execute(queryPrinter)
    conn.commit()
    
    #save time schedule
    timeValue = textEntry.get()
    queryT = 'update time set timeSet=%s'%(timeValue)
    c.execute(queryT)
    conn.commit()
    
    #save file path
    pathValue = file.get()
    queryF = 'update path set filePath="%s"'%(pathValue)
    c.execute(queryF)
    conn.commit()
    
    #save title
    titleValue = titleEntry.get()
    queryTtl = 'update title set windowTitle="%s"'%(titleValue)
    c.execute(queryTtl)
    conn.commit()
    window.title(titleValue)
    
    messagebox.showinfo('Info', 'Save Success!')

printLabel = Label(tabSetting, text="Select Printer")
printLabel.grid(column=0, row=1, pady=5, padx=5, sticky=W)


listPrinter = []

for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL+win32print.PRINTER_ENUM_CONNECTIONS, None, 1):
    listPrinter.append(printer[2])

c.execute('SELECT name FROM printerUsed where id = 1')
printVal = c.fetchone()[0]
variablePrint = StringVar()
variablePrint.set(printVal)
printerSelect = OptionMenu(tabSetting, variablePrint, *listPrinter)
printerSelect.grid(column=1, row=1, sticky=W)

buttonSaveSettings = Button(tabSetting, text="Save", background='#04ff00',command=saveSettings)
buttonSaveSettings.grid(column=0, row=8, pady=5, padx=5, sticky=W)

buttonSaveBranch = Button(tabBranch, text="Save", background='#04ff00',command=saveBranch)
buttonSaveBranch.grid(column=0, row=12, pady=5, padx=5, sticky=W)

def savePath():
    File = filedialog.askopenfile()
    pVal = File.name
    filePath.set(pVal)

buttonFile = Button(tabSetting, text="Select File", command=savePath)
buttonFile.grid(column=3, row=2, padx=5, sticky=E)

c.execute('SELECT filePath FROM path where id=1')
pVal = c.fetchone()[0]

fileLabel = Label(tabSetting, text="Select Application File")
fileLabel.grid(column=0, row=2, pady=5, padx=5, sticky=W)

filePath = StringVar()
file = Entry(tabSetting, width=30, textvariable=filePath, state='disabled')
file.grid(column=1, row=2, sticky=W)
filePath.set(pVal)

titleLabel = Label(tabSetting, text="Application Name")
titleLabel.grid(column=0, row=3, pady=5, padx=5, sticky=W)

titleVal = StringVar()
titleEntry = Entry(tabSetting, width=30, textvariable=titleVal)
titleEntry.grid(column=1, row=3, sticky=W)
titleVal.set(title)

#Application Tab
apiLabel = Label(tabAppRun, text="API Details")
apiLabel.grid(column=0, row=0, pady=5, sticky=W)

#get api
c.execute('SELECT * FROM api')
apiData = c.fetchone()

labelEndpoint = Label(tabAppRun, text='End Point')
labelEndpoint.grid(column=0,row=1, padx=20, sticky=W)

endPoint = StringVar()
api = Entry(tabAppRun, width=60, textvariable=endPoint, state='disabled')
api.grid(column=1, row=1, sticky=W)
endPoint.set(apiData[0])

labelUser = Label(tabAppRun, text='Username')
labelUser.grid(column=0,row=2, padx=20, sticky=W)

userAuth = StringVar()
user = Entry(tabAppRun, width=60, textvariable=userAuth, state='disabled')
user.grid(column=1, row=2, sticky=W)
userAuth.set(apiData[1])

labelPwd = Label(tabAppRun, text='Password')
labelPwd.grid(column=0,row=3, padx=20, sticky=W)

pwdAuth = StringVar()
pwd = Entry(tabAppRun, width=60, textvariable=pwdAuth, state='disabled', show='*')
pwd.grid(column=1, row=3, sticky=W)
pwdAuth.set(apiData[2])

def cancelEdit():
    api.configure(state='disabled')
    endPoint.set(apiData[0])
    user.configure(state='disabled')
    userAuth.set(apiData[1])
    pwd.configure(state='disabled', show='*')
    pwdAuth.set(apiData[2])
    buttonCancel.grid_remove()
    buttonSaveApi.grid_remove()
    
def saveApi():
    endPointVal = endPoint.get()
    userVal = userAuth.get()
    pwdVal = pwdAuth.get()
    
    api.configure(state='disabled')
    user.configure(state='disabled')
    pwd.configure(state='disabled', show='*')
    
    queryUpdateApi = 'update api set endPoint="{}", user="{}", password="{}"'.format(endPointVal,userVal,pwdVal)
    c.execute(queryUpdateApi)
    conn.commit()
    buttonSaveApi.grid_remove()
    buttonCancel.grid_remove()
    messagebox.showinfo('Info', 'Save Success!')


def editApi():
    global buttonCancel
    global buttonSaveApi
    api.configure(state='normal')
    user.configure(state='normal')
    pwd.configure(state='normal', show='')
    pwdAuth.set('')
    
    buttonSaveApi = Button(tabAppRun, text="Save", command=saveApi)
    buttonSaveApi.grid(column=1, row=4, pady=10, sticky=W)

    buttonCancel = Button(tabAppRun, text="Cancel", background="red", command=cancelEdit)
    buttonCancel.grid(column=1, row=4, sticky=E)
    

buttonChangeApi = Button(tabAppRun, text="Edit", command=editApi)
buttonChangeApi.grid(column=0, row=4, pady=10, padx=10, sticky=W)


def run():
    confirm = messagebox.askyesno("Info", "Start autoprint now?")
    if confirm:
        c.execute('SELECT filePath FROM path where id=1')
        path = c.fetchone()[0]
        os.system(path)
        buttonStart.config(background='#dbdbdb',state=DISABLED,text='running...')
        labelReOpen = Label(tabAppRun, text='*App has been running, please re-open this window if you want to start again')
        labelReOpen.grid(column=1, row=11, sticky=E)

startLabel = Label(tabAppRun, text="START APPLICATION")
startLabel.grid(column=1, row=9, sticky=E)

buttonStart = Button(tabAppRun, text="Start", background='#04ff00', command=run)
buttonStart.grid(column=1, row=10, pady=10, sticky=E)

window.mainloop()