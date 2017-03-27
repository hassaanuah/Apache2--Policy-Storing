import mysql.connector
import uuid
import time
import datetime


class DBManager:

	def __init__(self, host, user, password, dataBase):

		self.host = host
		self.password = password
		self.user = user
		self.dataBase = dataBase		

	def connect(self):

		self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.dataBase)
		return self.cnx
		#cnx.close()


	def deconnect(self):
		self.cnx.close()


############################################################################################################################


	def insert_emergency(self, Conditions, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value):
		cursor = self.cnx.cursor()
		add_emergency = "INSERT INTO Emergency (Conditions, Network_Support, S_IP, S_Port, D_IP, D_Port, Trans_Protocol, Action, Value) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(Conditions, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
		cursor.execute(add_emergency)
		return True


############################################################################################################################


	def insert_gop(self, Subscription, Package, Location, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value):
		cursor = self.cnx.cursor()
		add_gop = "INSERT INTO GOP (Subscription, Package, Location, Network_Support, S_IP, S_Port, D_IP, D_Port, Trans_Protocol, Action, Value) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(Subscription, Package, Location, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
		cursor.execute(add_gop)
		return True

############################################################################################################################


	def insert_identification(self, FQDN, MSISDN, IP, Unique_ID, Subscription):
		cursor = self.cnx.cursor()
		add_identification = "INSERT INTO ID_Table (FQDN, MSISDN, IPv4, Unique_ID, Subscription) VALUES ('%s', '%s', '%s', '%s', '%s')" %(FQDN, MSISDN, IP, Unique_ID, Subscription)
		cursor.execute(add_identification)
		return True


############################################################################################################################


	def retrieve_from_fqdn(self, fqdn):
		cursor = self.cnx.cursor()
		retrieve_identification = "select Subscription from ID_Table where FQDN= ('%s')" %(fqdn)
		cursor.execute(retrieve_identification)
		rows = []
		tablename = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					cursor = self.cnx.cursor()
					subscription = str(row[0])
					retrieve_subscription = "select * from Subscription where Name = ('%s')" %(subscription)
				cursor.execute(retrieve_subscription)
				try:
					rows = cursor.fetchall()
					if len(rows) > 0:
						for row in rows:
							tablename.append(row)
						pass #return (True, tablename)
					else:
						pass #return (False, retrieve_subscription)
				except:
					pass #return (False, retrieve_subscription)
		except:
			pass #return (False, retrieve_subscription)

		cursor = self.cnx.cursor()
		retrieve_identification = "select Unique_ID from ID_Table where FQDN= ('%s')" %(fqdn)
		cursor.execute(retrieve_identification)

		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					cursor = self.cnx.cursor()
					unique_id=str(row[0])
					retrieve_subscription = "select * from Customer_Discretion where Unique_ID = ('%s') and Active=1" %(unique_id)
				cursor.execute(retrieve_subscription)
				try:
					rows = cursor.fetchall()
					if len(rows) > 0:
						for row in rows:
							tablename.append(row)
						pass #return (True, tablename)
					else:
						pass #return (False, retrieve_subscription)
				except:
					pass #return (False, retrieve_subscription)



				
			else:
				pass #return (False, retrieve_subscription)
		except:
			pass #return (False, retrieve_subscription)


		cursor = self.cnx.cursor()
		retrieve_identification = "select Package from User_Package where Unique_ID= ('%s')" %(unique_id)
		cursor.execute(retrieve_identification)

		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					cursor = self.cnx.cursor()
					retrieve_subscription = "select * from Package where Name = ('%s')" %(row)
					cursor.execute(retrieve_subscription)
					try:
						rows = cursor.fetchall()
						if len(rows) > 0:
							for row in rows:
								tablename.append(row)
							pass #return (True, tablename)
						else:
							pass #return (False, retrieve_subscription)
					except:
						pass #return (False, retrieve_subscription)
		except:
			pass #return (False, retrieve_subscription)

		cursor = self.cnx.cursor()
		retrieve_subscription = "select * from UCOP where Unique_ID = ('%s') and Active=1" %(unique_id)
		cursor.execute(retrieve_subscription)
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					tablename.append(row)
				pass #return (True, tablename)
			else:
				pass #return (True, tablename)
		except:
			pass #return (False, retrieve_subscription)



		cursor = self.cnx.cursor()
		retrieve_subscription = "select * from Emergency where Active=1"
		cursor.execute(retrieve_subscription)
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					tablename.append(row)
				return (True, tablename)
			else:
				return (True, tablename)
		except:
			pass #return (False, retrieve_subscription)
				
		return False


