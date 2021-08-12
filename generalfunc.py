def checkInput(message = "Please enter input: ", valuemin = -1, valuemax = -1, errormsg = "Invalid input.", keepTrying = True):
    '''
    Handles the input request from user and checks it for KeyboardInterrupt and
    that the provided input is an INT. Also allows for limiting input to ranges
    
    ARGUMENTS ARE:
    **NOTE** TO PREVENT FLAG RAISING FOR RANGE VALUES, DO NOT PASS VALUE FOR VALUEMAN OR VALUEMAX AND LEAVE AS -1
    [message] - the input message request string
    [valuemin] - minimum acceptable value
    [valuemax] - maximum acceptable value
    [errormsg] - the message to display on rejection of data
    [keeptrying] - true will make the program keep attempt to collect input, false will allow for one run through of request. Will return False on first failure
    '''
    
    while True: 
        try:
            tocheck = input(message)
            tocheck = int(tocheck)
            
            if tocheck < valuemin and valuemin != -1:
                print("Input value is too low")
            elif tocheck > valuemax and valuemax != -1:
                print("Input value is too high")
            else:
                return tocheck
        except ValueError:
            print(errormsg)
        except KeyboardInterrupt:
            print(errormsg)

        if keepTrying == False:
            return False
