import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://a10dc4c0-4353-4824-9eb8-293d64e7fe81.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'iu1pgeSfgs7HbkRFmPgioTapNfOZsiwI'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 36,
            "anaemia": 0,
            "creatinine_phosphokinase": 200,
            "diabetes": 0,
            "ejection_fraction": 30,
            "high_blood_pressure": 0,
            "platelets": 120000,
            "serum_creatinine": 1.1,
            "serum_sodium": 135,
            "sex": 1,
            "smoking": 0,
            "time": 7
          },
          {
            "age": 39,
            "anaemia": 0,
            "creatinine_phosphokinase": 300,
            "diabetes": 0,
            "ejection_fraction": 50,
            "high_blood_pressure": 0,
            "platelets": 200000,
            "serum_creatinine": 0.9,
            "serum_sodium": 250,
            "sex": 0,
            "smoking": 0,
            "time": 1
          }
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
#headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


