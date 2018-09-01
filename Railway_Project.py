import datetime
import random
superUser={}
guestUser={}
trainInfo={}
booking={}
waitingList=[]
def init():
	superUser['admin']='admin'
	guestUser['ankit']={'name':'name','phone':'phone','age':'age','gender':'gender','pwd':'123'}
	trainInfo[12345]={
	'src':'pune',
	'dest':'delhi',
	'distance':'1200 km',
	'fare':{
		'SL':800,
		'AC3':1000,
		'AC2':1200,
		'AC1':1400
		},
	'seats':{
		'SL':64,
		'AC3':64,
		'AC2':64,
		'AC1':64
		},
	'dayOfRun':[1,0,0,0,1,0,0],
	'trainNumber':12345,
	'trainName':'Pune-Delhi Express'
	}
	trainInfo[12346]={
	'src':'Pune',
	'dest':'Delhi',
	'distance':'1200 km',
	'fare':{
		'SL':800,
		'AC3':1000,
		'AC2':1200,
		'AC1':1400
		},
	'seats':{
		'SL':64,
		'AC3':64,
		'AC2':64,
		'AC1':64
		},
	'dayOfRun':[0,0,0,0,0,0,0],
	'trainNumber':12346,
	'trainName':'Pune-Delhi Express'
	}
booking[12345]={102030:{'src':'pune','dest':'delhi','coach':'SL','Totalfare':12345,'seats':{10:'RL'}},'WL':[]}
init()

def dayOfWeek(dt):
	tempDate=dt.split('-')
	year=int(tempDate[0])
	month=int(tempDate[1])
	day=int(tempDate[2])
	return datetime.date(year,month,day).isoweekday()

def displayFare(trainNumber):
	fare=trainInfo.get(trainNumber).get('fare')
	print 'SL:%s AC3:%s AC2:%s AC1:%s' 	%(fare.get('SL'),fare.get('AC3'),fare.get('AC2'),fare.get('AC1'))
	#print 'AC3:%s' 	%(fare.get('AC3'))
	#print 'AC2:%s' 	%(fare.get('AC2'))
	#print 'AC1:%s' 	%(fare.get('AC1'))

def displaySeats(trainNumber):
	seat=trainInfo.get(trainNumber).get('seats')
	print 'SL:%s AC3:%s AC2:%s AC1:%s' %(seat.get('SL'),seat.get('AC3'),seat.get('AC2'),seat.get('AC1'))
	#print 'SL:%s' 	%(seat.get('SL'))
	#print 'AC3:%s' 	%(seat.get('AC3'))
	#print 'AC2:%s' 	%(seat.get('AC2'))
	#print 'AC1:%s' 	%(seat.get('AC1'))

def displayDayRuns(trainNumber):
	dayRun=trainInfo.get(trainNumber).get('dayOfRun')
	#print 'Monday:%s Tuesday:%s Wednesday:%s Thrusday:%s Friday:%s Saturday:%s' %(str(dayRun[0]),str(dayRun[1]),str(dayRun[2]),str(dayRun[3]),str(dayRun[4]),str(dayRun[5]),str(dayRun[6]))
	print 'Monday:',	dayRun[0]
	print 'Tuesday:',	dayRun[1]
	print 'Wednesday:',	dayRun[2]
	print 'Thrusday:',	dayRun[3]
	print 'Friday:',	dayRun[4]
	print 'Saturday:',	dayRun[5]
	print 'Sunday:',	dayRun[6]

def displayTrainInfo(trainNumber):
	info=trainInfo.get(trainNumber)
	print '='*40
	print 'Train Number:',trainNumber
	print 'Train Name:',info.get('trainName')
	print 'Total distance from %s to %s is: %s' %(info.get('src'),info.get('dest'),info.get('distance'))
	print 'Total fare for each class are:'
	displayFare(trainNumber)
	print 'Total seats availabe in each class are:'
	displaySeats(trainNumber)
	print 'Day of week train runs:'
	displayDayRuns(trainNumber)

def trainEnquiry():
	src=raw_input('Enter Source:').lower()
	dest=raw_input('Enter Destination:').lower()
	doj=raw_input('Enter date of journey(YYYY-MM-DD):')
	day=dayOfWeek(doj)
	trainNumbers= trainInfo.keys()
	for k in trainNumbers:
		if trainInfo.get(k).get('src')==src and trainInfo.get(k).get('dest')==dest and trainInfo.get(k).get('dayOfRun')[day-1]:
			displayTrainInfo(trainInfo.get(k).get('trainNumber'))
			return True
		else:
			print 'Sorry!! No trains available on the route.'

