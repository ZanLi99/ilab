import requests
import urllib.request, json


def get_awards(page, limit):
    try:
        url = f"https://api.fwc.gov.au/api/v1/awards?page={page}&limit={limit}"
        hdr ={
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': '04d87071235c4a0589baf617a3ab5fa0',
        }
        req = urllib.request.Request(url, headers=hdr)
        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        return response.read()
    except Exception as e:
        return e

# allowance: wage-allowances
# classification: pay-rates
# penalty: penalties
# ex_allowance: expense-allowances
# clauseID: classifications
def get_data(awardcode, parameter, page, limit):
    try:
        url = f"https://api.fwc.gov.au/api/v1/awards/{awardcode}/{parameter}?page={page}&limit={limit}"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': '04d87071235c4a0589baf617a3ab5fa0',
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        return response.read()
    except Exception as e:
        return(e)

    
import json
import requests

response = requests.get('https://date.nager.at/api/v3/publicholidays/2023/AU')
public_holidays = json.loads(response.content)

for public_holiday in public_holidays:
    print(public_holiday['date'])

response = requests.get('https://date.nager.at/api/v3/AvailableCountries')
AvailableCountries = json.loads(response.content)

for Countries in AvailableCountries:
    print(Countries['countryCode'], Countries['name'])
