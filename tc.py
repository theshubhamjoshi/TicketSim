import MySQLdb
import getpass
import os
import time
import smtplib
import datetime
from tabulate import tabulate

class Node():#Node class to implement Linked List and Queue
	def __init__(self,name,trainid, source, destination,seatno, time):
		self.name = name
		self.trainid = trainid
		self.source = source
		self.destination = destination
		self.seatno = seatno
		self.time = time
		self.next = None

class tc():#Main Ticket Checker class.
	
	
	def __init__(self):#Initializing the variables.
		self.db = MySQLdb.connect("localhost","root","Shubham@18","tc")
		self.cursor = self.db.cursor()
		self.email = None
		self.parent = None
		self.start = None
		self.rear = None
		
	def append(self,node):#appending booked tickets to LL.
		if self.parent == None:#Check if Node is None
			self.parent = node
		else:
			temp = self.parent
			while temp.next!= None:
				temp = temp.next
			temp.next = node
			
	def enqueue(self,node,coach):# enqueue the node for waiting list
	
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()


		server.login("ereservationssj@gmail.com", "Shubham@18")
		if self.start == None:#Check if start is None
			self.start = node
			self.rear = node
		else:
			self.rear.next = node
			self.rear = node
			
		temp2 = self.start
		email = temp2.name
		msg = ''
		while temp2 != None:
			msg += str(temp2.name) + " " + str(temp2.trainid) + " " + str(temp2.source) + " " + str(temp2.destination) + " " + str(temp2.seatno) + " " + str(temp2.time) + "\n"
			sql = "insert into waiting (email, trainid, seatno, coach) values ('%s','%s','%s','%s') ;"%(temp2.name,temp2.trainid,temp2.seatno, coach)
			self.cursor.execute(sql)
			self.db.commit()
			temp2 = temp2.next
			
		server.sendmail("ereservationssj@gmail.com", "%s"%(str(email)), msg)#Send confirmation mail.
			
		self.start = None;
		
		
		
	def login(self,email,password):#Login function to auth user.
		
		
		sql = "select * from users where email = '%s' and password = '%s';"%(email,password)
		self.cursor.execute(sql)
		x = self.cursor.fetchall()
		print x
		
		if x[0][1] == "Shubham SJ":
			return "admin"
			
		elif x:
			self.email = email
			return True
			
		else:
			return False
			
			
	def sendmail(self, coach):
		#Change to preffered SMTP Server.
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()

		#ENTER EMAIL AND PASS FOR SMTP LOGIN FROM GMAIL
		server.login("email here", "password here")


		msg = 'Ticket Details\n'
		
		temp2 = self.parent
		while temp2 != None:
			msg += str(temp2.name) + " " + str(temp2.trainid) + " " + str(temp2.source) + " " + str(temp2.destination) + " " + str(temp2.seatno) + " " + str(temp2.time) + "\n"
			sql = "insert into booked (email, trainid, seatno, coach) values ('%s','%s','%s','%s') ;"%(temp2.name,temp2.trainid,temp2.seatno, coach)
			self.cursor.execute(sql)
			self.db.commit()
			temp2 = temp2.next
			
		server.sendmail("ereservationssj@gmail.com", "%s"%(self.email), msg)
		
		server.quit()
		
		self.parent = None
		
		
			
			
	def register(self, name, email, password, confirm):
		if password == confirm:
			sql = "insert into users (name, email, password) values ('%s','%s','%s')"%(name,email,password)
			self.cursor.execute(sql)
			self.db.commit()
			return True
		else:
			return False
			
			
	def addTrain(self,number,source,destination,schedule,fair):
		
		sql = "insert into train values ('%s','%s','%s','%s','%s');"%(number,source,destination,schedule,fair)
		
		
		self.cursor.execute(sql)
		self.db.commit()
		x = self.cursor.fetchall()
		sql = "insert into vacancy values ('%s','AC','30');"%(number)
		self.cursor.execute(sql)
		self.db.commit()
		sql = "insert into vacancy values ('%s','SLR','30');"%(number)
		self.cursor.execute(sql)
		self.db.commit()
		for i in range(60):
			if i < 30:
				sql = "insert into seats values ('%s','AC','%s');"%(number,str(i+1))
				self.cursor.execute(sql)
				self.db.commit()
			else:
				
				sql = "insert into seats values ('%s','SLR','%s');"%(number,str(i+1-30))					
				self.cursor.execute(sql)
				self.db.commit()
		if x:
			return True
			
	def deleteTrain(self):
		count = 0
		while True:
			os.system('clear')
			print user
		
			sql = "select * from train;"
			self.cursor.execute(sql)
			x1 = self.cursor.fetchall()
		
			sql = "desc train;"
			self.cursor.execute(sql)
			x = self.cursor.fetchall()
			header1 = []
			for i in x:
				header1.append(i[0])
		
			print tabulate(x1,header1,tablefmt = 'psql')
		
			id1 = raw_input("\n\t\t\t\tEnter ID to delete : ")
			try:
				sql = "delete from seats where number = '%s';"%(id1)
				self.cursor.execute(sql)
				self.db.commit()
				sql = "delete from vacancy where number = '%s';"%(id1)
				self.cursor.execute(sql)
				self.db.commit()
				sql = "delete from train where number = '%s';"%(id1)
				self.cursor.execute(sql)
				self.db.commit()
				count += 1
			except:
				print "\n\t\t\t\tInvalid ID.."
				
			choice3 = raw_input("\n\t\t\t\tContinue? [y/n] : ")
			if choice3.lower() == 'y':
				pass
			elif choice3.lower() == 'n':
				if count!=0:
					return True
					
				break
				
	def updateSchedule(self):
		count = 0
		while True:
			os.system('clear')
			print user
		
			sql = "select * from train;"
			self.cursor.execute(sql)
			x1 = self.cursor.fetchall()
		
			sql = "desc train;"
			self.cursor.execute(sql)
			x = self.cursor.fetchall()
			header1 = []
			for i in x:
				header1.append(i[0])
		
			print tabulate(x1,header1,tablefmt = 'psql')
		
			id1 = raw_input("\n\t\t\t\tEnter ID to update : ")
			schedule  = raw_input("\n\t\t\t\tEnter new schedule : ")
			try:
				sql = "update train set schedule = '%s' where number = '%s';"%(schedule,id1)
				self.cursor.execute(sql)
				self.db.commit()
				count += 1
			except:
				print "\n\t\t\t\tInvalid ID.."
				
			choice3 = raw_input("\n\t\t\t\tContinue? [y/n] : ")
			if choice3.lower() == 'y':
				pass
			elif choice3.lower() == 'n':
				if count!=0:
					return True
				break
				
	def updateFair(self):
		count = 0
		while True:
			
			os.system('clear')
			print user
		
			sql = "select * from train;"
			self.cursor.execute(sql)
			x1 = self.cursor.fetchall()
		
			sql = "desc train;"
			self.cursor.execute(sql)
			x = self.cursor.fetchall()
			header1 = []
			for i in x:
				header1.append(i[0])
		
			print tabulate(x1,header1,tablefmt = 'psql')
		
			id1 = raw_input("\n\t\t\t\tEnter ID to update : ")
			schedule  = raw_input("\n\t\t\t\tEnter new fair : ")
			try:
				sql = "update train set fair = '%s' where number = '%s';"%(schedule,id1)
				self.cursor.execute(sql)
				self.db.commit()
				count+=1
			except:
				print "\n\t\t\t\tInvalid ID.."
				
			choice3 = raw_input("\n\t\t\t\tContinue? [y/n] : ")
			if choice3.lower() == 'y':
				pass
			elif choice3.lower() == 'n':
				if count!=0:
					return True
				break
				
		
			
			
	def book(self, source, destination):
		no = input("\n\t\t\t\tEnter no of seats : ")
		os.system('clear')
		print user
		
		sql = "select * from train where source = '%s' and destination = '%s';"%(source,destination)
		self.cursor.execute(sql)
		x1 = self.cursor.fetchall()
		
		sql = "desc train;"
		self.cursor.execute(sql)
		x = self.cursor.fetchall()
		header1 = []
		for i in x:
			header1.append(i[0])
		
		print tabulate(x1,header1,tablefmt = 'psql')
		
		schedule = raw_input("\n\t\t\t\tEnter Time : ")
	
		sql = "select * from vacancy where number = (select number from train where source = '%s' and destination = '%s' and schedule = '%s');"%(source,destination,schedule)
		self.cursor.execute(sql)
		x = self.cursor.fetchall()
		
		if x:
			os.system('clear')
			print user
			print "\n\t\t\t\t(%s) AC : %s Available"%(x[0][0],x[0][2])
			print "\n\t\t\t\t(%s) SLR : %s Available"%(x[0][0],x[1][2])
			while True:
				choice = raw_input("\n\t\t\t\tSelect Coach\n\t\t\t\t1.AC\n\t\t\t\t2.SLR\n\t\t\t\t3.Back\n\n\n\n\n>>> ")
				if choice == '1':
					count = int(x[0][2])
					for i in range(no):
						if count > 0:
							sql = "select * from seats where number = '%s' and coach = '%s';"%(x[0][0], "AC")
							self.cursor.execute(sql)
							y = self.cursor.fetchone()
							temp1 = Node(self.email,x[0][0],source,destination,y[2],datetime.datetime.now())
						
							self.append(temp1)
							sql = "delete from seats where seatno = %s and coach = 'AC';"%(str(y[2]))
							self.cursor.execute(sql)
							self.db.commit()
							sql = "update vacancy set available = '%s' where number = '%s' and coach = 'AC';"%(str(int(count)-1),x[0][0])
							self.cursor.execute(sql)
							self.db.commit()

							count -= 1
							
							
						else:
						
							temp1 = Node(self.email,x[0][0],source,destination,"Waiting",time.time())
							self.enqueue(temp1,"AC")
							
					self.sendmail("AC")
							
					return True
				
				elif choice == '2':
					count = int(x[1][2])
					for i in range(no):
						if count > 0:
							sql = "select * from seats where number = '%s' and coach = '%s';"%(x[0][0], "SLR")
							self.cursor.execute(sql)
							y = self.cursor.fetchone()
							temp1 = Node(self.email,x[0][0],source,destination,y[2],datetime.datetime.now())
						
							self.append(temp1)
							sql = "delete from seats where seatno = %s and coach = 'SLR';"%(str(y[2]))
							self.cursor.execute(sql)
							self.db.commit()
							sql = "update vacancy set available = '%s' where number = '%s' and coach = 'SLR';"%(str(int(count)-1),x[0][0])
							self.cursor.execute(sql)
							self.db.commit()
							count -= 1
							
							
						else:
							temp1 = Node(self.email,x[0][0],source,destination,"Waiting",time.time())
							self.enqueue(temp1,"SLR")
							
					self.sendmail("SLR")
					return True
						
						
				else:
					break
				
				
				
	def ticketChecker(self, email):
	
		sql = "desc booked;"
		self.cursor.execute(sql)
		x = self.cursor.fetchall()
		header = []
		for i in x:
			header.append(i[0])
	
		
		while True:
			os.system('clear')
			print user
			sql = "select * from booked where email = '%s'"%(email)
			self.cursor.execute(sql)
			x = self.cursor.fetchall()
			print tabulate(x, header, tablefmt="psql")

			id1 = raw_input("\n\t\t\tID to vacant : ")
		
			for i in x:
				if i[0] == int(id1):
					sql = "select * from booked where id = '%s'"%(i[0])
					self.cursor.execute(sql)
					temp4 = self.cursor.fetchone()
					coach = temp4[4]
					seat = temp4[3]
					trainid = temp4[2]
					email = temp4[1]
					
					
					self.db.commit()
					sql = "delete from booked where id = '%s'"%(i[0])
					self.cursor.execute(sql)
					self.db.commit()
					sql = "select * from waiting;"
					self.cursor.execute(sql)
					temp3 = self.cursor.fetchone()
					if temp3:
						sql = "insert into booked (email, trainid, seatno, coach) values('%s','%s','%s','%s');"%(temp3[1],temp3[2],str(seat[0]),temp3[4])
						self.cursor.execute(sql)
						self.db.commit()
					
						sql = "delete from waiting where id = '%s'"%(temp3[0])
						self.cursor.execute(sql)
						self.db.commit()
					
						server = smtplib.SMTP('smtp.gmail.com', 587)
						server.starttls()


						server.login("ereservationssj", "Shubham@18")
			
						msg = "Your ticket for train '%s' has been confirmed.\n Seat no : '%s'"%(temp3[2],seat)
			
						server.sendmail("ereservationssj@gmail.com", email, msg)
						
					else:
						sql = "select * from vacancy where number = '%s' and coach = '%s'"%(trainid, coach)
						self.cursor.execute(sql)
						temp9 = self.cursor.fetchone()
						
						sql = "update vacancy set available = '%s' where number = '%s' and coach = '%s'"%(str(int(temp9[2])+1),trainid, coach)
						self.cursor.execute(sql)
						self.db.commit()
						
						sql = "insert into seats values('%s','%s','%s')"%(trainid, coach, seat)
						self.cursor.execute(sql)
						self.db.commit()
					
					
			
			choice3 = raw_input("\n\t\t\t\tContinue? [y/n] : ")
			if choice3.lower() == 'y':
				pass
			elif choice3.lower() == 'n':
				break
				
			
		
		
		
				
				
			
		
		
			
			
	
		
			
			
			
			
			
