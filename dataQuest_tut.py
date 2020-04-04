#https://www.dataquest.io/blog/python-api-tutorial/
import requests
import json
from time import sleep
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

# parameters = {
#     "username": "tknick2", 
#     "password": "GitIsGr8" 
# }

# requests.get("https://api.github.com/tknick2", auth=requests.auth.HTTPBasicAuth("tknick2", "GitIsGr8"))

# response = requests.get("https://api.github.com/repos/omxhealth/t-k-interview/issues")
# print(response.status_code)
# jprint(response.json())

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



# test = response.json()

# timestamp = test[0]['updated_at']

# print(timestamp)

# parameters2 = {
#     "since": timestamp,
#     "state": "all"
# }

# responseEvents = requests.get(eventsURL)
# events = responseEvents.json()
# # print(response.status_code)
# print("Events...")
# print(str(len(events)))
# jprint(events)
# closedIssues = 0

# parameters = {
#     "state": "all",
#     "user": "tknick2",
# }



# #creates a string from a python object 
def jprint(obj):    
    print("Issue Title: " + obj['title']) 
    print("Issue ID: " + str(obj['id']))

#prints a new issue, and the current number of existing open issues and closed issues to the terminal
def ProcessIssue(issue, issues):
    if issue['state'] == "open":
        print("New Issue!!!!")
        jprint(issue)

    elif issue['state'] == "closed":
        print('Closed Issue!!!!')
        jprint(issue)
    
    closedIssues = 0
    allIssues = 0

    for issue in issues:
        if issue['state'] == "closed":
            closedIssues += 1
        allIssues += 1

    print("Total Issues: " + str(allIssues))
    print("Closed Issues: " + str(closedIssues))


#moves any new events into the eventsToProcess collection
def FindNewEvents(events, eventHandled):
    # #create a list of event IDs in the parameter events
    # eventIDs = []    
    # for item in events:
    #     eventIDs.append(item['id'])

    # #create a list of event IDs in the handled events
    # eventsHandledIDs = []
    # for item in eventsHandled:
    #     eventsHandledIDs.append(item['id'])

    # #collection of IDs from the supplied collection of events that are not in the handled collection
    # returnIDs = list(set(eventIDs) - set(eventsHandledIDs))

    #register globals
    # global eventsHandled

    #collection of event objects to return
    returnEvents = []

    

    #add event objects to the return collection and return
    for event in events:
        foundIt = False
        for eventHandled in eventsHandled:
            if event['id'] == eventHandled['id']:
                foundIt = True
                break
        if not foundIt:
            returnEvents.append(event)
    
    return returnEvents


#collection of handled event ids
eventsHandled = []

#collection of unhandled event ids in case more than 1 new event comes back
eventsToProcess = []

#git API URL for the repo of interest
issuesURL = "https://api.github.com/repos/omxhealth/t-k-interview/issues"
eventsURL = "https://api.github.com/repos/omxhealth/t-k-interview/events"

allIssues = 0
closedIssues = 0

while True:
    sleep(1)

    #retrieve all current events and issues
    response = requests.get(eventsURL, auth=requests.auth.HTTPBasicAuth("tknick2", "GitIsGr8"))
    events = response.json()
    # events = []
    # for item in eventsResponse:
    #     events.append(item['id'])

    response = requests.get(issuesURL, {"state": "all"}, auth=requests.auth.HTTPBasicAuth("tknick2", "GitIsGr8"))
    issues = response.json()
    # print(response.status_code)
    print("Checking for Issues...")
    # print(str())
    # jprint(issues)    

    #fill the processing buffer    
    eventsToProcess = FindNewEvents(events, eventsHandled)

    for event in eventsToProcess:
        for issue in issues:
            if 'action' in event['payload'] and event['type'] == "IssuesEvent" and (event['payload']['action'] == "closed" or event['payload']['action'] == "opened") and issue['id'] == event['payload']['issue']['id']:
                ProcessIssue(issue, issues)                
                eventsHandled.append(event)
                break

            
        


# for event in events:
#     if 'action' in event['payload'] and event['payload']['action'] == "closed" and event['type'] == "IssuesEvent":        
#         closedIssues += 1
#         for item in issues:
#             if(item['id'] == event['payload']['issue']['id']):
#                 print("closed issue")
#                 jprint(item)  
#                 break                                     
#     elif 'action' in event['payload'] and event['payload']['action'] == "opened" and event['type'] == "IssuesEvent":
#         for item in issues:
#             if(item['id'] == event['payload']['issue']['id']):
#                 print("open issue")
#                 jprint(item) 
#                 break                              
#     else:
#         print("nada")



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