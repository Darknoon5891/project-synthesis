#util model for project synthesis importer

# get required modules
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
        "e" : ["An error has occurred"]
    }

    try:
        os.system("cls")
        print(messages[code][0])
    except IndexError:
        print("error occurred")

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
        input_data_len = len(input_data) 
    except ValueError:
        raise ValueError

    #custom type checks
    if input_code == 0:
        try:
            if type(input_data) == str and input_data.isdigit() == False:
                if input_data_len > 3 and input_data_len < 24:
                    pass
            else:
                raise ValueError

        except ValueError:
            raise ValueError


if __name__ == "__main__":
    print("please run via start")
else:
    pass