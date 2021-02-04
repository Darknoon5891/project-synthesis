# Importer for Project Synthesis
# Author - Darknoon5891

def initialize():
    global os, time 
    import os, time

    global ut, add_object
    import util as ut
    import add_object

    #run pre required functions
    getbuild_mcversion()

    print("This script is designed to add items into the mod source code")
    print("if you have moved this file outside of the git file structure errors will occur")
    print("currently in development")

    #call menu
    main_menu()

def main_menu():
    print("Current mod mc version:", buildMCVersion)
    print("")

    #nav options
    print("What operation do you require:")
    print("Enter [a]dd to add an object")
    print("Enter [e]dit to edit an object")
    print("Enter [d]elete to remove an object")

    enter = input()
    enter = enter.lower()
    os.system("cls")

    nav(enter)

def nav(code):

    directory = {
        "a" : add_object.interface,
        "e" : "edit_object.Interface",
        "d" : "remove_object.Interface",
    }

    try:
        call = directory.get(code)
        call()
    except Exception:
        ut.message("rnv")
        time.sleep(1)
        os.system("cls")
        main_menu()

def getbuild_mcversion():
    
    global buildMCVersion
    
    path = ["../../src/main/resources/mcmod.info"]
    for i in range(len(path)):
        a = open(path[i], "r")
        a_read = a.read()
        a.close()
        
        try:
            x = (a_read.index('"mcversion": ') + 13)
            buildMCVersion = a_read[x:]

            #expects to encounter close quotation mark within 10 chars 
            y = 0
            for i in range(10):
                if buildMCVersion[i] == '"': # if it finds the mark break
                    y = y + 1
                elif y == 2: # expects opening mark encounter
                    buildMCVersion = buildMCVersion[:i]
                    break

        except ValueError:
            print("mod version unknown")
            buildMCVersion = "unknown"
            break

        break

    return buildMCVersion
        

if __name__ == "__main__":
    print("please run via start")
else:
    initialize()