def allocConfrmSeat(availableSeats,coach,PNR,trainNumber,numOfPassengers):
		while numOfPassengers and trainInfo[trainNumber]['seats'][coach]!=0 :
			trainInfo[trainNumber]['seats'][coach]=trainInfo[trainNumber]['seats'][coach]-1
			print "Current seats:",trainInfo[trainNumber]['seats'][coach]
			seatNumber=random.randint(1,64)
			print 'SEAT NUMBER:',seatNumber
			flag=1
			while flag:
				if seatNumber not in booking.get(trainNumber).get(PNR).get('seats'):
					seatType=seatNumber%8
					if seatType==0:
						seatType='LL'
					elif seatType==1:
						seatType='LM'
					elif seatType==2:
						seatType='LU'
					elif seatType==3:
						seatType='RL'
					elif seatType==4:
						seatType='RM'
					elif seatType==5:
						seatType='RU'
					elif seatType==6:
						seatType='SL'
					elif seatType==7:
						seatType='SU'
					print 'SEAT TYPE:',seatType
					booking[trainNumber][PNR]['seats'][seatNumber]=seatType
					numOfPassengers-=1
					flag=0

def allocWaiting(PNR,trainNumber):
	if len(booking[trainNumber]['WL'])==0:
		#print 'length of waiting list:',len(waitingList)
		booking[trainNumber]['WL'].append(1)
	else:
		count=booking[trainNumber]['WL'][-1]
		print "Waiting count:",count
		booking[trainNumber]['WL'].append(count+1)

def allotSeats(trainNumber,coach,numOfPassengers,PNR):
	availableSeats=trainInfo[trainNumber].get('seats').get(coach)

	if availableSeats>=numOfPassengers:
		print 'Inside Confirm Seats'
		allocConfrmSeat(availableSeats,coach,PNR,trainNumber,numOfPassengers)
	else:
		print 'Inside Waiting Seats'
		counter = numOfPassengers - availableSeats
		print 'counter:',counter
		print 'AVAILABLE SEATS:',availableSeats
		allocConfrmSeat(availableSeats,coach,PNR,trainNumber,numOfPassengers)
		while counter:
			allocWaiting(PNR,trainNumber)
			print 'Seats are less'
			counter-=1

