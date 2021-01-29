
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
        os.system("cls")
        print("Adding", object_type)
        
        try:
            print("What is the", object_type, "name")
            print("e.g. Magnite Gem")
            object_name = input("")
            os.system("cls")
            ut.input_validation(object_name, "objectName")
        except ValueError:
            ut.message("rnv")

        print("%s name: %s" % (object_type, object_name))

        try:
            while True:
                print("Confim the texture file is in the correct graphics folder")
                print("or you can move the file into the folder and reload to continue")
                print("[Y]es or [R]eload")
                
                conformation = input("")
                conformation = conformation.upper()

                if conformation[0] == "Y":
                    #check for texture
                    graphics_dir = os.listdir("../graphics")
                    #add texture search method

                    break
                else:
                    os.system("cls")

        except Exception:
            ut.message("rnv")

        if object_type == "item":
            Item() #make item
        elif object_type == "block":
            Block()
        else:
            raise ValueError
    
        
class Item():
    def __init__(self):
        print("Adding Item")       

    #add item to itemArray (ModItems array)

    #add item base
        #add unlocalizedname
        #add registryname
        #add creative tab
        #add array regestry (item)

    #resources
        #add lang (text append)
        #add model (json)
        #add texture (png)

class Block():
    def __init__(self):
        print("Adding Block")

    #add item to itemArray (ModBlocks array)
        #add material

    #add block base
        #add unlocalizedname
        #add registryname
        #add creative tab
        #add array regstery (item and block)

    #resources
        #add lang (text append)
        #add model (json)
        #add texture (png)


if __name__ == "__main__":
    print("please run via start")
else:
    pass