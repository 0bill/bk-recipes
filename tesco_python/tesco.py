import requests
import json

def get_home_page():

    url = "https://www.tesco.com/groceries/en-GB/search?query=*&page=3"

    payload = {}
    headers = {
    'authority': 'www.tesco.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
    }

    return requests.request("GET", url, headers=headers, data=payload)

def get_search_results(query, csrf_token, csrf_cookie):

    url = "https://www.tesco.com/groceries/en-GB/resources"

    payload = json.dumps({
    "resources": [
        {
        "type": "search",
        "params": {
            "query": {
            "query": query,
            "page": "1"
            }
        }
        }
    ],
    "sharedParams": {
        "query": {}
    },
    "requiresAuthentication": False
    })
    headers = {
        'authority': 'www.tesco.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': f'_csrf={csrf_cookie};',
        'origin': 'https://www.tesco.com',
        'pragma': 'no-cache',
        'referer': f'https://www.tesco.com/groceries/en-GB/search?query={query}',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
        'x-csrf-token': csrf_token
        }

    return requests.request("POST", url, headers=headers, data=payload)