def bookTicket():
	if True:
		print '*'*40
		option=int(raw_input('1.Book Ticket \n2.Go Back \nEnter your choice:'))
		if option==1:
			flag=coach=1
			while flag:				
				trainNumber=int(raw_input('Enter Train Number:'))
				if trainNumber in trainInfo:
					flag=0
					while coach:
						coachType=raw_input('Enter coach type(AC3/AC2/AC1/SL):')
						if coachType=='SL':
							coach=0
							src=trainInfo[trainNumber].get('src')
							dest=trainInfo[trainNumber].get('dest')
							numOfPassengers=int(raw_input('Enter Number of passengers:'))
							totalfare= numOfPassengers * (trainInfo[trainNumber].get('fare').get('SL'))
							PNR=random.randint(100000,999999)
							booking[trainNumber][PNR]={'src':src,'dest':dest,'coach':'SL','Totalfare':totalfare,'seats':{}}
							#booking[PNR]={'src':src,'dest':dest,'trainNumber':trainNumber,'coach':'SL','Totalfare':totalfare,'seats':{'WL':[]},'PNR':PNR}
							print 'PNR IS:',PNR
							allotSeats(trainNumber,coachType,numOfPassengers,PNR)
							print '\n',booking[trainNumber]
							print '\n\nTicket booked!!'
							bookTicket()
						elif coachType=='AC3':
							coach=0
							src=trainInfo[trainNumber].get('src')
							dest=trainInfo[trainNumber].get('dest')
							numOfPassengers=int(raw_input('Enter Number of passengers:'))
							totalfare= numOfPassengers * (trainInfo[trainNumber].get('fare').get('AC3'))
							PNR=random.randint(100000,999999)
							booking[trainNumber][PNR]={'src':src,'dest':dest,'coach':'AC3','Totalfare':totalfare,'seats':{}}
							print 'PNR IS:',PNR
							allotSeats(trainNumber,coachType,numOfPassengers,PNR)
							print '\n',booking[trainNumber]
							print '\n\nTicket booked!!'
							bookTicket()
							
						elif coachType=='AC2':
							coach=0
							src=trainInfo[trainNumber].get('src')
							dest=trainInfo[trainNumber].get('dest')
							numOfPassengers=int(raw_input('Enter Number of passengers:'))
							totalfare= numOfPassengers * (trainInfo[trainNumber].get('fare').get('AC2'))
							PNR=random.randint(100000,999999)
							booking[trainNumber][PNR]={'src':src,'dest':dest,'coach':'AC2','Totalfare':totalfare,'seats':{}}
							print 'PNR IS:',PNR
							allotSeats(trainNumber,coachType,numOfPassengers,PNR)
							print '\n',booking[trainNumber]
							print '\n\nTicket booked!!'
							bookTicket()
							
						elif coachType=='AC1':
							coach=0
							src=trainInfo[trainNumber].get('src')
							dest=trainInfo[trainNumber].get('dest')
							numOfPassengers=int(raw_input('Enter Number of passengers:'))
							totalfare= numOfPassengers * (trainInfo[trainNumber].get('fare').get('AC1'))
							PNR=random.randint(100000,999999)
							booking[trainNumber][PNR]={'src':src,'dest':dest,'coach':'AC1','Totalfare':totalfare,'seats':{}}
							print 'PNR IS:',PNR
							allotSeats(trainNumber,coachType,numOfPassengers,PNR)
							print '\n',booking[trainNumber]
							print '\n\nTicket booked!!'
							bookTicket()
						else:
							print'Invalid Coach type!! please enter a valid coach type'

				else:
					print'Invalid Train Number!! Please enter again.'
		elif option==2:
			#pass
			guestLoginPage()

		else:
			print 'Wrong Choice!! Enter again:'
			bookTicket()
	else:
		print 'Train not found'

def cancelTicket():
	pass

def statusCheck():
	pass

def guestLoginPage():
	while True:
		print '='*40
		print ' 1.Train Enquiry \n 2.Book Ticket \n 3.Cancel Ticket \n 4.PNR Status \n 5.Logout'
		choice=int(raw_input('Enter your choice:'))
		print '='*40
		if choice==1:
			trainEnquiry()

		elif choice==2:
			bookTicket()

		elif choice==3:
			cancelTicket()

		elif choice==4:
			statusCheck()

		elif choice==5:
			login()

		else:
			print '='*40
			print 'Invalid choice!! Please select a valid option.'
			guestLoginPage()

def DayRun(dayOfRun):
	for day in range(0,7):
		flag=1
		if day==0:
			while flag:
				print '*'*40
				x=int(raw_input('Monday(0/1):'))
				if x not in [0,1]:
					print 'Invalid input!! please enter 0 for non running and 1 for running'
				else:
					dayOfRun.append(x)
					flag=0

		elif day==1:
			while flag:
				print '*'*40
				x=int(raw_input('Tuesday(0/1):'))
				if x not in [0,1]:
					print 'Invalid input!! please enter 0 for non running and 1 for running'
				else:
					dayOfRun.append(x)
					flag=0
				
		elif day==2:
			while flag:
				print '*'*40
				x=int(raw_input('Wednesday(0/1):'))
				if x not in [0,1]:
					print 'Invalid input!! please enter 0 for non running and 1 for running'
				else:
					dayOfRun.append(x)
					flag=0

		elif day==3:
			while flag:
				print '*'*40
				x=int(raw_input('Thurday(0/1):'))
				if x not in [0,1]:
					print 'Invalid input!! please enter 0 for non running and 1 for running'
				else:
					dayOfRun.append(x)
					flag=0

		elif day==4:
			while flag:
				print '*'*40
				x=int(raw_input('Friday(0/1):'))
				if x not in [0,1]:
					print 'Invalid input!! please enter 0 for non running and 1 for running'
				else:
					dayOfRun.append(x)
					flag=0

		elif day==5:
			while flag:
				print '*'*40
				x=int(raw_input('Saturday(0/1):'))
				if x not in [0,1]:
					print 'Invalid input!! please enter 0 for non running and 1 for running'
				else:
					dayOfRun.append(x)
					flag=0

		elif day==6:
			while flag:
				print '*'*40
				x=int(raw_input('Sunday(0/1):'))
				if x not in [0,1]:
					print 'Invalid input!! please enter 0 for non running and 1 for running'
				else:
					dayOfRun.append(x)
					flag=0
	return dayOfRun

