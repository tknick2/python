#https://www.dataquest.io/blog/python-api-tutorial/
import requests
import json
from datetime import datetime

# #test 404 error code, this api doesnt exist!!!
# response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
# print(response.status_code)

# #tests success status code
# response = requests.get("http://api.open-notify.org/astros.json")
# print(response.status_code)



# #test json response
# response = requests.get("http://api.open-notify.org/astros.json")
# print(response.json())

# #creates a string from a python object 
def jprint(obj):
    #create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# #test jprint function
# jprint(response.json())

# #object for retrieving specific data from the api
# parameters = {
#     "lat": 40.71,
#     "lon": -74
# }

# #test api with parameters
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# jprint(response.json())

# #understanding response data based on documentation
# pass_times = response.json()['response']
# jprint(pass_times)

# #use a loop to extract just the five risetime values
# risetimes = []
# for d in pass_times:
#     time = d['risetime']
#     risetimes.append(time)
# print(risetimes)

# #change the format on the times to something that makes sense
# times = []
# for rt in risetimes:
#     time = datetime.fromtimestamp(rt)
#     times.append(time)
#     print(time)

# parameters2 = {
#     "current_user_url": 
# }

# response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview")
# print(response.status_code)
# jprint(response.json())

parameters = {
    "username": "tknick2", 
    "password": "GitIsGr8" 
}

response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/issues")
print(response.status_code)
jprint(response.json())

# response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/issues/events", params={
#     "number": 0
# })
# print(response.status_code)
# jprint(response.json())

# response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/issues/comments", params={
#     "number": 1
# })
# print(response.status_code)
# jprint(response.json())

test = response.json()

timestamp = test[0]['updated_at']

print(timestamp)

parameters2 = {
    "since": timestamp,
    "state": "all"
}

response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/issues", params=parameters2)
print(response.status_code)
jprint(response.json())

response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/events")
print(response.status_code)
jprint(response.json())

for issues in response.json():
    if hasattr(issues['payload'], "action") and issues['payload']['action'] == "closed"   and issues['type'] == "IssuesEvent":
        response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/issues", {"state": "closed"})        
        print("closed issues")
        jprint(response.json())
    elif hasattr(issues['payload'], "action") and issues['payload']['action'] == "opened" and issues['type'] == "IssuesEvent":
        response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/issues", {"state": "open"})        
        print("opened issues")
        jprint(response.json())
    else:
        print("nada")

closedIssues = 0

#ok this is confusing...why do i need the 0???
# for issue in response.json():    
#     # if issue['updated_at'] > timestamp:
#     #     timestamp = issue['updated_at']    
#     # if issue['closed_at'] != None:
#         # closedIssues += 1
#     print("ID: " + str(issue['id']))
#     print("Title: " + str(issue['title']))
# title = json.loads(json.dumps(response.json())

print("Closed Issues: " + str(closedIssues))
# print(json.dumps(title))