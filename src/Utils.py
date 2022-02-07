import json
import fnmatch
from attr import s
import pdfplumber as pdf

from MyConstants import *
from UserSession import UserSession

# Parse file and returns the menu for the couple (day, meal)
def lookupForMeal(user : UserSession):
    path = user.plan
    with pdf.open(path) as file:
        table = file.pages[pagePlan(path)].extract_table()
    return( table[ user.meal ][ user.day ] )

def lookupForAlternatives(user : UserSession, food : str):
    path = user.plan
    with pdf.open(path) as file:
        for page in file.pages[pageAlternatives(path):]:

            # look for keyword in the title
            title = page.extract_text().lower()
            if fnmatch.fnmatch(title,"*: "+food+"*"):

                # Extract and format the table
                table = page.extract_tables()
                table = [ l for l in table if food in l[1][0].lower() ]
                s = ''.join([ ': '.join(list(filter(None,l)))+"\n" for l in table[0][1:] ])
                return s

# find the page of the plan
def pagePlan(path : str):
    with pdf.open(path) as file:
        for page in file.pages:
            if KW_PLAN in page.extract_text():
                return file.pages.index(page)

# find the start page for the alternatives
def pageAlternatives(path : str):
    with pdf.open(path) as file:
        for page in file.pages:
            if KW_ALTERNATIVES in page.extract_text():
                return file.pages.index(page)

# check file format correctness
def checkCorrectness(path : str):
    return True if pageAlternatives(path) and pagePlan(path) else False

# load data from JSON DB
def load():
    try:
        with open(DB_PATH,'r') as file:
            users = json.load(file)
            return { int(userid) : UserSession( *(json.loads(users[userid])).values() ) for userid in users }
    except FileNotFoundError:
        return {}

# store data to JSON DB
def store(users : dict):
    with open(DB_PATH,'w') as file:
        json.dump({user:users[user].toJSON() for user in users.keys()},file)
