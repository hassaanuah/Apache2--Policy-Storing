ces =function(){//start classe

var selected_list=[];

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.auth_user = function() 
{
	login = $('#user').val();
	passwd = $('#inputPassword').val();
	$.ajax({
		url: "/py/form.py/authUser",
		data: {user:$('#user').val(), password:$('#inputPassword').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response){
			if(response.success == false) {}
			else {
				alert('mohsin')
				sessionStorage.setItem('login', $('#user').val());
				sessionStorage.setItem('passwd', $('#inputPassword').val());
				window.location='/htm/tables.htm';
			}	 
		}						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.logout = function() 
{
	sessionStorage.setItem('login', '');
	sessionStorage.setItem('passwd', '');
	window.location='../login.htm';
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_customer_discretion_checkvalue = function() 
{
	Unique_ID = $('#Unique_ID').val();
	Network_Support = $('#Network_Support').val();
	Source_IP = $('#Source_IP').val();
	Source_Port = $('#Source_Port').val();
	Destination_IP = $('#Destination_IP').val();
	Destination_Port = $('#Destination_Port').val();
	Transport_Pro = $('#Transport_Pro').val();
	Action = $('#Action').val();
	Value = $('#Value').val();
	Schedule_Start= $('#Schedule_Start').val();
	Schedule_End= $('#Schedule_End').val();
	Priority= $('#Priority').val();

	if (Unique_ID.length<1 || Network_Support.length<1 || Source_IP.length<1 || Source_Port.length<1 || Destination_IP.length<1 || Destination_Port.length<1 || Transport_Pro.length<1 || Action.length<1 || Value.length<1 || Schedule_Start.length<1 || Schedule_End.length<1 || Priority.length<1)
	{
		alert('No Field can be left empty ! Retry');
	}
	else{
		Schedule=Schedule_Start + ' / ' + Schedule_End;
		ces.add_customer_discretion(Schedule);
	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_customer_discretion = function(Schedule) 
{
	 $.ajax({
		url: "../py/form.py/add_customer_discretion",
		data: {Unique_ID:$('#Unique_ID').val(), Network_Support:$('#Network_Support').val(), Source_IP:$('#Source_IP').val(), Source_Port:$('#Source_Port').val(), Destination_IP:$('#Destination_IP').val(), Destination_Port:$('#Destination_Port').val(), Transport_Pro : $('#Transport_Pro').val(), Action:$('#Action').val(), Value : $('#Value').val(), Schedule:Schedule, Priority : $('#Priority').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		
		success: function(response){
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
	 	}
						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_emergency_checkvalue = function() 
{
	Conditions= $('#Conditions').val();
	Network_Support = $('#Network_Support').val();
	Source_IP = $('#Source_IP').val();
	Source_Port = $('#Source_Port').val();
	Destination_IP = $('#Destination_IP').val();
	Destination_Port = $('#Destination_Port').val();
	Transport_Pro = $('#Transport_Pro').val();
	Action = $('#Action').val();
	Value = $('#Value').val();

	if (Conditions.length<1 || Network_Support.length<1 || Source_IP.length<1 || Source_Port.length<1 || Destination_IP.length<1 || Destination_Port.length<1 || Transport_Pro.length<1 || Action.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_emergency();
	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_emergency = function() 
{
	 $.ajax({
		url: "../py/form.py/add_emergency",
		data: {Conditions:$('#Conditions').val(), Network_Support:$('#Network_Support').val(), Source_IP:$('#Source_IP').val(), Source_Port:$('#Source_Port').val(), Destination_IP:$('#Destination_IP').val(), Destination_Port:$('#Destination_Port').val(), Transport_Pro : $('#Transport_Pro').val(), Action:$('#Action').val(), Value : $('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
		}				
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_gop_checkvalue = function() 
{
	Subscription= $('#Subscription').val();
	Package= $('#Package').val();
	Location= $('#Location').val();
	Network_Support = $('#Network_Support').val();
	Source_IP = $('#Source_IP').val();
	Source_Port = $('#Source_Port').val();
	Destination_IP = $('#Destination_IP').val();
	Destination_Port = $('#Destination_Port').val();
	Transport_Pro = $('#Transport_Pro').val();
	Action = $('#Action').val();
	Value = $('#Value').val();

	if (Subscription.length<1 || Package.length<1 ||Location.length<1 || Network_Support.length<1 || Source_IP.length<1 || Source_Port.length<1 || Destination_IP.length<1 || Destination_Port.length<1 || Transport_Pro.length<1 || Action.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_gop();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_gop = function() 
{
	 $.ajax({
		url: "../py/form.py/add_gop",
		data: {Subscription:$('#Subscription').val(), Package:$('#Package').val(), Location:$('#Location').val(), Network_Support:$('#Network_Support').val(), Source_IP:$('#Source_IP').val(), Source_Port:$('#Source_Port').val(), Destination_IP:$('#Destination_IP').val(), Destination_Port:$('#Destination_Port').val(), Transport_Pro : $('#Transport_Pro').val(), Action:$('#Action').val(), Value : $('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
	
	
	
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
	 	}					
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_identification_checkvalue = function() 
{
	FQDN= $('#FQDN').val();
	MSISDN = $('#MSISDN').val();
	IP = $('#IP').val();
	Unique_ID = $('#Unique_ID').val();
	Subscription = $('#Subscription').val();

	if (FQDN.length<1 || MSISDN.length<1 || IP.length<1 || Unique_ID.length<1 || Subscription.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_identification();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_identification = function() 
{
	 $.ajax({
		url: "../py/form.py/add_identification",
		data: {FQDN:$('#FQDN').val(), MSISDN:$('#MSISDN').val(), IP:$('#IP').val(), Unique_ID:$('#Unique_ID').val(), Subscription:$('#Subscription').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
                }
						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_package_checkvalue = function() 
{
	Name= $('#Name').val();
	Network_Support = $('#Network_Support').val();
	Source_IP = $('#Source_IP').val();
	Source_Port = $('#Source_Port').val();
	Destination_IP = $('#Destination_IP').val();
	Destination_Port = $('#Destination_Port').val();
	Transport_Pro = $('#Transport_Pro').val();
	Action = $('#Action').val();
	Value = $('#Value').val();

	if (Name.length<1 || Network_Support.length<1 || Source_IP.length<1 || Source_Port.length<1 || Destination_IP.length<1 || Destination_Port.length<1 || Transport_Pro.length<1 || Action.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_package();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_package = function() 
{
	 $.ajax({
		url: "../py/form.py/add_package",
		data: {Name:$('#Name').val(), Network_Support:$('#Network_Support').val(), Source_IP:$('#Source_IP').val(), Source_Port:$('#Source_Port').val(), Destination_IP:$('#Destination_IP').val(), Destination_Port:$('#Destination_Port').val(), Transport_Pro : $('#Transport_Pro').val(), Action:$('#Action').val(), Value : $('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
                }					
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_subscription_checkvalue = function() 
{
	Name= $('#Name').val();
	Network_Support = $('#Network_Support').val();
	Source_IP = $('#Source_IP').val();
	Source_Port = $('#Source_Port').val();
	Destination_IP = $('#Destination_IP').val();
	Destination_Port = $('#Destination_Port').val();
	Transport_Pro = $('#Transport_Pro').val();
	Action = $('#Action').val();
	Value = $('#Value').val();

	if (Name.length<1 || Network_Support.length<1 || Source_IP.length<1 || Source_Port.length<1 || Destination_IP.length<1 || Destination_Port.length<1 || Transport_Pro.length<1 || Action.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_subscription();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_subscription = function() 
{
	 $.ajax({
		url: "../py/form.py/add_subscription",
		data: {Name:$('#Name').val(), Network_Support:$('#Network_Support').val(), Source_IP:$('#Source_IP').val(), Source_Port:$('#Source_Port').val(), Destination_IP:$('#Destination_IP').val(), Destination_Port:$('#Destination_Port').val(), Transport_Pro : $('#Transport_Pro').val(), Action:$('#Action').val(), Value : $('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
                }
						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_ucop_checkvalue = function() 
{
	Unique_ID= $('#Unique_ID').val();
	Reputation= $('#Reputation').val();
	Network_Support = $('#Network_Support').val();
	Source_IP = $('#Source_IP').val();
	Source_Port = $('#Source_Port').val();
	Destination_IP = $('#Destination_IP').val();
	Destination_Port = $('#Destination_Port').val();
	Transport_Pro = $('#Transport_Pro').val();
	Action = $('#Action').val();
	Value = $('#Value').val();

	if (Unique_ID.length<1 || Reputation.length<1 || Network_Support.length<1 || Source_IP.length<1 || Source_Port.length<1 || Destination_IP.length<1 || Destination_Port.length<1 || Transport_Pro.length<1 || Action.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_ucop();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_ucop = function() 
{
	 $.ajax({
		url: "../py/form.py/add_ucop",
		data: {Unique_ID:$('#Unique_ID').val(), Reputation:$('#Reputation').val(), Network_Support:$('#Network_Support').val(), Source_IP:$('#Source_IP').val(), Source_Port:$('#Source_Port').val(), Destination_IP:$('#Destination_IP').val(), Destination_Port:$('#Destination_Port').val(), Transport_Pro : $('#Transport_Pro').val(), Action:$('#Action').val(), Value : $('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
		}
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_user_package_checkvalue = function() 
{
	Unique_ID= $('#Unique_ID').val();
	Package= $('#Package').val();
	Schedule_Start= $('#Schedule_Start').val();
	Schedule_End= $('#Schedule_End').val();

	if (Unique_ID.length<1 || Package.length<1 || Schedule_Start.length<1 || Schedule_End.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		Schedule=Schedule_Start + ' / ' + Schedule_End;
		ces.add_user_package();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_user_package = function() 
{
	 $.ajax({
		url: "../py/form.py/add_user_package",
		data: {Unique_ID:$('#Unique_ID').val(), Package:$('#Package').val(), Schedule:Schedule},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
                }
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.show_query = function() 
{
	fqdn= $('#fqdn').val();
	msisdn= $('#msisdn').val();
	if (fqdn.length>1){
		$.ajax({
			url: "../py/form.py/retrieve_from_fqdn",
			data: {fqdn:$('#fqdn').val()},
			type: 'POST',
			dataType: "json",
			cache: false,
			success: function(response){
			     if(response.success == false) {data = response.tablename; alert(data); alert("Failed! Please Retry");}
			     else {

				    data = response.tablename;
				    var i = 0;
				    var create='';
				    while(i<data.length) {
					//create +='<label>'+data[i]+'</label><br><br>'
					create +=data[i]
			  	 	i = i + 1
				    }
				    $("#zone").empty();	
				    $("#zone").append(create);
			     }
			}					
		});//end ajax 	
	}

	else if (msisdn.length>1){
		$.ajax({
			url: "../py/form.py/retrieve_from_msisdn",
			data: {msisdn:$('#msisdn').val()},
			type: 'POST',
			dataType: "json",
			cache: false,
			success: function(response){
			     if(response.success == false) {data = response.tablename; alert(data); alert("Failed! Please Retry");}
			     else {
				    data = response.tablename;
				    var i = 0;
				    var create='';
				    while(i<data.length) {
					//create +='<label>'+data[i]+'</label><br><br>'
					create +=data[i]
			  	 	i = i + 1
				    }
				    $("#zone").empty();	
				    $("#zone").append(create);
			     }
			}
						
		});//end ajax 	
	}

	else {
		alert('Enter a querying Parameter')
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_ces_negotiation_policy_checkvalue = function() 
{
	Trans_Protocol= $('#Trans_Protocol').val();
	Link_Alias= $('#Link_Alias').val();
	Dest_CES_ID = $('#Dest_CES_ID').val();
	Reputation = $('#Reputation').val();
	Direction = $('#Direction').val();
	Policy_Required = $('#Policy_Required').val();
	Policy_Offer = $('#Policy_Offer').val();
	Policy_Available = $('#Policy_Available').val();
	Policy_Required_Constraints = $('#Policy_Required_Constraints').val();

	if (Trans_Protocol.length<1 || Link_Alias.length<1 || Dest_CES_ID.length<1 || Reputation.length<1 || Direction.length<1 || Policy_Required.length<1 || Policy_Offer.length<1 || Policy_Available.length<1 || Policy_Required_Constraints.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}

	else
	{
		ces.add_ces_negotiation_policy();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


this.add_ces_negotiation_policy = function() 
{
	 $.ajax({
		url: "../py/form.py/add_ces_negotiation_policy",
		data: {Trans_Protocol:$('#Trans_Protocol').val(), Link_Alias:$('#Link_Alias').val(), Dest_CES_ID:$('#Dest_CES_ID').val(), Reputation:$('#Reputation').val(), Direction:$('#Direction').val(), Policy_Required:$('#Policy_Required').val(), Policy_Offer:$('#Policy_Offer').val(), Policy_Available : $('#Policy_Available').val(), Policy_Required_Constraints:$('#Policy_Required_Constraints').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
	        }
						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_ces_policy_params_checkvalue = function() 
{
	Trans_Protocol= $('#Trans_Protocol').val();
	Link_Alias= $('#Link_Alias').val();
	Dest_CES_ID = $('#Dest_CES_ID').val();
	Reputation = $('#Reputation').val();
	Direction = $('#Direction').val();
	Parameters = $('#Parameters').val();
	Value = $('#Value').val();

	if (Trans_Protocol.length<1 || Link_Alias.length<1 || Dest_CES_ID.length<1 || Reputation.length<1 || Direction.length<1 || Parameters.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}

	else
	{
		ces.add_ces_policy_params();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_ces_policy_params = function() 
{
	 $.ajax({
		url: "../py/form.py/add_ces_policy_params",
		data: {Trans_Protocol:$('#Trans_Protocol').val(), Link_Alias:$('#Link_Alias').val(), Dest_CES_ID:$('#Dest_CES_ID').val(), Reputation:$('#Reputation').val(), Direction:$('#Direction').val(), Parameters:$('#Parameters').val(), Value:$('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
	 	     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
	 	}				
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_control_policy_params_checkvalue = function() 
{
	Local_FQDN= $('#Local_FQDN').val();
	Remote_FQDN= $('#Remote_FQDN').val();
	Direction = $('#Direction').val();
	Parameters = $('#Parameters').val();
	Value = $('#Value').val();

	if (Local_FQDN.length<1 || Remote_FQDN.length<1 || Direction.length<1 || Parameters.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}

	else
	{
	ces.add_control_policy_params();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_control_policy_params = function() 
{
	 $.ajax({
		url: "../py/form.py/add_control_policy_params",
		data: {Local_FQDN:$('#Local_FQDN').val(), Remote_FQDN:$('#Remote_FQDN').val(), Direction:$('#Direction').val(), Parameters:$('#Parameters').val(), Value:$('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
	
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
                }
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_host_id_checkvalue = function() 
{
	Local_FQDN= $('#Local_FQDN').val();
	ID_Type= $('#ID_Type').val();
	Value = $('#Value').val();

	if (Local_FQDN.length<1 || ID_Type.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_host_id();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_host_id = function() 
{
	 $.ajax({
		url: "../py/form.py/add_host_id",
		data: {Local_FQDN:$('#Local_FQDN').val(), ID_Type:$('#ID_Type').val(), Value:$('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
	
		success: function(response)
		{
	 	    if(response.success == false) {alert("Failed! Please Retry");}
		    else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
	 	}
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_host_negotiation_policy_checkvalue = function() 
{
	Local_FQDN= $('#Local_FQDN').val();
	Remote_FQDN= $('#Remote_FQDN').val();
	Reputation = $('#Reputation').val();
	Direction = $('#Direction').val();
	Policy_Required = $('#Policy_Required').val();
	Policy_Offer = $('#Policy_Offer').val();
	Policy_Available = $('#Policy_Available').val();
	Policy_Required_Constraints = $('#Policy_Required_Constraints').val();

	if (Local_FQDN.length<1 || Remote_FQDN.length<1 || Reputation.length<1 || Direction.length<1 || Policy_Required.length<1 || Policy_Offer.length<1 || Policy_Available.length<1 || Policy_Required_Constraints.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_host_negotiation_policy();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_host_negotiation_policy = function() 
{
	 $.ajax({
		url: "../py/form.py/add_host_negotiation_policy",
		data: {Local_FQDN:$('#Local_FQDN').val(), Remote_FQDN:$('#Remote_FQDN').val(), Reputation:$('#Reputation').val(), Direction:$('#Direction').val(), Policy_Required:$('#Policy_Required').val(), Policy_Offer:$('#Policy_Offer').val(), Policy_Available : $('#Policy_Available').val(), Policy_Required_Constraints:$('#Policy_Required_Constraints').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
	 	     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
	 	}
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_payload_policies_checkvalue = function() 
{
	Local_FQDN= $('#Local_FQDN').val();
	Remote_FQDN= $('#Remote_FQDN').val();
	Payload_Type = $('#Payload_Type').val();

	if (Local_FQDN.length<1 || Remote_FQDN.length<1 || Payload_Type.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
		ces.add_payload_policies();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_payload_policies = function() 
{
	 $.ajax({
		url: "../py/form.py/add_payload_policies",
		data: {Local_FQDN:$('#Local_FQDN').val(), Remote_FQDN:$('#Remote_FQDN').val(), Payload_Type:$('#Payload_Type').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
		}
						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_rloc_policies_checkvalue = function() 
{
	Local_FQDN= $('#Local_FQDN').val();
	Remote_FQDN= $('#Remote_FQDN').val();
	RLOC_Type = $('#RLOC_Type').val();
	Value = $('#Value').val();

	if (Local_FQDN.length<1 || Remote_FQDN.length<1 || RLOC_Type.length<1 || Value.length<1)
	{
		alert('No Field can be Left Empty ! Retry');
	}
	else
	{
	ces.add_rloc_policies();
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.add_rloc_policies = function() 
{
	 $.ajax({
		url: "../py/form.py/add_rloc_policies",
		data: {Local_FQDN:$('#Local_FQDN').val(), Remote_FQDN:$('#Remote_FQDN').val(), RLOC_Type:$('#RLOC_Type').val(), Value:$('#Value').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
	
		success: function(response)
		{
		     if(response.success == false) {alert("Failed! Please Retry");}
		     else {alert("Data has been successfully added"); window.location='../htm/tables.htm';}
                }
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.auth_user = function() 
{
	login = $('#user').val();
	passwd = $('#inputPassword').val();
	$.ajax({
		url: "/py/form.py/authUser",
		data: {user:$('#user').val(), password:$('#inputPassword').val()},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
			if(response.success == false) {window.location='/htm/forgetpasswordfailed.htm'}
			else {	
				sessionStorage.setItem('login', $('#user').val());
				sessionStorage.setItem('passwd', $('#inputPassword').val());
				window.location='/htm/tables.htm';
			}	 
	 	}						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.loadcestables = function()
{
	var login = sessionStorage.login;
	var passwd = sessionStorage.passwd;
	$.ajax({
		url: "../py/form.py/getdatabases",
		data: {user:login, password:passwd},
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response){
					     if(response.success == false) {alert("Logging and password are incorrect!");}
					     else {
						   tablename = response.tablename;
						   tablename2 = response.tablename_CES;
						    var i = 0;
	  					    var create='';
						    create +='<table  class="table table-striped">'
						    create +='<tr > <td ><label>Services Table name:</label></td><td ><label>Modify:</label> </td><td ><label>View:</label> </td></tr>'
						    while(i<tablename.length) {
	 						create +='<tr > <td ><label></label></a>'+tablename[i]+'</td><td ><a href="'+tablename[i]+'.htm" class="link"><label>Add</label></a></label> </td><td ><label> <a  href="#" onclick="ces.deletetable('+tablename[i]+');" class="link"><label>Delete</label> </a> </label> </td></tr>'
						   	i = i + 1	
						    }

						    create +='</table>'
	 					    $("#ces_zone").empty();	
		                                    $("#ces_zone").append(create);	


						    var i = 0;
	  					    var create='';
						    create +='   <br>   <br>   <br>   <br><table  class="table table-striped">'
						    create +='<tr > <td ><label>CES Table name:</label></td><td ><label>Modify:</label> </td><td ><label>View:</label> </td></tr>'
						    while(i<tablename2.length) {
	 						create +='<tr > <td ><label></label></a>'+tablename2[i]+'</td><td ><a href="'+tablename2[i]+'.htm" class="link"><label>Add</label></a></label> </td><td ><label> <a  href="#" onclick="cen.deletetable('+tablename2[i]+');" class="link"><label>Delete</label> </a> </label> </td></tr>'
						   	i = i + 1	
						    }
						    create +='</table>'
		                                    $("#ces_zone").append(create);	

					
					       }	 
	 	                           }				
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

this.authVerification = function() 
{
	var login = sessionStorage.login; 
	var passwd = sessionStorage.passwd;
	if (!login) window.location='../login.htm';
	 $.ajax({
		url: "../py/form.py/authUser",
		data: {user:login, password:passwd},	
		type: 'POST',
		dataType: "json",
		cache: false,
		success: function(response)
		{
		     if(response.success == false) {window.location='../login.htm';}
                }						
	});//end ajax 					
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}



