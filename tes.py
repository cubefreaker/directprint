import win32api
import win32print
import os
import sqlite3

dir = os.getcwd()
conn = sqlite3.connect('data.db')
c = conn.cursor()

def printFile(printer, path):
    return win32api.ShellExecute(
            0,
            "printto",
            "req.txt",
            # "/D:{}".format(printer),
            '"{}"'.format(printer),
            path,            
            0
        )

# for i in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1):
# 	print(i[2])
c.execute('SELECT name FROM printerUsed where id = 1')
printerName = c.fetchone()[0]
print(printerName)

# phandle = win32print.OpenPrinter(printerName)

# pJobs = win32print.EnumJobs(phandle,0,-1,1)

# pJobStat1 = win32print.GetJob(phandle,20,1)
# pJobStat2 = win32print.GetJob(phandle,20,2)
# pJobStat3 = win32print.GetJob(phandle,20,3)

# print(pJobStat1['Status'])



# for i in pJobs:
# 	if 'req' in i['pDocument']:
# 		print('PJOBS')
# 		print(i)
# 		print('\n')

# print(pJobStat1)
# print('\n')
# print(pJobStat2)
# print('\n')
# print(pJobStat3)
# print('\n')

# print(win32print.JOB_STATUS_BLOCKED_DEVQ)
# print(win32print.JOB_STATUS_DELETED)
# print(win32print.JOB_STATUS_DELETING)
# print(win32print.JOB_STATUS_ERROR)
# print(win32print.JOB_STATUS_OFFLINE)
# print(win32print.JOB_STATUS_PAPEROUT)
# print(win32print.JOB_STATUS_PAUSED)
# print(win32print.JOB_STATUS_PRINTED)
# print(win32print.JOB_STATUS_PRINTING)
# print(win32print.JOB_STATUS_RESTART)
# print(win32print.JOB_STATUS_SPOOLING)
# print(win32print.JOB_STATUS_USER_INTERVENTION)
# print(win32print.JOB_STATUS_COMPLETE)
# print(win32print.JOB_STATUS_RETAINED)
# printFile(printerName, 'req')

def checkStatus(printerName, docName):
	jobStatus = ''
	jobcheck = []
	phandle = win32print.OpenPrinter(printerName)
	data = ('req.txt',None,None)
	p = win32print.StartDocPrinter(phandle,1,data)
	print(p)
	addJob = win32print.AddJob(phandle)
	print(addJob)
	pJobsEnum = win32print.EnumJobs(phandle,0,-1,1)

	for job in pJobsEnum:
		# a = job
		if docName in job['pDocument']:
			jobCheck = job
			jobStatus = job['Status']
			print(jobCheck)

	# type(jobCheck)
	# type(a)
	#JOB STATUS LIST
	blockedDriver = win32print.JOB_STATUS_BLOCKED_DEVQ			#The driver cannot print the job
	jobDeleted = win32print.JOB_STATUS_DELETED					#Job has been deleted
	jobDeleting = win32print.JOB_STATUS_DELETING				#Job is being deleted
	jobError = win32print.JOB_STATUS_ERROR						#An error is associated with the job
	jobOffline = win32print.JOB_STATUS_OFFLINE					#Printer is offline
	jobPaperOut = win32print.JOB_STATUS_PAPEROUT				#Printer is out of paper
	jobPaused = win32print.JOB_STATUS_PAUSED					#Job is paused
	jobPrinted = win32print.JOB_STATUS_PRINTED					#Job has printed
	jobPrinting = win32print.JOB_STATUS_PRINTING				#Job is printing
	jobRestart = win32print.JOB_STATUS_RESTART					#Job has been restarted
	jobSpooling = win32print.JOB_STATUS_SPOOLING				#Job is spooling
	userIntervent = win32print.JOB_STATUS_USER_INTERVENTION		#Printer has an error that requires the user to do something
	jobComplete = win32print.JOB_STATUS_COMPLETE				#The job is sent to the printer, but may not be printed yet. See Remarks for more information

	status = 0

	
	print(jobStatus)

	while status == 0:
		
		if jobStatus == blockedDriver:
			print('\nThe driver can\'t print the job')
			print('\nPlease check printer driver...')
			input('\nPress enter to continue...\n')

		elif jobStatus == jobDeleted:
			print('Job has been deleted')
			status = 1

		elif jobStatus == jobDeleting:
			print('\nDeleting Job')

		elif jobStatus == jobError:
			print('\nPrinting Error')
			print('\nPlease check printer condition...')
			input('\nPress enter to continue...\n')

		elif jobStatus == jobOffline:
			print('\nPrinter Offline')
			print('\nPlease turn on printer and continue...')
			input('\nPress enter to continue...\n')

		elif jobStatus == jobPaperOut:
			print('\nPrinter out of paper')
			print('\nPlease refill the paper and continue...')
			input('\nPress enter to continue...\n')			

		elif jobStatus == jobPaused:
			print('\nJob paused')
			print('\nPlease resume the printing job and continue...')
			input('\nPress enter to continue...\n')

		elif jobStatus == jobPrinting:
			print('\nPrinting file...')

		elif jobStatus == jobPrinted:
			print('\nFile printed')
			status = 1

		elif jobStatus == jobRestart:
			print('\nRestarting job')

		elif jobStatus == jobSpooling:
			print('\nSpooling job')
			input('\nPress enter to continue...\n')

		elif jobStatus == userIntervent:
			print('\nJob has been intervented by user')
			input('\nPress enter to continue...\n')
			status = 1

		elif jobStatus == jobComplete:
			print('\nThe job is sent to the printer')

		else:
			print('\nPrinting Error')
			print('\nPlease check printer condition...')
			input('\nPress enter to continue...\n')

	return status

checkStatus(printerName,'req')
# pStatusLevel1 = win32print.GetPrinter(phandle,1)
# pStatusLevel2 = win32print.GetPrinter(phandle,2)
# pStatusLevel3 = win32print.GetPrinter(phandle,3)
# pStatusLevel4 = win32print.GetPrinter(phandle,4)
# pStatusLevel5 = win32print.GetPrinter(phandle,5)
# pStatusLevel7 = win32print.GetPrinter(phandle,7)
# pStatusLevel8 = win32print.GetPrinter(phandle,8)
# pStatusLevel9 = win32print.GetPrinter(phandle,9)
# print(pStatusLevel1)
# print('')
# print(pStatusLevel2)
# print('')
# print(pStatusLevel3)
# print('')
# print(pStatusLevel4)
# print('')
# print(pStatusLevel5)
# print('')
# print(pStatusLevel7)
# print('')
# print(pStatusLevel8)
# print('')
# print(pStatusLevel9)


