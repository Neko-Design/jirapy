# JIRAPy
Python Library for reading JIRA Tickets from JSON API

### What Does it Do
When building apps that integrate with JIRA using its API, its often repetitive to parse and read out data from the objects you're sent. JIRAPy handles the parsing and storing of data so that you can access it with easy to use handlers like `jiraticket.summary` or `jiraticket.tags`, and includes helpful looping and sorting functions so that filtering through data is as simple as `for tag in jiraticket.tags`

### Why
I was writing bots to automatically perform actions when a ticket was raised to our board and found that I was recreating the same functions every time I created a new bot. This keeps all the helpers in an easy to import class.

### How Do I Install It
For now, you need to clone this Git repo and copy it into your project, but soon you'll be able to run `pip install jirapy` to get it anywhere.

### Testing
To run the tests, launch `tests/ticketTest.py` and it will run though the expected values, producing a report similar to the below:

```
bash-3.2$ python ticketTest.py
 [INFO] Starting JIRAPy Tests
 [INFO] ------------------------------------------------------------
 [INFO] Ticket Summary SUCCESS
 [INFO] Ticket Description SUCCESS
 [INFO] Ticket Key SUCCESS
 [INFO] Ticket URL SUCCESS
 [INFO] Ticket Reporter SUCCESS
 [INFO] Ticket Status SUCCESS
 [INFO] ------------------------------------------------------------
 [INFO] Run Finished. All Tests Passed
 [INFO] 0 Tests Failed. 6 Passed.
```