#Interprets response from Camelot when sending command to it
def check_for_success(command):
    while(True):
        received = input()
        if(received == 'succeeded ' + command):
            return True
        elif(received == 'failed ' + command):
            return False
        elif(received.startswith('error')):
            return False

# Send a command to Camelot.
def action(command):
    print('start ' + command)
    return check_for_success(command)