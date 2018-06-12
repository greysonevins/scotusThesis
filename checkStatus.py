import os
import bs4
import threading
import requests
import re
from emailDecision import sendEmail
from datetime import datetime


URL = "https://www.supremecourt.gov/opinions/slipopinion/17"

CASE = "Trump v. Hawaii"
t = None
SENT = False
DECIDED = False
LASTDECIDED = ""


class DecisionInfo:
    def __init__(self, data):
        caseInfo = {
            "decision":  "No Title",
            "information": "No information",
            "url": "No URL",
            "time": str(datetime.now())

        }
        try:

            caseInfo["decision"] = data.text
        except:
            pass

        try:
            caseInfo["url"] = "https://www.supremecourt.gov/" + data["href"]
        except:
            pass

        try:
            caseInfo["information"] = data["title"].encode('ascii', 'ignore').decode('ascii')
        except:
            pass


        for key, value in caseInfo.items():
            setattr(self, key, value)



def checkStatus():
    global DECIDED, SENT, LASTDECIDED
    try:
        res = requests.get(URL)

        caseSoup = bs4.BeautifulSoup(res.text,'html.parser')


        caseDecisions = [DecisionInfo(a) for a in caseSoup.findAll('a', href=re.compile(r'^/opinions/17pdf?'))]

        LASTDECIDED = caseDecisions[0].decision
        os.system('clear')

        if any(case.decision == CASE for case in caseDecisions) and not SENT:
            case = [case for case in caseDecisions if case.decision == CASE][0]
            caseinfo =  case.information + '\n \n' + case.url + \
                                '\n Time Found: \n' + case.time
            print("DECIDED")
            DECIDED = True
            sendEmail(CASE, caseinfo)
            SENT = True

        elif SENT:
            print("Decided")
        else:
            print("\nNot Decided yet, As of: ")
            print(str(datetime.now()), "\n")
            print("Last Decided Case was: ", LASTDECIDED)


    except Exception as e:
        print(e)
        pass


    t = threading.Timer(30, checkStatus)
    t.start()


checkStatus()
