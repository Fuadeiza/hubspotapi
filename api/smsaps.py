import requests, base64
from requests.auth import HTTPBasicAuth

#Send sms api script
def send_sms(params):
    # user: hcristo@altera.cl
    # pass: SG9nYXIgZGUgY3Jpc3Rv
    # API KEY: axz5WHNe3K8Ahr29BD5PTUtCD1qZSbfTzFO
    # url="http://ws.alteragsm.cl/api/sms/send-sms"
    # params={
    #     "msg":"Hello Fuad","to":"56968495167"}
    api_URL="http://ws.alteragsm.cl/api/sms/send-sms/"
    header={'Api-Key':'axz5WHNe3K8Ahr29BD5PTUtCD1qZSbfTzFO'}
    r=requests.post(api_URL, headers=header,json=params,auth=HTTPBasicAuth('hcristo@altera.cl', 'SG9nYXIgZGUgY3Jpc3Rv'))
    req=r.text
    print(req)

#this create the workflow extension for the created app.(SendsmsApp)
# important parameters are 'name' and 'applicationId'
def create_extension():
    api_URL="https://api.hubapi.com/integrations/v1/224973/timeline/event-types?hapikey=283ba45e-46f0-4d6b-8bcc-0d28e80ce253&userId=9657838"
    payload={
        # "integrationAppId":"224973",
        "name":"SendsmsApp",
        "applicationId":"224973",
        "extensionName": "Send SMS",
        "webhookUrl": "https://api.myservice.com/hubspot/new-appointment",
        "fieldMetadata": [
            {
                "label": "Appointment Summary",
                "key": "appointment_title",
                "fieldType": "TEXT",
                "values": [
                    {
                        "type": "STATIC_VALUE",
                        "allowsMergeTags": True
                    }
                ]
            },
            {
                "label": "Requested Appointment Date",
                "key": "appointment_date",
                "fieldType": "DATE",
                "values": [
                    {
                        "type": "OBJECT_PROPERTY"
                    }
                ]
            },
            {
                "label": "Appointment Notes",
                "key": "appointment_notes",
                "fieldType": "TEXTAREA",
                "values": [
                    {
                        "type": "STATIC_VALUE",
                        "allowsMergeTags": True
                    }
                ]
            }
        ]
    }
    r=requests.post(api_URL,json=payload)
    req=r.json()
    print(req)

#
# this gets the 'authorization code needed for adding app to extension
def get_code():
    # This url is to be posted on the browser, it redirects you to your redirect_uri with code as a queryparams
    url = "https://app.hubspot.com/oauth/authorize?client_id=9b4fbd1f-6606-47af-aa99-2a6dfb2d667b&scope=contacts%20automation&redirect_uri=https://www.example.com/"

    r = requests.get(url)
    gotten_code = r.json()
    return gotten_code

def hold_code():
    # This gives you the access token, and refresh token for your app to be installed as part of extension
    gotten_code=get_code()
    api_url="https://api.hub.com/oauth/v1/token"
    data={"grant_type":'bd84305c-6df7-419b-a6c3-bb69e54edaaf','client_id':'224973','client_secret':'9b4fbd1f-6606-47af-aa99-2a6dfb2d667b', 'redirect_uri':'https://www.example.com/' }
    r=requests.get(api_url, params=data)
    print(r.json)


# https://app.hubspot.com/oauth/authorize?client_id=9b4fbd1f-6606-47af-aa99-2a6dfb2d667b&scope=contacts%20automation&redirect_uri=https://www.example.com/



#creating