############################################################################################################################


	def retrieve_from_msisdn(self, msisdn):
		cursor = self.cnx.cursor()
		retrieve_identification = "select Subscription from ID_Table where MSISDN= ('%s')" %(msisdn)
		cursor.execute(retrieve_identification)
		rows = []
		tablename = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					cursor = self.cnx.cursor()
					subscription = str(row[0])
					retrieve_subscription = "select * from Subscription where Name = ('%s')" %(subscription)
				cursor.execute(retrieve_subscription)
				try:
					rows = cursor.fetchall()
					if len(rows) > 0:
						for row in rows:
							tablename.append(row)
						pass #return (True, tablename)
					else:
						pass #return (False, retrieve_subscription)
				except:
					pass #return (False, retrieve_subscription)
		except:
			pass #return (False, retrieve_subscription)

		cursor = self.cnx.cursor()
		retrieve_identification = "select Unique_ID from ID_Table where MSISDN= ('%s')" %(msisdn)
		cursor.execute(retrieve_identification)

		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					cursor = self.cnx.cursor()
					unique_id=str(row[0])
					retrieve_subscription = "select * from Customer_Discretion where Unique_ID = ('%s') and Active=1" %(unique_id)
				cursor.execute(retrieve_subscription)
				try:
					rows = cursor.fetchall()
					if len(rows) > 0:
						for row in rows:
							tablename.append(row)
						pass #return (True, tablename)
					else:
						pass #return (False, retrieve_subscription)
				except:
					pass #return (False, retrieve_subscription)



				
			else:
				pass #return (False, retrieve_subscription)
		except:
			pass #return (False, retrieve_subscription)


		cursor = self.cnx.cursor()
		retrieve_identification = "select Package from User_Package where Unique_ID= ('%s')" %(unique_id)
		cursor.execute(retrieve_identification)

		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					cursor = self.cnx.cursor()
					retrieve_subscription = "select * from Package where Name = ('%s')" %(row)
					cursor.execute(retrieve_subscription)
					try:
						rows = cursor.fetchall()
						if len(rows) > 0:
							for row in rows:
								tablename.append(row)
							pass #return (True, tablename)
						else:
							pass #return (False, retrieve_subscription)
					except:
						pass #return (False, retrieve_subscription)
		except:
			pass #return (False, retrieve_subscription)

		cursor = self.cnx.cursor()
		retrieve_subscription = "select * from UCOP where Unique_ID = ('%s') and Active=1" %(unique_id)
		cursor.execute(retrieve_subscription)
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					tablename.append(row)
				pass #return (True, tablename)
			else:
				pass #return (True, tablename)
		except:
			pass #return (False, retrieve_subscription)



		cursor = self.cnx.cursor()
		retrieve_subscription = "select * from Emergency where Active=1"
		cursor.execute(retrieve_subscription)
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					tablename.append(row)
				return (True, tablename)
			else:
				return (True, tablename)
		except:
			pass #return (False, retrieve_subscription)
				
		return False

############################################################################################################################


	def insert_ces_negotiation_policy(self, Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints):
		cursor = self.cnx.cursor()
		add_ces_negotiation_policy = "INSERT INTO CES_Negotiation_Policy (Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints) VALUES ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s')" %(Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints)
		cursor.execute(add_ces_negotiation_policy)
		return True



