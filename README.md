# JIRAPy
Python Library for reading JIRA Data from JSON API

### What Does it Do
When building apps that integrate with JIRA using its API, its often repetitive to parse and read out data from the objects you're sent. JIRAPy handles the parsing and storing of data so that you can access it with easy to use handlers like `jiraticket.summary` or `jiraticket.tags`, and includes helpful looping and sorting functions so that filtering through data is as simple as `for tag in jiraticket.tags`.

JIRAPy works with data you already have, either from the APIs or from a WebHook. If you want a complete integration with a running JIRA instance that can pull down data for you, I highly recommend the [PyContribs](https://github.com/pycontribs) Package '[Jira](https://github.com/pycontribs/jira)' which provides a fantastic, complete, drop in solution.

### Why
I was writing bots to automatically perform actions when a ticket was raised to our board and found that I was recreating the same functions every time I created a new bot. This keeps all the helpers in an easy to import class.

### How Do I Install It
For now, you need to clone this Git repo and copy it into your project, but soon you'll be able to run `pip install jirapy` to get it anywhere.

### How Do I Use It
Import the class(es) you require from the module:

`from jirapy import JiraTicket`

then create a JIRA object from data returned from the API:

```
ticketdata = demo_function_that_returns_ticket_json("https://sample.jira.com/api/2/issue/sample-1")
jiraticket = JiraTicket(ticketdata)
```

and now you can read back values from the data:

```
print jiraticket.summary
> Ticket Summary
print jiraticket.reporter
> E. Neko
```

### Testing
To run the tests, launch `tests/ticketTest.py` and it will run though the expected values, producing a report similar to the below:

```
bash-3.2$ python ticketTest.py
 [INFO] Starting JIRAPy Tests
 [INFO] ---------------------------------------------
 [INFO] TEST Ticket Summary                   SUCCESS
 [INFO] TEST Ticket Description               SUCCESS
 [INFO] TEST Ticket Key                       SUCCESS
 [INFO] TEST Ticket URL                       SUCCESS
 [INFO] TEST Ticket Reporter                  SUCCESS
 [INFO] TEST Ticket Status                    SUCCESS
 [INFO] ---------------------------------------------
 [INFO] Run Finished. All Tests Passed
 [INFO] 0 Tests Failed. 6 Passed.
```
