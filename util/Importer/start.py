class Start():

    def __init__(self):
        #setup file path enviroment
        try:
            import os
            separator = "\\"
            filepatharray = []
            filepath = os.path.realpath(__file__)
            filepatharray = filepath.split(separator) #creates array out of string
            filepatharray.remove(filepatharray[-1]) #removes file name from path
            dirpath = separator.join(filepatharray)
            os.chdir(dirpath) #sets work path

        except ModuleNotFoundError:
            print("Error Setting Up Work Enviroment Path")
            print("Errors Expected")
        
        global menu
        import menu 

        #run required pre-main functions

        #call main modual
        menu.Main()
    

if __name__ == "__main__":
    Start()
else:
    print("please run via start")