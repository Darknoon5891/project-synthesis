
class Interface():
    def __init__(self):
        
        #imports
        global os, time, ut, main

        import os, time

        import util as ut
        import menu

        while True:
            print("Adding Object")
            print("Do you want to add a [b]lock or [i]tem")
            enterType = input()

            enterType = enterType.lower()

            if enterType == "b":
                AddBlock()
            elif enterType == "i":
                AddItem()
            else:
                ut.message("rnv")
                

class AddItem():
    def __init__(self):
        print("Adding Item")

    #add item def

class AddBlock():
    def __init__(self):
        print("Adding Block")
    
    #add block def


if __name__ == "__main__":
    print("please run via start")
else:
    pass