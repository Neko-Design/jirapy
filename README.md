# JIRAPy
Python Library for reading JIRA Data from JSON API

### What Does it Do
When building apps that integrate with JIRA using its API, its often repetitive to parse and read out data from the objects you're sent. JIRAPy handles the parsing and storing of data so that you can access it with easy to use handlers like `jiraticket.summary` or `jiraticket.tags`, and since it uses native Python data formats and objects, filtering through data is as simple as `for tag in jiraticket.tags`.

It also includes a few convenience functions to make basic operations in Python more friendly, including the `add_comment()` function which when provided with a valid User/Pass combination can post comments to the remote JIRA instance for that ticket. If you need to comment on a JIRA with Self-Signed SSL, see the section 'My JIRA Uses Self-Signed Certificates'

JIRAPy works with data you already have, either from the APIs or from a WebHook. If you want a complete integration with a running JIRA instance that can pull down data for you, I highly recommend the [PyContribs](https://github.com/pycontribs) Package '[Jira](https://github.com/pycontribs/jira)' which provides a fantastic, complete, drop in solution.

### Why
I was writing bots to automatically perform actions when a ticket was raised to our board and found that I was recreating the same functions every time I created a new bot. This keeps all the helpers in an easy to import class.

### How Do I Install It
Easy Method - Pip. Run `pip install jirapy` to download the latest version and its dependencies.

Alternatively, you can clone this repo and copy the `jirapy` folder into your project.

### How Do I Use It
Import the class(es) you require from the module:

`from jirapy import JiraTicket`

then create a JIRA object from data returned from the API:

```
ticketdata = get_ticket("https://neko-design.jira.com/api/rest/2/issue/jirapy-1")
jiraticket = JiraTicket(ticketdata)
```

and now you can read back values from the data:

```
print jiraticket.summary
> Ticket Summary
print jiraticket.reporter
> E. Neko
jiraticket.add_comment("Updated System, Please Check", "username", "password")
> 200
```

### My JIRA Uses Self-Signed Certificates
I've included the option to turn off SSL Verification for the comments feature. When you create the JiraTicket object, set the optional `verifyssl` parameter to `False`:

```
ticketdata = get_ticket("https://neko-design.jira.com/api/rest/2/issue/jirapy-1")
jiraticket = JiraTicket(ticketdata, False)
# Or with a Named Parameter
jiraticket = JiraTicket(ticketdata, verifyssl=False)
```

### Testing
To run the tests, launch `tests/ticketTest.py` and it will run though the expected values, producing a report similar to the below:

```
bash-3.2$ python ticketTest.py
WARNING:root:Ticket Has no Labels
WARNING:root:Ticket Has no Components
 [INFO] Starting JIRAPy Tests
 [INFO] ---------------------------------------------
 [INFO] TEST Ticket Summary                   SUCCESS
 [INFO] TEST Ticket Description               SUCCESS
 [INFO] TEST Ticket Key                       SUCCESS
 [INFO] TEST Ticket URL                       SUCCESS
 [INFO] TEST Ticket Reporter                  SUCCESS
 [INFO] TEST Ticket Status                    SUCCESS
 [INFO] TEST Ticket Labels                    SUCCESS
 [INFO] TEST Ticket Labels (Empty)            SUCCESS
 [INFO] TEST Ticket Components                SUCCESS
 [INFO] TEST Ticket Components (Empty)        SUCCESS
 [INFO] ---------------------------------------------
 [INFO] 0 Tests Failed. 10 Passed.
 [INFO] TESTS PASSED. All Tests Passed
```
