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


def get_classification(awardcode,page,limit):
    try:
        url = f"https://api.fwc.gov.au/api/v1/awards/{awardcode}/classifications?page={page}&limit={limit}"

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
        print(e)

