'''
Authors: Camelot Developers (Edited and Commented by Zach Moore)
Purpose: Formats a command to be interpreted by the Camelot game engine. Waits for success repsonse before executing other actions
'''

'''
Purpose: Waits for success or fail response from Camelot
Inputs: command that was sent to Camelot
Outputs: True for success, False for failure
'''

def check_for_success(command):

    # Keep getting responses until the success of fail the given command is received
    while True:

        # Get response from Camelot
        received = input()

        # Return True if success response, else false for fail response
        if received == 'succeeded ' + command:
            return True
        elif received == 'failed ' + command:
            return False
        elif received.startswith('error'):
            return False

'''
Purpose: Format an action for interpretation by Camelot
Inputs: Action to be sent to Camelot
Outputs: True for success, False for failure
'''
def action(command):
    # Format command
    print('start ' + command)

    # Call function to check for its success
    return check_for_success(command)