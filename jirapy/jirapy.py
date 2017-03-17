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
        self.id = self.ticket['issue']['id']
        self.key = self.ticket['issue']['key']
        self.url = self.ticket['issue']['self']
        self.description = self.ticket['issue']['fields']['description']
        self.summary = self.ticket['issue']['fields']['summary']
        self.reporter = self.ticket['issue']['fields']['reporter']['name']
        self.status = self.ticket['issue']['fields']['status']['name']