############################################################################################################################


	def insert_ces_policy_params(self, Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Parameters, Value):
		cursor = self.cnx.cursor()
		add_ces_policy_params = "INSERT INTO CES_Policy_Params (Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Parameters, Value) VALUES ('%s', '%s', '%s', '%s','%s', '%s', '%s')" %(Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Parameters, Value)
		cursor.execute(add_ces_policy_params)
		return True

############################################################################################################################


	def insert_control_policy_params(self, Local_FQDN, Remote_FQDN, Direction, Parameters, Value):
		cursor = self.cnx.cursor()
		add_control_policy_params = "INSERT INTO Control_Policy_Params (Local_FQDN, Remote_FQDN, Direction, Parameters, Value) VALUES ('%s', '%s', '%s', '%s','%s')" %(Local_FQDN, Remote_FQDN, Direction, Parameters, Value)
		cursor.execute(add_control_policy_params)
		return True

############################################################################################################################


	def insert_host_id(self, Local_FQDN, ID_Type, Value):
		cursor = self.cnx.cursor()
		add_host_id = "INSERT INTO HOST_ID (Local_FQDN, ID_Type, Value) VALUES ('%s', '%s', '%s')" %(Local_FQDN, ID_Type, Value)
		cursor.execute(add_host_id)
		return True


############################################################################################################################


	def insert_host_negotiation_policy(self, Local_FQDN, Remote_FQDN, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints):
		cursor = self.cnx.cursor()
		add_host_negotiation_policy = "INSERT INTO HOST_Negotiation_Policy (Local_FQDN, Remote_FQDN, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints) VALUES ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s')" %(Local_FQDN, Remote_FQDN, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints)
		cursor.execute(add_host_negotiation_policy)
		return True



############################################################################################################################


	def insert_payload_policies(self, Local_FQDN, Remote_FQDN, Payload_Type):
		cursor = self.cnx.cursor()
		add_payload_policies = "INSERT INTO Payload_Policies (Local_FQDN, Remote_FQDN, Payload_Type) VALUES ('%s', '%s', '%s')" %(Local_FQDN, Remote_FQDN, Payload_Type)
		cursor.execute(add_payload_policies)
		return True



############################################################################################################################


	def insert_rloc_policies(self, Local_FQDN, Remote_FQDN, RLOC_Type, Value):
		cursor = self.cnx.cursor()
		add_rloc_policies = "INSERT INTO RLOC_Policies (Local_FQDN, Remote_FQDN, RLOC_Type, Value) VALUES ('%s', '%s', '%s', '%s')" %(Local_FQDN, Remote_FQDN, RLOC_Type, Value)
		cursor.execute(add_rloc_policies)
		return True


############################################################################################################################


	def insert_package(self, Name, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value):
		cursor = self.cnx.cursor()
		add_package = "INSERT INTO Package (Name, Network_Support, S_IP, S_Port, D_IP, D_Port, Trans_Protocol, Action, Value) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(Name, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
		cursor.execute(add_package)
		return True


############################################################################################################################


	def insert_subscription(self, Name, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value):
		cursor = self.cnx.cursor()
		add_subscription = "INSERT INTO Subscription (Name, Network_Support, S_IP, S_Port, D_IP, D_Port, Trans_Protocol, Action, Value) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(Name, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
		cursor.execute(add_subscription)
		return True

############################################################################################################################


	def insert_customer_discretion(self, Unique_ID, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value, Schedule, Priority):
		cursor = self.cnx.cursor()
		add_customer_discretion = "INSERT INTO Customer_Discretion (Unique_ID, Network_Support, S_IP, S_Port, D_IP, D_Port, Trans_Protocol, Action, Value, Schedule, Priority) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(Unique_ID, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value, Schedule, Priority)
		cursor.execute(add_customer_discretion)
		return True

############################################################################################################################


	def insert_ucop(self, Unique_ID, Reputation, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value):
		cursor = self.cnx.cursor()
		add_ucop = "INSERT INTO UCOP (Unique_ID, Reputation, Network_Support, S_IP, S_Port, D_IP, D_Port, Trans_Protocol, Action, Value) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(Unique_ID, Reputation, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
		cursor.execute(add_ucop)
		return True

