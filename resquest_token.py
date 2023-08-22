import requests



# The API endpoint
#url = "http://0.0.0.0:5003/auth/token" 
url = "http://0.0.0.0:5003/people/allStudents"
url = "http://0.0.0.0:5003/cos/listCos/input_files"

new_data = {
    "username": "Charmander",
    "password": "PythonAvanzado1",
    "user_access_level":"1",
    "life_time_token": "2"
}

auth_token = ''
headers = {'Authorization': f'Bearer {auth_token}'}


# A GET request to the API
#response = requests.get(url, json=new_data)
response = requests.get(url, headers=headers)

# Print the response
response_json = response.json()
print(response_json)