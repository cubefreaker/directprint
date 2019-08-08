# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:50:48 2019

@author: hamzah
"""

import schedule
import win32api
import win32print
import win32timezone
import urllib.request
from traceback import print_exc
#from threading import Thread, Event
from requests.auth import HTTPBasicAuth
import os, json, time, logging, requests, sqlite3, sys



class printJob:
    """ A class used to get data invoice from opsifin API and print them directly to the printer """
    
    def __init__(self, url, usr, pwd):
        """
        Parameters
        ----------
        url : str
            The url of endpoint
        usr : str
            The username of auth
        pwd : str
            The password of auth
        """
        
        self.url = url
        self.usr = usr
        self.pwd = pwd

    def post(self, url, data):
        """
        Send 'POST' request and retrieve response data if exists
        
        Parameters
        ----------
        url : str
            The url of endpoint
        data : dict
            The data required to post
        """
        
        usr = self.usr
        pwd = self.pwd
        auth = HTTPBasicAuth(usr, pwd)
        data = json.dumps(data)
        response = requests.post(url, data=data, auth=auth)

        return response.json()

    def getFile(self, Inv, url):
        """
        Download invoice data directly to specified path from url given
        
        Parameters
        ----------
        Inv : str
            The invoice Number
        url : str
            The url to the pdf file of invoice
        """
        
        self.path = os.path.join(os.getcwd(), 'tempFile')

        return urllib.request.urlretrieve(url, self.path + '/{}.pdf'.format(Inv))

    def rmFile(self, Inv):
        """
        Remove specified invoice .pdf file
        
        Parameters
        ----------
        Inv : str
            The invoice number
        """
                
        path = os.path.join(self.path, Inv)

        return os.remove(path + '.pdf')


    def mkDir(self):
        """
        Create folder named 'tempFile' to temporarily store pdf invoice data
        """
        
        dir = 'tempFile'
        if not os.path.exists(dir):
            return os.makedirs(dir)
        else:
            pass

    def printFile(self, Inv, printer):
        """
        Print invoice pdf file directly to printer
        
        Parameters
        ----------
        Inv : str
            The invoice number
        printer : str
            The name of printer
        """
        
        path = self.path
        return win32api.ShellExecute(
            0,
            "printto",
            "{}.pdf".format(Inv),
            '"{}"'.format(printer),
            path,
            0
        )

def printChecker(printerName, docName):
    """
    Checking job status from pdf invoice given to the printer, whether still in queue or have completely printed
    
    Parameters
    ----------
    printerName : obj
        The object of printer name obtained from printer enumeration
    docName :
        The document name to check (in this case is invoice number)
    """
    
    print('Printing Now : {}'.format(docName))
    jobs = 1
    timeCount = 0
    while jobs:
        phandle = win32print.OpenPrinter(printerName)
        enumStat = 1
        while enumStat:
            try:
                print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
                enumStat = 0
            except Exception:
                time.sleep(3)
                pass
                 
        listPrintJobs = []
        
        if print_jobs:
            for job in print_jobs:
                listPrintJobs.append(job["pDocument"])
                
            if docName in job["pDocument"]:
                pass
            else:
                jobs = 0
        else:
             jobs = 0
        
        if timeCount == 120:
            print('Printing taking too long time...\nPlease check the printer state, maybe out of paper or something.')
        
        win32print.ClosePrinter(phandle)
        timeCount += 5
        time.sleep(5)
        
    print("Printing Complete")
    

#def cancelPrint(printerName, docName):
#    phandle = win32print.OpenPrinter(printerName)
#    print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
#    for job in print_jobs:
#        if docName in job["pDocument"]:
#            document = job["pDocument"]
#            print("Canceling Print: " + document)
#            win32print.SetJob(phandle, job["JobId"], 0, None, win32print.JOB_CONTROL_DELETE)

#    win32print.ClosePrinter(phandle)
#    time.sleep(1)

logging.basicConfig(filename='print.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

if __name__ == '__main__':

    print('APP STARTING...')
    time.sleep(2)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    print('\nINITIALIZATION')
    time.sleep(2)

    c.execute('select * from api')
    apiData = c.fetchone()
    endPoint = apiData[0]
    user = apiData[1]
    pwd = apiData[2]
    urlGet = endPoint+'/getData'
    printInv = printJob(endPoint, user, pwd)
    
    printInv.mkDir()
	
    def aJob():
        """
        Iterating print job from list data exists 
        """
        
        # -- Fetching List File -- #
        print('\nFETCHING FILE FROM SERVER')
        
        branchList = []
        implantList = []
        comList = []
        
        for row in c.execute('SELECT branchCode, implantCode FROM settings where isChecked="1"'):
            if row[0] and row[1]:
                implantList.append(row[1])
            elif row[0]:
                branchList.append(row[0])
        
        dataPost = {"Branch":branchList,"Implant":implantList,"CustomerId":comList}
        
        postStat = 1
        while postStat:
            try:
                dataList = printInv.post(urlGet, dataPost)
                postStat = 0
            except Exception:
                time.sleep(3)
                pass
            #except Exception as e:
            #    print ('type is:'+e.__class__.__name__)
            #    print_exc()
            #    input('\nPress enter to close...')
            #    sys.exit()

        for data in dataList:

            # ----------------- Download File ----------------- #
            print('\nDownloading File : ' + data['InvNo'])
            
            downStat = 1
            while downStat:
                try:
                    printInv.getFile(data['InvNo'], data['Link'])
                    downStat = 0
                except Exception:
                    time.sleep(3)
                    pass
                #except Exception as e:
                #    print ('type is:'+e.__class__.__name__)
                #    print_exc()
                #    input('\nPress enter to close...')
                #    sys.exit()
            
            print('Download Complete')
            
            c.execute('SELECT name FROM printerUsed where id = 1')
            printerName = c.fetchone()[0]
            
            print('\nPrinting File On : {}'.format(printerName))
            time.sleep(3)
            try:
                printInv.printFile(data['InvNo'],printerName)
            except Exception as e:
                print ('type is:'+e.__class__.__name__)
                print_exc()
                input('\nPress enter to close...')
                sys.exit()
            
            time.sleep(3)
            
            for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS+win32print.PRINTER_ENUM_LOCAL, None, 1):
                    if printerName in printer[2]:
                        pName = printer[2]
            
            try:
                printChecker(pName,data['InvNo'])
            except Exception as e:
                print ('type is:'+e.__class__.__name__)
                print_exc()
                input('\nPress enter to close...')
                sys.exit()
            
            print('Posting data')
            
            dataPostSuccess = {'InvNo': data['InvNo'], 'PrintProcess': 'Success'}
            
            postAfterStat = 1
            while postAfterStat:
                try:
                    printInv.post(endPoint, dataPostSuccess)
                    postAfterStat = 0
                except Exception:
                    time.sleep(3)
                    pass
                #except Exception as e:
                #    print ('type is:'+e.__class__.__name__)
                #    print_exc()
                #    input('\nPress enter to close...')
                #    sys.exit()
            
            logging.warning('Print success on invoice %s - Status Posted', data['InvNo'])
            print('Done Posting\n')

        for rmdata in dataList:
            printInv.rmFile(rmdata['InvNo'])


    aJob()

    c.execute('SELECT timeSet FROM time where id=1')
    val = c.fetchone()[0]
    schedule.every(int(val)).minutes.do(aJob)

    while True:
        schedule.run_pending()
