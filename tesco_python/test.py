import requests
import json

url = "https://www.tesco.com/groceries/en-GB/resources"

payload = json.dumps({
  "resources": [
    {
      "type": "search",
      "params": {
        "query": {
          "query": "Lowicz",
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
  'cookie': '_csrf=2ripPMk9dl_jwQ-OjTPeAd3s;',
  'origin': 'https://www.tesco.com',
  'pragma': 'no-cache',
  'referer': 'https://www.tesco.com/groceries/en-GB/search?query=milk',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
  'x-csrf-token': 'AYsIwyRM-TqjjuIuZV3fgfJQyQCDgIbtuuUY'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
