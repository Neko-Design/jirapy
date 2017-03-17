#!/bin/python

# JIRAPy Interface for JIRA JSON API
# Written by Ewen McCahon, 2017
# Version 0.0.1

import json

if __name__ == "__main__":
    print "JIRAPy Helper Classes. Import for helpful functions"

class JiraTicket:
    """
    JIRATicket
    Helper Library for using the JIRA JSON Ticket API
    """

    # Init Func
    def __init__(self, ticketjson):
        self.ticket = ticketjson
