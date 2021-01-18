class Start():

    def __init__(self):
        #setup file path enviroment
        try:
            global os
            import os
            separator = "\\"
            filepatharray = []
            filepath = os.path.realpath(__file__)
            filepatharray = filepath.split(separator) #creates array out of string
            filepatharray.remove(filepatharray[-1]) #removes file name from path
            dirpath = separator.join(filepatharray)
            os.chdir(dirpath) #sets work path

        except Exception:
            print("Error Setting Up Work Enviroment Path")
            print("Errors Expected")


        #imports
        import main 

        #run required pre-main functions
    
        #call main modual
        main.Main()
    

if __name__ == "__main__":
    Start()
else:
    print("please run via start")