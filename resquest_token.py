import requests



# The API endpoint
#url = "http://0.0.0.0:5003/auth/token" 
url = "http://0.0.0.0:5003/people/allStudents"
#url = "http://0.0.0.0:5003/cos/listCos/input_files"

#url = "http://172.16.238.11:5003/people/allStudents"
#url = "http://0.0.0.0:5003/ocr/ocrOneFile/example-1.pdf"

new_data = {
    "username": "Charmander",
    "password": "PythonAvanzado1",
    "user_access_level":"1",
    "life_time_token": "2"
}

auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6MTY5MzM1NDgzNS43MzQzNjIsImlhdCI6MTY5MzE4MjAzNSwianRpIjoiMmUwNjI0ZWEtZmU2YS00OWVmLWJjOTItZWIxMWVlNmZhZTY4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkNoYXJtYW5kZXIiLCJuYmYiOjE2OTMxODIwMzUsImV4cCI6MTY5MzM1NDgzNSwidXNlcl9sZXZlbF9hY2Nlc3MiOiIxIiwibGlmZV90aW1lX3Rva2VuIjoiMiJ9.DA3qUqWbEKNV8Pdbgt03VC2OZHQQHaIjHnizzH_jMv0'
headers = {'Authorization': f'Bearer {auth_token}'}


# A GET request to the API
#response = requests.get(url, json=new_data)
response = requests.get(url, headers=headers)

# Print the response
#response_json = response.json()
print(response)