def addTrain():
	addMore='y'
	while addMore=='y' or addMore=='yes':
		print '='*40
		trainNumber = int(raw_input('Enter the New Train Number:'))
		if trainNumber in trainInfo.keys():
			print 'Train number already present!! Enter different train number'
			addTrain()
		else:
			tempTrainInfo={}
			trainName=raw_input('Enter Train Name:')
			src=raw_input('Enter Source:')
			dest=raw_input('Enter Destination:')
			distance=raw_input('Enter distance(km):')

			print '+++++++++Entering Fare+++++++++'
			SL,AC3,AC2,AC1=int(raw_input('Enter SL fare:')),int(raw_input('Enter AC3 fare:')),int(raw_input('Enter AC2 fare:')),int(raw_input('Enter AC1 fare:'))
			
			print '+++++Entering Available Seats+++++++'
			SL_S,AC3_S,AC2_S,AC1_S=int(raw_input('Enter SL seats:')),int(raw_input('Enter AC3 seats:')),int(raw_input('Enter AC2 seats:')),int(raw_input('Enter AC1 seats:'))

			print 'Enter the day on which train runs:'
			dayOfRun=[]
			dayOfRun=DayRun(dayOfRun)
			tempTrainInfo[trainNumber]={
			'src':src,
			'dest':dest,
			'distance':distance,
			'fare':{
				'SL':SL,
				'AC3':AC3,
				'AC2':AC2,
				'AC1':AC1
				},
			'seats':{
				'SL':SL_S,
				'AC3':AC3_S,
				'AC2':AC2_S,
				'AC1':AC1_S
				},
			'dayOfRun':dayOfRun,
			'trainNumber':trainNumber,
			'trainName':trainName
			}
			trainInfo.update(tempTrainInfo)

			print '************Train details has been successfully added into database!!*******************'
			addMore=raw_input('Enter more train details?(Y/N):').lower()
	else:
		adminLoginPage()

def modifyTrainDetails(trainNumber):
	print 'Current Train Info:',trainInfo[trainNumber]
	currentTrainInfo=trainInfo[trainNumber]
	currentFare=currentTrainInfo['fare']
	curentSeats=currentTrainInfo['seats']
	print '='*40
	currentTrainInfo['trainName']=raw_input('Enter New Train Name:')
	currentTrainInfo['src']=raw_input('Enter New Source:')
	currentTrainInfo['dest']=raw_input('Enter New Destination:')
	currentTrainInfo['distance']=raw_input('Enter New distance(km):')
	print '\n'
	print '+++++++++Entering Fare+++++++++'
	currentFare['SL'],currentFare['AC3'],currentFare['AC2'],currentFare['AC1']=int(raw_input('Enter SL fare:')),int(raw_input('Enter AC3 fare:')),int(raw_input('Enter AC2 fare:')),int(raw_input('Enter AC1 fare:'))
	print '\n'
	print '+++++Entering Available Seats+++++++'
	curentSeats['SL'],curentSeats['AC3'],curentSeats['AC2'],curentSeats['AC1']=int(raw_input('Enter SL seats:')),int(raw_input('Enter AC3 seats:')),int(raw_input('Enter AC2 seats:')),int(raw_input('Enter AC1 seats:'))
	print '\n'
	print 'Enter the day on which train runs:'
	dayOfRun=[]
	currentTrainInfo['dayOfRun']=DayRun(dayOfRun)
	print '************Train details has been successfully updated into database!!*******************'
	displayTrainInfo(trainNumber)
	print '='*40

def modifyTrain():
	modifyMore='y'
	while modifyMore=='y' or modifyMore=='yes':
		print '++++++++++++++++ Modify Train Details ++++++++++++++'
		flag=1
		while flag:
			trainNumber=int(raw_input('Enter Train Number:'))
			if trainInfo.get(trainNumber):
				modifyTrainDetails(trainNumber)
				flag=0
			else:
				print 'No such train exists!! Enter a valid train number'
		modifyMore=raw_input('Do yo want to modify more trains?(Y/N):')
	else:
		print '*'*40
		adminLoginPage()

