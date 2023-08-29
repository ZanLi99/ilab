import requests
import urllib.request, json

def get_respone(page, limit):
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
    

def get_salary(awardCode, classificationID, page, limit):
    try:
        url = f"https://api.fwc.gov.au/api/v1/awards/{awardCode}/classifications/{classificationID}/pay-rates?page={page}&limit={limit}"
        hdr ={
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': '04d87071235c4a0589baf617a3ab5fa0',
        }
        req = urllib.request.Request(url, headers=hdr)
        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        print(response.getcode())
        return response.read()
    except Exception as e:
        print(e)

#get_salary(1,1,1,10)