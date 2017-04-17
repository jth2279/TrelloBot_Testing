"""
Author: Jordan Holland
Date: 4/17/2017
Description: Testing for the trellobot to interact with the Trello API using RESTful commands
Usage:
    - Get user ID
    - Get notifications for member
    - Post a new board
    - Get ID of board
    - Post list to board
    - Get ID of list
    - Post card to the list
    - Get ID of the card
    - Post checklist to card
    - Get ID of checklist
    - Post item to checklist
    - Post member to the card
    - Put new name on card
    - Post label to board
    - Post label to card
    - Get ID of item on checklist
    - Put item on checklist as finished
    - Get actions of board
    - Put board as closed
    - Post new organization
    - Put new name for organization
    - Delete 
"""

from trello import *
from flask import jsonify
import json, requests

TRELLO_APP_KEY = '1e00ede875c248e976fb967b8494e563'
TRELLO_TOKEN_KEY = '184c9ea4e02b7e929d3b49dd5e7ceb60be89bb809027db1620d1edf0a7ee1202'
BASE_URL = "https://api.trello.com/1"
USERNAME = "jordanholland5"
trello = TrelloApi(TRELLO_APP_KEY)
board = Boards(TRELLO_APP_KEY, TRELLO_TOKEN_KEY)
member = Members(TRELLO_APP_KEY, TRELLO_TOKEN_KEY)
card = Cards(TRELLO_APP_KEY, TRELLO_TOKEN_KEY)
checklist = Checklists(TRELLO_APP_KEY, TRELLO_TOKEN_KEY)
list = Lists(TRELLO_APP_KEY, TRELLO_TOKEN_KEY)
member = Members(TRELLO_APP_KEY, TRELLO_TOKEN_KEY)

numTest = 0
sucTest = 0

print ("##############################################################")
numTest = numTest + 1
print ("Getting member ID for " + USERNAME)
members = member.get(USERNAME)
memberID = members["id"]
if memberID != "":
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Getting notifications for member " + USERNAME)
r = requests.get(BASE_URL + "/members/" + memberID + "/notifications?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY)
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
numTest = numTest + 1
print ("Make a new board")
r = requests.post(BASE_URL + "/boards" + "?key=" + TRELLO_APP_KEY + "&" + "token=" + TRELLO_TOKEN_KEY, data={'name':'newTestBoard','prefs_permissionLevel':'public'})
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
#update current boards
print ("Getting board ID")
numTest = numTest + 1
boards = member.get_board('jordanholland5')
for b in boards:
    if b["name"] == "newTestBoard" and b["closed"] == False:
        shortURL = b["id"]
if shortURL != "":
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Add a list to Board " + shortURL)
numTest = numTest + 1
r = requests.post(BASE_URL + "/lists?key=" + TRELLO_APP_KEY + "&" + "token=" + TRELLO_TOKEN_KEY + "&name=newList&idBoard=" +shortURL)
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Getting list ID from Board " + shortURL)
numTest = numTest + 1
lists = board.get_list(shortURL)
listID = lists[0]["id"]
if listID != "":
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")    
print ("Add a card to list " + listID)
r = requests.post(BASE_URL + "/lists/" + listID + "/cards?key=" + TRELLO_APP_KEY + "&" + "token=" + TRELLO_TOKEN_KEY + "&name=newCard&due=null")
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful" + str(r.status_code))
print ("##############################################################\n")
print ("##############################################################") 
print ("Getting card ID for list " + listID)
numTest = numTest + 1
cards = list.get_card(listID)
cardID = cards[0]["id"]
if cardID != "":
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")    
print ("Add a checklist to card " + cardID)
r = requests.post(BASE_URL + "/checklists?key=" + TRELLO_APP_KEY + "&" + "token=" + TRELLO_TOKEN_KEY + "&name=newChecklist&idCard=" + cardID)
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Get checklist id for card " + cardID)
checklists = card.get_checklist(cardID)
checklistID = checklists[0]["id"]
numTest = numTest + 1
if checklistID != "":
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")    
print ("Add an item to checklist " + checklistID)
r = requests.post(BASE_URL + "/checklists/" + checklistID + "/checkItems?key=" + TRELLO_APP_KEY + "&" + "token=" + TRELLO_TOKEN_KEY + "&name=newChecklisItem")
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Add a member to card " + cardID)
r = requests.post(BASE_URL + "/cards/" + cardID + "/idMembers?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&value=" + memberID)
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Change name of card " + cardID)
r = requests.put(BASE_URL + "/cards/" + cardID + "/name?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&value=newname")
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Added Green newLabel to board " + shortURL)
r = requests.post(BASE_URL + "/labels?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&name=newLabel&color=green&idBoard=" + shortURL)
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Added Red newLabel to card " + cardID)
r = requests.post(BASE_URL + "/cards/" + cardID + "/labels?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&name=newLabel&color=red")
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Get checkItem id for checklist " + checklistID)
checkItems = checklist.get_checkItem(checklistID)
checkItemID = checkItems[0]["id"]
numTest = numTest + 1
if checklistID != "":
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Check off item on card " + cardID)
r = requests.put(BASE_URL + "/cards/" + cardID + "/checklist/" + checklistID + "/checkItem/" + checkItemID + "/state?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&idChecklist=" + checklistID + "&idCheckItem=" + checkItemID + "&value=complete")
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Check actions for board " + shortURL)
r = requests.get(BASE_URL + "boards/" + shortURL + "/actions?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY)
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Close board " + shortURL)
r = requests.put(BASE_URL + "boards/" + shortURL + "/closed?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&value=true")
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
    print (BASE_URL + "/boards/" + shortURL + "/closed?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&value=true")
print ("##############################################################\n")
print ("##############################################################")
print ("Creating organization...")
r = requests.post(BASE_URL + "/organizations?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY + "&name=testOrg&displayName=testOrg")
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    orgID = r.json()["id"]
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("##############################################################")
print ("Getting organization testOrg ID...")
r = requests.delete(BASE_URL + "/organizations/" + orgID + "?key=" + TRELLO_APP_KEY + "&token=" + TRELLO_TOKEN_KEY)
numTest = numTest + 1
if r.status_code == 200:
    print ("[x] Test sucessful")
    sucTest = sucTest + 1
else:
    print ("[ ] Test unsucessful")
print ("##############################################################\n")
print ("Tests completed: " + str(sucTest) + "/" + str(numTest))
