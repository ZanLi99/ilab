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


# def get_classification(awardcode,page,limit):
#     try:
#         url = f"https://api.fwc.gov.au/api/v1/awards/{awardcode}/classifications?page={page}&limit={limit}"

#         hdr ={
#         # Request headers
#         'Cache-Control': 'no-cache',
#         'Ocp-Apim-Subscription-Key': '04d87071235c4a0589baf617a3ab5fa0',
#         }

#         req = urllib.request.Request(url, headers=hdr)

#         req.get_method = lambda: 'GET'
#         response = urllib.request.urlopen(req)
#         return response.read()
#     except Exception as e:
#         return(e)

# def get_penalty(awardcode,page,limit):
#     try:
#         url = f"https://api.fwc.gov.au/api/v1/awards/{awardcode}/penalties?page={page}&limit={limit}"

#         hdr ={
#         # Request headers
#         'Cache-Control': 'no-cache',
#         'Ocp-Apim-Subscription-Key': '04d87071235c4a0589baf617a3ab5fa0',
#         }

#         req = urllib.request.Request(url, headers=hdr)

#         req.get_method = lambda: 'GET'
#         response = urllib.request.urlopen(req)
#         return response.read()
#     except Exception as e:
#         return(e)

# def get_ex_allowance(awardcode,page,limit):
#     try:
#         url = "https://api.fwc.gov.au/api/v1/awards/{awardcode}/expense-allowances?page={page}&limit={limit}"

#         hdr ={
#         # Request headers
#         'Cache-Control': 'no-cache',
#         'Ocp-Apim-Subscription-Key': '04d87071235c4a0589baf617a3ab5fa0',
#         }

#         req = urllib.request.Request(url, headers=hdr)

#         req.get_method = lambda: 'GET'
#         response = urllib.request.urlopen(req)
#         return response.read()
#     except Exception as e:
#         return(e)
    
# def allowance(awardcode,page,limit):
#     try:
#         url = f"https://api.fwc.gov.au/api/v1/awards/{awardcode}/wage-allowances?page={page}&limit={limit}"

#         hdr ={
#         # Request headers
#         'Cache-Control': 'no-cache',
#         'Ocp-Apim-Subscription-Key': '••••••••••••••••••••••••••••••••',
#         }

#         req = urllib.request.Request(url, headers=hdr)

#         req.get_method = lambda: 'GET'
#         response = urllib.request.urlopen(req)
#         return response.read()
#     except Exception as e:
#         return(e)