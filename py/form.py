import smtplib
from mod_python import apache, Session, util
import json
import cgi
from DBManager import DBManager

SMTP_SERVER = "localhost" # your SMTP server

dbManager_Service = DBManager("127.0.0.1","root","take5","Firewall_Policies")
dbManager_CES = DBManager("127.0.0.1","root","take5","CES_Policies")




def add_identification(req):
	info =req.form
	FQDN = info['FQDN']
	MSISDN = info['MSISDN']
	IP = info['IP']
	Unique_ID = info['Unique_ID']
	Subscription = info['Subscription']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_identification(FQDN, MSISDN, IP, Unique_ID, Subscription)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)



def add_emergency(req):
	info =req.form
	Conditions = info['Conditions'] 
	Network_Support = info['Network_Support']
	Source_IP = info['Source_IP']
	Source_Port = info['Source_Port']
	Destination_IP = info['Destination_IP']		
	Destination_Port = info['Destination_Port']
	Transport_Pro = info['Transport_Pro']
	Action = info['Action']
	Value = info['Value']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_emergency(Conditions, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)	


def add_gop(req):
	info =req.form
	Subscription = info['Subscription']
	Package = info['Package']
	Location = info['Location']
	Network_Support = info['Network_Support']
	Source_IP = info['Source_IP']
	Source_Port = info['Source_Port']
	Destination_IP = info['Destination_IP']		
	Destination_Port = info['Destination_Port']
	Transport_Pro = info['Transport_Pro']
	Action = info['Action']
	Value = info['Value']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_gop(Subscription, Package, Location, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)	


def add_package(req):
	info =req.form
	Name = info['Name']
	Network_Support = info['Network_Support']
	Source_IP = info['Source_IP']
	Source_Port = info['Source_Port']
	Destination_IP = info['Destination_IP']		
	Destination_Port = info['Destination_Port']
	Transport_Pro = info['Transport_Pro']
	Action = info['Action']
	Value = info['Value']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_package(Name, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)


def add_subscription(req):
	info =req.form
	Name = info['Name']
	Network_Support = info['Network_Support']
	Source_IP = info['Source_IP']
	Source_Port = info['Source_Port']
	Destination_IP = info['Destination_IP']		
	Destination_Port = info['Destination_Port']
	Transport_Pro = info['Transport_Pro']
	Action = info['Action']
	Value = info['Value']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_subscription(Name, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)


def add_ucop(req):
	info =req.form
	Unique_ID = info['Unique_ID']
	Reputation = info['Reputation']
	Network_Support = info['Network_Support']
	Source_IP = info['Source_IP']
	Source_Port = info['Source_Port']
	Destination_IP = info['Destination_IP']		
	Destination_Port = info['Destination_Port']
	Transport_Pro = info['Transport_Pro']
	Action = info['Action']
	Value = info['Value']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_ucop(Unique_ID, Reputation, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)


def add_customer_discretion(req):
	info =req.form
	Unique_ID = info['Unique_ID']
	Network_Support = info['Network_Support']
	Source_IP = info['Source_IP']
	Source_Port = info['Source_Port']
	Destination_IP = info['Destination_IP']		
	Destination_Port = info['Destination_Port']
	Transport_Pro = info['Transport_Pro']
	Action = info['Action']
	Value = info['Value']
	Schedule = info['Schedule']
	Priority = info['Priority']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_customer_discretion(Unique_ID, Network_Support, Source_IP, Source_Port, Destination_IP, Destination_Port, Transport_Pro, Action, Value, Schedule, Priority)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)


def add_user_package(req):
	info =req.form
	Unique_ID = info['Unique_ID']
	Package = info['Package']
	Schedule = info['Schedule']
	result = {}
	dbManager_Service.connect()
	result['success'] =  dbManager_Service.insert_user_package(Unique_ID, Package, Schedule)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)


