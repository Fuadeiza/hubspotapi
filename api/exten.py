import requests
# def get_code():
# url = 'https://app.hubspot.com/oauth/authorize?client_id=9b4fbd1f-6606-47af-aa99-2a6dfb2d667b&scope=contacts%20automation&redirect_uri=https://www.example.com/'
# r = requests.get(url)
# for i in r.history:
#     print(i.url)
# gotten_code = r.url
# print(gotten_code)


# https://www.example.com/?code=bd84305c-6df7-419b-a6c3-bb69e54edaaf

api_url="https://api.hubapi.com/oauth/v1/token"

data={"grant_type":'authorization_code','client_secret':'b1ee0ee3-96f5-419b-9ba0-ded34f1a76cd','client_id':'9b4fbd1f-6606-47af-aa99-2a6dfb2d667b', 'redirect_uri':'https://www.example.com/', 'code':'52e17c39-8f89-4f8e-8103-3c47dc2b4164' }
r=requests.post(api_url, data=data)
print(r.json)



# https://api.hubapi.com/oauth/v1/token?grant_type=authorization_code&client_id=9b4fbd1f-6606-47af-aa99-2a6dfb2d667b&client_secret=b1ee0ee3-96f5-419b-9ba0-ded34f1a76cd&redirect_uri=https://www.example.com/&code=52e17c39-8f89-4f8e-8103-3c47dc2b4164

