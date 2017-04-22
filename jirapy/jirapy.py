#!/bin/python

# JIRAPy Interface for JIRA JSON API
# Written by Ewen McCahon, 2017
# Version 0.0.1

import json
import logging
import requests

if __name__ == "__main__":
    print "JIRAPy Helper Classes. Import for helpful functions"

class JiraTicket:
    """
    JIRATicket
    Helper Library for using the JIRA JSON Ticket API
    """

    # Init Func
    def __init__(self, ticketdata, verifyssl=True):
        self.ticket = ticketdata
        self.id = self.ticket['issue']['id']
        self.key = self.ticket['issue']['key']
        self.url = self.ticket['issue']['self']
        self.description = self.ticket['issue']['fields']['description']
        self.summary = self.ticket['issue']['fields']['summary']
        self.reporter = self.ticket['issue']['fields']['reporter']['name']
        self.status = self.ticket['issue']['fields']['status']['name']
        self.fields = self.ticket['issue']['fields']
        
        # Tickets don't always have labels
        try:
            self.labels = self.ticket['issue']['fields']['labels']
        except KeyError:
            logging.warn("Ticket Has no Labels")
            self.labels = None
        # Tickets don't always have components either
        try:
            self.components = self.ticket['issue']['fields']['components']
        except KeyError:
            logging.warn("Ticket Has no Components")
            self.components = None
        
        # SSL Configuration for Comments Function
        self._verifyssl = verifyssl

    def add_comment(self, comment=None, username=None, password=None):
        """
        Add Comment
        Posts a Comment on the remote JIRA ticket
        If public comments are disabled this requires a
        username and password to be supplied.BaseException
        """
        resource = "/comment"
        headers = {'Content-type': 'application/json'}
        message = {
            "body": comment
        }
        proxies = {
            "http": None,
            "https": None
        }
        try:
            logging.info("Posting Comment to " + self.key)
            jira_comment = requests.post(self.url + resource, headers=headers,
                                         json=message, verify=self._verifyssl, proxies=proxies,
                                         auth=(username, password))
            return str(jira_comment.status_code)
        except:
            logging.info("Error Commenting on JIRA Ticket: " + self.key)