temp = tc()
user = "\n\n\n\t\t\tRailway E-Reservation Platform"
while True:
	os.system('clear')
	
	print user
	
	choice = raw_input("\n\t\t\t\t1.Login\n\t\t\t\t2.Register\n\t\t\t\t3.Ticket Checker\n\n\n\n\n>>> ")
	if choice == "1":
		os.system('clear')
		print user
		email = raw_input("\n\t\t\tEmail : ")
		password = getpass.getpass("\n\t\t\tPassword : ")
		x = "\n\t\t\t\tLogging in "
		for i in range(4):
			os.system('clear')
			print user
			print x
			time.sleep(1)
			x+="."
			
		if temp.login(email,password)=="admin":
			os.system('clear')
			print user
			print "\n\t\t\tLogged In Successfuly.."
			time.sleep(1)
			os.system('clear')
			user += "\n\t\t\tWelcome Admin : %s"%(email)
			
			while True:
				os.system('clear')
				print user
				
				choice = raw_input("\n\t\t\t\t1.Add New Train\n\t\t\t\t2.Delete Train\n\t\t\t\t3.Change Schedule\n\t\t\t\t4.Update Fair\n\t\t\t\t5.Logout\n\n\n\n\n>>> ")
				
				if choice == '1':
					os.system('clear')
					print user	
					if temp.addTrain(raw_input("\n\t\t\t\tNumber : "),raw_input("\n\t\t\t\tSource : "),raw_input("\n\t\t\t\tDestination : "),raw_input("\n\t\t\t\tSchedule : "),raw_input("\n\t\t\t\tFair : ")):
						os.system('clear')
						print user
						print "\n\t\t\tTrain Added Successfully."
						time.sleep(1.5)
						
				if choice == '2':
					os.system('clear')
					print user	
					if temp.deleteTrain():
						os.system('clear')
						print user
						print "\n\t\t\tTrain Deleted Successfully."
						time.sleep(1.5)
						
				if choice == '3':
					os.system('clear')
					print user	
					if temp.updateSchedule():
						os.system('clear')
						print user
						print "\n\t\t\tSchedule Updated Successfully."
						time.sleep(1.5)
						
				if choice == '4':
					os.system('clear')
					print user	
					if temp.updateFair():
						os.system('clear')
						print user
						print "\n\t\t\tFair Updated Successfully."
						time.sleep(1.5)
				if choice == '5':
					os.system('clear')
					user = "\n\n\n\t\t\tRailway E-Reservation Platform"
					break
						
					 
			
		elif temp.login(email,password):
			os.system('clear')
			print user
			print "\n\t\t\tLogged In Successfuly.."
			time.sleep(1)
			os.system('clear')
			user += "\n\t\t\tUser :- %s"%(email)
			
			while True:
				os.system('clear')
				print user
				
				choice = raw_input("\n\t\t\t\t1.Book Now\n\t\t\t\t2.Logout\n\n\n\n\n>>> ")
				if choice == '1':
					os.system('clear')
					print user
					temp.book(raw_input("\n\t\t\t\tSource : "),raw_input("\n\t\t\t\tDestination : "))
				if choice == '2':
					os.system('clear')
					user = "\n\n\n\t\t\tRailway E-Reservation Platform"
					break
					
		else:
			os.system('clear')
			print user
			print "\n\t\t\tInvalid Login.."
			time.sleep(1)
		
					
	elif choice == '2':
		os.system('clear')
		print user
		name = raw_input("\n\t\t\tName : ")
		email = raw_input("\n\t\t\tEmail : ")
		password = getpass.getpass("\n\t\t\tPassword : ")
		password1 = getpass.getpass("\n\t\t\tPassword : ")
		if temp.register(name,email,password,password1):
			os.system('clear')
			print user
			print "\n\t\t\tSuccessfuly registered.."
			time.sleep(2)
			
			
	elif choice == '3':
		os.system('clear')
		print user
		"""name = raw_input("\n\t\t\tName : ")
		email = raw_input("\n\t\t\tEmail : ")
		password = getpass.getpass("\n\t\t\tPassword : ")
		password1 = getpass.getpass("\n\t\t\tPassword : ")
		if temp.register(name,email,password,password1):
			os.system('clear')
			print user
			print "\n\t\t\tSuccessfuly registered.."
			time.sleep(2)"""
			
		temp.ticketChecker(raw_input("\n\t\t\t\tEmail : "))
		
			
		
				
				
				
	
	

		
		
		
		


		
