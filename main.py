from jwttoken import get_token

import requests
import json

token = get_token()
print(token)

url = "https://api.appstoreconnect.apple.com/v1/apps/6673915598/analyticsReportRequests"

# URL für Analytics Report Request:
# url = "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests"

payload = json.dumps({
  "data": {
    "type": "analyticsReportRequests",
    "attributes": {
      "accessType": "ONGOING"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6673915598"
        }
      }
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + token
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)