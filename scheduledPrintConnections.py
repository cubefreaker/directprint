import schedule
import win32api
import win32print
import win32timezone
import urllib.request
from traceback import print_exc
from threading import Thread, Event
from requests.auth import HTTPBasicAuth
import os, json, time, logging, requests, sqlite3, sys



class printJob:

    def __init__(self, url, usr, pwd):
        self.url = url
        self.usr = usr
        self.pwd = pwd

    def post(self, url, data):
        usr = self.usr
        pwd = self.pwd
        auth = HTTPBasicAuth(usr, pwd)
        data = json.dumps(data)
        response = requests.post(url, data=data, auth=auth)

        return response.json()

    #def post(self, Inv, status):
    #    url = self.url
    #    usr = self.usr
    #    pwd = self.pwd
    #    auth = HTTPBasicAuth(usr, pwd)
    #    data = json.dumps({"InvNo": Inv, "PrintProcess": status})
    #    response = requests.post(url, data=data, auth=auth)

    #    return response

    def getFile(self, Inv, url):
        self.path = os.path.join(os.getcwd(), 'tempFile')

        return urllib.request.urlretrieve(url, self.path + '/{}.pdf'.format(Inv))

    def rmFile(self, Inv):
        path = os.path.join(self.path, Inv)

        return os.remove(path + '.pdf')


    def mkDir(self):
        dir = 'tempFile'
        if not os.path.exists(dir):
            return os.makedirs(dir)
        else:
            pass

    def printFile(self, Inv, printer):
        path = self.path
        return win32api.ShellExecute(
            0,
            "printto",
            "{}.pdf".format(Inv),
            '"{}"'.format(printer),
            path,
            0
        )

stop_event = Event()

def printChecker(printerName, docName):
    jobs = [1]
    while jobs:
        jobs = []
        phandle = win32print.OpenPrinter(printerName)
        print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
        if print_jobs:
            jobs.extend(list(print_jobs))
        for job in print_jobs:
            if docName in job["pDocument"]:
                document = job["pDocument"]
                print("Printing Now: " + document + " - status %s"%(job["Status"]))
        win32print.ClosePrinter(phandle)
        time.sleep(5)
        # check if the other thread sent a signal to stop execution.
        #if stop_event.is_set():
        #    break

def cancelPrint(printerName, docName):
    phandle = win32print.OpenPrinter(printerName)
    print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
    for job in print_jobs:
        if docName in job["pDocument"]:
            document = job["pDocument"]
            print("Canceling Print: " + document)
            win32print.SetJob(phandle, job["JobId"], 0, None, win32print.JOB_CONTROL_DELETE)

    win32print.ClosePrinter(phandle)
    time.sleep(1)

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
        global identifier
        # -- Fetching List File -- #
        print('\nFETCHING FILE FROM SERVER')
        
        branchList = []
        implantList = []
        
        for row in c.execute('SELECT branchCode, implantCode FROM settings where isChecked="1"'):
            if row[0] and row[1]:
                implantList.append(row[1])
            elif row[0]:
                branchList.append(row[0])
        
        dataPost = {"Branch":branchList,"Implant":implantList}
        
        try:
            dataList = printInv.post(urlGet, dataPost)
        except Exception as e:
            print ('type is:'+e.__class__.__name__)
            print_exc()
            input('\nPress enter to close...')
            sys.exit()
            
        # branch = '-'+branchCode+'-'
        #for data in printInv.get():
        #    for row in c.execute('SELECT branchCode FROM settings where isChecked="1"'):
        #        branch = row[0]+'-'
        #        if branch in data['InvNo']:
        #            dataList.append(data)
        #        else:
        #            pass
        #print(dataList)
	#time.sleep(10000)

        for data in dataList:

            # ----------------- Download File ----------------- #
            print('\nDownloading File : ' + data['InvNo'])
            
            try:
                printInv.getFile(data['InvNo'], data['Link'])
            except Exception as e:
                print ('type is:'+e.__class__.__name__)
                print_exc()
                input('\nPress enter to close...')
                sys.exit()
            
            print('Download Complete')

            identifier = 1
            def printFix():
                global identifier
                # ------ Print File ------ #

                c.execute('SELECT name FROM printerUsed where id = 1')
                printerName = c.fetchone()[0]
                print('\nPrinting File On : {}'.format(printerName))
                
                try:
                    printInv.printFile(data['InvNo'],printerName)
                except Exception as e:
                    print ('type is:'+e.__class__.__name__)
                    print_exc()
                    input('\nPress enter to close...')
                    sys.exit()

                # check print status
                for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS, None, 1):
                    if printerName in printer[2]:
                        pName = printer[2]
                        
                state = Thread(target=printChecker, args=(pName, data['InvNo'],))
                try:
                    state.start()
                except Exception as e:
                    print ('type is:'+e.__class__.__name__)
                    print_exc()
                    input('\nPress enter to close...')
                    sys.exit()
                
                # set timeout
                state.join(timeout=30)

                if state.is_alive():
                    #stop_event.set()
                    if identifier < 3:
                        identifier = identifier + 1
                        print('Printing taking too long time, retrying attemp...')
                        cancelPrint(printerName, data['InvNo'])
                        printFix()
                    else:
                        cancelPrint(printerName, data['InvNo'])
                        print('TIME OUT: Print Failed')
                        dataPostFailed = {'InvNo': data['InvNo'], 'PrintProcess': 'Failed'}
                        try:
                            printInv.post(endPoint, dataPostFailed)
                        except Exception as e:
                            print ('type is:'+e.__class__.__name__)
                            print_exc()
                            input('\nPress enter to close...')
                            sys.exit()
                        
                        logging.warning('Print failed on invoice %s - Time Out ', data['InvNo'])
                        time.sleep(5)
                        sys.exit()
                        return False
                else:
                    print("Printing Complete")
                    return True

            if printFix() == True:
                # -------- Posting status ----- #
                print('Posting data')
                dataPostSuccess = {'InvNo': data['InvNo'], 'PrintProcess': 'Success'}
                
                try:
                    printInv.post(endPoint, dataPostSuccess)
                except Exception as e:
                    print ('type is:'+e.__class__.__name__)
                    print_exc()
                    input('\nPress enter to close...')
                    sys.exit()
                logging.warning('Print success on invoice %s - Status Posted', data['InvNo'])
                print('Done Posting\n')
            else:
                sys.exit()


        for rmdata in dataList:
            printInv.rmFile(rmdata['InvNo'])


    aJob()

    c.execute('SELECT timeSet FROM time where id=1')
    val = c.fetchone()[0]
    schedule.every(int(val)).minutes.do(aJob)

    while True:
        schedule.run_pending()
