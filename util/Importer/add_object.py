def interface():
        #imports
        global os, time, ut, menu

        import os, time
        import util as ut
        import menu

        while True:
            print("Adding Object")
            print("Do you want to add a [b]lock or [i]tem")
            entertype = input()
            entertype = entertype.lower()

            if entertype[0] == "b":
                add_object_get_info("block")
                break
            elif entertype[0] == "i":
                add_object_get_info("item")
                break
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
        ut.input_validation(object_name, "object_name")
        object_name = object_name.lower()

    except ValueError:
        ut.message("rnv")
        add_object_get_info(object_type)

    try:
        while True:
            print("%s name: %s" % (object_type, object_name))

            print("Confirm the texture file is in the correct graphics folder")
            print("or you can move the file into the folder and reload to continue")
            print("if the name is not right please go to the menu")
            print("[y]es or [r]eload or [m]enu")
            
            conformation = input("")
            conformation = conformation.lower()

            if conformation[0] == "y":
                object_texture_path = get_object_texture_file(object_name) #check for texture
                construct_object(object_type, object_name, object_texture_path) #construct object
            elif conformation[0] == "m":
                menu.main_menu()
            else:
                os.system("cls")
                time.sleep(1)

    except Exception:
        ut.message("rnv")


def get_object_texture_file(object_name):

    file_format_type = ".png" 
    working_dir = "../graphics/"
    working_dir_array = ["..", "graphics"]
    dir_ls_array = os.listdir(working_dir)

    textrue_file_criteria = [[0, "material name matched"], [0, "object name matched (no conflict)"], [0, "file type valid"]]
    texture_file_valid = False

    texture_file_path = [] #path in list format
    object_texture_path = "" #path to be returned (str)

    #make expected object name
    object_name_array = object_name.split() #object name split (array)
    expected_object_texture_array_name = object_name_array
    expected_object_texture_array = ["_"] * (len(expected_object_texture_array_name) * 2 - 1)
    expected_object_texture_array[0::2] = expected_object_texture_array_name
    expected_object_texture_array.append(file_format_type)
    expected_object_texture_name = "".join(expected_object_texture_array)

    #case 1 match martial and object name
    try:
        #match material type
        for i in object_name_array:
            textures_found = 0
            for x in range(len(dir_ls_array)):
                if i == dir_ls_array[x]:
                    textures_found += 1
                    if textures_found > 1:
                        raise FileExistsError
                    working_dir_array.append(dir_ls_array[x])
                    textrue_file_criteria[0][0] += 1 #update criteria
                else:
                    pass
        
        #update working dictionary
        working_dir = "/".join(working_dir_array)
        dir_ls_array = os.listdir(working_dir)

        #find texture file 
        textures_found = 0 #textue files found
        for i in dir_ls_array:
            if i == expected_object_texture_name:
                textures_found += 1
            else:
                #didn't match texture file name
                pass
    except Exception:
        pass

    #case 2 match object name
    print("breakpoint")
    #resolve conflicts        
    #manual entry if no file is found
        
    #make texture string
    return object_texture_path


def construct_object():
    #add object construction and init
    pass


class Item():
    def __init__(self):
        print("Adding Item")       

    #add item to itemArray (ModItems array)

    #add item base
        #add unlocalized name
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
        #add unlocalized name
        #add registryname
        #add creative tab
        #add array registry (item and block)

    #resources
        #add lang (text append)
        #add model (json)
        #add texture (png)


if __name__ == "__main__":
    print("please run via start")
else:
    pass