############################################################################################################################


	def insert_user_package(self, Unique_ID, Package, Schedule):
		cursor = self.cnx.cursor()
		add_user_package = "INSERT INTO User_Package (Unique_ID, Package, Schedule) VALUES ('%s', '%s', '%s')" %(Unique_ID, Package, Schedule)
		cursor.execute(add_user_package)
		return True

############################################################################################################################


	def insertCloud(self, cloudname, cloudlocation, longitude, latitude, url, cloudprovider, providerusername, providerpassword, availablememory, availablecpu, availablestorage, availablenetwork, totalmemory, totalcpu, totalstorage, totalnetwork, country, city, continent):

		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM cloud WHERE CloudName = '%s'"%(cloudname)
		cursor.execute(get_user)
		if len(cursor.fetchall()) > 0:
			return False	
		add_cloud = "INSERT INTO cloud (CloudName, CloudLocation, Longitude, Latitude, URL, ProviderUserName, ProviderPassword, AvailableMemory, AvailableCPU, AvailableStorage, AvailableNetwork, TotalMemory, TotalCPU, TotalStorage, TotalNetwork, Country, City, Continent, CloudProvider) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(cloudname, cloudlocation, longitude, latitude, url, providerusername, providerpassword, availablememory, availablecpu, availablestorage, availablenetwork, totalmemory, totalcpu, totalstorage, totalnetwork, country, city, continent, cloudprovider)

		cursor.execute(add_cloud)
		return True


############################################################################################################################


	def insertUser_admin(self, firstName, lastName, user, password, secretquestion, secretanswer, secretkey):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM adminuser WHERE UserName = '%s'"%(user)
		cursor.execute(get_user)
		if len(cursor.fetchall()) > 0:
			return False	
		if secretkey=='adminces':
			add_user = "INSERT INTO adminuser (FirstName, LastName, UserName, Password, SecurityQuestion, SecurityAnswer) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %(firstName, lastName, user, password, secretquestion, secretanswer)
			cursor.execute(add_user)
			return True
		return False



############################################################################################################################


	def authUser(self, user, password):
		if user =='hassaan':
			if password=='ces':
				return True
		return False

	def authUser_admin(self, user, password):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM adminuser WHERE UserName = '%s' and Password = '%s'"%(user, password)
		S = cursor.execute(get_user)
		rows = []
		try:
			if len(cursor.fetchall()) > 0:
				return True
			else:
				return False
		except:
			return False


	def forgotpassword(self, user):
		cursor = self.cnx.cursor()
		get_user = "SELECT SecurityQuestion FROM user WHERE UserName = '%s'"%(user)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		secretquestion = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False	


	def forgotpassword_admin(self, user):
		cursor = self.cnx.cursor()
		get_user = "SELECT SecurityQuestion FROM adminuser WHERE UserName = '%s'"%(user)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		secretquestion = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False



	def verifyanswer(self, user, pwd):
		cursor = self.cnx.cursor()
		get_user = "SELECT Password FROM user WHERE UserName = '%s' and SecurityAnswer = '%s'"%(user,pwd)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False



	def verifyanswer_admin(self, user, pwd):
		cursor = self.cnx.cursor()
		get_user = "SELECT Password FROM adminuser WHERE UserName = '%s' and SecurityAnswer = '%s'"%(user,pwd)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False



	def clear_database(self):
		cursor = self.cnx.cursor()
		get_user = "delete from user"
		S = cursor.execute(get_user)
		return True	




	def gettables(self, user, password):
		cursor = self.cnx.cursor()
		get_user = "show tables;"
		S = cursor.execute(get_user)
		rows = []
		tablename = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				for row in rows:
					tablename.append(row[0])
				return (True, tablename)
			else:
				return (False, rows)
		except:
			return (False, rows)


