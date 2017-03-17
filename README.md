# JIRAPy
Python Library for reading JIRA Tickets from JSON API

### What Does it Do
When building apps that integrate with JIRA using its API, its often repetitive to parse and read out data from the objects you're sent. JIRAPy handles the parsing and storing of data so that you can access it with easy to use handlers like `jiraticket.name` or `jiraticket.tags`, and includes helpful looping and sorting functions so that filtering through data is as simple as `for tag in jiraticket.tags`

### Why
I was writing bots to automatically perform actions when a ticket was raised to our board and found that I was recreating the same functions every time I created a new bot. This keeps all the helpers in an easy to import class.

### How Do I Install It
For now, you need to clone this Git repo and copy it into your project, but soon you'll be able to run `pip install jirapy` to get it anywhere.
