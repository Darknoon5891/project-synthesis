#util moudel for project synthesis importer

# get required moduels
def get_required_imports(*args):
    if len(args) == 0:
        return False
    else:
        return args

# Message Functions 
def message(code):
    import os
    import time

    code = str(code)
    messages = {
        "short_name" : ["message content"],
        "rnv" : ["Response not valid"],
        "e" : ["An error has occured"]
    }

    try:
        os.system("cls")
        print(messages[code][0])
    except IndexError:
        print("error occoured")

    time.sleep(1)
    os.system("cls")
    #return to caller function

#validate inputs (input protection)
def input_validation(input_data, input_type):

    #expected importer input types ("name" : ["type", "validation", "comment"])
    types_dict = {
        "object_name" : ["str", 0, "used for naming, registration and texturing when manipulating objects"]
    }

    #assign type code
    try:
        input_code = types_dict[input_type][1]
    except ValueError:
        raise ValueError

    #cutom type checks
    if input_code == 0:
        try:
            if type(input_data) == str and input_data.isdigit() == False:
                pass
            else:
                raise ValueError

        except ValueError:
            raise ValueError


if __name__ == "__main__":
    print("please run via start")
else:
    pass