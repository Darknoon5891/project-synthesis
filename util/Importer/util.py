# easy access re-callable functions

# util = ut
# function names use short name for efficiency
# however its simple to understand their function

# Required Functions

def get_required_imports(*args):

    argsLen = len(args)

    if argsLen == 0:
        return

    for i in args:
        print(i)

# Message Functions 

def message(code):

    import time

    code = str(code)
    messages = {
        "short_name" : ["name message", "required import(s) (new string per import)"],
        "rnv" : ["Response not valid"]
    }

    #get message and imports from messagesdict
    for i in messages:
        if messages[i] == code:
            for x in messages[i]:
                print(x)

    #assign imports to messageImports
    # get_required_imports(messageImports)

    #assign message to messageString
    # print(messageString)
    try:
        print(messages[code][0])
    
    except IndexError:
        print("error occoured")
        time.sleep(1)
            

    time.sleep(1)
    return