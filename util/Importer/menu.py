# Importer for Project Synthesis
# Author - Darknoon5891

class Main():
    def __init__(self):

        global os, time 
        import os, time

        global ut, add_object
        import util as ut
        import add_object

        #run pre required functions
        Main.getbuild_mcversion()

        print("This script is designed to add items into the mod source code")
        print("if you have moved this file outside of the git file structure errors will occur")
        print("currently only adding items are supported")

        Main.main_interface()

    def main_interface():
        print("Current mod mc version:", buildMCVersion)
        print("")
        #Main Options
        print("What operation do you require:")
        print("Enter [A]dd to add an object")
        print("Enter [E]dit to edit an object")
        print("Enter [D]elete to remove an object")

        enter = input()
        enter = enter.upper()
        os.system("cls")

        Main.nav(enter)

    def nav(code):

        directory = {
            "A" : add_object.Interface,
            "E" : "edit_object.Interface",
            "D" : "remove_object.Interface",
        }

        try:
            call = directory.get(code)
            call()
        except Exception as e:
            ut.message("rnv")
            time.sleep(1)
            os.system("cls")
            Main.main_interface()

    def getbuild_mcversion():
        
        global buildMCVersion
        
        path = ["../../src/main/resources/mcmod.info"]
        for i in range(len(path)):
            a = open(path[i], "r")
            aRead = a.read()
            a.close()
            
            try:
                x = (aRead.index('"mcversion": ') + 13)
                buildMCVersion = aRead[x:]

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
    Main()