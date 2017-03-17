def sep(width=45):
    info("-" * width)

def info(message):
    print " [INFO] " + message

def error(message):
    print "[ERROR] " + message

def padstat(message, status, width=45):
    return message + " " * (width - (len(message) + len(status))) + status