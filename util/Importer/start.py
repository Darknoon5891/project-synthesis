class Start():

    def __init__(self):
        #setup working directory path
        try:
            import os
            separator = "\\"
            filepatharray = []
            filepath = os.path.realpath(__file__)
            filepatharray = filepath.split(separator) #creates array out of string
            filepatharray.remove(filepatharray[-1]) #removes file name from path
            dirpath = separator.join(filepatharray) #required working dictionary
            os.chdir(dirpath) #assigns working dictionary

        except ModuleNotFoundError:
            print("Error setting up work environment path")
            print("Errors Expected")
        
        global menu
        import menu 
        menu.initialize() #call menu module
    

if __name__ == "__main__":
    Start()
else:
    pass