def add_ces_negotiation_policy(req):
	info =req.form
	Trans_Protocol = info['Trans_Protocol']
	Link_Alias = info['Link_Alias']
	Dest_CES_ID = info['Dest_CES_ID']
	Reputation = info['Reputation']
	Direction = info['Direction']
	Policy_Required = info['Policy_Required']
	Policy_Offer = info['Policy_Offer']
	Policy_Available = info['Policy_Available']
	Policy_Required_Constraints = info['Policy_Required_Constraints']
	result = {}
	dbManager_CES.connect()
	result['success'] =  dbManager_CES.insert_ces_negotiation_policy(Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def add_ces_policy_params(req):
	info =req.form
	Trans_Protocol = info['Trans_Protocol']
	Link_Alias = info['Link_Alias']
	Dest_CES_ID = info['Dest_CES_ID']
	Reputation = info['Reputation']
	Direction = info['Direction']
	Parameters = info['Parameters']
	Value = info['Value']
	result = {}
	dbManager_CES.connect()
	result['success'] =  dbManager_CES.insert_ces_policy_params(Trans_Protocol, Link_Alias, Dest_CES_ID, Reputation, Direction, Parameters, Value)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def add_control_policy_params(req):
	info =req.form
	Local_FQDN = info['Local_FQDN']
	Remote_FQDN = info['Remote_FQDN']
	Direction = info['Direction']
	Parameters = info['Parameters']
	Value = info['Value']
	result = {}
	dbManager_CES.connect()
	result['success'] =  dbManager_CES.insert_control_policy_params(Local_FQDN, Remote_FQDN, Direction, Parameters, Value)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def add_host_id(req):
	info =req.form
	Local_FQDN = info['Local_FQDN']
	ID_Type = info['ID_Type']
	Value = info['Value']
	result = {}
	dbManager_CES.connect()
	result['success'] =  dbManager_CES.insert_host_id(Local_FQDN, ID_Type, Value)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def add_host_negotiation_policy(req):
	info =req.form
	Local_FQDN = info['Local_FQDN']
	Remote_FQDN = info['Remote_FQDN']
	Reputation = info['Reputation']
	Direction = info['Direction']
	Policy_Required = info['Policy_Required']
	Policy_Offer = info['Policy_Offer']
	Policy_Available = info['Policy_Available']
	Policy_Required_Constraints = info['Policy_Required_Constraints']
	result = {}
	dbManager_CES.connect()
	result['success'] =  dbManager_CES.insert_host_negotiation_policy(Local_FQDN, Remote_FQDN, Reputation, Direction, Policy_Required, Policy_Offer, Policy_Available, Policy_Required_Constraints)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def add_payload_policies(req):
	info =req.form
	Local_FQDN = info['Local_FQDN']
	Remote_FQDN = info['Remote_FQDN']
	Payload_Type = info['Payload_Type']
	result = {}
	dbManager_CES.connect()
	result['success'] =  dbManager_CES.insert_payload_policies(Local_FQDN, Remote_FQDN, Payload_Type)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def add_rloc_policies(req):
	info =req.form
	Local_FQDN = info['Local_FQDN']
	Remote_FQDN = info['Remote_FQDN']
	RLOC_Type = info['RLOC_Type']
	Value = info['Value']
	result = {}
	dbManager_CES.connect()
	result['success'] =  dbManager_CES.insert_rloc_policies(Local_FQDN, Remote_FQDN, RLOC_Type, Value)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def addUser(req):
	info =req.form
	firstName = info['firstName']
	lastName = info['lastName']
	user = info['user']
	password = info['password']
	secretquestion = info['secretquestion']		
	secretanswer = info['secretanswer']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.insertUser(firstName, lastName, user, password, secretquestion, secretanswer)
	dbManager.deconnect()
	return json.dumps(result,indent=1)



def addUser_admin(req):
	info =req.form
	firstName = info['firstName']
	lastName = info['lastName']
	user = info['user']
	password = info['password']
	secretquestion = info['secretquestion']		
	secretanswer = info['secretanswer']
	secretKey = info['secretKey']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.insertUser_admin(firstName, lastName, user, password, secretquestion, secretanswer, secretKey)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def authUser(req):
	info =req.form
	user = info['user']
	password = info['password']		
	result = {}
	result['success'] =  dbManager_Service.authUser(user, password)
	return json.dumps(result,indent=1)


def authUser_admin(req):
	info =req.form
	user = info['user_admin']
	password = info['password_admin']		
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.authUser_admin(user, password)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def forgetpassword(req):
	info =req.form
	user = info['user']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.forgotpassword(user)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def forgetpassword_admin(req):
	info =req.form
	user = info['user']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.forgotpassword_admin(user)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def verify_answer(req):
	info =req.form
	user = info['user']
	answer = info['password']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.verifyanswer(user,answer)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def verify_answer_admin(req):
	info =req.form
	user = info['user']
	answer = info['password']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.verifyanswer_admin(user,answer)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def clear_database(req):
	info =req.form
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.clear_database()
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def getdatabases(req):
	info =req.form
	user = info['user']
	password = info['password']		
	result = {}
	dbManager_Service.connect()
	(result['success'], result['tablename']) =  dbManager_Service.gettables(user, password)
	dbManager_Service.deconnect()
	dbManager_CES.connect()
	(result['success'], result['tablename_CES']) =  dbManager_CES.gettables(user, password)
	dbManager_CES.deconnect()
	return json.dumps(result,indent=1)


def retrieve_from_fqdn(req):
	info =req.form
	fqdn = info['fqdn']
	result = {}
	dbManager_Service.connect()
	(result['success'], result['tablename']) =  dbManager_Service.retrieve_from_fqdn(fqdn)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)


def retrieve_from_msisdn(req):
	info =req.form
	msisdn = info['msisdn']
	result = {}
	dbManager_Service.connect()
	(result['success'], result['tablename']) =  dbManager_Service.retrieve_from_msisdn(msisdn)
	dbManager_Service.deconnect()
	return json.dumps(result,indent=1)


def delete_machine(req):
	info =req.form
	result = {}
	dbManager.connect()
	result['success'] =  dbManager_Service.delete_firewall_table()
	dbManager.deconnect()
	return json.dumps(result,indent=1)



