
class Interface():
    def __init__(self):
        #imports
        global os, time, ut, menu

        import os, time
        import util as ut
        import menu

        while True:
            print("Adding Object")
            print("Do you want to add a [B]lock or [I]tem")
            entertype = input()
            entertype = entertype.upper()

            if entertype[0] == "B":
                Interface.add_object_get_info("block")
            elif entertype[0] == "I":
                Interface.add_object_get_info("item")
            else:
                ut.message("rnv")
                

    def add_object_get_info(object_type):
        print("Adding", object_type)
        
        try:
            print("What is the", object_type, "name")
            print("e.g. Magnite Gem")
            object_name = input("")
            os.system("cls")
            ut.input_validation(object_name, "objectName")
        except ValueError:
            ut.message("rnv")

        print(object_type, "name:", object_name)

        try:
            while True:
                print("Confim the texture file is in the correct graphics folder")
                print("or you can move the file into the folder and reload to continue")
                print("[Y]es or [R]eload")
                
                conformation = input("")
                conformation = conformation.upper()

                if conformation[0] != "Y":
                    print(os.listdir("../graphics"))
                    break
                else:
                    os.system("cls")

        except Exception:
            ut.message("rnv")

        try:
            Item() #make item
        except Exception:
            ut.message("e")
    

        
class Item():
    def __init__(self):
        print("Adding Item")       

    #add item to itemArray (ModItems)
    #add item base

    #add lang
    #add model
    #add texture




if __name__ == "__main__":
    print("please run via start")
else:
    pass