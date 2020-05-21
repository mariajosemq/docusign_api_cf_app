import json
from flask import Flask, request, jsonify 
import requests
import objectpath
import os

app = Flask(__name__) 
port = int(os.getenv("PORT", 9009)) #definicion de puerto de salida

@app.route('/envelopes', methods=['POST']) 
def envelopes():

	getTemplateData = request.json.get("templateData")
	print(getTemplateData)

	#url for creating the envelope
	url_1 = "https://demo.docusign.net/restapi/v2.1/accounts/{}/envelopes".format(getTemplateData['accountId'])

	#payload to create the envelope
	payload_1 = {

	    "templateId": getTemplateData['templateId'],
	    "emailSubject": "Envio de Docusign DC3",
	    "status": "sent",
	    "templateRoles": [
	        {
	            "email": getTemplateData['email'],
	            "name": getTemplateData['employeeFullName'],
	            "roleName": "Signer",
	            "tabs": {
	            "textTabs":[
	               {
	                  "tabLabel":"employeeFullName",
	                  "value": getTemplateData['employeeFullName']
	               },
	               {
	                  "tabLabel":"occupation",
	                  "value": getTemplateData['occupation']
	               },
	               {
	                  "tabLabel":"CU_1",
	                  "value": getTemplateData['CU_1']
	               },
	               {
	                  "tabLabel":"CU_2",
	                  "value": getTemplateData['CU_2']
	               },
	               {
	                  "tabLabel":"CU_3",
	                  "value": getTemplateData['CU_3']
	               },
	               {
	                  "tabLabel":"CU_4",
	                  "value": getTemplateData['CU_4']
	               },
	               {
	                  "tabLabel":"CU_5",
	                  "value": getTemplateData['CU_5']
	               },
	               {
	                  "tabLabel":"CU_6",
	                  "value": getTemplateData['CU_6']
	               },
	               {
	                  "tabLabel":"CU_7",
	                  "value": getTemplateData['CU_7']
	               },
	               {
	                  "tabLabel":"CU_8",
	                  "value": getTemplateData['CU_8']
	               },
	               {
	                  "tabLabel":"CU_9",
	                  "value": getTemplateData['CU_9']
	               },
	               {
	                  "tabLabel":"CU_10",
	                  "value": getTemplateData['CU_10']
	               },
	               {
	                  "tabLabel":"CU_11",
	                  "value": getTemplateData['CU_11']
	               },
	               {
	                  "tabLabel":"CU_12",
	                  "value": getTemplateData['CU_12']
	               },
	               {
	                  "tabLabel":"CU_13",
	                  "value": getTemplateData['CU_13']
	               },
	               {
	                  "tabLabel":"CU_14",
	                  "value": getTemplateData['CU_14']
	               },
	               {
	                  "tabLabel":"CU_15",
	                  "value": getTemplateData['CU_15']
	               },
	               {
	                  "tabLabel":"CU_16",
	                  "value": getTemplateData['CU_16']
	               },
	               {
	                  "tabLabel":"CU_17",
	                  "value": getTemplateData['CU_17']
	               },
	               {
	                  "tabLabel":"job",
	                  "value": getTemplateData['job']
	               },
	               {
	                  "tabLabel":"companyName",
	                  "value": getTemplateData['companyName']
	               },
	               {
	                  "tabLabel":"RF_1",
	                  "value": getTemplateData['RF_1']
	               },
	               {
	                  "tabLabel":"RF_2",
	                  "value": getTemplateData['RF_2']
	               },
	               {
	                  "tabLabel":"RF_3",
	                  "value": getTemplateData['RF_3']
	               },
	               {
	                  "tabLabel":"RF_4",
	                  "value": getTemplateData['RF_4']
	               },
	               {
	                  "tabLabel":"RF_5",
	                  "value": getTemplateData['RF_5']
	               },
	               {
	                  "tabLabel":"RF_3",
	                  "value": getTemplateData['RF_3']
	               },
	               {
	                  "tabLabel":"RF_6",
	                  "value": getTemplateData['RF_6']
	               },
	               {
	                  "tabLabel":"RF_7",
	                  "value": getTemplateData['RF_7']
	               },
	               {
	                  "tabLabel":"RF_8",
	                  "value": getTemplateData['RF_8']
	               },
	               {
	                  "tabLabel":"RF_9",
	                  "value": getTemplateData['RF_9']
	               },
	               {
	                  "tabLabel":"RF_10",
	                  "value": getTemplateData['RF_10']
	               },
	               {
	                  "tabLabel":"RF_11",
	                  "value": getTemplateData['RF_11']
	               },
	               {
	                  "tabLabel":"RF_12",
	                  "value": getTemplateData['RF_12']
	               },
	               {
	                  "tabLabel":"RF_13",
	                  "value": getTemplateData['RF_13']
	               },
	               {
	                  "tabLabel":"courseName",
	                  "value": getTemplateData['courseName']
	               },
	               {
	                  "tabLabel":"hourDuration",
	                  "value": getTemplateData['hourDuration']
	               },
	               {
	                  "tabLabel":"since_year_1",
	                  "value": getTemplateData['since_year_1']
	               },
	               {
	                  "tabLabel":"since_year_2",
	                  "value": getTemplateData['since_year_2']
	               },
	               {
	                  "tabLabel":"since_year_3",
	                  "value": getTemplateData['since_year_3']
	               },
	               {
	                  "tabLabel":"since_year_4",
	                  "value": getTemplateData['since_year_4']
	               },
	               {
	                  "tabLabel":"since_month_1",
	                  "value": getTemplateData['since_month_1']
	               },
	               {
	                  "tabLabel":"since_month_2",
	                  "value": getTemplateData['since_month_2']
	               },
	               {
	                  "tabLabel":"since_day_1",
	                  "value": getTemplateData['since_day_1']
	               },
	               {
	                  "tabLabel":"since_day_2",
	                  "value": getTemplateData['since_day_2']
	               },
	               {
	                  "tabLabel":"to_year_1",
	                  "value": getTemplateData['to_year_1']
	               },
	               {
	                  "tabLabel":"to_year_2",
	                  "value": getTemplateData['to_year_2']
	               },
	               {
	                  "tabLabel":"to_year_3",
	                  "value": getTemplateData['to_year_3']
	               },
	               {
	                  "tabLabel":"to_year_4",
	                  "value": getTemplateData['to_year_4']
	               },
	               {
	                  "tabLabel":"to_month_1",
	                  "value": getTemplateData['to_month_1']
	               },
	               {
	                  "tabLabel":"to_month_2",
	                  "value": getTemplateData['to_month_2']
	               },
	               {
	                  "tabLabel":"to_day_1",
	                  "value": getTemplateData['to_day_1']
	               },
	               {
	                  "tabLabel":"to_day_2",
	                  "value": getTemplateData['to_day_2']
	               },
	               {
	                  "tabLabel":"courseArea",
	                  "value": getTemplateData['courseArea']
	               },
	               {
	                  "tabLabel":"agentName",
	                  "value": getTemplateData['agentName']
	               },
	               {
	                  "tabLabel":"instructorName",
	                  "value": getTemplateData['instructorName']
	               }
		    ]
		}
	}
]}


	#headers to authenticate to the DocuSign account
	headers = {
	  'X-DocuSign-Authentication': json.dumps({"Username": getTemplateData['emailAccount'],"Password": getTemplateData['password'],"IntegratorKey": getTemplateData['integratorKey']}),
	  'Content-Type': 'application/json'
	}
	print(headers)

	#response of creating the envelope
	response = requests.request("POST", url_1, headers= headers, data = json.dumps(payload_1))
	print(response.text.encode('utf8'))

	#url for viewing the recipient (to get the generated document url)
	url_2 = "https://demo.docusign.net/restapi/v2.1/accounts/{}/envelopes/{}/views/recipient".format(getTemplateData['accountId'],response.json()['envelopeId'])

	#payload to "request" the generated document url
	payload_2 = {
		"authenticationMethod": "None",
		"email": getTemplateData['email'],
		"recipientId": "1",
		"returnUrl": "https://demo.docusign.net/restapi/v2/accounts/{}/envelopes/{}".format(getTemplateData['accountId'],response.json()['envelopeId']),
		"userName": getTemplateData['email']
	}

	response_2 = requests.request("POST", url_2, headers=headers, data = json.dumps(payload_2))

	print(response_2.text.encode('utf8'))

	#returns the genetared docusign document url
	return response_2.text.encode('utf8')



@app.route('/errors', methods=['POST']) 
def errors(): 
  json.loads(request.get_data())
  return jsonify(status=200) 
 
app.run(host='0.0.0.0',  port=port)