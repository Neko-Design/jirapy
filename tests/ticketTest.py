import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../jirapy'))
from jirapy import JiraTicket
import tools

# Variables
TID = "424242"
TURL = "https://jira.ewenmccahon.me/issue/JIRAPY-1337"
TKEY = "JIRAPY-1337"
TSUM = "JIRAPy Hasn't Released Yet"
TDESC = "It's just not happening fast enough"
TSTAT = "Waiting for Support"
TUSR = "neko"

# Sample Data Object
ticketdata = {
    "issue" : {
        "id": TID,
        "self": TURL,
        "key": TKEY,
        "fields": {
            "summary" : TSUM,
            "description" : TDESC,
            "status" : {
                "name" : TSTAT
            },
            "reporter" : {
                "name" : TUSR
            }
        }
    },
    "timestamp" : 1462941258113
}

# Ticket Object
ticket = JiraTicket(ticketdata)

# Tests
fails = 0
passes = 0

tools.info("Starting JIRAPy Tests")
tools.sep()

# Check Ticket Summary
if ticket.summary == TSUM:
    tools.info("Ticket Summary SUCCESS")
    passes += 1
else:
    tools.error("Ticket Summary FAILED")
    fails += 1

# Check Ticket Description
if ticket.description == TDESC:
    tools.info("Ticket Description SUCCESS")
    passes += 1
else:
    tools.error("Ticket Description FAILED")
    fails += 1

# Check Ticket Key
if ticket.key == TKEY:
    tools.info("Ticket Key SUCCESS")
    passes += 1
else:
    tools.error("Ticket Key FAILED")
    fails += 1

# Check Ticket URL
if ticket.url == TURL:
    tools.info("Ticket URL SUCCESS")
    passes += 1
else:
    tools.error("Ticket URL FAILED")
    fails += 1

# Check Ticket Reporter
if ticket.reporter == TUSR:
    tools.info("Ticket Reporter SUCCESS")
    passes += 1
else:
    tools.error("Ticket Reporter FAILED")
    fails += 1

# Check Ticket Status
if ticket.status == TSTAT:
    tools.info("Ticket Status SUCCESS")
    passes += 1
else:
    tools.error("Ticket Status FAILED")
    fails += 1

# Results
tools.sep()
if fails > 0:
    tools.error("Run Finished. Tests have Failed")
else:
    tools.info("Run Finished. All Tests Passed")

tools.info(str(fails) + " Tests Failed. " + str(passes) + " Passed.")