def removeTrain():
	print '*'*40
	trainNumber=int(raw_input('Enter Train Number:'))
	if trainNumber in trainInfo:
		trainInfo.pop(trainNumber)
		print 'Train Removed successfully!!'
		#print 'Total trains:',trainInfo
		adminLoginPage()
	else:
		print 'No train found with train number:',trainNumber,'. Please enter a valid train number'
		removeTrain()

def makeUserAdmin():
	name=raw_input('Enter user name:')
	if name in guestUser:
		if name not in superUser:
			tempGuestUser=guestUser.pop(name)
			superUser[name]=tempGuestUser
			print 'User \'%s\' upgraded to Admin.' %(name)
		else:
			print 'User is already admin!!'
			adminLoginpage()

	else:
		print 'User does not exist!! Enter a valid user name.'
		makeUserAdmin()

def editPassword():
	flag=outer=inner=1
	while flag:
		print '*'*40
		uname=raw_input('Enter the username:')
		if uname in superUser:
			flag=0
			while outer:
				pwd=raw_input('Enter the current password:')
				if superUser.get(uname)==pwd:
					outer=0
					while inner:
						newPwd=raw_input('Enter new password:')
						rePwd=raw_input('Re-Enter password:')
						if newPwd==rePwd and newPwd != pwd:
							superUser[uname]=newPwd
							print 'Password Updated!!'
							inner=0
						elif newPwd == pwd:
							print 'New password can not be old password!!'
						else:
							print 'Password do not match!! Please enter again.'
				else:
					print 'Wrong password!! Please Enter again.'
		else:
			print 'User does not exist!! Please enter valid user.'

def adminLoginPage():
	while True:
		print '='*40
		print ' 1.Add Train \n 2.Modify Train \n 3.Remove Train \n 4.Make User Admin \n 5.Edit Password \n 6.Logout'
		choice=int(raw_input('Enter your choice:'))
		print '='*40
		if choice==1:
			addTrain()

		elif choice==2:
			modifyTrain()

		elif choice==3:
			removeTrain()

		elif choice==4:
			makeUserAdmin()

		elif choice==5:
			editPassword()

		elif choice==6:
			login()

		else:
			print '='*40
			print 'Invalid choice!! Please select a valid option.'
			adminLoginPage()

def LoginPage():
	print '='*40
	uname=raw_input('Enter the user name:')
	uname=uname.lower()
	if guestUser.get(uname):
		attempt=3
		while attempt:
			pwd=raw_input('Enter the Password:')
			if guestUser.get(uname).get('pwd')==pwd:
				print 'Login Successfull!!'
				guestLoginPage()
			else:
				attempt -=1
				print 'Wrong Password!! Attempt left %d' %(attempt)
		else:
			print '='*40
			print 'Wrong attempt made for 3 time. Exiting....'
			exit()

	elif superUser.get(uname):
		attempt=3
		while attempt:
			pwd=raw_input('Enter the Password:')
			if superUser.get(uname)==pwd:
				print 'Login Successfull as Admin!!'
				adminLoginPage()
			else:
				attempt -=1
				print 'Wrong Password!! Attempt left %d' %(attempt)
		else:
			print '='*40
			print 'Wrong attempt made for 3 time. Exiting....'
			exit()
	else:
		print 'No such user found!! Please SignUp first'
		#login()

def SignUpPage():
	print '='*16,'Welcome!!','='*17
	'''
	name=raw_input('Enter your Full Name:')
	phone=raw_input('Enter your Phone number:')
	age=int(raw_input('Enter your age:'))
	gender=raw_input('Enter your gender(M/F):')
	'''
	flag=1;
	while flag:
		username=raw_input('Enter your account username:').lower()
		if guestUser.get(username) or superUser.get(username):
			print 'User Name already exists. Please enter a differnt user name!!'
		else:
			flag=0
			pwd=raw_input('Enter you account Password:')
			guestUser[username]=pwd
			print 'Account created Successfully!!'
			login()

while True:
	def login():
		print '='*40
		print ' 1.Login \n 2.SignUp \n 3.Exit'
		print '='*40
		choice=int(raw_input('Enter your choice:'))

		if choice==1:
			LoginPage();
		elif choice==2:
			SignUpPage();
		elif choice==3:
			print "Thank you !! Please visit again :)"
			exit()
		else:
			print 'Wrong Input!! Please enter a valid option.'
	login()


